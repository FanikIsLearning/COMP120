print("""apple, 
orange, 
pineapple""" )
print("----------------")

ex1 = "HOI KIT, FAN, 1123 ABC STREET,MISSISSAUGA" 
firstname = "HOI KIT"
lastname = "FAN"
address = "1123 ABC STREET,MISSISSAUGA"
full_list = f"I am {firstname} {lastname}, living in {address}"
print(full_list)
print("----------------")

agile = ["scrum", "xp", "kanban"]
print(agile)
print(agile.pop(2))
print(agile)
agile.insert(2,"Devop")
print (agile)
agile.append("kanban")
print(agile)
print(agile[-1:-2:-1])
print("----------------")

ex3 = ["comp100","comp120","comp213"]
print(f"you are enrolled in {ex3[0]}")
print(f"you are enrolled in {ex3.pop(1)}")
print(f"you are enrolled in {ex3[1]}")