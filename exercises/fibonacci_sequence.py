def main():
    seq = [1,1]
    nth_term = int(input("Enter the nth term of the sequence: "))
    res = 1
    while len(seq) < nth_term:
        res = seq[len(seq) - 1] + seq[len(seq) - 2]
        seq.append(res)
    print(res)

main()
