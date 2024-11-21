for aa in amino_acids:
    #If Cystein is not found between character 20 and 40 inclusive, print Cystein not found
    if aa.find("Cystein", 0, 40) == -1:
        print("Cystein not found")
    #Count occurrences and replace two with one
    elif aa.count("Cystein") == 1:
        print(aa)
    elif aa.count("Cystein") == 2:
        print(aa.replace("Cystein Cystein", "Cystein"))
    else:
        print(aa.replace("Cystein Cystein Cystein", "Cystein")) #Replace three occurrences with one

amino_acids = ["Cystein", "Cystein Cystein", "Cystein Cystein Cystein"] 
#aa.replace(intended_value_for_replacement, new_value): if the intended value for replacement is not found in aa, return the original value in aa.
#aa = "Cystein Cystein"
#aa.count("Cystein")
#2
