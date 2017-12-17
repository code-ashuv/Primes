import os.path

primes = []

start = input("Enter Start Number: ")
end = input("Enter End Number: ")

while end <= start:
	end = input("Enter End Number: (greater than Start Number)  ")
	
if os.path.isfile("primeNumb.txt"):
	File = open("primeNumb.txt",'r')
	for eachline in File:
		primes.append(int(eachline))
	File = open("primeNumb.txt",'a')
else:
	File = open("primeNumb.txt",'w')

print primes

if start == 1:
	start = 2
	print "Skipping 1"
count_primes = 0
for number in range(start, end+1):
	isNotPrime = 0
	if number > 3:
		if float(number)%2 == 0:
			isNotPrime += 1
		if float(number)%3 == 0:
			isNotPrime += 1
	for each in primes:
		if float(number)%each == 0:
			isNotPrime = 1
		if each == number and isNotPrime >= 1:
			isNotPrime = 0
	if isNotPrime == 0:
		primes.append(number)
		print number, "is a Prime Number.", "----",
		print "Number ", number, "written in file."
		File.write(str(number))
		File.write('\n')
		count_primes += 1
	else:
		print number, " is Not a prime number."	

print "Total prime number from, ", start-1, " to ", end, "is ", count_primes

File.close()
