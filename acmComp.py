def main():
    n = int(input())
    i = 0
    while (True):
        if (n == 1){
            return i
        }
        if (n % 2 == 0){
            n = n/2
        } else{
            n = 3n + 1
        }
        if (n < 1){
            break
        }
    return "EILEEN YOU'RE WRONG"
