from django import forms
from .models import RatingTableOne,RatingTableTwo

class RatingTableOneForm(forms.ModelForm):
    class Meta:
      model = RatingTableOne
      fields ='__all__'


class RatingTableTwoForm(forms.ModelForm):
    class Meta:
      model = RatingTableTwo
      fields ='__all__'  