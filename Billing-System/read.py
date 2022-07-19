def read_file(): 
    file=open("products.txt","r") 
    lines=file.readlines()
    L=[]
    for line in lines:
        L.append(line.replace("\n","").split(","))
    file.close()
    print("Following products are avilable in our Store")
    print("--------------------------------------------")
    print("PRODUCT\t\tPRICE\t\tQUANTITY")
    print("--------------------------------------------")
    return L

print(read_file())

