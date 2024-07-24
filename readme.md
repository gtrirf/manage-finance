# Moliya Menejmenti Loyihasi

Bu loyiha moliyaviy daromadlar va chiqimlarni boshqarish uchun veb-ilova yaratishdan iborat. 
Foydalanuvchilar o'zlarining moliyaviy ko'rsatkichlarini kuzatish, 
turli vaqt oralig'ida daromad va chiqimlarni ko'rish, shuningdek, yangi turdagi moliyaviy 
ma'lumotlarni kiritishlari mumkin.

## O'rnatish

Loyihani ishlatish uchun quyidagi amallarni bajaring:

1. Repoyitoriyani klonlash:
   ```bash
   https://github.com/gtrirf/manage-finance.git
   
2. Virtual muhit yaratish:
    ```bash
   python -m venv env
   ```
3. Virtual muhitni faollashtirish:
    windows uchun
   ```bash
   env\Scripts\activate
   ```
   macOS/Linux
   ```bash
   source env/bin/activate
   ```
4. Zarur kutubxonalarni o'rnatish:
   ```bash
   pip install -r requirements.txt
   ```
5. Django ma'lumotlar bazasini yaratish:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. Ilovani ishga tushirish:
   ```bash
   python manage.py runserver
   ```
   
Ilovani ishga tushirishdan keyin, brauzer orqali quyidagi manzilga kirishingiz mumkin:
http://localhost:8000


Xususiyatlar
Login va Ro'yxatdan o'tish: Foydalanuvchilar email orqali autentifikatsiyadan o'tishi mumkin.
Daromad va Chiqimlar Charti: Foydalanuvchilar o'zlarining daromad va chiqimlarini kunlik, haftalik, oylik yoki yillik formatlarda ko'rishlari mumkin.
Yangi Turdagi Ma'lumotlar Yaratish: Foydalanuvchilar yangi moliyaviy ma'lumotlar turini yaratishlari va ularga mos ikonalarni tanlashlari mumkin.
Loyihaning Tuzilishi
Loyiha Django freymvorkida ishlab chiqilgan va quyidagi asosiy komponentlarni o'z ichiga oladi:


Models: Moliyaviy ma'lumotlar, turli foydalanuvchilar va ularning ma'lumotlarini saqlash uchun ma'lumotlar bazasi modeli.

Views: Foydalanuvchi interfeysi va ma'lumotlarni ko'rsatish uchun foydalaniladigan funksiya va klasslar.

Templates: HTML fayllari va statik resurslar.

Static: CSS va JavaScript fayllari.

Hissadorlar
Agar loyiha bo'yicha savollaringiz bo'lsa yoki o'z hissangizni qo'shmoqchi bo'lsangiz, quyidagi kontaktlar orqali bog'lanishingiz mumkin:

Email: iravshanov90@gmail.com
