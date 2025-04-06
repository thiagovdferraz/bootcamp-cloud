import boto3

# Criando o cliente SQS
sqs = boto3.client('sqs')

# URL da fila SQS
queue_url = 'https://sqs.us-west-2.amazonaws.com/242172718396/minha-fila-aula13-sqs'

# Recebendo mensagens da fila
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=10,  # Número máximo de mensagens a receber
    WaitTimeSeconds=10       # Tempo máximo de espera (em segundos)
)

# Verificando se há mensagens recebidas
if 'Messages' in response:
    for message in response['Messages']:
        print(f"Mensagem recebida: {message['Body']}")
        
        # Excluindo a mensagem da fila após o processamento
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )
        print(f"Mensagem excluída: ID {message['MessageId']}")
else:
    print("Nenhuma mensagem disponível na fila.")