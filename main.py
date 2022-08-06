#!/usr/bin/python3
import sys

dbg_flag = False

def dbg(str):
    if dbg_flag:
        print(str)


if len(sys.argv) < 2 or sys.argv[1] == None or sys.argv[1] == "":
    print("Please add a read file. Usage: ./main.py input.txt")
    quit()

with open(sys.argv[1], 'r') as file:
    for index, line in enumerate(file.readlines()):
        if index == 0:
            submission = line.strip()
        elif index == 1:
            key = line.strip()
        dbg(line.strip())

correct = 0
total = 0
in_multi_choice = False
compare_against = ["", ""]
review_list = []

for index, current in enumerate(key):
    entry = submission[index]

    if current == "(":
        in_multi_choice = True
        dbg("Entering MultiChoice")
        continue

    if current == ")":
        in_multi_choice = False
        total += 1
        if compare_against[0] == compare_against[1]:
            correct += 1
            dbg(compare_against[0] + " " + compare_against[1])
            compare_against = ["", ""]
        dbg("Exiting MultiChoice")
        continue

    if in_multi_choice:
        compare_against[0] += entry
        compare_against[1] += current
        dbg("Adding {} to submission list and {} to key list\nLists:\n{}\n{}\n".format(entry, current, compare_against[0], compare_against[1]))
    else:
        total += 1
        if entry == current:
            dbg(entry + " == " + current)
            correct += 1
        else:
            review_list.append("#{}".format(total))
            dbg(entry + " != " + current)

print("You got a {frac:.1%}! You got {correct} correct, {incorrect} incorrect. You answered {total} questions.\nYou should review: {review_list}".format(frac=(correct/total), correct=correct, incorrect=(total-correct), total=total, review_list=review_list))
