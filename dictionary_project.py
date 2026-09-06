# Get Pull Request Infromation on a Github Repo using Python
import requests

# /repos/{owner}/{repo}/pulls

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_detail = response.json()
print(complete_detail[0]["id"])
print(complete_detail[0]["user"]["login"])

#to print the entire range of a specific detail
for i in range(len(complete_detail)):
    print(complete_detail[i]["id"])