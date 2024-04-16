import requests
import pandas as pd


class CustomProcessFetcher:
    def __init__(self, bearer_token,scenarioid, urlcustomization,urlimpact, urlexecute):
        self.bearer_token = bearer_token
        self.urlCustomization = urlcustomization
        self.urlExecute = urlexecute
        self.scenarioId = scenarioid
        self.urlImpact = urlimpact

    def fetch_custom_process(self):
        headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        url = f"{self.urlCustomization}/{self.scenarioId}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()["customization"]["parameters"]
            table = {}
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

            return table
        else:
            return response.status_code

    def fetch_execute(self):
        headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        params = {
            'scenarioId': self.scenarioId
        }

        response = requests.post(self.urlExecute, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            names = self.fetch_impact()

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
            return df.to_dict()

        else:
            return response.status_code



    def fetch_impact(self):
        headers = {
            "Authorization": f'Bearer {self.bearer_token}',
            "Content-Type": "application/json"
        }

        response = requests.get(self.urlImpact, headers=headers)

        if response.status_code == 200:
            names = response.json()
            return names
        else:
            return response.status_code

