from django.db import models
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    class AuthS(models.TextChoices):
        MINISTER = 'PRI_MNG', _('Başkan')
        CO_MINISTER = 'COO_MNG', _('Başkan Yardımcısı')
        ECONOMIC_COORDINATOR = 'ECO_COO', _('Mali Koordinatör')
        PR_COORDINATOR = 'PR_COOR', _('PR Koordinatörü')
        SECRETARY = 'GEN_SEC', _('Genel Sekreter')
        CONTROLLER = 'CONTRO', _('Denetim Kurulu Üyesi')
        CONTROLLER_MANAGER = 'CON_MNG', _('Denetim Kurulu Başkanı')
        PY_DEV_TEAM_COORDINATOR = 'PY_COOR', _('Python Developer Team Koordinatörü')
        BACKEND_TEAM_COORDINATOR = 'BCK_COO', _('Backend Developer Team Koordinatörü')
        FRONTEND_TEAM_COORDINATOR = 'FRO_COO', _('Frontend Developer Team Koordinatörü')
        DOCER_TEAM_COORDINATOR = 'DOC_COO', _('Documenter Team Koordinatörü')
        DESIGNER_TEAM_COORDINATOR = 'DES_COO', _('Designer Team Koordinatörü')
        GUI_DEVELOPER_TEAM_COORDINATOR = 'GUI_COO', _('GUI Developer Team Koordinatörü')
        PY_DEV_TEAM_MEMBER = 'PY_MEMB', _('Python Developer Team Aktif Üyesi')
        BACKEND_TEAM_MEMBER = 'BCK_MEM', _('Backend Developer Team Aktif Üyesi')
        FRONTEND_TEAM_MEMBER = 'FRO_MEM', _('Frontend Developer Team Aktif Üyesi')
        DOCER_TEAM_MEMBER = 'DOC_MEM', _('Documenter Team Aktif Üyesi')
        DESIGNER_TEAM_MEMBER = 'DES_MEM', _('Designer Team Aktif Üyesi')
        GUI_DEVELOPER_TEAM_MEMBER = 'GUI_MEM', _('GUI Developer Team Aktif Üyesi')
        MEMBER = 'MEMBERS', _('Üye')
    name = models.TextField(max_length=32, verbose_name='Ad')
    surname = models.TextField(max_length=32, verbose_name='Soyad')
    email = models.EmailField(verbose_name='Mail Adresi')
    phone_number = models.TextField(max_length=13, verbose_name='Telefon Numarası')
    auth = models.TextField(max_length=7, choices=AuthS.choices, default=AuthS.MEMBER, verbose_name='Üyelik Durumu')


# Create your models here.
