import json
import requests

def khalti_payment(member, txn):
    payload = {
        "return_url": "https://example.com/payment/",
        "website_url": "https://kmc.com/",
        "amount": int(txn.amount * 100),
        "purchase_order_id": txn.id,
        "purchase_order_name": txn.name,
        "customer_info": {
            "name": member.first_name,
            "email": member.email,
            "phone": member.phone,
        },
        "product_details": [
            {
                "identity": member.id,
                "name": txn.name,
                "total_price": int(txn.amount*100),
                "quantity": 1,
                "unit_price": int(txn.amount*100),
            }
        ],
    }


    khalti_url = "https://dev.khalti.com/api/v2/epayment/initiate/"
    headers = {
        "Authorization":"key ba8efafdda414b00bc80ec49b2600af9",
        "Content-Type": "application/json",
    }
    r = requests.post(url=khalti_url, headers=headers, data=json.dumps(payload))
    print(r.text)
    if r.status_code == 200:
        return r.json()
    else:
        return {
            "error":"failure"
        }