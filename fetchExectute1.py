import requests
import pandas as pd
import json as js

def fetchExectute1():
    # Define your bearer token
    bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTbG1SbG1TN3V0OWtjUHZJdERQTk9UNG45c1F5RDNJTGpmdWs4TU5jQzZZIn0.eyJleHAiOjE3MTM4MjkxMTMsImlhdCI6MTcxMzIyNDMxMywianRpIjoiNWEzYjZjZDYtZjcxMy00NjA5LTkxODAtMTIyMjVmYmRmMTcwIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FkdmFuY2VkIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImRiNzdlYzZiLWQyZWEtNDRiZS04MTYyLWY1YmU5NzY5YmM4NSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImNsaWVudCIsInNlc3Npb25fc3RhdGUiOiI0Nzc0OGMwZi1kZGEwLTQyYjgtYTY3My1iMjFkMjY1MmU3ODUiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJleHBlcnQiLCJkZWZhdWx0LXJvbGVzLXRlc3QiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiI0Nzc0OGMwZi1kZGEwLTQyYjgtYTY3My1iMjFkMjY1MmU3ODUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZXhwZXJ0IiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIn0.HPHgX50MldCydoc_moFLs1T6LuuJj8dUB7ea45X5PuMMsWX3OY0CCUYCm4umaTDStRecxJ0Tl-0GQyxWXEUwbLjh6KU73Ev2l7CwMC6PXiyyLAQZqlg_3pyOJai1ygOSnuMqeZUgt2-sffIhLnkJy69lCRGJbmArr8pl_jpliuSYJwq3zC306hpnRRoFIHMN2RtbL6GOYr_rNhRDd-Mm6pxl0aHczFaxg-BVnE3iQRo08Zdyn_G_P7kwmxmhzH4d8KN_NUofDw3O6g4Zei0MVPicjrKcNjLhpp0PEomax7OFZ_hfTYOKjXllPzN14CjtXuneKjXTQsduJfQl4jmOEw"

    url = 'http://localhost:30226/api/v1/basic/calculate-scenario'

    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json; charset=utf-8'
    }
    params = {
        'scenarioId': '83b6ad84-33e9-4615-9a44-34246baaa484'
    }

    response = requests.post(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
    else:
        print("bho")

    url = "http://localhost:30226/api/v1/impact-method/6070b11f-e863-486c-9748-14341de36259"

    headers = {
        "Authorization":  f'Bearer {bearer_token}',
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        names = response.json()
    else:
        print("bho")

    data = data[0]["phaseResults"]
    names = names["impactCategories"]
    table = {}
    for item in names:
        table[item["name"]] = {}
    for i in range(0, len(data)):
        for j in range(0, len(data[i]["nodeImpactResult"]["impactList"])):
            for item in names:
                if item["refId"] == data[i]["nodeImpactResult"]["impactList"][j]["refId"]:
                    value_unit = (data[i]["nodeImpactResult"]["impactList"][j]["value"],
                                  data[i]["nodeImpactResult"]["impactList"][j]["unit"])
                    table[item["name"]][data[i]["nodeImpactResult"]["name"]] = value_unit

    df = pd.DataFrame(table)
    df = df.transpose()

    print(df.to_dict())
    return df.to_dict()
