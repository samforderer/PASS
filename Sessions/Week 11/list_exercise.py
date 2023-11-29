years = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]

print(years)

# Remove 2025 from the list
years.remove(2025)

print(years)

# Add 2027 to the list 
years.append(2027)

# Check if 2017 is in the list, if so, remove it
if 2017 in years:
    years.remove(2017)
else:
    print('its not there')
   
# sort the list 
years.sort()

print(years)

# print items 3-5 inclusive
for i in range(3,6):
    print(years[i])
