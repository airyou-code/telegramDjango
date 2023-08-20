from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from main.models import Person
import asyncio
import telegram


class McDonaldCuponGenAPIView(APIView):

    @csrf_exempt
    def post(self, request):
        data = request.data
        return HttpResponse('rabotaet')


class WebhookAPIView(APIView):

    @csrf_exempt
    def post(self, request):

        data = request.data
        update = telegram.Update.de_json(
            data, telegram.Bot(settings.TELEGRAM_TOKEN)
        )

        user = update.message.from_user
        person, created = Person.objects.update_or_create(
            tg_id=user.id,
            defaults={
                "first_name": user.first_name,
                "username": user.username,
                "is_bot": user.is_bot,
                "language_code": user.language_code,
                "link": user.link,
                "name": user.name,
            }
        )
        message = update.message.text
        chat_id = update.message.chat.id

        async def send_telegram_message(chat_id, message):
            bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
            await bot.sendMessage(chat_id=chat_id, text=message)

        asyncio.run(send_telegram_message(chat_id, message))
        return HttpResponse('ok')
