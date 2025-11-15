SETUP DJANGO
===
---
CÁC LỆNH CHECK PHIÊN BẢN
---

### PYTHON

```
python --version
```

### PIP

```
pip --version
```

### DJANGO

```
django-admin --version
```
CÁC LỆNH TẢI VỀ
---

### PIP

```
python get-pip.py
```

> [!Caution] 
> Phải tải [gói pip](https://quantrimang.com/url?u=aHR0cHM6Ly9ib290c3RyYXAucHlwYS5pby9nZXQtcGlwLnB5) hoặc [gói pip cho python 3.2](https://quantrimang.com/url?u=aHR0cHM6Ly9ib290c3RyYXAucHlwYS5pby8zLjIvZ2V0LXBpcC5weQ%3D%3D) về trước 

### TẢI VỀ DJANGO

```
python -m pip install django
```
---
SETUP DỰ ÁN
===
---
TẠO DỰ ÁN MỚI
---
```
django-admin startproject <Name project>
```
CHẠY DỰ ÁN
---
```
python manage.py runserver
```
Sau đó ấn vào đường link mà terminal phản hồi

TẠO APP
---
```
python manage.py startapp <Name app>
```
---
MODEL-VIEW-TEMPLATE-URL
===
---
VIEW
---
> [!Note]
> View là tập hợp những hàm chuyên phụ trách xử lý cách yêu câu http

Chúng được tạo ở trong file `views.py` và có format như sau:
```py
from django.shortcuts import render

# Create your views here.
```
Hãy thử thay thế nó bằng nội dung như sau
```python
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
     return HttpResponse("Hello world!")
```
Khi này thì nếu bạn **gọi hàm** này ra thì nó sẽ **phản hồi** thông điệp *Hello World*
> [!Warning]
> Hiện giờ nó vẫn chưa hiện phản hồi đâu. Nếu muốn hiện thì phải dùng một thứ làm cầu nối

URL
---
> [!nOTE]
> Url nó giống như một cầu nối để **kết nối** các views lại với nhau

Chúng nằm ở trong file `urls.py` **cùng thư mục** với file `views.py` và có format như sau:
```py
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]
```
> [!Caution]
> Việc kết nối này mới chỉ có quy mô nằm trong **nội bộ app** thôi. Ta cần phải kết nối file này với file `urls.py` tổng **nằm ngay dưới** thư mục chính của project với format như sau:
> ```py
> from django.contrib import admin
> from django.urls import include, path
>   
> urlpatterns = [
>   path('', include('members.urls')),
>   path('admin/', admin.site.urls),
> ]
> ```

Lúc này thì khi chạy dự án thì nó sẽ ra kết quả *Hello World*