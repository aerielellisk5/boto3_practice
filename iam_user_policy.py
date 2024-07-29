# Create a script to manage IAM (Identity and Access Management) users and policies:

# Create a new IAM user. **CHECK**
# Attach a managed policy to the user (e.g., AmazonS3ReadOnlyAccess). **CHECK**
# Create and attach an inline policy to the user to allow specific actions (e.g., list and get objects in a specific S3 bucket). **CHECK**
# List the policies attached to the user.
import os
import json
import boto3
client = boto3.client('iam')

# print(os.access('./created_policy.json', os.R_OK))
# create a user
def create_user(userName):
  response = client.create_user(
    UserName=userName
  )
  print(f'the user {userName} is created')

# delete a user
def delete_user(userName):
  response = client.delete_user(
    UserName = userName
  )
  print(f'the user {userName} was deleted')


# Attach a managed policty to the user
def attach_policy_to_user(userName, policy):
  response = client.attach_user_policy(
    UserName = userName,
    PolicyArn = f'arn:aws:iam::aws:policy/{policy}',
  )
  print(f'the {policy} was attached to the user, {userName}')
  print(response['ResponseMetadata']['HTTPHeaders']['date'])
  # response = {'ResponseMetadata': {'RequestId': '7aaa3873-25b5-4d23-9633-46b9f2626279', 'HTTPStatusCode': 200, 'HTTPHeaders': {'date': 'Mon, 29 Jul 2024 02:09:53 GMT', 'x-amzn-requestid': '7aaa3873-25b5-4d23-9633-46b9f2626279', 'content-type': 'text/xml', 'content-length': '212'}, 'RetryAttempts': 0}}
  
def create_policy(policyName, policyDocument): 
    with open('./created_policy.json', 'r') as file:
      policyDocument = json.load(file)
      print(file)
      
    policy_document_json = json.dumps(policyDocument)
    
    response = client.create_policy(
    PolicyName = policyName,
    PolicyDocument = policy_document_json,
    Path = '/',
  )
# path_to_json = './created_policy.json'    
# create_policy('list_and_get_s3', path_to_json)    



# Attach created policy to user

def attach_created_user_policy(userName, policyName, policyDocument):
  with open('./created_policy.json', 'r') as file:
      policyDocument = json.load(file)
      print(file)
      policy_document_json = json.dumps(policyDocument)
  
  response = client.put_user_policy(
    UserName = userName,
    PolicyName = policyName, 
    PolicyDocument = policy_document_json
  )
    
  print(userName)
  print(policyName)
  print(policyDocument)
  print('User policy was added')

path_to_json = './created_policy.json'   
# attach_created_user_policy('Aeriel', 'list_and_get_s3', path_to_json)  

# List the policies attached to the user
def list_user_attached_policies(userName):
  response = client.list_attached_user_policies(
    UserName = userName
  )
  # print(userName)
  # print('big item')
  # print(response['AttachedPolicies'])
  # print('Only Attached Policies')
  for item in response['AttachedPolicies']:
    print(item['PolicyName'])
    
  
  response2 = client.list_policiies
  
        

list_user_attached_policies('Aeriel')
#check by using an api call
# aws iam list-attached-user-policies \
#     --user-name Aeriel
#  confirmed this returns the object that something is attached
    




# Step 1: Create the user
# create_user('Aeriel')
# Step 1A: Add the ability to delete the user
# delete_user('Aeriel')
#Step 2: Attach a managed policy to the user
# attach_policy_to_user('Aeriel', 'AmazonS3ReadOnlyAccess')
# Step 3: Create and attach an inline policy to the user to allow specific actions
# path_to_json = './created_policy.json'
# create_policy('list_and_get_s3', path_to_json)
# Step 4: List all the user policies attached to that specific user

