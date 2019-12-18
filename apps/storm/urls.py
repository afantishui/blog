from django.conf.urls import url
from .views import IndexView

# template_name 是指定使用的模板文件，传递给视图，进行数据渲染
urlpatterns = [
    url(r'^$', IndexView.as_view(template_name='index.html'), name='index')
]