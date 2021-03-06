# Generated by Django 3.0.2 on 2020-03-13 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0003_auto_20200313_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='')),
                ('edition', models.IntegerField(default=0)),
                ('publication_year', models.IntegerField(default=0)),
                ('authors', models.ManyToManyField(to='authors.Author')),
            ],
        ),
    ]
