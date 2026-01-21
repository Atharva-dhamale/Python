
Max=lambda No1,No2,No3 : No1 if No1>No2 and No1>No3 else (No2 if No2>No3  else No3)

def main():
    
    Ret=Max(10,20,15)

    print(Ret)
    

if __name__=="__main__":
    main()