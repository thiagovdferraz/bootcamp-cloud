import boto3

# Criando o cliente SQS
sqs = boto3.client('sqs')

# URL da fila SQS
queue_url = 'https://sqs.us-west-2.amazonaws.com/242172718396/minha-fila-aula13-sqs'

# Enviando uma mensagem para a fila
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Mensagem de exemplo para minha-fila-standard'
)

# Exibindo o ID da mensagem enviada
print(f"Mensagem enviada com sucesso! ID da mensagem: {response['MessageId']}")