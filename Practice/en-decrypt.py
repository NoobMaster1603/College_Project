morse_code = {'A' : '.-','B' : '-...','C' : '-.-','D' : '-..','E' : '.','F' : '..-.','G' : '--.','H' : '....','I' : '..','J' : '.---','K' : '-.-','L' : '.-..','M' : '--','N' : '-.','O' : '---','P' : '.--.','Q' : '--.-','R' : '.-.','S' : '...','T' : '-','U' : '..-','V' : '...-','W' : '.--','X' : '-..-','Y' : '-.--','Z' : '--..','0' : '-----','1' : '.----','2' : '..---','3' : '...--','4' : '....-','5' : '.....','6' : '-....','7' : '--...','8' : '---..','9' : '----.','Error' : '........',' ':'/'}

morse_code_to_text = {value : key for key,value in morse_code.items()} #Interchange of key and value

def encrypt_morse(text):
    result = []
    for char in text.upper():
        result.append(morse_code.get(char,''))
    return ' '.join(result)

def decode_morse_code(text):
    result =[]
    for code in text.split(' '):
        result.append(morse_code_to_text.get(code,''))
    return ''.join(result)

if __name__ == '__main__':
    print("--------------------------------")
    print("1. Encrypt to Morse Code")
    print("2. Decrypt from Morse Code")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        text = input("Enter text that need to encrypted: ")
        print("Encrypted Morse Code: ", encrypt_morse(text))    
        print("--------------------------------")
    elif choice == 2:
        text = input("Enter morse code neede to decrypt: ")
        print("Decrypted Morse Code: ", decode_morse_code(text))
        print("--------------------------------")
    else:
        print("Invalid choice")