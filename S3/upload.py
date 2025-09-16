import json
import boto3

s3 = boto3.client("s3", region_name="us-east-1")
bucket = "summoners"
test = {"puuid": "XYZ", "name": "dump1ng0d", "level": 100}

puuid = test['puuid']
key =  f"riot-raw/region=na1/puuid={puuid}/-summoner.json"


data = json.dumps(test, indent=0, ensure_ascii=False).encode("utf-8")

s3.put_object(
    Bucket=bucket,
    Key=key,
    Body=data,
    ContentType="application/json",     
    Metadata={"puuid": puuid, "source": "riot-summoner-v4"}                
)