aList = ["test", 123, "desk", {"table": "cup"}, False, 'c']
print(aList)

print(aList[-1])
print(aList[1])

print("\nChanging the second element from 123 to 321")
aList[1] = 321
print(aList[1])

print(aList)
print(f"the list is {len(aList)} elements long\n")

report_card = {"name": "Isaac", "subject": "Math", "grades": (90, 85, 88)}
print(report_card)
print(f"dict length: {len(report_card)}")

# Accessing dictionary with key
x = report_card["name"]
print(f"{x}")

report_card["graduation"] = 2027
print(f"Added new key value pair: graduation: {report_card['graduation']}")
print(f"dict length: {len(report_card)}")

report_card.update({"subject": "Python"})
print(f"Changes subject from Math to {report_card["subject"]}")

report_card.pop("graduation")
print(f"Removed graduation from dictionary\n{report_card}")
print(f"dict length: {len(report_card)}")

