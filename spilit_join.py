def split_join(line):
    line=line.split(" ")
    c="-".join(line)
    return c

if __name__ == '__main__':
    line = input()
    result = split_join(line)
    print(result)
   
