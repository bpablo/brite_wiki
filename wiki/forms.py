from django import forms
from .models import ObsField
import numpy as np

#display a pick list for obs field

class SelectFieldForm(forms.Form):
    using = 'brite_obs'
    field = forms.ModelChoiceField(
        label = 'Select Field',
        queryset = ObsField.objects.none()
    )

    def __init__(self, *args, **kwargs):
        super(SelectFieldForm, self).__init__(*args)
        #query db to get fields for drop down menu
        self.fields['field'].queryset = ObsField.objects.using(self.using).filter()





class UploadFileForm(forms.Form):
    report = forms.FileField(
        required=True,
        label = 'BRITE Observations'
        )

    def __init__(self,*args, **kwargs):
#        self.request = kwargs.pop('request', None)
        super(UploadFileForm, self).__init__(*args)

    def clean(self):
        cleaned_data = super(UploadFileForm, self).clean()

        return cleaned_data

    # def parse_file(self):
    #     # load in file and put into a format to be handle_uploaded_file
    #     records = np.loadtxt(self, delimiter=',', type = 'str', skiprows=1,  columns=[1,2,3,4,6,8,9,20])
    #
    #     print(records[0])
    #
    #     return records
#class UploadFieldForm(forms.Form):

#    title = forms.CharField(max_length=50)
#    file = forms.FileField()
