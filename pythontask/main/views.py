from django.shortcuts import render
from django.views.generic import View
from .models import Appointment, Task
from django.core.mail import send_mail
from django.shortcuts import redirect
from datetime import datetime
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Главная страница', 'taska': tasks})


def about(request):
    return render(request, 'about.html')


# create
def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)



# Отправка писем по электронной почте
class AppointmentView(View):
    # Обрабатываем get-запрос
    def get(self, request, *args, **kwargs):
        return render(request, 'mails.html')

    # Обрабатываем post-запрос
    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.POST['date'], "%Y-%m-%d"),
            client_name=request.POST['client_name'],
            message=request.POST['message'],
        )
        appointment.save()

        send_mail(
            subject=f'{appointment.client_name}: {appointment.date.strftime("%S-%m-%d")}',
            message=appointment.message,
            from_email='imaralievasadbek@yandex.ru',
            recipient_list=['imaraliev.kg2005@gmail.com']

        )

        return redirect('mails:mails')

