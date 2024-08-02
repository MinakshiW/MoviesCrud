from django import forms
from .models import Movie

r = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

s = [
    ('Published', 'Published'),
    ('Not Published', 'Not Published'),
]

g = [
    ('Horror', 'Horror'),
    ('Action', 'Action'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Comedy', 'Comedy'),
    ('Thriller', 'Thriller'),
]

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

        labels = {
            'id': 'ID',
            'title' : 'Movie Title',
            'review' : 'Review Content',
            'created_at' : 'Created At',
            'email' : 'Reviewer E-mail ID',
        }

        widgets = {
            'id' : forms.NumberInput(attrs={'class': 'form-control'}),
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'director' : forms.TextInput(attrs={'class': 'form-control'}),
            'review' : forms.Textarea(attrs={'class': 'form-control', 'style': 'height:100px'}),
            'rating' : forms.RadioSelect(choices = r),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=s, attrs={'class': 'form-control'}),
            'genre': forms.Select(choices=g, attrs={'class': 'form-control'}),
        }