import json

def response(message, status_code):
    return {
        'statusCode': str(status_code),
        'body': json.dumps(message),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
            },
        }

def lambda_handler(event, context):
    try:
        return response({'message': 'SUCCESS'}, 200)
    except Exception as e:
        return response({'message': e.message}, 400)
        
