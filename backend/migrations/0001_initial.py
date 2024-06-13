# Generated by Django 4.2.13 on 2024-06-13 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('subtitle', models.CharField(max_length=1024)),
                ('is_display', models.CharField(choices=[(0, 'hidden'), (1, 'display')], max_length=2)),
                ('content_text', models.TextField()),
                ('content_html', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Article_Info',
            fields=[
                ('article_info_id', models.AutoField(primary_key=True, serialize=False)),
                ('read_count', models.IntegerField(default=0)),
                ('comment_count', models.IntegerField(default=0)),
                ('like_count', models.IntegerField(default=0)),
                ('reprinted_count', models.IntegerField(default=0)),
                ('updated_date', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(choices=[(1, 'coding'), (2, 'product'), (3, 'english')], max_length=2)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('diary_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('weather', models.CharField(max_length=64)),
                ('mood', models.CharField(max_length=32)),
                ('cover', models.CharField(max_length=256)),
                ('diary_text', models.TextField()),
                ('diary_html', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('guest_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('master_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[(0, 'male'), (1, 'female')], max_length=2)),
                ('mail', models.CharField(max_length=128)),
                ('auth_code', models.CharField(default='xiaoyi', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=32)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('sub_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(max_length=32)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.category')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('message_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=4056)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_display', models.CharField(choices=[(0, 'hidden'), (1, 'display')], max_length=2)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.guest')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=4056)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_display', models.CharField(choices=[(0, 'hidden'), (1, 'display')], max_length=2)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.article')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.guest')),
            ],
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('coffee_id', models.AutoField(primary_key=True, serialize=False)),
                ('coffee_fee', models.DecimalField(decimal_places=2, max_digits=20)),
                ('coffee_date', models.DateTimeField(auto_now_add=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.guest')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_info',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='backend.article_info'),
        ),
        migrations.AddField(
            model_name='article',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.sub_category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='backend.tag'),
        ),
    ]