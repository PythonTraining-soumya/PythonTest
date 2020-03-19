
# In dictionary data type we use curly braces to input data
# here we use keys for eg) 1, 2, age are key
a = {1: "FirstName", 2: "LastName", "age":  45, "greet": "Hello", "de": "say"}
# get the first key
print(a[1])

# get the age key
print(a["age"])
print(a['age'])

# get greet key value
print(a["greet"])

# get de key value
print(a["de"])

# To pass the values to the dictionary in run time
dic = {}
dic["FirstName"] = "Soumya"
dic["LastName"] = "Balu"
dic["age"] = 31
dic["gender"] = "Female"
print(dic)
print(dic["LastName"])
