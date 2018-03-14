from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import json

@csrf_exempt
def slackPost(request):
    try:
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
            
            response = {"message":"hello world"}
            return JsonResponse(response)
    except:
        pass
def home(request):
    return HttpResponse("hello world")