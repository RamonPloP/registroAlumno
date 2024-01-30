import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
import pandas as pd
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class ReporteMensualApp:
    def __init__(self, master):
        self.master = master
        master.title("Reporte Mensual App")

        # Etiqueta y entrada para seleccionar el mes
        self.label_mes = tk.Label(master, text="Selecciona el mes (formato: MM-AAAA):")
        self.entry_mes = tk.Entry(master)
        self.label_mes.pack()
        self.entry_mes.pack()

        # Botón para generar el informe
        self.button_generar = tk.Button(master, text="Generar Informe", command=self.generar_informe)
        self.button_generar.pack()

    def cargar_datos_adicionales(self, rutas_archivos):
        # Cargar y combinar datos adicionales de cada parte
        dfs = []
        for ruta_archivo in rutas_archivos:
            df = pd.read_excel(ruta_archivo)
            dfs.append(df)

        df_combinado = pd.concat(dfs, ignore_index=True)
        return df_combinado

    def generar_informe(self):
        mes = self.entry_mes.get()
        def enviar_correo_adjunto(destinatario, asunto, cuerpo, archivo_adjunto, nombre):
            # Configura el servidor SMTP (Gmail)
            servidor_smtp = 'smtp.gmail.com'
            puerto_smtp = 587
            usuario = 'socialservicio15@gmail.com'
            contrasena = 'rseizkhfibjjcuop'

            # Configura el mensaje
            mensaje = MIMEMultipart()
            mensaje['From'] = usuario
            mensaje['To'] = destinatario
            mensaje['Subject'] = asunto
            mensaje.attach(MIMEText(cuerpo, 'plain'))

            # Adjunta el archivo al mensaje
            with open(archivo_adjunto, 'rb') as archivo:
                adjunto = MIMEApplication(archivo.read(), _subtype="xlsx")
                adjunto.add_header('Content-Disposition', f'attachment; filename={nombre}')
                mensaje.attach(adjunto)

            # Conéctate al servidor SMTP y envía el correo
            with smtplib.SMTP(servidor_smtp, puerto_smtp) as server:
                server.starttls()
                server.login(usuario, contrasena)
                server.sendmail(usuario, destinatario, mensaje.as_string())
                print('Archivo enviado exitosamente')

        if not mes:
            messagebox.showerror("Error", "Por favor, ingresa un mes válido.")
            return

        try:
            client = MongoClient('mongodb://localhost:27017/')
            db = client['alumnos']
            collection = db['alumnos']

            query = {"_date": mes}
            data = list(collection.find(query))

            print("Ruta actual: ", os.getcwd())

            print(f"Número total de documentos en la base de datos: {len(data)}")

            if not data:
                messagebox.showinfo("Información", "No hay datos disponibles en la base de datos.")
                return

            df = pd.DataFrame(data)

            rutas_archivos = ['./bibliotecas/ing.xlsx', './bibliotecas/conta.xlsx', './bibliotecas/fisica.xlsx', './bibliotecas/conta.xlsx']
            # Cargar datos adicionales de cada parte
            df_datos_adicionales = self.cargar_datos_adicionales(rutas_archivos)

            print("Valores únicos en la columna de combinación en df:")
            print(df['_matricula'].unique())

            print("Valores únicos en la columna de combinación en df_datos_adicionales:")
            print(df_datos_adicionales['_matricula'].unique())


            # Enlazar datos de la base de datos con datos adicionales
            df_combinado = pd.merge(df, df_datos_adicionales, on='_matricula', how='inner')

            df_combinado.to_excel(f'./informes/informe_mensual_{mes}.xlsx', index=False)

            messagebox.showinfo("Información", f"Informe generado correctamente para el mes {mes}.")

            # Llama a la función para enviar el correo con el archivo adjunto
            archivo_adjunto = f'./informes/informe_mensual_{mes}.xlsx'
            nombre = f'Reporte_Mensual_{mes}.xlsx'
            destinatario = 'a348411@uach.mx'
            asunto = (f'Informe Mensual {mes}')
            cuerpo = 'Informe mensual.'

            enviar_correo_adjunto(destinatario, asunto, cuerpo, archivo_adjunto, nombre)

        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReporteMensualApp(root)
    root.mainloop()
