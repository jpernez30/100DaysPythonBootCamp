# Write your code below this line 👇
def prime_checker(number):
  isPrime = True;
  if n <= 1:
    isPrime = False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      isPrime = False

  if(isPrime):
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
    

# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)