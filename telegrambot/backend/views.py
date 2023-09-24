from django.views import View
from django.http import JsonResponse
from backend.tasks import process_telegram_event
import json


class TelegramBotWebhookView(View):

    def post(self, request, *args, **kwargs):
        process_telegram_event.delay(json.loads(request.body))
        return JsonResponse({"ok": "POST request processed"})

    def get(self, request, *args, **kwargs):  # for debug
        return JsonResponse({"ok": "Get request received! But nothing done"})
