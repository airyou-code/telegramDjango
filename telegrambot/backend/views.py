from django.views import View
from django.http import JsonResponse
from telegram import Update
import json
from bot import dispatcher
from bot.main import bot
# from django.conf import settings
# from users.models import Person


def process_telegram_event(update_json):
    update = Update.de_json(update_json, bot)
    dispatcher.process_update(update)


class TelegramBotWebhookView(View):
    # WARNING: if fail - Telegram webhook will be delivered again.
    # Can be fixed with async celery task execution
    def post(self, request, *args, **kwargs):
        # process_telegram_event(json.loads(request.body))

        # e.g. remove buttons, typing event
        return JsonResponse({"ok": "POST request processed"})

    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request received! But nothing done"})

# class WebhookAPIView(APIView):

#     @csrf_exempt
#     def post(self, request):

#         data = request.data
#         update = telegram.Update.de_json(
#             data, telegram.Bot(settings.TELEGRAM_TOKEN)
#         )

#         user = update.message.from_user
#         person, created = Person.objects.update_or_create(
#             tg_id=user.id,
#             defaults={
#                 "first_name": user.first_name,
#                 "username": user.username,
#                 "is_bot": user.is_bot,
#                 "language_code": user.language_code,
#                 "link": user.link,
#                 "name": user.name,
#             }
#         )
#         message = update.message.text
#         chat_id = update.message.chat.id

#         async def send_telegram_message(chat_id, message):
#             bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
#             await bot.sendMessage(chat_id=chat_id, text=message)

#         asyncio.run(send_telegram_message(chat_id, message))
#         return HttpResponse('ok')
