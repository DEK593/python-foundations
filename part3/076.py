n = int(input().strip())
    
    
if n % 2 != 0:
        print("Weird")
elif n % 2 == 0 and 2 < n < 5:
        print("Not weird")
elif n >= 6 and n <= 20:
        print("Weird")
elif n > 20:
        print("Not weird")