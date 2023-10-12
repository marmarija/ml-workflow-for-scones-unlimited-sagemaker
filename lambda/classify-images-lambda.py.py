import json
import boto3
import base64

# Fill this in with the name of your deployed model
ENDPOINT = "image-classification-2023-09-30-19-01-55-236"

runtime = boto3.Session().client('sagemaker-runtime')

def lambda_handler(event, context):
    # Decode the image data
    image = base64.b64decode(event["body"]["image_data"])
    
    # Invoke the endpoint using the SageMaker runtime client
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',
        Body=image
    )
    
    #event["body"]["inferences"] = response['Body'].read().decode("utf-8")
    inferences = json.loads(response['Body'].read().decode('utf-8'))
    event["body"]['inferences'] = [float(value) for value in inferences] 
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
#Reference: The use of Boto3 instead of sagemaker to create a runtime proposed by a session lead in the AWS AI & ML Scholarship Program Slack chat