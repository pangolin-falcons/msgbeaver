import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv
load_dotenv()

class SendSMS:

    def __init__(self):
        region = "us-east-1"
        self.client = boto3.client('pinpoint', region_name=region)

    def send(self, phoneNum, message):

        originationNumber = "+19706237718"
        destinationNumber = phoneNum

        applicationId = os.getenv("APP_ID")
        messageType = "PROMOTIONAL"

        registeredKeyword = "HELP"

        senderId = "msgbeaver"

        try:
            response = self.client.send_messages(
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
            return ["Failure", e.response['Error']['Message']]
        else:
            return ["Success", response['MessageResponse']['Result'][destinationNumber]['MessageId']]