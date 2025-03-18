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
    dob_validator = RegexValidator(
        regex=r'^(19[0-9]{2}|20[0-2][0-9])-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$',
        message="Format tanggal lahir harus YYYY-MM-DD dan usia minimal 12 tahun."
    )
    tanggal_lahir = forms.CharField(
        label="Tanggal Lahir",
        max_length=10,
        validators=[dob_validator]
    )
    
    # 4. Nomor HP: hanya boleh angka, tanpa tanda '+' atau '-' dengan panjang 8-15 digit
    phone_number_validator = RegexValidator(
        regex=r'^62\d{7,13}$',
        message="Nomor HP harus dimulai dengan '62' dan berisi 8-15 digit angka (contoh: 621234567890)."
    )
    nomor_hp = forms.CharField(
        label="Nomor HP",
        max_length=15,
        validators=[phone_number_validator]
    )

    # 5. Email: menggunakan EmailField bawaan Django
    email_validator = RegexValidator(
        regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        message="Masukkan email yang valid, contoh: user@example.com"
    )
    email = forms.CharField(
        label="Email",
        max_length=255,
        validators=[email_validator]
    )
    
    # 6. URL Blog: menggunakan URLField bawaan Django
    url_validator = RegexValidator(
        regex=r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\/?$',
        message="Masukkan URL yang valid, contoh: http://example.com"
    )
    url_blog = forms.CharField(
        label="URL Blog",
        max_length=255,
        validators=[url_validator]
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
        try:
            dob = datetime.datetime.strptime(tanggal, "%Y-%m-%d").date()
            today = datetime.date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 12:
                raise ValidationError("Usia minimal harus 12 tahun.")
        except ValueError:
            raise ValidationError("Format tanggal tidak valid. Gunakan format YYYY-MM-DD.")
        return tanggal
