from flask import Flask, jsonify
from FetchProcessData import CustomProcessFetcher
app = Flask(__name__)

# Assuming df is defined and contains the DataFrame you want to serve
bearer_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJTbG1SbG1TN3V0OWtjUHZJdERQTk9UNG45c1F5RDNJTGpmdWs4TU5jQzZZIn0.eyJleHAiOjE3MTQ0ODMyNzksImlhdCI6MTcxMzg3ODQ3OSwianRpIjoiMGM4MDNjOWUtZjc0Ny00MTZiLTkxNGQtMWE1MzQzM2U4YTNkIiwiaXNzIjoiaHR0cDovL2tleWNsb2FrOjgwODAvcmVhbG1zL0FkdmFuY2VkIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImRiNzdlYzZiLWQyZWEtNDRiZS04MTYyLWY1YmU5NzY5YmM4NSIsInR5cCI6IkJlYXJlciIsImF6cCI6ImNsaWVudCIsInNlc3Npb25fc3RhdGUiOiJmYzE5YmFlZC1iNTA0LTQ4YWEtYjYxOS00MmYxYjlhMDI4NWMiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIi8qIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJleHBlcnQiLCJkZWZhdWx0LXJvbGVzLXRlc3QiLCJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIl19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJvcGVuaWQgZ3JvdXBzIHByb2ZpbGUgZW1haWwiLCJzaWQiOiJmYzE5YmFlZC1iNTA0LTQ4YWEtYjYxOS00MmYxYjlhMDI4NWMiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiZXhwZXJ0IiwiZ2l2ZW5fbmFtZSI6IiIsImZhbWlseV9uYW1lIjoiIn0.EMlMOui3LT8JYtyH7Wc-ku-GerYc2nx6Mhg6oLfZcAP23_BGCTjn4X2lOcSHX80zbY2rztVvx2_7Z2N2GJAjiOfviBgECGrjMtcocs2YluG--pzKNb2jzm3XFIl6IeIafVtdGDSrGhrkv9aGKnQBUfRgY3W677XhUFTH-GHFpGVWkO9Ex024tOmNfunPBe39-l9_itjmHKRw6wnljbPxnzElqVGBbvLP_AtTgUg08JcXYEzVW0F_yd8NFKIt-6akPbMa8n7hmyDPbqNlehtgDt9JjuswJYZy_Qd-O7yyeooxONLX2M574G5rMe2i5B0O8Cl1nXPspQvvJSIM3YAuUA"
urlCustomization = "http://localhost:30226/api/v1/customized-process"
urlExecute = "http://localhost:30226/api/v1/basic/calculate-scenario"
urlImpact = "http://localhost:30226/api/v1/impact-method/6070b11f-e863-486c-9748-14341de36259"
urlScenarioName = "http://localhost:30226/api/v1/scenario"
custom_process_fetcher = CustomProcessFetcher(bearer_token, urlCustomization, urlImpact, urlExecute, urlScenarioName)

@app.route('/fetchData/<scenarioid>', methods=['GET'])
def get_table_data(scenarioid):
    data = custom_process_fetcher.fetch_custom_process(scenarioid)
    return jsonify(data)

@app.route('/fetchExecute/<scenarioid>', methods=['GET'])
def get_table_execute(scenarioid):
    data = custom_process_fetcher.fetch_execute(scenarioid)
    return jsonify(data)

@app.route('/fetchName/<scenarioid>', methods=['GET'])
def get_scenario_name(scenarioid):
    data = custom_process_fetcher.fetch_scenario_name(scenarioid)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
