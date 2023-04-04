x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.1
x [1][0] = 15
print (x)

#1.2
students [0]['last_name'] = "Bryant"
print (students)

#1.3
sports_directory ["soccer"][0] = "Andres"
print(sports_directory)

# 1.4
z[0]["y"] = 30
print(z)

# -------------------------------------------------------------------------------------

#2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for dictonary in some_list:
        output = ""
        for key, value in dictonary.items():
            output += f"{key} - {value}, "
        print(output[:-2])

iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# ----------------------------------------------------------------------------------------

#3
def iterateDictionary2(key_name, some_list):
    for dictonary in some_list:
        print(dictonary[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# ----------------------------------------------------------------------------------------

#4
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for value in some_dict[key]:
            print(value)
        
printInfo(dojo)