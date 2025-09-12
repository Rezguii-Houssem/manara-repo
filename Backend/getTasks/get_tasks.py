import json
import boto3
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTasks')

def lambda_handler(event, context):
    # Extract user ID from request
    user_id = event.get('queryStringParameters', {}).get('userId', 'default-user')
    
    try:
        response = table.query(
            KeyConditionExpression=Key('userId').eq(user_id)
        )
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps(response['Items'])
        }
    except Exception as e:
        print(f'Error fetching tasks: {e}')
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
            },
            'body': json.dumps({'error': 'Could not fetch tasks'})
        }