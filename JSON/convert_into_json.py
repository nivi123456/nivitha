import json
x={
    'name':'nivi',
    'age':19,
    'gender':'female',
    'single':True,
    'married':False,
    'pets':('dog','cat'),
    'bike':None,
    'cars':[
        {'model':'BMW 230','mpg':27.5},
        {'model':'ford edge','mpg':24.1}
        ]
    }
y=json.dumps(x)
print(y)
