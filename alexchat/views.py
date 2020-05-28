# import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#import csrf from CSRF protection
from django.views.decorators.csrf import csrf_exempt
#import df_library
from library.df_response_lib import *
# complex lookups with Q-objects
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
#import json to get json request
import json
from bankbranch.models import BankBranch

@csrf_exempt
def index(request):
    # request object
    req = json.loads(request.body)
    # getting the action from dialogflow
    get_action = req.get('queryResult').get('action')

    # Welcoming Note
    if get_action == 'input.welcome':
        tr = telegram_response()
        welcome_note = ''.join(
                    ["Hi! I'm Alex \n--An Open-Banking Agent-- \nI can help you with these services: \n\n",
                        ">> Find the nearest banking hall.\n",
                        ">> Locate the closest ATM point.\n" ,
                        ">> Help get bank USSD code."
                    ])
        get_reply = {'fulfillmentText' : '{}'.format(welcome_note)}

    if get_action == 'get_bank_suggestion':

        # Dialogflow Telegram Response Library
        tr = telegram_response()
        title = "Which of the banks is of interest to you?"
        quick_replies_list = ["firstbank", "UBA", "Access", "Union"]
        tr_quick_replies = tr.quick_replies(title, quick_replies_list)

        # Dialogflow Response library
        ff_response = fulfillment_response()
        ff_text = ff_response.fulfillment_text(title)
        ff_messages = ff_response.fulfillment_messages([tr_quick_replies])

        get_reply = ff_response.main_response(ff_text, ff_messages)

    if get_action == 'get_bank':
        # Dialogflow Telegram response
        get_intent_parameter = req.get('queryResult').get('parameters')
        get_bank_name_parameter = get_intent_parameter['bank_name']
        get_bankparams_location = get_intent_parameter['bank_location']

        # Get Bank and Location
        get_bank_and_location = getBankNameLocationQuery(get_bank_name_parameter, get_bankparams_location)
        get_reply = {'fulfillmentText' : '{}'.format(get_bank_and_location)}

        # return json response
    return JsonResponse(get_reply, safe=False)

def getBankNameLocationQuery(bank, locate):
    # get the branch
    try:
        location = BankBranch.objects.all().filter(bank__icontains = bank, location__icontains = locate)
        result = ''
        for filtered_location in location:
            result += '>> {}\n'.format(filtered_location.address)
    except ObjectDoesNotExist:
        result = 'The bank branch does not exist in this location.'

    return result



