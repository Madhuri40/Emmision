vrow = {"A": "A value", "B": "Bvalue", "c": "red"}
for k,v in vrow.items():
    if v is not None:
        del vrow[k]
print(f"vrow:{vrow}")