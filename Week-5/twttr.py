def main():
    word = list(input("Your text here: "))
    print(shorten(word))
    
def shorten(word):
    word = list(word)
    vowels = list("aeiou")
    for letter in word[:]:
        if letter in vowels:
            word.remove(letter)
    return("".join(word))

if __name__ == "__main__":
    main()