from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

# Create your models here.
class Pembicara(models.Model):
    Nama = models.CharField(max_length=100)
    panggilan = models.CharField(max_length=30, blank=True)
    Slug = models.SlugField(default='', editable=False, max_length=140)
    Pekerjaan = models.CharField(max_length=100)
    Perusahaan = models.CharField(max_length=100)
    Deskripsi_singkat = models.TextField(blank=True)
    Foto = models.ImageField(upload_to='web/')
    Email = models.EmailField(blank=True)
    Facebook = models.URLField(blank=True)
    Twitter = models.URLField(blank=True)
    Linkedin = models.URLField(blank=True)
    Instagram = models.URLField(blank=True)
    Keterangan = models.TextField(blank=True)
    keynote = models.BooleanField(default=True)

    def __str__(self):
        return self.Nama

    class Meta:
        verbose_name = ("Pembicara")
        verbose_name_plural = ("Pembicara")

    def save(self, *args, **kwargs):
        value = self.Nama
        self.Slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Event(models.Model):
    Judul = models.CharField(max_length=100)
    Slug = models.SlugField(default='', editable=False, max_length=140)
    Mulai = models.DateTimeField()
    Selesai = models.DateTimeField(blank=True)
    Pembicara = models.ForeignKey(Pembicara, on_delete=models.PROTECT ,null=True)
    Lokasi = models.TextField(blank=True)
    Link = models.URLField(blank=True)
    Keterangan = models.TextField(blank=True)

    def __str__(self):
        return self.Judul

    class Meta:
        verbose_name = ("Acara")
        verbose_name_plural = ("Acara")

    def save(self, *args, **kwargs):
        value = self.Judul
        self.Slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def waktu(self):
        return self.Mulai.strftime('%d-%B-%Y')
    def jammulai(self):
        return self.Mulai.strftime('%H:%M')
    def jamselesai(self):
        return self.Selesai.strftime('%H:%M')


class Artikel(models.Model):
    Judul = models.CharField(max_length=150)
    Slug = models.SlugField(default='', editable=False, max_length=140)
    Tanggal = models.DateField(null=True)
    Isi = HTMLField()
    tags = TaggableManager()

    def __str__(self):
        return self.Judul

    class Meta:
        verbose_name = ("Artikel")
        verbose_name_plural = ("Artikel")

    def save(self, *args, **kwargs):
        value = self.Judul
        self.Slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Sponsor(models.Model):
    UNIVERSITY = '0'
    CORPORATE = '1'
    MEDIA = '2'

    KATEGORI_CHOICES = (
        (UNIVERSITY, 'University Sponsors'),
        (CORPORATE, 'Corporate Sponsors'),
        (MEDIA, 'Media Sponsors'),
    )

    nama = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='web/logosponsor')
    kategori = models.CharField(max_length=1, choices=KATEGORI_CHOICES, default=0)
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return self.nama

class team(models.Model):
    nama = models.CharField(max_length=100)
    panggilan = models.CharField(max_length=30, blank=True)
    jabatan = models.CharField(max_length=150, blank=True)
    foto = models.ImageField(upload_to='web/teams/', blank=True)
    keterangan = models.TextField(blank=True)
    no_urut = models.PositiveIntegerField(blank=True)
    scientific_coord = models.BooleanField(default=False)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name = ("team")
        verbose_name_plural = ("teams")