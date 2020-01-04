from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from django import forms
from .models import Post

CHOICES= [
    ('now','Opublikuj teraz'),
    ('later','Zaplanuj post')
]

class PostForm(forms.ModelForm):
    manage_post = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id' : 'managePost'}))

    class Meta:
        model = Post
        fields = ('photo', 'title', 'manage_post', 'published_date',)
        widgets = {
            'published_date': DateTimePickerInput(attrs={'id' : 'publishedDate', 'placeholder' : 'Wybierz datę'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['manage_post'].label = 'Zarządzaj swoim postem'