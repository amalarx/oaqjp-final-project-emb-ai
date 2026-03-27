# Bvariant
driver_name = input("Enter driver name: ")
distance = float(input("Enter distance (km): "))
consumption = float(input("Enter fuel consumption (L/100km): "))
price = float(input("Enter fuel price (KZT/L): "))

litres_needed = distance * consumption / 100
fuel_cost = litres_needed * price
cost = fuel_cost / distance

print("=" * 30)
print("     ROAD TRIP SUMMARY")
print("=" * 30)
print("Driver :", driver_name)
print("Distance :", distance, "km")
print("Consumption :", consumption, "L/100km")
print("Fuel price :", price, "KZT/L")
print("-" * 30)
print("Litres needed:", litres_needed, "L")
print("Fuel cost :", fuel_cost, "KZT")
print("Cost per km :", cost, "KZT")
print("=" * 30)

print("Trip longer than 300 km:", distance > 300)
print("Fuel cost above 5000 KZT:", fuel_cost > 5000)