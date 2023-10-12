import json

THRESHOLD = .7


def lambda_handler(event, context):

    try:
        body = json.loads(event["body"])
        inferences = body.get("inferences", [])
        meets_threshold = max(inferences) > THRESHOLD

        if meets_threshold:
            return {
                'statusCode': 200,
                'body': json.dumps(event)
            }
        else:
            raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
    