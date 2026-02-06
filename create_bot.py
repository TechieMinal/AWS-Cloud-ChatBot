import boto3

def create_bot():
    client = boto3.client('lex-models')
    response = client.put_bot(
        name='ChatbotExample',
        description='Chatbot for enhancing cloud computing',
        locale='en-US',
        childDirected=False,
        intents=[
            {
                'intentName': 'GreetingIntent',
                'intentVersion': '$LATEST'
            }
        ],
        clarificationPrompt={
            'messages': [{'contentType': 'PlainText', 'content': 'Sorry, can you rephrase that?'}],
            'maxAttempts': 2
        },
        abortStatement={
            'messages': [{'contentType': 'PlainText', 'content': 'Sorry, I couldn’t understand.'}]
        },
        idleSessionTTLInSeconds=300
    )
    print("Lex bot created:", response)
    import boto3

def create_bot():
    try:
        client = boto3.client('lex-models')
        response = client.put_bot(
            name='ChatbotExample',
            description='Chatbot for enhancing cloud computing',
            locale='en-US',
            childDirected=False,
            intents=[
                {
                    'intentName': 'GreetingIntent',
                    'intentVersion': '$LATEST'
                }
            ],
            clarificationPrompt={
                'messages': [{'contentType': 'PlainText', 'content': 'Sorry, can you rephrase that?'}],
                'maxAttempts': 2
            },
            abortStatement={
                'messages': [{'contentType': 'PlainText', 'content': 'Sorry, I couldn’t understand.'}]
            },
            idleSessionTTLInSeconds=300
        )
        print("Lex bot created:", response)
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    create_bot()

if __name__ == "__main__":
    main()