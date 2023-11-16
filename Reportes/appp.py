import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from datetime import datetime, timedelta
import pandas as pd

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

            print(f"Número total de documentos en la base de datos: {len(data)}")

            if not data:
                messagebox.showinfo("Información", "No hay datos disponibles en la base de datos.")
                return

            # Generación de reporte en Excel
            df = pd.DataFrame(data)

            df.to_excel(f'./informes/informe_mensual_{mes}.xlsx', index=False)

            messagebox.showinfo("Información", f"Informe generado correctamente para el mes {mes}.")

        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ReporteMensualApp(root)
    root.mainloop()
