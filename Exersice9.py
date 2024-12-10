city_population = {}

while True:
    
    city = input("Enter the name of a city (or 'stop' to finish): ").strip()
    if city.lower() == "stop":
        break
    population = len(city.replace(" ", "")) * 1_000_000 
    
    city_population[city] = population

sorted_cities = sorted(city_population.items(), key=lambda x: x[1], reverse=True)

print("\nCities and their populations (sorted by population):")
for city, population in sorted_cities:
    print(f"{city}: {population:,} citizens")
