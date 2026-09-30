import tkinter as tk
from random import choice

class Oyun:
    SECENEKLER = ("Taş", "Kağıt", "Makas")
    KAZANAN = {("Taş", "Makas"), ("Kağıt", "Taş"), ("Makas", "Kağıt")}

    def __init__(self):
        self.yeniden_baslat()

    def oyna(self, secim):
        pc = choice(self.SECENEKLER)
        if secim == pc:
            return pc, "Berabere"
        if (secim, pc) in self.KAZANAN:
            self.__skor[0] += 1
            return pc, "Kazandın"
        self.__skor[1] += 1
        return pc, "Kaybettin"

    def yeniden_baslat(self):
        self.__skor = [0, 0]

    @property
    def skor(self):
        return tuple(self.__skor)

class Arayuz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Taş Kağıt Makas")
        self.oyun = Oyun()
        self.bilgi = tk.Label(self, text="Seçimini yap!", font=("Arial", 14), width=32, height=3)
        self.bilgi.pack()
        cerceve = tk.Frame(self)
        cerceve.pack()
        for s in Oyun.SECENEKLER:
            tk.Button(cerceve, text=s, width=10, command=lambda s=s: self.tikla(s)).pack(side="left", padx=5, pady=5)
        tk.Button(self, text="Yeniden Başla", command=lambda: (self.oyun.yeniden_baslat(), self.bilgi.config(text="Skor: 0 - 0"))).pack(pady=5)

    def tikla(self, secim):
        pc, sonuc = self.oyun.oyna(secim)
        self.bilgi.config(text=f"Sen: {secim} | Bilgisayar: {pc}\n{sonuc}!\nSkor: {self.oyun.skor[0]} - {self.oyun.skor[1]}")

Arayuz().mainloop()
