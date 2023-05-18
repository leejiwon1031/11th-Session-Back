from django.contrib import admin
from .models import Blog,Comment,HashTag      # (from .models import * 로 해도 됑)

#Register your models here.
admin.site.register(Blog)       #Blog 모델을 장고 Admin에 등록
# Register your models here.
admin.site.register(Comment)
admin.site.register(HashTag)