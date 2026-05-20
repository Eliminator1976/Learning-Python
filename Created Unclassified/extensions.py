
print("hello")
name = input("Pls provide the name with extension of your file to receive its file type ").strip().lower()

def main(name):
    if name.endswith('.gif'):
        print("GIF \"Graphics Interchange Format\"")
    elif name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png'):
        print("Image type")
    elif name.endswith('.pdf'):
        print("Portable Document Format")
    elif name.endswith('.txt'):
        print("Text file")
    elif name.endswith('.zip'):
        print("Compressed File type")
    else:
        print("application/octet-stream")
    
main(name)
    
    