# GesSanat — Online Sanat Galerisi & Atölye Rezervasyon Sistemi

## Proje Hakkında

GesSanat, sanat eserlerinin sergilendiği, atölye ve etkinlik rezervasyonlarının yapılabildiği bir online sanat galerisi ve rezervasyon sistemidir. Kullanıcılar eserleri inceleyebilir, satın alabilir, atölyelere katılabilir ve değerlendirme yapabilir.

---

## Teknolojiler

| Katman | Teknoloji |
|---|---|
| Backend | Python 3.11, Django 5.2 |
| Veritabanı | MySQL 8.0 |
| Frontend | HTML, CSS, Bootstrap 5, JavaScript |
| Geliştirme Ortamı | PyCharm, VS Code |
| Veritabanı Yönetimi | MySQL Workbench |

---

## Kurulum

### Gereksinimler

- Python 3.11+
- MySQL 8.0+
- pip

### Adımlar

**1. Projeyi klonla:**
```bash
git clone https://github.com/kullanici/sanat_galerisi.git
cd sanat_galerisi
```

**2. Sanal ortam oluştur ve aktif et:**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

**3. Bağımlılıkları yükle:**
```bash
pip install django mysqlclient Pillow
```

**4. MySQL'de veritabanı oluştur:**
```sql
CREATE DATABASE sanat_galerisi;
```

**5. `sanat_galerisi/settings.py` içindeki veritabanı ayarlarını güncelle:**
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sanat_galerisi',
        'USER': 'root',
        'PASSWORD': 'şifreniz',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

**6. Migrate işlemlerini çalıştır:**
```bash
python manage.py makemigrations
python manage.py migrate
```

**7. Admin kullanıcısı oluştur:**
```bash
python manage.py createsuperuser
```

**8. Sunucuyu başlat:**
```bash
python manage.py runserver
```

**9. Tarayıcıda aç:**
```
http://127.0.0.1:8000/
```

---

## Proje Yapısı

```
sanat_galerisi/
├── sanat_galerisi/        # Proje ayarları
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── artworks/              # Eser yönetimi
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── events/                # Etkinlik yönetimi
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── users/                 # Kullanıcı yönetimi
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── orders/                # Sipariş ve ödeme
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── reservations/          # Rezervasyon yönetimi
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── reviews/               # Yorum ve değerlendirme
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/             # HTML şablonları
├── static/                # CSS, JS, görseller
├── media/                 # Kullanıcı yüklenen dosyalar
└── manage.py
```

---

## Veritabanı Tabloları

| Tablo | Açıklama |
|---|---|
| users | Kullanıcı bilgileri |
| artists | Sanatçı bilgileri |
| artworks | Eser bilgileri |
| events | Etkinlik bilgileri |
| event_sessions | Etkinlik seans tarihleri |
| reservations | Rezervasyon kayıtları |
| orders | Sipariş kayıtları |
| payments | Ödeme kayıtları |
| cart | Sepet öğeleri |
| coupons | İndirim kuponları |
| favorites | Favori eserler |
| reviews | Yorum ve değerlendirmeler |
| review_votes | Yorum oyları |
| support_tickets | Destek talepleri |
| comparisons | Karşılaştırma kayıtları |

---

## Özellikler

### Kullanıcı İşlemleri
- Kayıt olma ve giriş yapma
- Profil bilgilerini güncelleme
- Şifre değiştirme
- Sipariş ve rezervasyon takibi

### Eser İnceleme
- Tüm eserleri listeleme ve detay görüntüleme
- Sanatçı bilgilerini okuma
- Eserleri favorilere ekleme
- Sepete ekleme ve satın alma

### Atölye & Etkinlikler
- Etkinlikleri listeleme ve detay görüntüleme
- Birden fazla seans tarihi seçimi
- Katılımcı sayısı belirleme
- Rezervasyon oluşturma, güncelleme ve iptal

### Ödeme Sistemi
- Kredi kartı, banka kartı, havale seçenekleri
- İndirim kuponu uygulama
- Sipariş ve rezervasyon ödeme sayfası

### Yorum Sistemi
- Sadece satın alan kullanıcılar eser yorumu yapabilir
- Sadece etkinliğe katılan kullanıcılar etkinlik yorumu yapabilir
- Yorum filtreleme (en yeni, en yüksek puan, en faydalı)
- Like/dislike ile yorum oylama
- Galeri yöneticisi yorum yanıtlama
- Ortalama puan hesaplama

### Kampanya & İndirim
- Kampanyalı eser ve etkinlikler
- İndirim kuponu sistemi
- Kullanıcıya özel kuponlar

### Karşılaştırma
- Birden fazla eseri karşılaştırma
- Birden fazla etkinliği karşılaştırma
- Karşılaştırma kaydetme

### Müşteri Destek
- İletişim formu
- Destek talebi oluşturma ve takip
- Admin yanıt sistemi

### Yönetici Paneli
- Özet rapor ekranı
- Eser istatistikleri (görüntülenme, yorum, satış)
- Etkinlik istatistikleri (doluluk oranı, ortalama puan, rezervasyon sayısı)
- Toplam kullanıcı, sipariş, rezervasyon ve gelir

---

## Admin Paneli

```
http://127.0.0.1:8000/admin/
```

Admin panelinden eser, etkinlik, kullanıcı, seans ve kupon eklenebilir.

---

## Geliştiriciler

**Gülşeri Demir**  
**Elif Uçar**
 
2025–2026

---

## Notlar

- Görseller `media/` klasöründe saklanır.
- Şifreler düz metin olarak saklanmaktadır (geliştirme ortamı).
- `DEBUG = True` sadece geliştirme ortamı içindir, production'da `False` yapılmalıdır.
