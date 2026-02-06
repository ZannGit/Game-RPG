#LATIHAN 1

class HeroLatihan1:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

print("HASIL LATIHAN 1:")
hero1 = HeroLatihan1("Layla", 100, 15)
hero2 = HeroLatihan1("Zilong", 120, 20)  # Tambah hero2 seperti modul
hero1.info()
hero2.info()
hero1.hp = 500
print(f"Update HP Hero 1: {hero1.hp}")

#LATIHAN 2

class HeroLatihan2:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

print("\n----------------------------")
print("HASIL LATIHAN 2:")
print("\n--- Pertarungan Dimulai ---")  # Sesuai modul
h1 = HeroLatihan2("Layla", 100, 15)
h2 = HeroLatihan2("Zilong", 120, 20)
h1.serang(h2)
h2.serang(h1)

#LATIHAN 3

class HeroLatihan3:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def serang(self, lawan):  # Tambahkan method ini untuk warisan
        print(f"{self.name} menyerang {lawan.name}!")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} terkena damage {damage}. Sisa HP: {self.hp}")

class Mage(HeroLatihan3):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")  # Sesuai modul
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")  # Sesuai modul

print("\n----------------------------")
print("HASIL LATIHAN 3:")
print("\n--- Update Class Hero ---")  # Sesuai modul
eudora = Mage("Eudora", 80, 30, 100)
balmond = HeroLatihan3("Balmond", 200, 10)
eudora.info()
eudora.serang(balmond)  # Tambahkan serangan biasa untuk demo warisan
eudora.skill_fireball(balmond)

#LATIHAN 4

class HeroLatihan4:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal
    
    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")  # Sesuai modul
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):  # Tambahkan method ini seperti modul
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")

print("\n----------------------------")
print("HASIL LATIHAN 4:")
hero_aman = HeroLatihan4("Layla", 100)
hero_aman.set_hp(-50)
print(f"HP Layla (via Getter): {hero_aman.get_hp()}")
print(f"Akses Paksa (Name Mangling): {hero_aman._HeroLatihan4__hp}")

#LATIHAN 5

from abc import ABC, abstractmethod

class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass

class HeroKonkret(GameUnit):
    def __init__(self, nama):
        self.nama = nama
    
    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")  # Sesuai modul

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")  # Sesuai modul

class Monster(GameUnit):  # Tambahkan class Monster seperti modul
    def __init__(self, jenis):
        self.jenis = jenis
    
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")
    
    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")

print("\n----------------------------")
print("HASIL LATIHAN 5:")
h = HeroKonkret("Alucard")
m = Monster("Serigala")
h.info()
m.info()

#LATIHAN 6

class Hero:  # Rename dari HeroBase -> Hero sesuai modul
    def __init__(self, nama):
        self.nama = nama
    
    def serang(self):  # Rename dari aksi() -> serang() sesuai modul
        print("Hero menyerang dengan tangan kosong.")

class MagePoly(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")  # Sesuai modul

class ArcherPoly(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")  # Sesuai modul

class HealerPoly(Hero):  # Ini sudah bagus, sudah jawab Tugas Analisis 6.1
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")

print("\n----------------------------")
print("HASIL LATIHAN 6:")
print("\n--- PERANG DIMULAI ---")  # Sesuai modul
pasukan = [
    MagePoly("Eudora"),
    ArcherPoly("Miya"), 
    HealerPoly("Estes")
]

for pahlawan in pasukan:
    pahlawan.serang()  # Rename dari .aksi() -> .serang()

print("\n----------------------------")
print("PROGRAM SELESAI")