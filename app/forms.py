from django import forms
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.forms import ModelForm
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from app.models import Product, Women, Men, User, Contact
from app.token import account_activation_token


class ProductModelForm(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class WomenModelForm(ModelForm):

    class Meta:
        model = Women
        fields = '__all__'


class MenModelForm(ModelForm):

    class Meta:
        model = Men
        fields = '__all__'

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=155)

    def clean_email(self):
        email = self.data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('This email not found')
        return email

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=155)
    email = forms.EmailField()
    password = forms.CharField(max_length=55)
    confirm_password = forms.CharField(max_length=55)

    def clean_email(self):
        email = self.data.get('email')
        if User.objects.filter(email=email):
            raise ValidationError('This email already exists')
        return email

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('confirm password is wrong')
        return password

    def save(self):
        user = User.objects.create_user(
            email=self.data.get('email'),
            password=self.data.get('password')
        )

        user.save()

def send_email(email, request, _type):

    user = User.objects.get(email=email)
    subject = 'Activate your account'
    current_site = get_current_site(request)
    message = render_to_string('app/auth/active_message.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(str(user.pk))),
        'token': account_activation_token.make_token(user),
    })

    from_email = EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    print('Send to MAIL')


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'