from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from django import forms
from .models import Post

CHOICES= [
    ('now','Opublikuj teraz'),
    ('later','Zaplanuj na później')
]

class PostForm(forms.ModelForm):
    manage_post = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id' : 'managePost'}))

    class Meta:
        model = Post
        fields = ('title', 'photo', 'manage_post', 'published_date',)
        widgets = {
            'published_date': DateTimePickerInput(attrs={'id' : 'publishedDate'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['manage_post'].label = 'Zarządzaj swoim postem'