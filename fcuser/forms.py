from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=32, label='사용자 이름')
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        },
        widget=forms.PasswordInput, label='비밀번호')

    def clean(self):
        # super()는 메소드 오버라이딩 
        cleaned_data = super().clean()  # 값이 들어있는지 검사한다. 들어잇으면 아래 변수를 할당, 없으면 실패하고 튕군다. 
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:
                self.add_error('username', '등록되지 않은 아이디입니다.')
                return
                    
            if not check_password(password, fcuser.password):
                self.add_error('password', '비밀번호를 틀렸습니다.')

            else:
                self.user_id = fcuser.id