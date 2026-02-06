import json
import boto3

def lambda_handler(event, context):
    user_input = event['inputTranscript']
    if user_input.lower() in ['hello', 'hi']:
        return {
            'dialogAction': {
                'type': 'Close',
                'fulfillmentState': 'Fulfilled',
                'message': {'contentType': 'PlainText', 'content': 'Hello! How can I assist you today?'}
            }
        }
    else:
        return {
            'dialogAction': {
                'type': 'Close',
                'fulfillmentState': 'Fulfilled',
                'message': {'contentType': 'PlainText', 'content': 'I’m here to help with cloud computing queries.'}
            }
        }
    def lambda_handler(event, context):
    user_input = event.get('inputTranscript', '').strip().lower()
    responses = {
        'hello': 'Hello! How can I assist you today?',
        'hi': 'Hello! How can I assist you today!',
        'default': "I’m here to help with cloud computing queries."
    }
    response = responses.get(user_input, responses['default'])
    return {
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {'contentType': 'PlainText', 'content': response}
        }
    }