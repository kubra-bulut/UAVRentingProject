FROM python:3.10

# Çalışma dizini oluştur
WORKDIR /usr/src/app

# Gerekli dosyaları kopyala
COPY requirements.txt ./

# Bağımlılıkları yükle
RUN pip install --no-cache-dir -r requirements.txt

# Projeyi kopyala
COPY . .

# Port ayarla
EXPOSE 8000

# Komutu çalıştır
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
