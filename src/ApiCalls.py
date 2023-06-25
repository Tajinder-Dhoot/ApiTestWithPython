import requests


def get_postman_key():
    with open('/Volumes/Cipher/postman-and-newman/postman_apis_key.txt') as file:
        api_key = file.readline()
        return api_key


x_api_key = get_postman_key()
headers = {
    'X-API-Key': x_api_key
}


def get_postman_environments():
    request = requests.get(
        'https://api.getpostman.com/environments',
        headers=headers
    )
    return request.json()


def get_environment_id(environment):
    environments = get_postman_environments()['environments']
    for env in environments:
        if env['name'] == environment:
            return env['id']

    return None


print(get_postman_environments())
print(get_environment_id("STAGING"))
