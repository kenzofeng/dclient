import boto3

aws_client = boto3.client('ecr', region_name="ap-southeast-1", aws_access_key_id="AKIAINAWPIMCZRZUK7YQ",
                          aws_secret_access_key="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")

def list_esc_repositories():
    global aws_client
    aws_client.describe_repositories()
    print(aws_client.get_authorization_token())

reposiories = [{"name": "tomcat", "uri": "tomcat"}, {"name": "accor-adapter", "uri": "accor-adapter"}]