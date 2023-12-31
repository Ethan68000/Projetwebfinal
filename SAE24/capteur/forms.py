from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class CapteurForm(ModelForm):
    class Meta:
        model = models.Capteur
        fields = "__all__"


class DonneesForm(ModelForm):
    class Meta:
        model = models.Donnees
        fields = "__all__"