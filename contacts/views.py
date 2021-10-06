from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Checagem dos campos:

        # Verifica se o usuário já enviou uma pergunta antes:
        if request.user.is_authenticated:
            # Queremos saber se o usuário fez uma pergunta para o imóvel em questão:
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request,
                               'You already have made an inquiry to this listing')
                return redirect('/listings/'+listing_id)

        Contact.objects.create(listing=listing, listing_id=listing_id,
                               name=name, email=email, phone=phone, message=message, user_id=user_id)

        # Envia um e-mail ao vendedor do respectivo imóvel, informando quanto a pergunta feita:
        send_mail(
            'Property listing inquiry',
            f'There has been an inquiry for {listing}. Please, sign into de admin panel for more information.',
            'btretest@gmail.com',
            [realtor_email, 'nunes.237@hotmail.com'],
            fail_silently=False
        )

        messages.success(
            request, 'Your request has been submitted, a realtor will get back to you soon.')
        return redirect('/listings/'+listing_id)
