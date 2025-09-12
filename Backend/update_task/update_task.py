import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTasks')

def lambda_handler(event, context):
    user_id = 'default-user'  # In production, extract from auth context
    task_id = event['pathParameters']['taskId']
    task_data = json.loads(event['body'])
    
    if not task_id:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({'error': 'Task ID is required'})
        }
    
    # Build update expression
    update_expression = 'SET updatedAt = :updatedAt'
    expression_attribute_values = {
        ':updatedAt': datetime.utcnow().isoformat()
    }
    
    if 'title' in task_data:
        update_expression += ', title = :title'
        expression_attribute_values[':title'] = task_data['title']
    
    if 'description' in task_data:
        update_expression += ', description = :description'
        expression_attribute_values[':description'] = task_data['description']
    
    if 'completed' in task_data:
        update_expression += ', completed = :completed'
        expression_attribute_values[':completed'] = task_data['completed']
    
    try:
        response = table.update_item(
            Key={
                'userId': user_id,
                'taskId': task_id
            },
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expression_attribute_values,
            ReturnValues='ALL_NEW'
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps(response['Attributes'])
        }
    except Exception as e:
        print(f'Error updating task: {e}')
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({'error': 'Could not update task'})
        }