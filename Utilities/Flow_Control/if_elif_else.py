for aa in amino_acids:
    #If Cystein is not found between character 20 and 40 inclusive, print Cystein not found
    if aa.find("Cystein", 20, 40) == -1:
        print("Cystein not found")
    #Count occurrences and replace two with one
    elif aa.count("Cystein") == 2:  
        print(aa.replace("Cystein Cystein", "Cystein"))
    else:
        print(aa.replace("Cystein Cystein Cystein", "Cystein")) #Replace three occurrences with one

aa = "Cystein Cystein Cystein"
