# Generated by Django 3.0.7 on 2020-06-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(help_text='Unique category page URL.', unique=True)),
                ('description', models.TextField()),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=500, verbose_name='Meta Description')),
                ('meta_keywords', models.CharField(help_text='Comma separated set to SEO keywords for meta tag', max_length=500, verbose_name='Meta Keywords')),
                ('category_status', models.IntegerField(choices=[(0, 'Active'), (1, 'InActive')], default=0)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(help_text='Unique market page URL.', unique=True)),
                ('description', models.TextField()),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=500, verbose_name='Meta Description')),
                ('meta_keywords', models.CharField(help_text='Comma separated set to SEO keywords for meta tag', max_length=500, verbose_name='Meta Keywords')),
                ('market_status', models.IntegerField(choices=[(0, 'Active'), (1, 'InActive')], default=0)),
            ],
            options={
                'verbose_name_plural': 'Markets',
                'db_table': 'markets',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text='Unique product page URL.', unique=True)),
                ('description', models.TextField()),
                ('meta_description', models.CharField(help_text='Content for description meta tag', max_length=500, verbose_name='Meta Description')),
                ('meta_keywords', models.CharField(help_text='Comma separated set to SEO keywords for meta tag', max_length=500, verbose_name='Meta Keywords')),
                ('sku', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.BooleanField(default=True)),
                ('weigth', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('image_url', models.CharField(max_length=500)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('quantity', models.IntegerField()),
                ('product_status', models.IntegerField(choices=[(0, 'Active'), (1, 'InActive')], default=0)),
                ('categories', models.ManyToManyField(to='catalogueApp.Category')),
                ('markets', models.ManyToManyField(to='catalogueApp.Market')),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-created_date'],
            },
        ),
    ]
