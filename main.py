from linkedList import LinkedList

lst = LinkedList()

lst.append("dog")
lst.append("cat")
lst.append("parrot")
lst.append("hamster")
lst.append("snake")
lst.append("turtle")

print("Initial list:")
print(lst.to_string())

print("\nList size:", lst.size())

print("\nDoes list contain 'cat'?", lst.contains("cat"))
print("Does list contain 'lion'?", lst.contains("lion"))

print("\nIndex of 'parrot':", lst.find("parrot"))
print("Index of 'lion':", lst.find("lion"))

print("\nElement at index 3:", lst.at(3).value if lst.at(3) else None)

print("\nInserting 'lion' at index 2")
lst.insert_at("lion", 2)
print(lst.to_string())

print("\nRemoving element at index 4")
lst.remove_at(4)
print(lst.to_string())

print("\nPopping last element")
lst.pop()
print(lst.to_string())
