import boto3
from botocore.exceptions import ClientError

import urllib.request
import json


def http(event):
    url = event['url']
    response = urllib.request.urlopen(url)

    return json.loads(response.read())

def telnet(event):
    import telnetlib

    HOST = event.get('host', 'towel.blinkenlights.nl')
    PORT = event.get('port', None)

    try:
        tn = telnetlib.Telnet(HOST, PORT)
        response = {'success':str(tn.read_some())}

    except ConnectionRefusedError as error:
        response = {'error':str(error)}

    return response


def lambda_handler(event, context):
    if 'action' in event:
        if event['action'] == 'telnet':
            response = telnet(event)
        else:
            response = {'error':'unknown action', event:event}
            
    else:
        response = http(event)
        
        
    return response
