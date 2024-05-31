from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="İstifadəçi adı",
        error_messages={
            'required': "İstifadəçi adı daxil edilməlidir.",
            'max_length': "İstifadəçi adı 30 simvoldan çox ola bilməz."
        }
    )
    password = forms.CharField(
        max_length=10,
        label="Şifrə",
        widget=forms.PasswordInput,
        error_messages={
            'required': "Şifrə daxil edilməlidir.",
            'max_length': "Şifrə 10 simvoldan çox ola bilməz."
        }
    )

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=30,
        label="İstifadəçi adı",
        error_messages={
            'required': "İstifadəçi adı daxil edilməlidir.",
            'max_length': "İstifadəçi adı 30 simvoldan çox ola bilməz."
        }
    )
    password = forms.CharField(
        max_length=10,
        label="Şifrə",
        widget=forms.PasswordInput,
        error_messages={
            'required': "Şifrə daxil edilməlidir.",
            'max_length': "Şifrə 10 simvoldan çox ola bilməz."
        }
    )
    confirm = forms.CharField(
        max_length=10,
        label="Şifrəni təsdiqlə",
        widget=forms.PasswordInput,
        error_messages={
            'required': "Şifrəni təsdiqləməlisiniz.",
            'max_length': "Şifrəni təsdiqlə 10 simvoldan çox ola bilməz."
        }
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and len(username) < 5:
            raise forms.ValidationError("İstifadəçi adı ən azı 5 simvol olmalıdır.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 6:
            raise forms.ValidationError("Şifrə ən azı 6 simvol olmalıdır.")
        return password

    def clean_confirm(self):
        confirm = self.cleaned_data.get('confirm')
        password = self.cleaned_data.get('password')
        if password and confirm and password != confirm:
            raise forms.Val

