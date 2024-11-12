import boto3
import json

# Inicializando el cliente de DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('CorporateLog')

def list_logs_by_cpu(cpu_id):
    # Escaneo de la tabla
    response = table.scan()
    logs = response['Items']
    
    # Imprimir todos los logs para verificar los campos disponibles
    print("Todos los logs:")
    print(json.dumps(logs, indent=4, default=str))  # Se usa default=str para manejar objetos que no son serializables

    # Filtrando logs por CPU ID
    filtered_logs = [log for log in logs if 'CPUid' in log and log['CPUid'] == cpu_id]
    
    return filtered_logs

if __name__ == '__main__':
    cpu_id = '256165216163814'  # ID de CPU a filtrar
    logs = list_logs_by_cpu(cpu_id)
    
    # Retornando resultado en formato JSON
    print("Logs filtrados:")
    print(json.dumps(logs, indent=4, default=str))  # Se usa default=str para manejar objetos que no son serializables
