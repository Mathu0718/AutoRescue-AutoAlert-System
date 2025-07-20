import boto3
import json
import datetime

sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('accident_logs')

# Simulated hospital mapping
hospital_lookup = {
    "Location A": "hospitalA.nearby@example.com",
    "Location B": "hospitalB.nearby@example.com",
    "Location C": "hospitalC.nearby@example.com"
}

def handler(event, context):
    data = json.loads(event['body']) if 'body' in event else event

    vibration = data.get("vibration", False)
    deformation = data.get("deformation", False)
    airbag = data.get("airbag", False)
    location = data.get("location", "")

    if (vibration and deformation) or airbag:
        hospital_email = hospital_lookup.get(location, "fallback@example.com")
        timestamp = datetime.datetime.now().isoformat()

        sns.publish(
            TopicArn='arn:aws:sns:YOUR_REGION:YOUR_ACCOUNT_ID:accident-alerts',
            Message=f"🚨 Accident detected at {location}!\n"
                    f"Vibration: {'✅' if vibration else '❌'}\n"
                    f"Deformation: {'✅' if deformation else '❌'}\n"
                    f"Airbag: {'✅' if airbag else '❌'}\n"
                    f"Time: {timestamp}",
            Subject="AutoRescue Alert"
        )

        table.put_item(Item={
            'id': timestamp,
            'location': location,
            'vibration': vibration,
            'deformation': deformation,
            'airbag': airbag,
            'email_sent': hospital_email,
            'timestamp': timestamp,
            'status': 'Alert Sent'
        })

        return { "statusCode": 200, "body": json.dumps({ "message": "🚨 Alert Sent to hospital!" }) }

    else:
        return { "statusCode": 200, "body": json.dumps({ "message": "No emergency detected." }) }
