states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# getting items from the list
print(states_of_america[0])
print(states_of_america[-1])

# modifying items in the list
print(f"before update: {states_of_america[0]}")
states_of_america[0] = "Delaware!"
print(f"after update: {states_of_america[0]}")

# adding items to the list
print(f"length before adding a new element: {len(states_of_america)}")
states_of_america.append("Delaware!")
print(f"length after adding a new element: {len(states_of_america)}")