# Student Name: LEELA ALOYSIUS
# Student Number: 1033505

# Add answer below this line

bal = float(input('Balance? '))  
year = int(input('Years? '))  
interest_rate = float(input('Interest Rate(%)? '))  

# Print the table header
print(f"{'Year':<8}{'Balance':<15}{'Interest':<15}{'Total Int.':<15}")
print("-" * 50)

total_interest = 0 

for current_year in range(1, year + 1):  
    interest = bal * (interest_rate / 100)  
    bal += interest 
    total_interest += interest  
   
    print(f"{current_year:<8}{bal:,.2f}{interest:,.2f}{total_interest:,.2f}")
