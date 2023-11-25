from django import forms
from app_satoc.models import OriginalFolderSource, FinalFileName

# class Form_OriginalFolderSource(forms.ModelForm):
#     class Meta:
#         model = OriginalFolderSource
#         fields = '__all__'

# class Form_FinalFileName(forms.ModelForm):
#     class Meta:
#         model = FinalFileName
#         fields = '__all__'
#         print(fields)



from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['first_name', 'last_name', 'email', 'company', 'role_job_title']