count = 5
limit = 3

if count < limit:
    print(count,  "Count 5 is less than limit 3")

else:
    print("Count 5 is not less than limit 3")


print("")


amounts = [5, 16, 44, 31, 107, 48, 22, 999, 8]
message = "OK"
low_limit = 10
high_limit= 99
missing = 999

for i in amounts:
    if(i < low_limit):
    	message = "Too few items"
    elif(i < high_limit):
    	message = "Too many items"
    	if(i == missing):
    		message = "Unknown number of items - recheck inventory"
    print(i, message)

print("")

prices_list = [4.95, 9.90, 12.44, 1.99, 27.95,
               5.00, 11.05, 144.23, 20.00]
message = ""
bargain = 5.00
quality = 20.00

for i in prices_list:
	if(i <= bargain):
		message = "Sale price!"
	if(i >= quality):
		message = "Exclusive offering"
	print(i, message)        


