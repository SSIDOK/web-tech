from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm


def contact_us_page(request):
    # return render(request, 'contact/contact_us.html')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                'Повідомлення від користувача',
                f'Ім\'я: {name}\nЕлектронна адреса: {email}\nПовідомлення: {message}',
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )
            form.save()
            return redirect('contact:contact_us_page')
    else:
        form = ContactForm()

    return render(request, 'contact/contact_us.html', {'form': form})
