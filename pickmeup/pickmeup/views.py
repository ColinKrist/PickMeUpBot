from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from . import sensitive_settings
from . import watson_tone
from slackclient import SlackClient
import json
from threading import Thread
#set up global instance of SlackReplyClient
sc = SlackClient(sensitive_settings.SECRET_POST_KEY)

@csrf_exempt
def slackPost(request):
    byte_string = request.body
    my_raw_json = byte_string.decode('utf8').replace("'",'"') #replace outer ' with "
    print(my_raw_json)
    post_data = json.loads(my_raw_json)

    if(post_data['type']=="url_verification"):
        if(post_data['token'] == settings.VERIFY_TOKEN): 
            return JsonResponse({"challenge":post_data['challenge'],"token":post_data['token']})
        else:
            return HttpResponse('500')

    if(post_data['type'] == "event_callback"):
        if('bot_id' in post_data['event']):
            print('bot message - ignoring')
            return HttpResponse(status="200")
        else:
            t = Thread(target=watson_tone.analyzeMessageAndPostToChat,args=[post_data,sc])
            t.start()
    return HttpResponse(status="200")

def home(request):
    return HttpResponse("hello world")