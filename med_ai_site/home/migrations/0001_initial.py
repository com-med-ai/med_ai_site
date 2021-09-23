# Generated by Django 3.2.7 on 2021-09-23 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=32, verbose_name='Ad')),
                ('surname', models.TextField(max_length=32, verbose_name='Soyad')),
                ('email', models.EmailField(max_length=254, verbose_name='Mail Adresi')),
                ('phone_number', models.TextField(max_length=13, verbose_name='Telefon Numarası')),
                ('auth', models.TextField(choices=[('PRI_MNG', 'Başkan'), ('COO_MNG', 'Başkan Yardımcısı'), ('ECO_COO', 'Mali Koordinatör'), ('PR_COOR', 'PR Koordinatörü'), ('GEN_SEC', 'Genel Sekreter'), ('CONTRO', 'Denetim Kurulu Üyesi'), ('CON_MNG', 'Denetim Kurulu Başkanı'), ('PY_COOR', 'Python Developer Team Koordinatörü'), ('BCK_COO', 'Backend Developer Team Koordinatörü'), ('FRO_COO', 'Frontend Developer Team Koordinatörü'), ('DOC_COO', 'Documenter Team Koordinatörü'), ('DES_COO', 'Designer Team Koordinatörü'), ('GUI_COO', 'GUI Developer Team Koordinatörü'), ('PY_MEMB', 'Python Developer Team Aktif Üyesi'), ('BCK_MEM', 'Backend Developer Team Aktif Üyesi'), ('FRO_MEM', 'Frontend Developer Team Aktif Üyesi'), ('DOC_MEM', 'Documenter Team Aktif Üyesi'), ('DES_MEM', 'Designer Team Aktif Üyesi'), ('GUI_MEM', 'GUI Developer Team Aktif Üyesi'), ('MEMBERS', 'Üye')], default='MEMBERS', max_length=7, verbose_name='Üyelik Durumu')),
            ],
        ),
    ]