test_dict= {"Codingal": 1, "is": 2, "best": 3, "for": 4, "Coding": 5}

print("The original dictionary: " + str(test_dict))

k=int(input("Enter your chosen value: "))
frequency=0

for key in test_dict:
  if test_dict[key]==k:
    frequency=frequency+1

print("Frequency of", k, "in the dictionary is: " + str(frequency))