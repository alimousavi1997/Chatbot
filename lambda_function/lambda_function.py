import json

def lambda_handler(event, context):
    # فقط یه پیام ساده برمی‌گردونه
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": "Hello from CatBot Lambda!"
        })
    }
