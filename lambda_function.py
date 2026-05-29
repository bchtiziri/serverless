import json
from datetime import datetime

def lambda_handler(event, context):
    route = event.get("rawPath", "/")
    print("Route reçue:", route)  # pour voir dans CloudWatch

    if "/hello" in route:
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Bonjour depuis AWS Lambda !"})
        }

    elif "/time" in route:
        now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "statusCode": 200,
            "body": json.dumps({"heure_utc": now})
        }

    elif "/echo" in route:
        body = json.loads(event.get("body") or "{}")
        return {
            "statusCode": 200,
            "body": json.dumps({"echo": body})
        }

    else:
        return {
            "statusCode": 404,
            "body": json.dumps({"erreur": "Route introuvable", "route_recue": route})
        }
