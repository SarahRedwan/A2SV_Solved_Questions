def swap_case(s):
    swap=[]
    for x in s:
        if x.isalpha():
            if x.islower():
                swap.append(x.upper())
            else:
                swap.append(x.lower())
        else:
            swap.append(x)
    return "".join(swap)


        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
