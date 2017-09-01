from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = form.save(commit=False)
			# Set the chosen password
			new_user.set_password(form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			return render(request,'acc/register_done.html',{'new_user': new_user})
	else:
		form = UserRegistrationForm()
	return render(request,'acc/register.html',{'form': form})


@login_required
def profile(request):
	return render(request, 'acc/home.html')