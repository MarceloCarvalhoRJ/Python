def liters_100km_to_miles_gallon(liters):
    gallons = liters / 3.785411784
    miles = ((100 * 1000) / 1609.344) / gallons 
    return miles


def miles_gallon_to_liters_100km(miles):
    tot_km = miles * 1.609344  # Convert miles to kilometers
    gallon = 3.785411784
    tot_litters = gallon * 100 / tot_km
    return tot_litters  # Convert kilometers per liter to liters per 100 km

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

print()

def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb):
    return lb * 0.4535923
 
 
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
 
    return weight / height ** 2
 
 
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))
 