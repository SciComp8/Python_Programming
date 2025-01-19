social_science_data = [
    ["respondent_id", "age", "gender", "education_level", "income", "employment_status", "marital_status", "survey_score"],
    [1, 25, "Female", "Bachelor's", 45000, "Employed", "Single", 78],
    [2, 34, "Male", "Master's", 60000, "Employed", "Married", 85],
    [3, 29, "Non-binary", "High School", 32000, "Unemployed", "Single", 65],
    [4, 45, "Female", "PhD", 75000, "Employed", "Married", 90],
    [5, 51, "Male", "Bachelor's", 50000, "Retired", "Divorced", 70],
]

for row in social_science_data:
    print(row)

# Return the elements of social science records starting from index 0 and continuing up to but *not including index 2*
social_science_data[0:2]
social_science_data[:2]

# Return all the social science records from index 2 onward
social_science_data[2:]

# Return all the social science records except the first and the last
social_science_data[1:-1]

# Return the last 3 social science records 
social_science_data[-3:]

# Return the last 2 social science records 
social_science_data[-2:]
