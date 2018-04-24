

def combo(fileName, amt):
    #Validation
    #TODO: Check for valid file name
    #TODO: Check for positive amount value
    
    #Amount is less than second smallest gift price
    #NOT POSSIBLE
    
    #Since the file size in large depending on local RAM size compared to the file size
    #either stream the data in or read all the file in memory
    
    #Find the max priced gift item which is less in value than amt, lets call it a and price a_price
    #Find the max priced gift item which is less than amt - a_price, lets call it b and b_price
    #If amt = (a_price + b_price), return (a, b)
    #Else save this pair as the optimal found yet
    #Continue with the next max gift price item after a, lets call it a`
    #Find b` for a`
    #If a` + b` is more than a + b but less than amt, it becomes optimal
    #When the next price after a has no combination better than (a, b), we stop the search
    #Return optimal
    
    
    
    
class Gift:
     
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    
if __name__ == "__main__":
    combo("prices.txt", 200)
    

