import requests
host_url = "http://127.0.0.1:5000"
# response = requests.get(f"{host_url}/helloworld/Jane")
# response = requests.post(f"{host_url}/helloworld")
data = [{"id" : 12, "likes" : 110, "name" : "Harry", "views" : 100},
        {"id": 70, "likes" : 170, "name" : "Steve", "views" : 1100},
        {"id": 80, "likes" : 180, "name" : "Bruce", "views" : 10900}]
for i in range(len(data)) :
    response = requests.put(f"{host_url}/video/{str(data[i]['id'])}", data[i]) 
    print(response.json())
input()
# response = requests.delete(f"{host_url}/video/0") 
# print(response.json())
input()
response = requests.get(f"{host_url}/video/10") 
print(response.json())

response = requests.patch(f"{host_url}/video/2", {"views" : 99})
print(response.json())