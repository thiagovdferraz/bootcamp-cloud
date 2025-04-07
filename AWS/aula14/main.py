import boto3
import json

# Criar o cliente SNS
sns_client = boto3.client('sns', region_name='us-east-1')

# Criar a mensagem JSON
message = {
    "nome": "tferraz",
    "aula": "aula14-teste-enviar-via-python-protocol-email",
}

# Publicar a mensagem no tópico SNS
response = sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:398128123123892388932:sns-topico-aula14',
    Message=json.dumps(message)
)

print(response)