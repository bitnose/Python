
d = {"a": 10, "b": 20, "c": 30}


#a) How can we print the value of the item whose key is "b"?
print(d["b"])


#b) How can we add a new item to the dictionary? The key should be "e" and the value should be 40.
d["e"] = 40
print(d)


#c) How can we replace the value of the item whose key is "b"? The new value should be 15.
d["b"] = 15
print(d)


#d) How can we remove an item whose key is "a"?
d.pop("a")
print(d)

#del d["a"]
#print(d)


#e) How can we avoid a KeyError when we want to print the value of an item whose key is "xyz"
if "xyz" in d: print(d["xyz"])
else:
    print("'xyz' is not found in the dictionary")


x = d.get("xyz")
if x:
    print(x)
else:
    print("'xyz' is not found in the dictionary")

print(x)


#a) get all items (key-value pairs) from a dictionary?
for key, value in d.items():
    print(f"{key} {value}")



#b) get all keys (keys only, no values) from a dictionary?
for key in list(d.keys()):
    print(key)

#c) get all values (values only, no keys) from a dictionary?
for value in list(d.values()):
    print(value)

# Creates an empty dictionary 
countries = {}
# Adds a new item with the key as String and values as dictionary. It's a nested dictionary!
countries["Finland"] = {"name": "Suomi", "area": 338_472} 
# Adds the second item in the dictionary.
countries["Sweden"] = {"name": "Sverige", "area": 440_295}
# Prints the value in the nested key
print(countries["Finland"]["name"]) # Suomi
print(countries["Finland"]["area"]) # 338472
# Prints the keys and the values
print(countries)
    # {'Finland': {'name': 'Suomi', 'area': 338472}, 'Sweden': {'name': 'Sverige', 'area': 440295}}
    
# Prints only the keys on the first level
print(*countries) # Finland Sweden