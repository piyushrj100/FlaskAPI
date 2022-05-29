import requests
host_url = "http://127.0.0.1:5000"
# response = requests.get(f"{host_url}/helloworld/Jane")
# response = requests.post(f"{host_url}/helloworld")
data = [{"id" : 167, "likes" : 12310, "name" : "Suresh", "views" : 456},
        {"id": 34, "likes" : 19870, "name" : "Piyush", "views" : 37592},
        {"id": 89, "likes" : 1823, "name" : "Rajan", "views" : 1250}]
for i in range(len(data)) :
    response = requests.put(f"{host_url}/video/{str(data[i]['id'])}", data[i]) 
    print(response.json())
# # input()
# # response = requests.delete(f"{host_url}/video/80") 
# # print(response.json())
# input()
# response = requests.get(f"{host_url}/video/80") 
# print(response.json())

# # response = requests.patch(f"{host_url}/video/2", {"views" : 99})


# # print(response.json())
# response=requests.get(f"{host_url}/video_info?name=Harry&views=100")
# print(response.json())