import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTasks')

def lambda_handler(event, context):
    user_id = 'default-user'  # In production, extract from auth context
    task_data = json.loads(event['body'])
    
    item = {
        'userId': user_id,
        'taskId': str(uuid.uuid4()),
        'title': task_data['title'],
        'description': task_data.get('description', ''),
        'completed': task_data.get('completed', False),
        'createdAt': datetime.utcnow().isoformat(),
        'updatedAt': datetime.utcnow().isoformat()
    }
    
    try:
        table.put_item(Item=item)
        
        return {
            'statusCode': 201,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps(item)
        }
    except Exception as e:
        print(f'Error creating task: {e}')
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({'error': 'Could not create task'})
        }