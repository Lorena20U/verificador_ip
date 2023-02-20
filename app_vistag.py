import tkinter as tk

class Verificador(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self, width=50)
        self.entry.pack(side="top")

        self.action_button = tk.Button(self, text="Verificar", command=self.check_ip, width=10, height=5)
        self.action_button.pack(side="top")

        self.label = tk.Label(self, text="", width=50, height=10)
        self.label.pack(side="top")

    def check_ip(self):
        ip = self.entry.get()

        octs = ip.split(".")
        val = 1
        if len(octs) != 4:
            val = 0
        
        for part in octs:
            try:
                int_part = int(part)
            except ValueError:
                val = 0

            if int_part < 0 or int_part > 255:
                val = 0
        
        if val == 0:
            self.label.configure(text=f"La dirección IP {ip} es inválida :(")
            return

        tipo = "privada"
        clase = ""

        # Rangos clases ip privadas
        if int(octs[0]) == 10:
            clase = "A"
        elif int(octs[0]) == 172 and int(octs[1]) >= 16 and int(octs[1]) <= 31:
            clase = "B"
        elif int(octs[0]) == 192 and int(octs[1]) == 168:
            clase = "C"
        else:
            tipo = "global"
            # Rangos clases ip publicas
            if 0 <= int(octs[0]) <= 126:
                clase = "A"
            if 128 <=int(octs[0]) <= 191:
                clase = "B"
            if 192 <= int(octs[0]) <= 223:
                clase = "C"
            if 224 <= int(octs[0]) <= 239:
                clase = "D"
            if 240 <= int(octs[0]) <= 254:
                clase = "E"

        self.label.configure(text=f"IP: {ip} de tipo {tipo}, Clase: {clase}.")

root = tk.Tk()
app = Verificador(master=root)
app.mainloop()