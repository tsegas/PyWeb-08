# added form.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class PostForm(forms.Form):
   title = forms.CharField()
   content = forms.CharField(widget=forms.Textarea)

   def send_email(self):
       # send email using the self.cleaned_data dictionary
       pass