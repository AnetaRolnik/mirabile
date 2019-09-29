from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'photo', 'published_date',)
        widgets = {
            'published_date': DateTimePickerInput(),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Tytuł'
        self.fields['photo'].label = 'Zdjęcie'
        self.fields['published_date'].label = 'Data publikacji'