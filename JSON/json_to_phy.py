import json
x='{"name":"nivi","age":19,"gender":"female"}'
y=json.loads(x)
print(y['name'])
print(y['age'])
print(y['gender'])
