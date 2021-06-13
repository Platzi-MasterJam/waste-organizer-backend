import pandas as pd
import requests
import json

file_name = "products.csv"

df = pd.read_csv(file_name)

def post_product(data):
    # baseurl = "https://69xlj1.deta.dev"
    baseurl = "http://localhost:3000"
    url = f"{baseurl}/products"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("Se creo el producto", data["key"])
    else:
        print("No se creo el producto", data["key"])

for _, row in df.iterrows():
    post_product(row.to_dict())