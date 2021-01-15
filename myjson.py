import json
person = {"name": "John", "age": 30, "city": "New York", "has Children": False, "title": ["engineer","Programmer"]}
#convert to JSON
#person_json = json.dumps(person)
#with formatting and indentation
person_json2 = json.dumps(person, indent=4,sort_keys=True)

# result
#print(person)
#print(person_json)
#print(person_json2)



#make a json file
#with open('person.json','w') as file:
 #   json.dump(person, file, indent=4)

person=json.loads(person_json2)
print(person)