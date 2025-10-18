import boto3

# If needed, set region explicitly:
# dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

# Insert a second record
table.put_item(Item={
    'StudentID': 'S002',
    'Name': 'Jane Smith',
    'Age': 22,
    'Department': 'Mathematics'
})

# Read it back
resp = table.get_item(Key={'StudentID': 'S002'})
print(resp['Item'])
