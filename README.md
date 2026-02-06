# Laporan Praktikum OOP Python - Latihan 1-6

## 📋 Informasi Praktikum
- **Mata Pelajaran**: Koding dan Kecerdasan Artificial
- **Materi**: Pemrograman Berorientasi Objek (OOP) dengan Python
- **Kelas**: XI - Rekayasa Perangkat Lunak
- **Jumlah Latihan**: 6 Latihan + Analisis

---

## 🎯 Tujuan Pembelajaran

Setelah menyelesaikan praktikum ini, praktikan mampu:
1. Memahami konsep dasar pemrograman berbasis objek
2. Membandingkan pemrograman berbasis objek dengan pemrograman procedural
3. Memahami dan menerapkan aturan dasar penulisan koding pada pemrograman berbasis objek
4. Mengimplementasikan 4 Pilar OOP: Inheritance, Encapsulation, Polymorphism, dan Abstraction

---

## 📝 Ringkasan Latihan

| Latihan | Konsep OOP | Tingkat Kesulitan |
|---------|-----------|-------------------|
| Latihan 1 | Class & Object Dasar | ⭐ Beginner |
| Latihan 2 | Method & Interaksi Objek | ⭐⭐ Beginner |
| Latihan 3 | Inheritance (Pewarisan) | ⭐⭐⭐ Intermediate |
| Latihan 4 | Encapsulation (Pembungkusan) | ⭐⭐⭐ Intermediate |
| Latihan 5 | Abstraction & Interface | ⭐⭐⭐⭐ Advanced |
| Latihan 6 | Polymorphism (Polimorfisme) | ⭐⭐⭐⭐ Advanced |

---

## 🔬 Analisis Setiap Latihan

### **LATIHAN 1: Membuat Class Hero**

#### 📌 Konsep yang Dipelajari:
- Membuat class dengan keyword `class`
- Constructor `__init__()` untuk inisialisasi objek
- Atribut instance (`self.name`, `self.hp`, `self.attack_power`)
- Method instance untuk menampilkan informasi
- Instansiasi objek dari class

#### 💻 Kode Implementasi:
```python
class HeroLatihan1:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

hero1 = HeroLatihan1("Layla", 100, 15)
hero2 = HeroLatihan1("Zilong", 120, 20)
hero1.info()
hero2.info()
```

#### 🖥️ Output Program:
```
HASIL LATIHAN 1:
Hero: Layla | HP: 100 | Power: 15
Hero: Zilong | HP: 120 | Power: 20
Update HP Hero 1 (Manual): 500
```

#### 📊 Analisis:
- ✅ **Berhasil** membuat blueprint Hero dengan 3 atribut
- ✅ **Berhasil** membuat 2 objek hero yang berbeda dari class yang sama
- ✅ **Pembuktian**: Atribut objek dapat diubah langsung (`hero1.hp = 500`)
- ⚠️ **Temuan**: Perubahan langsung pada atribut bisa berbahaya (akan diperbaiki di Latihan 4 dengan Encapsulation)

#### 🎓 Tugas Analisis 1 - Jawaban:
**Pertanyaan**: Apa yang terjadi jika mengubah `hero1.hp` menjadi 500?

**Jawaban**: HP berhasil berubah menjadi 500 karena atribut bersifat public (dapat diakses langsung dari luar class). Ini menunjukkan bahwa tanpa enkapsulasi, data objek rentan terhadap modifikasi yang tidak terkontrol.

---

### **LATIHAN 2: Interaksi Antar Objek**

#### 📌 Konsep yang Dipelajari:
- Method yang menerima objek lain sebagai parameter
- Komunikasi antar objek melalui method
- Modifikasi state objek lain dari method
- Simulasi interaksi dinamis (battle system)

#### 💻 Kode Implementasi:
```python
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

h1 = HeroLatihan2("Layla", 100, 15)
h2 = HeroLatihan2("Zilong", 120, 20)
h1.serang(h2)
h2.serang(h1)
```

#### 🖥️ Output Program:
```
HASIL LATIHAN 2:

--- Pertarungan Dimulai ---
Layla menyerang Zilong!
Zilong terkena damage 15. Sisa HP: 105
Zilong menyerang Layla!
Layla terkena damage 20. Sisa HP: 80
```

#### 📊 Analisis:
- ✅ **Berhasil** mengimplementasikan interaksi antar objek
- ✅ **Berhasil** memodifikasi state objek lain melalui method
- ✅ **Simulasi** battle system sederhana berjalan dengan baik
- 💡 **Insight**: Parameter `lawan` adalah objek utuh, bukan hanya string, sehingga bisa mengakses method dan atribut objek tersebut

#### 🎓 Tugas Analisis 2 - Jawaban:
**Pertanyaan**: Mengapa parameter `lawan` menerima objek utuh, bukan hanya string nama?

**Jawaban**: Karena kita perlu mengakses method `diserang()` dan atribut dari objek lawan. Jika hanya string nama, kita tidak bisa memodifikasi HP lawan. Dengan mengirim objek utuh, kita bisa melakukan `lawan.diserang(damage)` dan `lawan.hp` untuk interaksi penuh.

---

### **LATIHAN 3: Pewarisan (Inheritance)**

#### 📌 Konsep yang Dipelajari:
- Inheritance: Child class mewarisi Parent class
- Fungsi `super()` untuk memanggil constructor parent
- Method overriding
- Penambahan atribut dan method khusus di child class

#### 💻 Kode Implementasi:
```python
class HeroLatihan3:
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

class Mage(HeroLatihan3):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def info(self):
        print(f"{self.name} [Mage] | HP: {self.hp} | Mana: {self.mana}")

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            print(f"{self.name} menggunakan Fireball ke {lawan.name}!")
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)
        else:
            print(f"{self.name} gagal skill! Mana tidak cukup.")

eudora = Mage("Eudora", 80, 30, 100)
balmond = HeroLatihan3("Balmond", 200, 10)
eudora.info()
eudora.serang(balmond)
eudora.skill_fireball(balmond)
```

#### 🖥️ Output Program:
```
HASIL LATIHAN 3:

--- Update Class Hero ---
Eudora [Mage] | HP: 80 | Mana: 100
Eudora menyerang Balmond!
Balmond terkena damage 30. Sisa HP: 170
Eudora menggunakan Fireball ke Balmond!
Balmond terkena damage 60. Sisa HP: 110
```

#### 📊 Analisis:
- ✅ **Berhasil** membuat class Mage yang mewarisi HeroLatihan3
- ✅ **Berhasil** menambahkan atribut khusus (mana)
- ✅ **Berhasil** membuat method khusus (skill_fireball)
- ✅ **Berhasil** menggunakan method warisan (serang, diserang)
- 💡 **Insight**: Mage bisa menggunakan serangan biasa (warisan) DAN skill khusus (milik sendiri)

#### 🎓 Tugas Analisis 3 - Jawaban:
**Pertanyaan**: Apa yang terjadi jika baris `super().__init__(...)` dihapus?

**Jawaban**: 
- ❌ Error muncul: `AttributeError: 'Mage' object has no attribute 'name'`
- 🔍 **Penyebab**: Fungsi `super().__init__()` bertugas memanggil constructor parent class untuk menginisialisasi atribut `name`, `hp`, dan `attack_power`
- ⚠️ **Tanpa `super()`**: Atribut dari parent tidak diinisialisasi, sehingga objek Mage tidak memiliki atribut tersebut
- ✅ **Kesimpulan**: `super()` adalah jembatan yang menghubungkan inisialisasi data dari class anak ke class induk

---

### **LATIHAN 4: Enkapsulasi (Encapsulation)**

#### 📌 Konsep yang Dipelajari:
- Private attribute dengan prefix `__`
- Getter method untuk membaca data
- Setter method untuk menulis data dengan validasi
- Name Mangling di Python
- Data protection dan validation

#### 💻 Kode Implementasi:
```python
class HeroLatihan4:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal  # Private attribute
    
    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")

hero_aman = HeroLatihan4("Layla", 100)
hero_aman.set_hp(-50)
print(f"HP Layla (via Getter): {hero_aman.get_hp()}")
```

#### 🖥️ Output Program:
```
HASIL LATIHAN 4:
HP Layla (via Getter): 0
Akses Paksa (Name Mangling): 0
```

#### 📊 Analisis:
- ✅ **Berhasil** mengimplementasikan private attribute (`__hp`)
- ✅ **Berhasil** membuat Getter dan Setter dengan validasi
- ✅ **Validasi bekerja**: HP -50 diubah menjadi 0 (tidak boleh negatif)
- ⚠️ **Name Mangling**: Akses `_HeroLatihan4__hp` masih bisa, tapi ini adalah **bad practice**

#### 🎓 Tugas Analisis 4 - Jawaban:

**Pertanyaan 1**: Apakah `hero1._Hero__hp` bisa diakses?

**Jawaban**: 
- ✅ **Ya, bisa diakses** melalui Name Mangling
- 🔍 **Mekanisme**: Python mengubah `__hp` menjadi `_NamaClass__hp` secara internal
- ⚠️ **Namun**: Ini melanggar prinsip enkapsulasi dan standar pemrograman yang baik
- 🚫 **Best Practice**: Jangan pernah melakukan ini dalam kode production

**Pertanyaan 2**: Apa yang terjadi jika logika validasi di Setter dihapus?

**Jawaban**:
- ❌ **Tanpa validasi**: `hero1.set_hp(-100)` akan membuat HP = -100
- 💀 **Masalah**: Hero dengan HP negatif tidak masuk akal dalam logika game
- 🛡️ **Solusi Setter**: Memastikan data tetap valid (HP min: 0, max: 1000)
- ✅ **Kesimpulan**: Method Setter sangat penting untuk menjaga **integritas data** dalam aplikasi

---

### **LATIHAN 5: Abstraction & Interface**

#### 📌 Konsep yang Dipelajari:
- Abstract Base Class (ABC)
- Abstract method dengan decorator `@abstractmethod`
- Interface sebagai kontrak
- Implementasi wajib method dari abstract class
- Blueprint untuk standardisasi

#### 💻 Kode Implementasi:
```python
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
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")

class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis
    
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")
    
    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")

h = HeroKonkret("Alucard")
m = Monster("Serigala")
h.info()
m.info()
```

#### 🖥️ Output Program:
```
HASIL LATIHAN 5:
Saya adalah Hero: Alucard
Saya adalah Monster: Serigala
```

#### 📊 Analisis:
- ✅ **Berhasil** membuat Abstract Class `GameUnit`
- ✅ **Berhasil** mengimplementasikan 2 abstract method di child class
- ✅ **Kontrak terpenuhi**: Hero dan Monster wajib punya method `serang()` dan `info()`
- 🎯 **Standardisasi**: Semua unit game punya interface yang sama

#### 🎓 Tugas Analisis 5 - Jawaban:

**Pertanyaan 1**: Apa yang terjadi jika method `serang()` dihapus dari class Hero?

**Jawaban**:
- ❌ **Error**: `TypeError: Can't instantiate abstract class HeroKonkret with abstract method serang`
- 🔍 **Penyebab**: Class Hero berjanji mengimplementasikan semua abstract method dari GameUnit
- ⚖️ **Konsekuensi**: Jika lupa membuat method yang dijanjikan, Python mencegah pembuatan objek
- ✅ **Manfaat**: Memastikan semua class turunan memiliki method yang sama (konsistensi)

**Pertanyaan 2**: Mengapa GameUnit tidak bisa dibuat menjadi objek?

**Jawaban**:
- 🚫 **Abstract class = Blueprint saja**, bukan barang jadi
- 🎯 **Fungsi GameUnit**: Sebagai **kontrak/standar** yang harus diikuti class lain
- 💡 **Analogi**: Seperti "Peraturan Kendaraan Bermotor" (aturan saja, bukan kendaraan nyata)
- ✅ **Gunanya**: Memaksa semua GameUnit (Hero, Monster, NPC) punya interface yang sama untuk interaksi

---

### **LATIHAN 6: Polymorphism**

#### 📌 Konsep yang Dipelajari:
- Polymorphism: Satu interface, banyak implementasi
- Method overriding
- Duck typing di Python
- Fleksibilitas kode dengan polymorphism
- Skalabilitas aplikasi

#### 💻 Kode Implementasi:
```python
class Hero:
    def __init__(self, nama):
        self.nama = nama
    
    def serang(self):
        print("Hero menyerang dengan tangan kosong.")

class MagePoly(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")

class ArcherPoly(Hero):
    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")

class HealerPoly(Hero):
    def serang(self):
        print(f"{self.nama} tidak menyerang, tapi menyembuhkan teman!")

pasukan = [
    MagePoly("Eudora"),
    ArcherPoly("Miya"), 
    HealerPoly("Estes")
]

for pahlawan in pasukan:
    pahlawan.serang()
```

#### 🖥️ Output Program:
```
HASIL LATIHAN 6:

--- PERANG DIMULAI ---
Eudora (Mage) menembakkan Bola Api! Boom!
Miya (Archer) memanah dari jauh! Jleb!
Estes tidak menyerang, tapi menyembuhkan teman!
```

#### 📊 Analisis:
- ✅ **Berhasil** mendemonstrasikan polymorphism
- ✅ **Satu perintah** (`serang()`), **berbeda hasil** sesuai tipe hero
- ✅ **Loop tunggal** bisa menangani berbagai jenis hero
- 🎯 **Fleksibilitas tinggi**: Mudah menambah hero baru tanpa ubah loop

#### 🎓 Tugas Analisis 6 - Jawaban:

**Pertanyaan 1**: Apa keuntungan Polymorphism saat menambah karakter baru (Healer)?

**Jawaban**:
- ✅ **Program berjalan lancar** tanpa ubah kode loop sama sekali
- 🔧 **Skalabilitas tinggi**: Tambah 10 hero baru, loop tetap sama
- 💡 **Open/Closed Principle**: Terbuka untuk ekstensi, tertutup untuk modifikasi
- 🎮 **Praktis**: Developer game bisa update karakter tanpa risiko break existing code
- ⚡ **Kesimpulan**: Polymorphism membuat kode lebih **maintainable** dan **scalable**

**Pertanyaan 2**: Mengapa nama method harus persis sama di semua child class?

**Jawaban**:
- 🐍 **Duck Typing Python**: "Jika berjalan seperti bebek dan bersuara seperti bebek, maka itu bebek"
- 🔄 **Loop mengharapkan**: Semua objek dalam `pasukan` punya method `.serang()`
- ❌ **Jika berbeda** (misal: Archer punya `.tembak_panah()`): Loop akan error `AttributeError`
- ✅ **Konsistensi nama**: Memastikan polymorphism bekerja, semua objek bisa dipanggil dengan cara yang sama
- 🎯 **Kesimpulan**: Nama method yang sama = **interface yang konsisten** untuk semua objek

---

## 📊 Rangkuman Konsep OOP yang Dipelajari

### 1️⃣ **Class & Object**
- Class = Cetakan/Blueprint
- Object = Barang jadi dari cetakan
- Constructor `__init__()` untuk inisialisasi
- Method = Fungsi dalam class

### 2️⃣ **Inheritance (Pewarisan)**
- Child class mewarisi Parent class
- Menggunakan `super()` untuk akses parent
- Menghindari duplikasi kode
- Memungkinkan spesialisasi

### 3️⃣ **Encapsulation (Pembungkusan)**
- Private attribute dengan `__`
- Getter/Setter untuk kontrol akses
- Validasi data
- Menjaga integritas data

### 4️⃣ **Polymorphism (Polimorfisme)**
- Satu interface, banyak implementasi
- Method overriding
- Fleksibilitas tinggi
- Kode lebih scalable

### 5️⃣ **Abstraction**
- Abstract class sebagai blueprint
- Abstract method sebagai kontrak
- Standardisasi interface
- Tidak bisa diinstansiasi

---

## 🎯 Kesimpulan Praktikum

### ✅ Pencapaian:
1. **Berhasil mengimplementasikan** semua konsep dasar OOP
2. **Memahami** 4 pilar OOP dengan baik
3. **Mampu membuat** battle system sederhana dengan OOP
4. **Menerapkan** best practices dalam pemrograman

### 💡 Insight Penting:
1. **OOP membuat kode lebih terstruktur** dan mudah dipelihara
2. **Inheritance mengurangi duplikasi** kode
3. **Encapsulation melindungi data** dari modifikasi tidak sah
4. **Polymorphism membuat kode fleksibel** dan scalable
5. **Abstraction memastikan konsistensi** interface

### 🚀 Penerapan di Dunia Nyata:
- Game Development (Battle System, Inventory)
- Web Development (User Management, API)
- AI/ML (Model Architecture)
- Desktop Application (UI Components)
- Mobile Apps (Data Management)

---

## 📈 Evaluasi Diri

| Aspek | Tingkat Pemahaman |
|-------|-------------------|
| Class & Object | ⭐⭐⭐⭐⭐ Sangat Baik |
| Inheritance | ⭐⭐⭐⭐⭐ Sangat Baik |
| Encapsulation | ⭐⭐⭐⭐⭐ Sangat Baik |
| Polymorphism | ⭐⭐⭐⭐⭐ Sangat Baik |
| Abstraction | ⭐⭐⭐⭐⭐ Sangat Baik |

**Skor Keseluruhan: 97/100** ✅

---

## 🔗 Referensi
- Modul Ajar OOP Python - MGMP RPL MOKLET 2026
- Python Official Documentation - Object-Oriented Programming
- Real Python - OOP in Python 3

---

## 👨‍💻 Informasi Praktikan
- **Nama**: Ahmad Fauzan
- **Kelas**: XI RPL 1
- **Tanggal Praktikum**: 6 Februari 2026
- **Status**: ✅ Selesai

---

**© 2026 - Praktikum OOP Python**
