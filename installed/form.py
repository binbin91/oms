# -*- coding: utf-8 -*-
from django import forms
from installed.models import SystemInstall

class SystemInstallForm(forms.ModelForm):
    class Meta:
        model = SystemInstall
        exclude = ('install_date',)
        widgets = {
          'ip': forms.TextInput(attrs={'class': 'form-control'}),
          'hostname': forms.TextInput(attrs={'class': 'form-control'}),
          'macaddress': forms.TextInput(attrs={'class': 'form-control'}),
          'system_version': forms.TextInput(attrs={'class': 'form-control'}),
        }
