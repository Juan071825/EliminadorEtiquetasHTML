import tkinter as tk
from tkinter import ttk


class eliminador:

    def __init__(self):
        self.etiqueta:bool = False
        self.ventana = tk.Tk()
        self.entrada = tk.Text(self.ventana, height=12)
        self.salida = tk.Text(self.ventana, height=12)

    def establecer_estado(self, letra:str):

        if letra == "<":
            self.etiqueta = True
        elif letra == ">":
            self.etiqueta = False
        else:
            pass


    def eliminar(self, texto:str):
        texto_lista = []
        index = 0
        for letra in texto:
            self.establecer_estado(letra)
            if self.etiqueta == False and letra not in ['<','>']:
                texto_lista.append(letra)
            else:
                pass
            index += 1
        return ''.join(texto_lista)

    def procesar(self):
        html = self.entrada.get("1.0", tk.END)
        texto_limpio = self.eliminar(html)

        self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, texto_limpio)


    def copiar_resultado(self):
        self.ventana.clipboard_clear()
        self.ventana.clipboard_append(self.salida.get("1.0", tk.END))
        self.ventana.update()

    def ejecutar(self):
        self.ventana.title("Eliminador de etiquetas HTML")
        self.ventana.geometry("800x600")

        ttk.Label(self.ventana, text="Texto HTML").pack(pady=5)


        self.entrada.pack(fill="both", expand=True, padx=10)

        # Botones
        frame_botones = ttk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        ttk.Button(frame_botones, text="Limpiar HTML", command=self.procesar).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Copiar resultado", command=self.copiar_resultado).pack(side="left", padx=5)

        ttk.Label(self.ventana, text="Texto limpio").pack(pady=5)


        self.salida.pack(fill="both", expand=True, padx=10)

        self.ventana.mainloop()


   



if __name__ == "__main__":

    programa = eliminador()
    programa.ejecutar() 