from django.forms import ModelForm
from .models import Fighting

class FightingForm(ModelForm):
  class Meta:
    model = Fighting
    fields = ['date', 'villain']