def convert(dec):
    binary=[]
    while(dec>1):
        digit=dec%2
        binary.append(digit)
        dec=dec//2
    
    binary.append(dec)
    binary=binary[::-1]
    bin_no=0
    for x in binary:
        bin_no=bin_no*10+x

    print(bin_no)

def main():
    input_no=int(input("Enter a decimal no: "))
    convert(input_no)

main()