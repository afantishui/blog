# 简介
基于 Python3.6 + Django2.1.7 仿制[stormsha个人博客](https://stormsha.com/)

## 博客效果
[afanti.fun](afanti.fun)

## 功能介绍，相对简单

- Django 自带的后台管理系统，加入富文本编辑
- 文章分类、标签
- 文章评论系统
- 强大的全文搜索功能，只需要输入关键词就能展现全站与之关联的文章
- Sitemap 网站地图

## 运行项目
- 环境准备（python3.6 mysql 不在此处详说）
- 下载源码
-  安装依赖
```
pip install -r requriements.txt 
```
- 修改blog/setting.py的数据库配置

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
            # 服务器ip
            'HOST': '*.*.*.186',
            'PORT': '3306',
            #数据库账号密码
            'USER': '***',
            'PASSWORD': '******',
            # 数据库名
            'NAME': 'blog',
            # 避免映射数据库时出现警告
            'OPTIONS': {
                'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
                'charset': 'utf8mb4',
            },
    }
}
```
- 创建mysql数据库，可借助Navicat，数据库信息与setting配置一致
- 创建数据库后进行数据库迁移

```
python manage.py makemigrations sign
python manage.py migrate
```
- 运行项目，然后访问 服务器ip:8000
```
python manage.py runserver  0.0.0.0:8000
```
- 创建超级管理员，然后可以登录管理后台 服务器ip:8000/admin

```
- python manage.py createsuperuse
```
## 搭建教程

- [stormSha个人博客](https://stormsha.com/)

## 搭建过程的问题
- 1.[后台管理加入富文本](http://47.106.82.186/article/13/)
- 待更

## Nginx+uWSGI 部署
- 待更
