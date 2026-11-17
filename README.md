پروژه کانتینرسازی بک‌اند با Docker

توضیحات پروژه

در این پروژه یک بک‌اند ساده با زبان برنامه‌نویسی پایتون ساخته شده و با استفاده از Docker داخل یک Container اجرا شده است.

ابزارهای استفاده‌شده

* Python
* Flask
* Docker
* GitHub

فایل‌های پروژه

* app.py : کد اصلی بک‌اند
* requirements.txt : کتابخانه‌های موردنیاز پروژه
* Dockerfile : دستورالعمل ساخت Docker Image
* .dockerignore : مشخص کردن فایل‌هایی که نباید وارد Image شوند

ساخت Docker Image

برای ساخت Image از دستور زیر استفاده می‌کنیم:

docker build -t my-backend .

اجرای Container

برای اجرای بک‌اند و اتصال پورت‌ها از دستور زیر استفاده می‌کنیم:

docker run -d -p 5000:5000 --name my-backend-container my-backend

بررسی وضعیت Container

برای مشاهده Containerهای در حال اجرا:

docker ps

تست بک‌اند

برای بررسی عملکرد بک‌اند:

curl http://localhost:5000/

اتصال پورت‌ها (Port Mapping)

پورت 5000 سیستم به پورت 5000 داخل Container متصل شده است.

نتیجه نهایی

بک‌اند با موفقیت داخل Docker Container اجرا شده است و با استفاده از Port Mapping می‌توان به آن دسترسی داشت. وضعیت اجرای Container نیز با دستور docker ps بررسی شده است.
