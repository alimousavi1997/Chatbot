import json
import boto3

# connection to bedrock
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        user_message = body.get("message", "")

        # Input for model Nova
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"text": user_message}
                    ]
                }
            ],
            "inferenceConfig": {
                "maxTokens": 200,
                "temperature": 0.7
            }
        }

        response = bedrock.invoke_model(
            modelId="amazon.nova-lite-v1:0",   # Later Claude maybe
            contentType="application/json",
            accept="application/json",
            body=json.dumps(payload)
        )

        result = json.loads(response["body"].read())
        reply = result["output"]["message"]["content"][0]["text"]

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"reply": reply})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
