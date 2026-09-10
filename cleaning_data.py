import json 
import re

with open("cinemas.jsonl", "r", encoding='utf8') as file:
    for line in file:
        data = json.loads(line.strip()) #single line 
        content = [data["content"]]
        print(type(content))
        for strings in content:
            print(type(strings))
            #reg = re.compile("\n.*?- ")
            #a = re.sub(reg,"\n", strings)