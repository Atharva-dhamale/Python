

CountEven = lambda No: len(list(filter(lambda No:No%2==0, No)))


def main():

    Data=[2,5,16,30,33,3,60]

    print(CountEven(Data))


    

if __name__=="__main__":
    main()