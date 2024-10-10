set_a = {1, 2, 3}
set_b = {2, 3, 4}

# union
set_c = set_a.union(set_b)
print(set_c)

# intersection
set_d = set_a.intersection(set_b)
print(set_d)

# diference
print(set_a.difference(set_b))
print(set_b.difference(set_a))

# symmetric_difference
print(set_a.symmetric_difference(set_b))

# issubset
print(set_a.issubset(set_c))
print(set_c.issubset(set_a))

# issuperset
print(set_b.issuperset(set_c))
print(set_c.issuperset(set_b))

# isdisjoint
set_e = {5, 6, 7}
print(set_a.isdisjoint(set_b))
print(set_a.isdisjoint(set_e))

# add
cars = {"Civic", "Lancer", "Corolla"}
cars.add("Cruize")
print(cars)

# copy
cars_copy = cars.copy()
print(cars_copy)

# clear
cars_copy.clear()
print(cars_copy)

# discard
cars.discard("Corolla")
print(cars)

# pop
print(cars.pop())
print(cars)

# remove
cars.remove("Lancer")
print(cars)

# len
print(len(set_c))

# in
print("Civic" in cars)
print("Cruize" in cars)