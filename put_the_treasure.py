#Printing map
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#Spliting number 
vertical = int(position[0])
horizontal = int(position[1])
#Put treasure into rows
selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"
#Print
print(f"{row1}\n{row2}\n{row3}\n")