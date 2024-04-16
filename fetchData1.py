import requests
import pandas as pd
import json as js

# Define your bearer token
bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTbG1SbG1TN3V0OWtjUHZJdERQTk9UNG45c1F5RDNJTGpmdWs4TU5jQzZZIn0.eyJleHAiOjE3MTM4MjkxMTMsImlhdCI6MTcxMzIyNDMxMywianRpIjoiNWEzYjZjZDYtZjcxMy00NjA5LTkxODAtMTIyMjVmYmRmMTcwIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FkdmFuY2VkIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImRiNzdlYzZiLWQyZWEtNDRiZS04MTYyLWY1YmU5NzY5YmM4NSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImNsaWVudCIsInNlc3Npb25fc3RhdGUiOiI0Nzc0OGMwZi1kZGEwLTQyYjgtYTY3My1iMjFkMjY1MmU3ODUiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJleHBlcnQiLCJkZWZhdWx0LXJvbGVzLXRlc3QiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiI0Nzc0OGMwZi1kZGEwLTQyYjgtYTY3My1iMjFkMjY1MmU3ODUiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZXhwZXJ0IiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIn0.HPHgX50MldCydoc_moFLs1T6LuuJj8dUB7ea45X5PuMMsWX3OY0CCUYCm4umaTDStRecxJ0Tl-0GQyxWXEUwbLjh6KU73Ev2l7CwMC6PXiyyLAQZqlg_3pyOJai1ygOSnuMqeZUgt2-sffIhLnkJy69lCRGJbmArr8pl_jpliuSYJwq3zC306hpnRRoFIHMN2RtbL6GOYr_rNhRDd-Mm6pxl0aHczFaxg-BVnE3iQRo08Zdyn_G_P7kwmxmhzH4d8KN_NUofDw3O6g4Zei0MVPicjrKcNjLhpp0PEomax7OFZ_hfTYOKjXllPzN14CjtXuneKjXTQsduJfQl4jmOEw"

url = 'http://localhost:30226/api/v1/customized-process/83b6ad84-33e9-4615-9a44-34246baaa484'

headers = {
    'Authorization': f'Bearer {bearer_token}',
    'Content-Type': 'application/json; charset=utf-8'
}
params = {
    'scenarioId': '83b6ad84-33e9-4615-9a44-34246baaa484'
}

response = requests.get(url, headers=headers)

table = {}

if response.status_code == 200:
    data = response.json()["customization"]["parameters"]
    for item in data:
        alias = item["alias"]
        table[alias] = {
            "options": [],
            "unit": item.get("unitOfMeasure"),
            "current value": item.get("value")
        }

        options = item.get("options")
        if options is None:
            continue
        for option in options:
            table[alias]["options"].append(option.get("label"))
            if option.get("value") == item.get("value"):
                table[alias]["current value"] = option.get("label")

    print(js.dumps(table, indent=4))
else:
    print(response.status_code)

