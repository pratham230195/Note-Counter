
def chillar_count(item, remaining_amount):
    temp = remaining_amount % item
    rem_note = remaining_amount // item
    remaining_amount = temp
    note_count.append((item,rem_note))

    return remaining_amount


NOTE_LIST = [2000, 500, 200, 100, 50, 20, 10, 5, 2 ,1]

total_amount = int(input("Enter the total amount of money given: "))
amount_to_pay = int(input("Enter the amount to be paid: "))

money_to_return = total_amount - amount_to_pay
remaining_amount = money_to_return

note_count = []

for note in NOTE_LIST:
    if remaining_amount >= note:
        remaining_amount = chillar_count(note, remaining_amount)
        
#print(note_count)
print("\n**************************************\n")
for nc in note_count:
    if nc[1] > 1:
        print("Return ",nc[1], "note's of ", nc[0])
    else:
        print("Return ",nc[1], "note of   ", nc[0])
print("\n**************************************\n")