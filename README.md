# BOZ213d01u01-TasKagitMakas
Melih Erdem Ceren  25040322  BÖTE 2.sınıf
# ✊✋✌️ Taş Kağıt Makas

Python ve **tkinter** ile yazılmış, nesne tabanlı programlama (OOP) prensiplerine uygun basit bir Taş Kağıt Makas oyunu. Bilgisayar Ve Öğretim Teknolojileri Öğretmenliği bölümü **Nesne Tabanlı Programlama** dersi için hazırlanmıştır.

## Özellikler

- Taş, Kağıt veya Makas butonlarına tıklayarak oyna
- Bilgisayar her turda rastgele seçim yapar
- Sonuç ekranda **Kazandın / Kaybettin / Berabere** olarak gösterilir
- Skor takibi (Sen - Bilgisayar)
- **Yeniden Başla** butonu ile skor sıfırlanır
- Sadece standart kütüphaneler kullanılır (`tkinter`, `random`), ekstra kurulum gerekmez

## Kurulum ve Çalıştırma

Python 3.6 veya üzeri yüklü olmalıdır.

```bash
git clone https://github.com/kullanici-adin/tas-kagit-makas.git
cd tas-kagit-makas
python main.py
```

> **Not:** Linux'ta tkinter yüklü değilse `sudo apt install python3-tk` komutuyla kurabilirsin. Windows ve macOS'ta Python ile birlikte gelir.

## Nasıl Oynanır?

1. Pencerede **Taş**, **Kağıt** veya **Makas** butonlarından birine tıkla.
2. Bilgisayarın seçimi ve tur sonucu ekranda görünür.
3. Skor her turdan sonra güncellenir.
4. Baştan başlamak istersen **Yeniden Başla** butonuna bas.

Kurallar: Taş makası, makas kağıdı, kağıt taşı yener.

## Kullanılan OOP Kavramları

| Kavram | Projedeki Kullanımı |
|---|---|
| **Sınıf ve Nesne** | `Oyun` (oyun mantığı) ve `Arayuz` (görsel arayüz) olmak üzere iki sınıf vardır. |
| **Encapsulation (Kapsülleme)** | Skor `__skor` olarak private tutulur; dışarıdan yalnızca `skor` property'si ile okunabilir. |
| **Inheritance (Kalıtım)** | `Arayuz` sınıfı `tk.Tk` sınıfından miras alır. |
| **Composition (Bileşim)** | `Arayuz`, içinde bir `Oyun` nesnesi (`self.oyun`) barındırır. |

### Sınıflar

**`Oyun`**
- `__init__()` : Oyunu başlatır, skoru sıfırlar.
- `oyna(secim)` : Kullanıcının seçimini alır, `(bilgisayar_secimi, sonuc)` şeklinde bir tuple döndürür.
- `yeniden_baslat()` : Skoru sıfırlar.
- `skor` (property) : Mevcut skoru `(kazanma, kaybetme)` olarak döndürür.

**`Arayuz(tk.Tk)`**
- Pencereyi, butonları ve skor/sonuç yazısını oluşturur.
- Butona tıklanınca `Oyun.oyna()` metodunu çağırır ve dönen değeri ekranda gösterir.

## Proje Yapısı

```
tas-kagit-makas/
├── main.py
└── README.md
```

## Ekran Görüntüsü

<!-- Oyunun ekran görüntüsünü ekleyip aşağıdaki satırı düzenle -->
![Oyun ekran görüntüsü](ekran_goruntusu.png)

## Geliştirici
Melih Erdem Ceren
25040322
Böte 2.Sınıf

**Adın Soyadın** — Bilgisayar ve Öğretim Teknolojileri Öğretmenliği, 2. Sınıf
Ders: Nesne Tabanlı Programlama
