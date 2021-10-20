# Generated by Django 3.1.4 on 2020-12-12 19:13

import django.core.files.storage
from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_productfile_user_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='C:\\Users\\Stephen\\Dropbox\\kcworkapps\\cfe_api_proj\\static_cdn\\protected_media'), upload_to=products.models.upload_product_file_loc),
        ),
    ]