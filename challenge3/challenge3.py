
#Big O
#n = length of the string
#c = count of occurences of X
#O(n + n + (c * 2^c) + (n * 2^c)), which is O(n + ((n+c) * 2^c))
#Worst case is when the string only has Xs: O(n * 2^n)

def combosOfOnesAndZeros(txt):
    if not txt:
        print "Input is empty"
        return
    if "X" not in txt:
        print txt
        return
    
    #Find all indexes of X, O(n)
    indexsOfX = []
    for ind in xrange(len(txt)):
        if txt[ind] == "X":
            indexsOfX.append(ind)
    #Count occurrences of X
    cntOfX = len(indexsOfX)
    
    #Turn string to list of characters, since python strings are immutable, O(n)
    charsInLst = list(txt)
    
    #O(2^cntOfX), worst case when the input is all Xs
    #xrange() returns a generator object, so even if there are high count of occurrences of X
    #memory required will be in limit
    for i in xrange(2**cntOfX):
        #Get binary representation, left padded by zeros of the int
        binaryString = "{0:0>2b}".format(i)
        
        replacedStr = charsInLst
        cnt = 0
        #O(cntOfX)
        for ch in binaryString:
            indexToReplace = indexsOfX[cnt]
            replacedStr[indexToReplace] = ch
            cnt += 1
        #Back to string, O(n)
        print "".join(replacedStr)
   
if __name__ == "__main__":
    combosOfOnesAndZeros("10X10X0")
    

