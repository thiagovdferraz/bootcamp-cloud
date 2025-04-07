import boto3

# criar o cliente SNS
sns_client = boto3.client('sns', region_name='us-east-1')

# criar a mensagem formatada como string para o email
message = f"""
Olá,

Aqui estão os detalhes da aula de hoje:

Nome: Thiago Ferraz
Aula: aula14-sns

At.te,
Thiago Ferraz
DE
"""

# publicar a mensagem no tópico SNS
response = sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:0921398289747321783784123781378:sns-topico-aula14',
    Message=message,
    MessageAttributes={
        'email': {
            'DataType': 'String',
            'StringValue': 'Email format message'
        }
    }
)
print(response)