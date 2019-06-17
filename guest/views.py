from django.shortcuts import redirect, render
from django.views.generic import CreateView,TemplateView,ListView,UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from .decorators import permission_required
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.cache import never_cache


from .models import User,Guest
from .forms import StudentSignUpForm


# Create your views here.

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def home(request):
    # if request.user.is_authenticated:
    #     if request.user.is_teacher:
    #         return redirect('teachers:quiz_change_list')
    #     else:
    #         return redirect('students:quiz_list')
    return render(request, 'classroom/home.html')


# @method_decorator(login_required, name='dispatch')
# @method_decorator(login_required, name='dispatch')
# @permission_required(user.has_perm('guest.view_post'), login_url="/account/login/")
# @method_decorator(never_cache, name='dispatch')
# @method_decorator([login_required, student_required], name='dispatch')
# @method_decorator([login_required], name='dispatch')
# @login_required
# @method_decorator(login_required, name='dispatch')
# @method_decorator(user_passes_test(lambda user: user.is_superuser))
# @permission_required('polls.can_vote', login_url="/login/")
@method_decorator([login_required],name='dispatch')
class ProfileHomeView(ListView):

    
    # fields = ('productname','brandid','categoryid','status')
    # list_editable = ['status']
    # list_per_page = 20
    # ordering = ['addeddate']
    # search_fields = ['productname']
    # actions = [activate_status,deactivate_status]
    # model = Guest
    # context_object_name = 'guest' 

    def get_queryset(self):
        # return Guest.objects.filter(title__icontains='war')[:5]
        return Guest.objects.all()[:5]
        


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        # kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')    

