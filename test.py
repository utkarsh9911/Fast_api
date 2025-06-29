from pydantic import BaseModel, Field, computed_field
import pydantic
print(pydantic.__version__)

dic = [{'name': 'yash', 'age': 80, 'city': 'delhi'}, {'city': 'delhi', 'age': 20, 'name': 'yash'}]
import json
# ans = [key for key, value in dic.items() if value == 'delhi']
# print(ans)  # Output: ['city']

# sorted_list = sorted(dic.items(), key = lambda x: x[1])
# print(sorted_list)  # Output: [('age', 20), ('city', 'delhi'), ('name', 'yash')]


# sorrtd_list = sorted(dic, key = lambda x: x.get('age', 0), reverse=False)
# print(sorrtd_list)  # Output: [('name', 'yash'), ('city', 'delhi'), ('age', 20)]


# dictt = {'name': 100, 'age': 80, 'city': 70}
# ans =  sorted(dictt.items() , key= lambda x: x[1], reverse=True)
# print(ans)

# with open('patient.json', 'r') as f:
#     dataa = json.load(f)

# print(dataa)
# print(dataa[0])