from two.ol.views import ModelForm
from twodemo.demoapp.models import Demo

class DemoForm(ModelForm):
    class Meta:
        model = Demo

