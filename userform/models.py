from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class User(models.Model):

    GOLONGAN_DARAH_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    nama = models.CharField(
        max_length=255,
        help_text="Nama hanya boleh mengandung huruf, angka, dan karakter . _ -"
    )
    password = models.CharField(max_length=255)
    tanggal_lahir = models.DateField(help_text="Usia minimal 12 tahun")
    nomor_hp = models.CharField(
        max_length=15,
        help_text="Format: kode negara - nomor telepon (minimal 8, maksimal 15 angka)"
    )
    email = models.EmailField(max_length=255)
    url_blog = models.URLField(max_length=255)
    deskripsi_diri = models.TextField(
        help_text="Minimal 5, maksimal 1000 karakter",
        max_length=1000
    )

    golongan_darah = models.CharField(
        max_length=3,
        choices=GOLONGAN_DARAH_CHOICES,
        help_text="Golongan darah harus berupa: A+, A-, B+, B-, O+, O-, AB+, atau AB-."
    )   

    no_polis_asuransi = models.CharField(
        max_length=10,
        help_text="Nomor polis harus terdiri dari 5 hingga 10 angka."
    )


    def __str__(self):
        return self.nama
