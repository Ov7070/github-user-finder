
import requests as r

user = input("user name : ")

add = f"https://api.github.com/users/{user}"

try:
    end = r.get(add)

    print(end.status_code)

    if end.status_code == 200:
        data = end.json()

        print(f"login : {data['login']}")

        name = data['name'] if data['name'] is not None else "Not available"
        print(f"name : {name}")

        print(f"followers : {data['followers']}")
        print(f"following : {data['following']}")
        print(f"public repos : {data['public_repos']}")

        bio = data['bio'] if data['bio'] is not None else "Not available"
        location = data['location'] if data['location'] is not None else "Not available"
        company = data['company'] if data['company'] is not None else "Not available"

        print(f"bio : {bio}")
        print(f"location : {location}")
        print(f"company : {company}")
        print(f"public gists : {data['public_gists']}")
        print(f"profile : {data['html_url']}")

    elif end.status_code == 404:
        print("User not found")

    else:
        print(f"Error: {end.status_code}")

except r.exceptions.RequestException:
    print("Connection error")