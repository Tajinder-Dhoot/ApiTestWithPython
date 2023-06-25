import requests

headers = {
    'X-API-Key': 'PMAK-6468c6b63bfd607008ff93df-e6c18afb9e7e59c80f8ed6c696441f57a8'
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
