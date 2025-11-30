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
py -m django --version
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
>
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
>
> [!nOTE]
> Url nó giống như một cầu nối để **kết nối** các views lại với nhau

Chúng nằm ở trong file `urls.py` **cùng thư mục** với file `views.py` và có format như sau:

```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'), # views.members thì members phải là tên view, không phải tên app
]
```

> [!Caution]
> Việc kết nối này mới chỉ có quy mô nằm trong **nội bộ app** thôi. Ta cần phải kết nối file này với file `urls.py` tổng **nằm ngay dưới** thư mục chính của project với format như sau:
>
> ```py
> from django.contrib import admin
> from django.urls import include, path
>   
> urlpatterns = [
>   path('', include('members.urls')), # Cái này mới là tên app :)
>   path('admin/', admin.site.urls),
> ]
> ```

Lúc này thì khi chạy dự án thì nó sẽ ra kết quả *Hello World*

TEMPLATE
---
- Template là những trang html giúp phản hồi lại các yêu cầu http từ người dùng
- Nó nằm trong thư mục template và thư mục đó cũng **nằm trong** app members

Ta tạo tạm một file `index.html` như sau
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hello</h1>
    Ta vừa mới tạo xong một template rồi đó
</body>
</html>
```
Sau đó, ta chỉnh sửa phản hồi trong phần views như sau:
```py
from django.shortcuts import render
from django.http import HttpResponse

def members(request):
     return render(request, 'index.html')
```
> [!caution]
> Nếu chúng ta muốn thực hiện những dự án phức tạp hơn thì ta phải thêm app vào trong `setting.py` để hệ thống dễ dàng kiểm soát bằng cách thêm tên app vào phần `INSTALLED_APP[]`

Sau đó thì ta chạy lệnh sau
```
python manage.py makemigration
python manage.py migrate
```
MODEL
-
Một class là một cái bảng trong databasse