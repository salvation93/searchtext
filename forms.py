from django import forms

from search.models import Articles

# form class
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['topic','body','author']