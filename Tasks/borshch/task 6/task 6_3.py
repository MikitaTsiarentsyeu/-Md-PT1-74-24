count=0

def chr_counter(string, count, chr, i=0):
    if i == len(string) - 1:
        if string[i] == chr:
            count += 1
        return count
    else:
        if string[i] == chr:
            count += 1
        return chr_counter(string, count, chr, i + 1)

string = "any string with any symbols"

print(chr_counter(string, count, "y"))
