import requests as r

user=input("user name : ")

add=f"https://api.github.com/users/{user}"

end=r.get(add )
print(end.status_code)

data=end.json()

print(f"login  :{data['login']}")
print(f"name :{data['name']}")
print(f"followers :{data['followers']}")
print(f"following :{data['following']}")
print(f"public repos : {data['public_repos']}")