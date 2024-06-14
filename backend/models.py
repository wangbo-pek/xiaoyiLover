from django.db import models


# 文章
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=1024)
    is_display = models.CharField(max_length=2, choices=((0, 'hidden'), (1, 'display')))
    updated_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    # 文章 1:1 文章信息
    article_info = models.OneToOneField(to='Article_Info', on_delete=models.CASCADE)
    # 2级分类 1:n 文章
    sub_category = models.ForeignKey(to='Sub_Category', on_delete=models.CASCADE)
    # 文章 n:n 标签
    tag = models.ManyToManyField(to='Tag')

    def __str__(self):
        return f'{self.article_id}|{self.title}'


# 文章信息
class Article_Info(models.Model):
    article_info_id = models.AutoField(primary_key=True)
    content_text = models.TextField()
    content_html = models.TextField()
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    reprinted_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.article_info_id}|{self.article}'


# 日记
class Diary(models.Model):
    diary_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    weather = models.CharField(max_length=64)
    temperature = models.IntegerField
    mood = models.CharField(max_length=32)
    cover = models.CharField(max_length=256)
    diary_text = models.TextField()
    diary_html = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.diary_id}|{self.title}'


# 文章分类
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.category_id}|{self.category_name}'


# 文章2级分类
class Sub_Category(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    sub_category_name = models.CharField(max_length=32)
    # 1级分类 1:n 2级分类
    category = models.ForeignKey(to='Category', to_field='category_id', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sub_category_id}|{self.sub_category_name}'


# 标签
class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tag_id}|{self.tag_name}'


# 我的信息
class Master(models.Model):
    master_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    gender = models.CharField(max_length=2, choices=((0, 'male'), (1, 'female')))
    mail = models.CharField(max_length=128)
    auth_code = models.CharField(max_length=64, default='xiaoyi')


# 访客信息
class Guest(models.Model):
    guest_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)


# 留言
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=4056)
    created_date = models.DateTimeField(auto_now_add=True)
    is_display = models.CharField(max_length=2, choices=((0, 'hidden'), (1, 'display')))
    # 访客 1:n 留言
    guest = models.ForeignKey(to='Guest', to_field='guest_id', on_delete=models.CASCADE)


# 评论
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=4056)
    created_date = models.DateTimeField(auto_now_add=True)
    is_display = models.CharField(max_length=2, choices=((0, 'hidden'), (1, 'display')))
    # 访客 1:n 评论
    guest = models.ForeignKey(to='Guest', to_field='guest_id', on_delete=models.CASCADE)
    # 文章 1:n 评论
    article = models.ForeignKey(to='Article', to_field='article_id', on_delete=models.CASCADE)


# coffee
class Coffee(models.Model):
    coffee_id = models.AutoField(primary_key=True)
    coffee_fee = models.DecimalField(max_digits=20, decimal_places=2)
    coffee_date = models.DateTimeField(auto_now_add=True)
    # 访客 1:n 捐赠
    guest = models.ForeignKey(to='Guest', to_field='guest_id', on_delete=models.CASCADE)
