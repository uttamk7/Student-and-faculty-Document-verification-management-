# Generated by Django 2.1.4 on 2020-03-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docapp', '0002_upload_docs_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='document_result',
            name='uploaded_status',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]