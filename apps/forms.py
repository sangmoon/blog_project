# form about Article
from django import forms
from .models import Article, CATEGORY_CHOICES


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'category', 'content',)
        exclude = ('user', 'created_at', 'updated_at',)
        widgets = {
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'title',
                'class': 'form-control input-md',
            }),

            'category': forms.fields.Select(attrs={
                'choices': CATEGORY_CHOICES,
                'class': 'form-control input-md'
            }),

            'content': forms.Textarea(attrs={
                'placeholder': 'content',
                'class': 'form-control input-md',
            }),
        }
