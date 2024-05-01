"""Write a function named apt_search1. It takes a city parameter (string), a max_rent
parameter (int), a min_beds parameter (int), and a pets_allowed parameter (boolean).
It simply returns a string similar to one of these examples:"""


def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        return f'''Welcome to GC Property Management! Looking up Listings in 
            {city} for {min_beds} bedroom apartments that allow pets, all within a 
            budget of ${max_rent} per month\n'''
    else:
        return f'''Welcome to GC Property Management! Looking up Listings in 
            {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} 
            per month\n'''


print(apt_search1("Baltimore", 1000, 2, True))
print(apt_search1("Charlotte", 950, 1, False))


def apt_search2(city, max_rent, min_beds=2, pets_allowed=False):
    if pets_allowed:
        return f'''Welcome to GC Property Management! Looking up Listings in 
        {city} for {min_beds} bedroom apartments that allow pets, all within a 
        budget of ${max_rent} per month\n'''
    else:
        return f'''Welcome to GC Property Management! Looking up Listings in 
        {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} 
        per month\n'''


print(apt_search2("Detriot", 900))
print(apt_search2("Boston", 1200, 1))
print(apt_search2("New York City", 1500, pets_allowed=True))

#lambda functions

plus_one_hundred = lambda num: num + 100

square_num = lambda num: num*num

concatenate = lambda str: "-"+str

divide_by_three = lambda num: num/3


print(plus_one_hundred(30))
print(square_num(4))
print(concatenate("hello"))
print(divide_by_three(9))
