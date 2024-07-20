from django.shortcuts import render,redirect

def home(request):
      return render(request,'dashboard/Home.html')


def register(request):
    if request.method=='POST':
        form=UserRegistrationform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Account Created For {username} Successfully")
            return redirect("login")
    else:
        form=UserRegistrationform()
    context={
        'form':form
    }

    return render(request,'superuse/register.html',context)

# Create your views here.
