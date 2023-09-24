from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from backend.views import TelegramBotWebhookView
# from django.http import HttpResponse

# curl -F "url=https://a0ec-86-49-182-250.ngrok.io/webhook/" https://api.telegram.org/bot\1963236028:AAFOxSiJgx2v64Bmno_VcYBBhJGNE1xSLz4/setWebhook


# urlpatterns = [
#     path(
#         'super_secter_webhook/',
#         csrf_exempt(TelegramBotWebhookView.as_view())
#     ),
# ]
