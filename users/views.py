from django.shortcuts import render

from  django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.views.generic import CreateView

class UserCreationView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    context_object_name = 'user'
    success_url = '/'
@login_required
def profile(request):
    context = {'user': request.user}
    return render(request, 'users/profile.html', context)


