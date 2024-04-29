import requests
import pandas as pd


class CustomProcessFetcher:
    def __init__(self, bearer_token, urlcustomization,urlimpact, urlexecute, urlscenarioname):
        self.bearer_token = bearer_token
        self.urlCustomization = urlcustomization
        self.urlExecute = urlexecute
        self.urlImpact = urlimpact
        self.urlScenarioName = urlscenarioname

    def fetch_custom_process(self, scenarioid):
        headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        url = f"{self.urlCustomization}/{scenarioid}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()["customization"]["parameters"]
            table = {}
            for item in data:
                key = item["display"]["tab"]
                alias = item["alias"]

                # Append the alias to the table[key]
                if key not in table:
                    table[key] = {}

                options = item.get("options")
                if options is not None:
                    if item.get("unitOfMeasure") is not None:
                        table[key][alias] = {"options": [], "unit": item.get("unitOfMeasure"),
                                             "current value": item.get("value")}
                    else:
                        table[key][alias] = {"options": [], "current value": item.get("value")}
                    for option in options:
                        table[key][alias]["options"].append(option.get("label"))
                        if option.get("value") == item.get("value"):
                            table[key][alias]["current value"] = option.get("label")
                else:
                    if item.get("unitOfMeasure") is not None:
                        table[key][alias] = {"unit": item.get("unitOfMeasure"), "current value": item.get("value")}
                    else:
                        table[key][alias] = {"current value": item.get("value")}

            return table
        else:
            return response.status_code

    def fetch_execute(self, scenarioid):
        headers = {
            'Authorization': f'Bearer {self.bearer_token}',
            'Content-Type': 'application/json; charset=utf-8'
        }
        params = {
            'scenarioId': scenarioid
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


    def fetch_scenario_name(self,scenarioid):
        url = f"{self.urlScenarioName}/{scenarioid}"
        headers = {
            "Authorization": f'Bearer {self.bearer_token}',
            "Content-Type": "application/json"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            names = response.json()["name"]
            return names
        else:
            return response.status_code

