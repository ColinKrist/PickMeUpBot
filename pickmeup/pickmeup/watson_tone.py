from watson_developer_cloud import ToneAnalyzerV3

from . import sensitive_settings

from django.conf import settings #set the message threshold for the app here




def analyzeMessageAndPostToChat(data,slackClient):
    posting_channel = data['event']['channel']
    message = data['event']['text']
    tone_result = analyzeTone(message)
    bot_message = testingFormatMessage(message,tone_result)
    #formatMessage(message,tone_result)
    slackClient.api_call(
        "chat.postMessage",
        channel=posting_channel,
        text=bot_message
    )


def getToneData(message):
    tone_settings = sensitive_settings.creds['tone_analyzer']
    creds = tone_settings[0]['credentials']
    u = creds['username']
    p = creds['password']
    tone_check = ToneAnalyzerV3(
        version = "2017-09-21",
        username = u,
        password = p,
    )
    return tone_check.tone({"text":message})


def analyzeTone(message):
    thresh = settings.TONE_THRESHOLD
    toneData = getToneData(message)
    tones = {value['tone_name']: value['score'] for value in toneData['document_tone']['tones']}
    print(tones)
    maxToneValue = thresh
    maxTone = ""
    for tone in tones:
        if(tones[tone]>maxToneValue):
            maxTone,maxToneValue = tone,tones[tone]
            print("new maxTone: {}:{}".format(tone,tones[tone]))
    
    return {"tone":maxTone,"score":maxToneValue}


def testingFormatMessage(m,toneData):
    return ("Hey just wanted to say you message looked {}! Score: {} \nOriginal message: {}".format(toneData['tone'],toneData['score'],m))
