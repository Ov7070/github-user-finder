
import requests as r

user = input("user name : ")

add = f"https://api.github.com/users/{user}"

end = r.get(add)

print(end.status_code)

if end.status_code == 200:
    data = end.json()

    print(f"login : {data['login']}")
    print(f"name : {data['name']}")
    print(f"followers : {data['followers']}")
    print(f"following : {data['following']}")
    print(f"public repos : {data['public_repos']}")
    print(f"bio : {data['bio']}")
    print(f"location : {data['location']}")
    print(f"company : {data['company']}")
    print(f"public gists : {data['public_gists']}")
    print(f"profile : {data['html_url']}")

elif end.status_code == 404:
    print("User not found")

else:
    print(f"Error: {end.status_code}")