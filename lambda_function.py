import json
from datetime import datetime

def lambda_handler(event, context):
    route = event.get("rawPath", "/")

    if route == "/hello":
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Bonjour depuis AWS Lambda !"})
        }

    elif route == "/time":
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "statusCode": 200,
            "body": json.dumps({"heure_utc": now})
        }

    elif route == "/echo":
        body = json.loads(event.get("body") or "{}")
        return {
            "statusCode": 200,
            "body": json.dumps({"echo": body})
        }

    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"erreur": "Route introuvable"})
        }
