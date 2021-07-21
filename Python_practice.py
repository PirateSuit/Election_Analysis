# counties = ["Arapahoe", "Denver", "Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties")
# else:
#     print("El Paso is not in the list of counties")
    
# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso are in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties.")

# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# for county in counties:
#     print(county)

# for i in range(len(counties)):
#     print(counties[i])    

# numbers = [0, 1, 2, 3, 4]
# for num in numbers:
#     print(num)

# numbers = [0, 1, 2, 3, 4]
# for num in range(5):
#     print(num)

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(county)

# for county in counties_dict.keys():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict["Denver"])

# for county in counties_dict:
#     print(counties_dict.get("Denver"))

# for county, voters in counties_dict.items():
#    print(county, voters)

# for key, values in counties_dict.items():
#    print(key, "county has", values, "registered voters.")


# Iterating through a list of dictionaries:

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county in range(len(voting_data)):
#    print(voting_data[county]['county'])

# # Get the values from a list of dictionaries:
# # Only the values

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# # Only the "registered voters" value (aka the number):

# for county_dict in voting_data:
#     print(county_dict["registered_voters"])

# Printing Formats:

# F-strings: Formatted String Literals:

# Original Code:

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# The same code using f-strings:

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# Using f-strings with dictionaries:

# Code from line 51:
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")

# Now, using f-strings:

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# Multiline f-strings:

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)

# Same thing, but formatting the floating point decimals.

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

# Skill Drill: Print each registered voter from the dictionary.

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters")

# Skill Drill: Print each county and registered voter from the dictionary:

## CANT FIGURE THIS ONE OUT

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
                {"county":"Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for items in county_dict.items():
        print(items)

