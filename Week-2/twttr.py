vowels = ['a','e','i','o','u']
#want a program which doesnt change the case of letters and just deletes the vowels from the text
def main():
    text = input("Input: ").strip()
    for char in text:
        if char.lower() in vowels:
           text = text.replace(char,"")
    print(text) 
        
main()