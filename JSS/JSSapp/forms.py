from django import forms
from .models import Jasoseol, Comment

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol
        fields = ('title', 'content',)
    # 폼 커스텀하기 (기본호출함수 init 활용)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목" # title의 label값 수정
        self.fields['content'].label = "자기소개서 내용"
        self.fields['title'].widget.attrs.update({
            'class': 'jss_title', # class 속성 추가 -> css 적용
            'placeholder': '제목', # placeholder 속성 추가
        })
        self.fields['content'].widget.attrs.update({
            'class': 'jss_content_form', # class 속성 추가 -> css 적용
        })

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content', )