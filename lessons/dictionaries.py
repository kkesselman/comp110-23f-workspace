"""Practice using dictionaries"""

#Constructing a dictionary 
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}

#Adding a key value pair to a dictionary 
ice_cream["mint"] = 3 

#Removing a key value pair from a dictionary 
ice_cream.pop("mint")

#Accessing a value 
print(ice_cream["chocolate"])

#Adjusting a value
ice_cream["vanilla"] = 10 

print(ice_cream)
print(len(ice_cream))

print("mint" in ice_cream)

if "mint" in ice_cream: 
    print(ice_cream["mint"])
else: print("No orders of mint.")

for key in ice_cream: 
    print(f"{key} has {ice_cream[key]} orders.")