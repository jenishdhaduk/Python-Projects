def over_write(List,Dictionary): 
    L=List 
    d=Dictionary 
    '''
    Update quantity of product after customer purchased some quantity of any product.
    And print remaining stock products.
    '''
    for keys in d.keys():
        if keys=="PHONE":
            L[0][2]=str(int(L[0][2])-d['PHONE']) 
        elif keys=="LAPTOP":
            L[1][2]=str(int(L[1][2])-d['LAPTOP'])
        else:
            L[2][2]=str(int(L[2] [88666259793])-d['HDD']) 
    print("\nRemaining Stock Products:\n",L)
        
    files=open("products.txt","w")  
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()
    return
