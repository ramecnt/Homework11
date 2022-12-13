import json

def get_all():
    with open("candidates.json", "r", encoding = 'utf-8') as file:
        return json.load(file)

def get_by_id(id):
    file = get_all()
    for i in file:
        if i['id'] == id:
            return i

def get_by_name(name):
    result = []
    file = get_all()
    for i in file:
        if i['name'].split()[0] == name:
            result.append(i)
    return result

def get_by_skill(skill_name):
    result = []
    file = get_all()
    for i in file:
        if skill_name in i['skills'].lower().split(', '):
            result.append(i)
    return result