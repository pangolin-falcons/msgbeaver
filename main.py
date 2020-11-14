from conversations import Conversations
import boto3
from botocore.exceptions import ClientError

region = "us-east-1"

originationNumber = "+19706237718"
destinationNumber = "+19378421922"

message = ("We cannot deny or confirm.")
applicationId = "f1dcce6b6bcd4e789ad5609e847a3941"
messageType = "PROMOTIONAL"

registeredKeyword = "HELP"

senderId = "msgbeaver"

client = boto3.client('pinpoint',region_name=region)

try:
    response = client.send_messages(
        ApplicationId=applicationId,
        MessageRequest={
            'Addresses': {
                destinationNumber: {
                    'ChannelType': 'SMS'
                }
            },
            'MessageConfiguration': {
                'SMSMessage': {
                    'Body': message,
                    'Keyword': registeredKeyword,
                    'MessageType': messageType,
                    'OriginationNumber': originationNumber,
                    'SenderId': senderId
                }
            }
        }
    )

except ClientError as e:
    print(e.response['Error']['Message'])
else:
    print("Message sent! Message ID: "
            + response['MessageResponse']['Result'][destinationNumber]['MessageId'])