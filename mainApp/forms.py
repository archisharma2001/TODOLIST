#used an API for form creation
from django.forms import ModelForm 
from mainApp.models import TODO


class TODOForm(ModelForm):
    class Meta:
        model= TODO
        fields= ['title', 'status', 'priority']