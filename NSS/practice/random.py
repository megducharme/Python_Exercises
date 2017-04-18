flowers = ["daisy", "rose", "sunflower"]

large_flowers = set()

for f in flowers:
    large_flowers.add('a large ' + f)

print(large_flowers)


larger_flowers = ["a large " + f for f in flowers]

print(larger_flowers)
