import csv

providers = [["10.10.10.1", 0], # Providers' IP and points
             ["10.10.10.2", 0],
             ["10.10.10.3", 0],
             ["10.10.10.4", 0]] 
points = [100, 50, 20, 10] # Points for 1st, 2nd, 3rd and 4th place

with open("C:\\arbitrage_ascii.csv") as csv_file:
    csvRead = csv.reader(csv_file)
    next(csvRead)
    next(csvRead)
    next(csvRead)
    
    i = 0 # Iterator for points attribution
    
    for row in csvRead:
        provider_ip = row[5].lstrip() # Get provider's IP for each row
    
        # Attribute points to provider, 1st provider to appear will get 1st points
        # (since csv file is sorting with ascending frame.time_epoch)
        for j in range(0, len(providers)): 
            if provider_ip == providers[j][0]:
                providers[j][1] += points[i]
        
        if i < len(providers) - 1:
            i += 1 # 2nd provider will get 2nd points, etc.
        else:
            i = 0 # Reset i when moving on to next sequence

# Print points for each provider
for k in range(0, len(providers)):
    print("Provider", providers[k][0], "-", providers[k][1], "points")

# Sort providers by points, in descending order
def getKey(item):
    return item[1]
sortedProviders = sorted(providers, key = getKey, reverse = True)

# Print the best 2 providers
print("\nBest providers:")
print("#1 ", sortedProviders[0][0])
print("#2 ", sortedProviders[1][0])