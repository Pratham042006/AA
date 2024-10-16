pizzas = int(input("Enter the number of pizzas: "))
slices_per_pizza = int(input("Enter the number of slices per pizza: "))
people = int(input("Enter the number of people: "))

total_slices = pizzas * slices_per_pizza
slices_per_person = total_slices // people
slices_leftover = total_slices % people

print("Each person gets", slices_per_person, "slices.")
print("There will be", slices_leftover, "slices leftover.")