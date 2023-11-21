import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
import pandas as pd
import os

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

        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReporteMensualApp(root)
    root.mainloop()
