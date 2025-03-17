from django import forms
from .models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import datetime

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    # 1. Nama: hanya boleh diisi huruf, angka, dan karakter ('.', '_', '-')
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9._-]+$',
        message='Nama hanya boleh mengandung huruf, angka, dan karakter . _ -'
    )
    nama = forms.CharField(
        label="Nama",
        max_length=255,
        validators=[name_validator]
    )
    
    # 2. Password: minimal 8 karakter, boleh mengandung huruf, angka, dan karakter spesial
    password_validator = RegexValidator(
        regex=r'^[\w!@#$%^&*()_+\-=\[\]{};:"\\|,.<>/?]+$',
        message='Password hanya boleh mengandung huruf, angka, dan karakter spesial'
    )
    password = forms.CharField(
        label="Password",
        max_length=255,
        min_length=8,
        widget=forms.PasswordInput,
        validators=[password_validator]
    )
    
    # 3. Tanggal Lahir: validasi usia minimal 12 tahun
    tanggal_lahir = forms.DateField(
        label="Tanggal Lahir",
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    # 4. Nomor HP: hanya boleh angka, tanpa tanda '+' atau '-' dengan panjang 8-15 digit
    nomor_hp_validator = RegexValidator(
        regex=r'^\d{8,15}$',
        message='Nomor HP harus terdiri dari 8 sampai 15 digit angka tanpa simbol seperti + atau -'
    )
    nomor_hp = forms.CharField(
        label="Nomor HP",
        max_length=15,
        validators=[nomor_hp_validator]
    )
    
    # 5. Email: menggunakan EmailField bawaan Django
    email = forms.EmailField(
        label="Email",
        max_length=255
    )
    
    # 6. URL Blog: menggunakan URLField bawaan Django
    url_blog = forms.URLField(
        label="URL Blog",
        max_length=255
    )
    
    # 7. Deskripsi Diri: minimal 5 karakter, maksimum 1000 karakter
    deskripsi_diri = forms.CharField(
        label="Deskripsi Diri",
        widget=forms.Textarea,
        min_length=5,
        max_length=1000
    )
    
    # 8. Golongan Darah (Dropdown dengan Predefined Value)
    golongan_darah_validator = RegexValidator(
        regex=r'^(A|B|O|AB)[+-]$',
        message="Golongan darah harus berupa: A+, A-, B+, B-, O+, O-, AB+, atau AB-."
    )

    golongan_darah = forms.CharField(
        label="Golongan Darah",
        max_length=3,
        validators=[golongan_darah_validator]
    )

    no_polis_asuransi_validator = RegexValidator(
        regex=r'^\d{5,10}$',
        message="Nomor polis harus terdiri dari 5 hingga 10 angka."
    )
    
    no_polis_asuransi = forms.CharField(
        label="No. Polis Asuransi",
        max_length=10,
        validators=[no_polis_asuransi_validator]
    )

    def clean_tanggal_lahir(self):
        tanggal = self.cleaned_data.get('tanggal_lahir')
        if tanggal:
            today = datetime.date.today()
            age = today.year - tanggal.year - ((today.month, today.day) < (tanggal.month, tanggal.day))
            if age < 12:
                raise ValidationError("Usia minimal harus 12 tahun.")
        return tanggal
