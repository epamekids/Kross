class Registration(forms.Form):
    nickname = forms.CharField(label = "Your Nickname",required=True)
    firstname = forms.CharField(label ="First Name")
    lastname = forms.CharField(label ="Last Name")
    email = forms.EmailField(label ="Your Email Address",required=True)
