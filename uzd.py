import json

with open("calc.json", "r") as read_file:
    data = json.load(read_file)

uzd = {
    
    "input1": 2,
    "commment":"accept any number",
    "input2": 3,
    "commment":"accept any number",
    "operator":"+",
    "comment":"options here: '+','-','*','/' "

}

data = json.loads(uzd)

unformatted_json = json.dumps(uzd)
print(unformatted_json)  


#    file.write(jsonResponse)
