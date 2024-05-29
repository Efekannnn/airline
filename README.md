![image](https://github.com/Efekannnn/airline-automation-website/assets/139994163/5ce12d4d-9ded-46ae-886b-09d09a403eb8)
# Uçuş Rezervasyon ve Yönetim Uygulaması

Bu uygulama, bir bilet satış ve yönetim platformudur. Uygulama kullanıcıların uçuşları aramasına, bilet rezervasyonu yapmasına ve yöneticilerin satılan biletleri yönetmesine olanak tanır.

## Özellikler

- Kullanıcılar, uçuşları tarih, varış ve kalkış noktalarına göre arayabilir.
- Uygun uçuşları bulduktan sonra, kullanıcılar bilet rezervasyonu yapabilir.
- Yöneticiler, bilet satışlarını ve rezervasyonları yönetebilir, iptal edebilir ve güncelleyebilir.
- Admin paneli aracılığıyla sistem yöneticileri, uçuşları, havaalanlarını ve diğer sistem ayarlarını yönetebilir.

## Kullanılan Teknolojiler

- **Django**: Güçlü bir Python web çatısı.
- **MySQL ve SQLite**: Veritabanı yönetimi için kullanılan ilişkisel veritabanı yöneticileri.
- **Bootstrap**: Hızlı ve duyarlı web tasarımı için popüler CSS kütüphanesi.
- **HTML, CSS ve JavaScript**: Temel web teknolojileri.

## Kurulum

1. Projeyi klonlayın:

Komut istemini(terminali) açın ve alttaki kodu yazarak uygulamayı klonlayın. 
git clone https://github.com/Efekannnn/airline-automation-website.git

2. Bir ide aracılığıyla ile klonladığınız projeyi açın ve Sanal ortam oluşturup oluşturduğunuz sanal ortamı etkinleştirin.

Komut istemini açıp projenin olduğu dosyaya eriştikten sonra komut istemine(terminale) aşağıdakileri yazın.

Unix/Linux veya MacOs için:
python3 -m venv myenv
source myenv/bin/activate

Windows için: 
py -m venv env
.\env\Scripts\activate

3. Gerekli bağımlılıkları yükleyin:
   
pip freeze > requirementstxt
pip install -r requirements.txt(bu dosya boş gelirse ekler bölmesinde bulunan rquirments.txt dosyasının içindeki yazıları bu dosyaya kopyalayın)

4. Veritabanını migrate edin:
   
Komut istemini açıp projenin olduğu dosyaya eriştikten sonra komut istemine(terminale) aşağıdakileri yazın.
python manage.py migrate

5. Sunucuyu başlatın:
   
Komut istemini açıp projenin olduğu dosyaya eriştikten sonra komut istemine(terminale) aşağıdakileri yazın.
python manage.py runserver

6. Admin belirleyin:

Komut istemciyi açıp python manage.py createsuperuser komutu ile admin belirleyin ve artık http://127.0.0.1:8000/admin/ bağlantısından admin girişi yapabilirsiniz.

## Geliştirilen Arayüzün Diğer Örnek Görsellerine ekler klasöründe bulunan **IMAGESOFAPP** klasöründen erişebilirsiniz.  



