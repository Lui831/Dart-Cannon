import json
import requests
import datetime

def lambda_handler(event, context):
    print(event)
    
    res = requests.post(
            url='https://industrial.api.ubidots.com/api/v1.6/devices/pc-de-teste',
            headers={'Accept': 'application/json',
                "X-Auth-Token": "Token-Serjao-eh-maneiro123!"
            },
            json={
                "text-shot": {
                    "value": 69,
                    "context": {
                        "text": "Alvo encontrado! Agora: " + str(datetime.datetime.now()),
                        "img": "https://dupcyf4snobps.cloudfront.net/" + event["Records"][0]['s3']['object']['key']
                    }
                }
            },
        )
        
    print(res)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
