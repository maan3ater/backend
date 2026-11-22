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






طراحی Test Case و CI/CD Pipeline پروژه Backend

1. معرفی پروژه

این پروژه یک Backend ساده با Python و Flask است که با استفاده از Pytest تست می‌شود. همچنین GitHub Actions برای اجرای خودکار تست‌ها و Docker برای ساخت Image استفاده شده است.

2. پنج Test Case

شماره	تست	نتیجه مورد انتظار
1	درخواست GET به /	Status 200
2	درخواست GET به /health	Status 200
3	درخواست به مسیر نامعتبر	Status 404
4	درخواست POST به /	Status 405
5	بررسی پیام صفحه اصلی	Backend is running successfully!

3. نمودار CI/CD Pipeline

Developer
    |
    v
GitHub Repository
    |
    v
GitHub Actions
    |
    v
Install Python
    |
    v
Install Dependencies
    |
    v
Run 5 Test Cases
    |
  +---+---+
  |       |
 PASS    FAIL
  |       |
  v       v
Docker   Stop
Build    Pipeline
  |
  v
Success

4. مراحل Pipeline

1. دریافت کد از GitHub
2. نصب Python و کتابخانه‌ها
3. اجرای پنج تست با Pytest
4. در صورت موفقیت، ساخت Docker Image
5. پایان Pipeline

5. مرحله شکست تست

اگر یکی از تست‌ها شکست بخورد، GitHub Actions وضعیت Failed نمایش می‌دهد و مرحله Docker Build اجرا نمی‌شود. پس از اصلاح خطا، Pipeline دوباره اجرا خواهد شد.

6. ارتباط Docker با CI/CD

Docker برنامه و وابستگی‌های آن را در قالب یک Image بسته‌بندی می‌کند. در این پروژه، پس از موفقیت تست‌ها، Docker Image ساخته می‌شود تا برنامه در محیط‌های مختلف به شکل یکسان اجرا شود.

7. نتیجه‌گیری

در این پروژه با استفاده از Pytest و GitHub Actions تست‌های Backend به‌صورت خودکار اجرا می‌شوند. Docker نیز پس از موفقیت تست‌ها، Image پروژه را می‌سازد. این فرآیند باعث شناسایی سریع خطاها و افزایش کیفیت نرم‌افزار می‌شود.

توجه: در این پروژه ساخت Docker Image انجام می‌شود، اما Deploy خودکار پیاده‌سازی نشده است.
