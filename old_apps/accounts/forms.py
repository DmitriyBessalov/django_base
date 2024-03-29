from django import forms
from .models import Category
from django.core.exceptions import ValidationError


class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField(required=False)

    CHOICES = (
        ('qg', '22'),
        ('33', '44'),
        ('45', '55'),
    )

    cat = forms.ChoiceField(choices=CHOICES, required=False)
    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    Countries = forms.MultipleChoiceField(choices=CHOICES, widget=forms.SelectMultiple)

    date1 = forms.DateField(label="Дата", widget=forms.DateInput(attrs={'type': 'date'}))
    file = forms.FileField(required=False)


class AddPostModelForm(forms.ModelForm):

    class Meta:
        model = Category
        # fields = "__all__"
        fields = ['name', 'slug', 'content', 'is_published', 'cat', 'like', 'Countries', 'date1', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'like': forms.RadioSelect(),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('Длина превышает 20 символов')
        return title
