from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('get_token/', views.getToken),

    # 获取所有文章、分类、标签
    path('get_all_articles/', views.getAllArticles),
    path('get_all_category/', views.getAllCategory),
    path('get_all_tag/', views.getAllTag),

    # 创建文章
    path('create_article/', views.createArticle)

]
