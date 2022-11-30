from django import forms



class PhotoForm(forms.Form):
    photo = forms.FileField(label="",required=True, 
                        widget=forms.FileInput(
                            attrs={
                                "name":"photo",
                                "type":"file",
                                "class": "form-control",
                                "id":"inputGroupFile04",
                                "aria-describedby":"inputGroupFileAddon04",
                                "aria-label":"Upload",
                            }))