from django.shortcuts import render
from mainmenu.models import coustmers
from mainmenu.forms import coustmer_form


# Create your views here.

def home(request):

    success_message=""

    if request.method=='POST':

        forms=coustmer_form(request.POST)

        if forms.is_valid():

            forms.save()

            success_message="BOOKING CONFIRMED"

            forms=coustmer_form()

    else:
        forms=coustmer_form()

    return render(request,'mainmenu/index.html',{'forms':forms,'success_message':success_message})
    
def coustmer1(request):
    data=coustmers.objects.all()
    return render(request,'mainmenu/register.html',{'data':data})
    
def homepage(request):
     return render (request,"mainmenu/home.html")
    

    # def bookingpage(request):
    #     return render (request,"mainmenu/booking.html")
    

def contactpage(request):
    return render (request,"mainmenu/contact.html")
    

def aboutpage(request):
        return render (request,"mainmenu/about.html")
    

# def registerpage(request):
#         return render (request,"mainmenu/register.html")
