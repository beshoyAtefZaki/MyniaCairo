from django.shortcuts import render
from django import forms
# Create your views here.
from .models import Cars_Models ,UserMode



TRIPKIND= (
        ("1","المنيا"),
        ("2","القاهرة")
        )
# create form
def find_alpha(st):
    for i in st :
        if i.isalpha() == True:
            return False
    if len(st) != 11:
            return False
    return True
class RegisterForm(forms.Form):
    user_name = forms.CharField(
                        widget=forms.TextInput(
                        attrs={"class":"form-control" ,
                                "placeholder":"user name"}))
    phone_number = forms.CharField(
                        widget=forms.TextInput(
                        attrs={"class":"form-control" ,
                                "placeholder":"Phone Number"}))
    car_model = forms.ChoiceField(choices=UserMode ,
                        widget=forms.Select(
                        attrs={"class":"form-control" ,
                                }))
    datel =  forms.DateTimeField(widget=forms.DateTimeInput(format="dd/mm/yyyy",
                    attrs={"type": "date" ,
                    "date-format":"dd/mm/yyyy",
                    "value":"2018-07-22"} ) ,
                     input_formats="dd/mm/yyyy")

    start_range  = forms.TimeField(widget=forms.TimeInput(attrs={"type": "time" },format='%H:%M'))
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not find_alpha(phone_number) :
            raise forms.ValidationError("Error Phone Number ")
        return phone_number

class CreateJuornyForm(forms.Form):
    user_name = forms.CharField(
                        widget=forms.TextInput(
                        attrs={"class":"form-control" ,
                                "placeholder":"user name"}))
    phone_number = forms.CharField(
                        widget=forms.TextInput(
                        attrs={"class":"form-control" ,
                                "placeholder":"Phone Number"}))
    car_model = forms.ChoiceField(choices=Cars_Models ,
                        widget=forms.Select(
                        attrs={"class":"form-control" ,
                                }))
    go_from = forms.ChoiceField(choices=TRIPKIND ,
                        widget=forms.Select(
                        attrs={"class":"form-control" ,
                                }))
    journey_kind = forms.ChoiceField(choices=UserMode ,
                        widget=forms.Select(
                        attrs={"class":"form-control" ,
                                }))
    date =  forms.DateTimeField(widget=forms.DateTimeInput(format="dd/mm/yyyy",
                    attrs={"class":"form-control",
                    "type": "date" ,
                    "date-format":"dd/mm/yyyy",
                      } ) ,
                     input_formats="dd/mm/yyyy")
    start_range  = forms.TimeField(widget=forms.TimeInput(
                                        attrs={"class":"form-control","type": "time"} ,
                                        format='%H:%M'))
    end_range  = forms.TimeField(widget=forms.TimeInput(
                                        attrs={"class":"form-control","type": "time"} ,
                                        format='%H:%M'))



    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not find_alpha(phone_number) :
            raise forms.ValidationError("Error Phone Number ")
        return phone_number
#create Home page
#under development
def home(request):
    home_page = "home.html"
    content = {
    }
    return render(request ,home_page,content)





def user_register(request):
    form = CreateJuornyForm(request.POST or None)
    if form.is_valid():
        print (form.cleaned_data)
    content = {
    "form":form
    }
    return render (request,"createjuorny.html",content)

def createjuorny(request):
    pass
