import email
from multiprocessing import context
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
from django.utils import timezone
from .forms import SignUpForm
from .models import User,OtpProfile
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
import random as r
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self): 
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
       
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()      
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def getName(request):
    
#     if request.method == 'POST':
       
#         form = NameForm(request.POST)
       
#         if form.is_valid():
            
#             return HttpResponseRedirect('/thanks/')

#     else:
#         form = NameForm()

#     return render(request, 'polls/name.html', {'form': form})

def your_name(request):
    return HttpResponse('Thanku')

def contactForm(request):
    if request.method == 'POST':
        get_otp = request.POST.get('otp')
        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)
            if int(get_otp) == OtpProfile.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.save()
                return HttpResponseRedirect('/login/')

        form = SignUpForm(request.POST)
        if form.is_valid():
            
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name').split(' ')
            
            otp=""
            for i in range(4):
                otp+=str(r.randint(1,9))
            print ("Your One Time Password is ")
        

            usr = User.objects.get(username=username)
            # import pdb;pdb.set_trace()
            print(usr)
            usr.email = username
            # print(usr.email)
            # print(email)
            # print(usr)
            usr.first_name = name[0]
            if len(name) > 1:
                usr.last_name = name[1]
            usr.is_active = False
            print(usr.password)
            usr.save()
            OtpProfile.objects.create(user = usr, otp = otp)
            recipients = ['abhijeetss21398@gmail.com']
            mess = f"Hello {usr},\nYour OTP is {otp}\nThanks!"
            # message1 = "your one time otp is "+otp
            send_mail("Email Verifications", mess, email, recipients)
            print('post')
            return render(request, 'polls/name.html',{'otp':True,'usr': usr})
    else:
        form = SignUpForm()
        print('get')
    return render(request, 'polls/name.html', {'form': form})


def loginpage(request):    
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse('polls:index'))
        else:
            return HttpResponse("Login failed")
    return render(request, 'polls/login.html')
# def otpVerification(request):
#     otp = request.session['otp']
#     context = {'otp':otp}
#     print(context)
#     return render(request, 'polls/verifications.html',context)

#def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#     # return HttpResponse("Hello, world. You're at the polls index.")

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
