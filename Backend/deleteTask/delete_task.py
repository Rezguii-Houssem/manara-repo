import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTasks')

def lambda_handler(event, context):
    user_id = 'default-user'  # In production, extract from auth context
    task_id = event['pathParameters']['taskId']
    
    if not task_id:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({'error': 'Task ID is required'})
        }
    
    try:
        table.delete_item(
            Key={
                'userId': user_id,
                'taskId': task_id
            }
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({'message': 'Task deleted successfully'})
        }
    except Exception as e:
        print(f'Error deleting task: {e}')
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({'error': 'Could not delete task'})
        }