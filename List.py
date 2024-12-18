colors = [" Green", " Blue", " Black" , " White" , " Red", " Blue"]


# to start from end to begin by index
print(colors[-2])

# start from begin to end by index
print(colors[0])

# to print only the some of begin
print(colors[:3])

# to print only the some of end
print(colors[:-3])

#to print from the meddle of the list
print(colors[1:-2])

# to replace with other list 
colors[1:4] = ["Yellow", " Gray", " Orange"]
print(colors)

# We can use len of the the color 
print(len(colors))

# add some more list 
colors.append(["Orange", "Gray"])
print(colors)

# to add it in the specials place 
colors.insert(2 , "Orange")
print(colors)

# to remove from list
colors.remove("Blue")
print(colors)

# to clear the list
colors.clear()
print(colors)

# to count the number of any item in the list ( be careful with the space )
print(colors.count(" Blue"))

# To sort the list 
colors.sort()
print(colors)
# To sort the list into a new list 
colors_1 = sorted(colors)
print(colors_1)

# To reverse the list
colors.reverse()
print(colors)