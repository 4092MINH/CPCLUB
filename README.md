SETUP DJANGO
===
---
*Nguồn: W3S*

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
Một class trong model là một cái bảng trong databasse

TẠO MỘT MODEL
-
Trước tiên, trong Member ta mở file và ghi đoạn sau
```py
from django.db import models

class ModelMember(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
```
- Mục đầu tiên là `firstname` là một `CharField` chứa firstname
- `lastname` tương tự

Sau khi tạo xong một model thì ta thực hiện cặp lệnh makemigrations vào

---
DJANGO ADMIN
=
---
Django Admin là công cụ tuyệt vời giúp chúng ta thay đổi database một cách dễ dàng hơn

TẠO TÀI KHOẢN VÀ TRUY CẬP VÀO ADMIN SITE
-
Thực hiện lệnh sau
```
python manage.py createsuperuser
```
Và chúng ta điền thông tin vào

Sau đó, ta chạy dự án và ở url ta thêm `/admin` là đến giao diện đăng nhập

CÁCH THÊM MODEL
-
Chúng ta ghi đoạn code sau
```py
from django.contrib import admin
from .models import ModelMember
# Register your models here.

# minhpnk - Homnayemdotnha@23

admin.site.register(ModelMember)
```
Lúc này, khi quay lại thì ta đã thấy phần cập nhật member

CÁCH THAY ĐỔI NHÃN MODEL
-
Rất đơn giản, ta chỉ cần thêm một hàm `__str__()` vào trong model là ok
```py
from django.db import models

# Create your models here.
class ModelMember(models.Model):
    ho = models.CharField(max_length=255)
    ten = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ho} {self.ten}"
```
CÁCH THAY ĐỔI GIAO DIỆN CỦA TRANG ADMIN
---
Ta có thể dùng `admin.site` để thay đổi giao diện như `title`, `header`, `index_title`
```py
from django.contrib import admin
from .models import Member

admin.site.site_header = "Hệ thống quản lý học sinh"
admin.site.site_title = "Quản lý học sinh"
admin.site.index_title = "Chúc một ngày tốt lành"
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'student_id', 'diem_cong', 'slug']
    search_fields = ['name', 'email', 'student_id']
    prepopulated_fields = {'slug': ('name',)} # Auto-generate slug from name field

admin.site.register(Member, MemberAdmin)
```

CÁCH THÊM MỤC HIỂN THỊ VÀ MỤC TÌM KIẾM
-
Tạo một hàm tên là `MemberAdmin()` và làm như sau
```py
from django.contrib import admin
from .models import ModelMember

class MemberAdmin(admin.ModelAdmin):
    list_display = ('codeforces_id', 'org')
    search_fields = ('ho', 'ten', 'codeforces_id')
admin.site.register(ModelMember, MemberAdmin)
```

TỪ MODEL CHO ĐẾN SẢN PHẨM
=
Bài này sẽ giúp chúng ta cách trình bày dữ liệu từ model lên html

TẠO TEMPLATE
-
Sau khi tạo model, thì ta làm một file html như sau

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Học sinh trong lớp thầy Thái</h1>
    <ul>
        {% for x in hocsinh %}
            <li>{{x.ho}} {{x.ten}}</li> <!--Cái này ta gọi là biến-->
        {% endfor %} <!--Những cái trong %% được gọi là Django Tag-->
    </ul>
</body>
</html>
```

CHỈNH SỬA VIEW
-
Ta phải bỏ model vào view. Trong file views ta phải import tên model và gửi nó sang template như sau:
```py
from django.shortcuts import render
from django.http import HttpResponse
from .models import ModelMember

def members(request):
     hocsinh = ModelMember.objects.all()
     return render(request, 'index.html', {'hocsinh': hocsinh})
```
CÁCH TẠO PAGE THÔNG TIN CHI TIẾT
=
TEMPLATE
-
Ta vẫn cứ làm như cũ
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Học sinh trong lớp thầy Thái</h1>
    <ul>
        {% for x in hocsinh %}
            <li>{{x.ho}} {{x.ten}}</li>
        {% endfor %}
    </ul>

</body>
</html>
```
VIEWS
-
Ta thêm hàm mới như sau
```py
def detail(request, member_id): # Đây là id mà lệnh sẽ gửi vào
    member = ModelMember.objects.get(id=member_id) # Nó sẽ lấy lệnh tương ứng
    return render(request, 'detail.html', {'hocsinh': member})
```
URLS
-
Ta cũng thêm đường link nhưng mà ta chỉnh sửa một chút
```py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.members),
    path('detail/<int:member_id>', views.detail, name='member_detail'),
]
```
CÁCH ẤN VÀO TÀI KHOẢN THÌ NÓ HIỂN THỊ THÔNG TIN
-
Ta chỉnh sửa như sau. Cụ thể, ta thêm một cái `<a>` với đường link tương ứng là được
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Học sinh trong lớp thầy Thái</h1>
    <ul>
        {% for x in hocsinh %}
            <li><a href="detail/{{x.id}}">{{x.ho}} {{x.ten}}</a></li>
        {% endfor %}
    </ul>

</body>
</html>
```
CÁCH DEPLOY DỰ ÁN
=
Ta dùng Render để chạy code django

CHUẨN BỊ
-
### Cài Gunicorn (Web Server) và Whitenoise (Quản lý file tĩnh):

```
pip install gunicorn whitenoise
```

### TẠO FILE `requirements.txt`
```
pip freeze > requirements.txt
```
### CẤU HÌNH `settings.py`
```py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Thêm dòng này
    # ... các dòng khác
]
```
### CẤU HÌNH STATIC FILES
```py
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```
### CHO PHÉP HOST
```py
ALLOWED_HOSTS = ['*'] # Hoặc tên miền render sau khi tạo (ví dụ: 'app-name.onrender.com')
DEBUG = False # Khi chạy thật phải tắt Debug
```
### TẠO FILE `build.sh`
```
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```