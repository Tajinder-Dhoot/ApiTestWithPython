import json

with open('../files/employee.json') as file:
    data = json.load(file)
    print(data['firstName'])
    print(data['teams'])
    print(data['teams'][1])


def get_main_team_of_employee():
    with open('../files/employee.json') as file_1:
        data_1 = json.load(file_1)
        team_roles = data_1['teamRoles']
        for team_role in team_roles:
            if team_role['role'] == 'QA Lead':
                return team_role['team']
        return "employee has supportive role only"


print("main team: " + get_main_team_of_employee())
