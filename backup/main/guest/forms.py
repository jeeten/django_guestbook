from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.auth.models import Group

# from classroom.models import (Answer, Question, Student, StudentAnswer,Subject, User)

from .models import User, Guest


# class TeacherSignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_teacher = True
#         if commit:
#             user.save()
#         return user


def signupForm(request):
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
    return render(request, 'signup.html', {'form': form})


class StudentSignUpForm(UserCreationForm):
    # UserCreationForm.renderer()
    # interests = forms.ModelMultipleChoiceField(
    #     # queryset=Subject.objects.all(),
    #     queryset = None,
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_guest = True
        user.is_staff = True
        user.save()
        group = Group.objects.get(name='Post Master')
        user.groups.add(group)
        # guset = Guest.objects.create(user=user)
        # guest.interests.add(*self.cleaned_data.get('interests'))
        return user


# class StudentInterestsForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('interests', )
#         widgets = {
#             'interests': forms.CheckboxSelectMultiple
#         }


# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ('text', )


# class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
#     def clean(self):
#         super().clean()

#         has_one_correct_answer = False
#         for form in self.forms:
#             if not form.cleaned_data.get('DELETE', False):
#                 if form.cleaned_data.get('is_correct', False):
#                     has_one_correct_answer = True
#                     break
#         if not has_one_correct_answer:
#             raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')


# class TakeQuizForm(forms.ModelForm):
#     answer = forms.ModelChoiceField(
#         queryset=Answer.objects.none(),
#         widget=forms.RadioSelect(),
#         required=True,
#         empty_label=None)

#     class Meta:
#         model = StudentAnswer
#         fields = ('answer', )

#     def __init__(self, *args, **kwargs):
#         question = kwargs.pop('question')
#         super().__init__(*args, **kwargs)
#         self.fields['answer'].queryset = question.answers.order_by('text')
