from django.shortcuts import render, HttpResponseRedirect
import matplotlib.pyplot as plt
from testform.forms import ContactForm,GuestForm
from guest.models import Guest
from django.contrib.auth.decorators import permission_required, login_required,user_passes_test
from django.views.decorators import csrf
# Create your views here.


@login_required
# @csrf
# @permission_required('is_staff')
@user_passes_test(lambda user: user.is_guest)
def contuct(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            guestPost = form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."
            guestPost.image = request.FILES['image']
            guestPost.author = request.user # Set the user object here
            guestPost.save() # Now you can send it to DB

            # guest = Guest(author_id=request.user.id)
            # form.author_id=request.user.id
            # form.save()
            # guest = Guest()
            # guest = Guest(image =request.FILES['image'] ,descriptin = "hello",author_id=request.user.id)
            # guest = Guest(descriptin = "hello",author_id=1)
            # guest.save()

            return HttpResponseRedirect('/contuct/guestlist/')
    else:        
        form = GuestForm()

    return render(request, 'contuct.html', {'form': form})

def guestList(request):
    guests = Guest.objects.all()
    return render(request, 'guestlist.html', {'guests': guests})


