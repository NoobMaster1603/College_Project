# Import required modules
import tkinter

# En-Decrypt Program
morse_code = {'A' : '.-','B' : '-...','C' : '-.-','D' : '-..','E' : '.','F' : '..-.','G' : '--.','H' : '....','I' : '..','J' : '.---','K' : '-.-','L' : '.-..','M' : '--','N' : '-.','O' : '---','P' : '.--.','Q' : '--.-','R' : '.-.','S' : '...','T' : '-','U' : '..-','V' : '...-','W' : '.--','X' : '-..-','Y' : '-.--','Z' : '--..','0' : '-----','1' : '.----','2' : '..---','3' : '...--','4' : '....-','5' : '.....','6' : '-....','7' : '--...','8' : '---..','9' : '----.','Error' : '........',' ':'/'}
morse_code_to_text = {value : key for key,value in morse_code.items()} # Interchange of key and value

# Cipher text by shift value
def cipher_text(text,shift):
    result = ""
    for char in text:
        ascii_value = ord(char)
        if 32<=ascii_value<=126:
            shifted = (ascii_value - 32 + shift) % (126 - 32 + 1) + 32
            result += chr(shifted)
        else:
            result += char
    return result
    
def decipher_text(text,shift):
    return cipher_text(text,-shift)

# Logic block for morse code
def encrypt_morse(text):
    result = []
    for char in text.upper():
        result.append(morse_code.get(char,''))
    return ' '.join(result)

def decode_morse(text):
    result =[]
    for code in text.split(' '):
        result.append(morse_code_to_text.get(code,''))
    return ''.join(result)


# Create a GUI window
class App():
    def __init__(self,root):
        self.root = root
        # Set the window title
        self.root.title("Morse Encode-Decode")
        self.root.geometry("500x400")

        # Create a choosing  window
        tkinter.Label(root, text="Choose your operation: ").pack(pady = 10)

        # Create a Frame where you can preform actions
        self.frame = tkinter.Frame(root)
        self.frame.pack(pady=10)
        
        # Buttons for choosing operation
        tkinter.Button(self.frame, text = "Morse Encode", command = self.m_encode_window).grid(row=1, column=0)
        tkinter.Button(self.frame, text = "Morse Decode", command = self.m_decode_window).grid(row=1, column=1)
        tkinter.Button(self.frame, text = "Cipher Encode", command = self.c_encode_window).grid(row=3, column=0)
        tkinter.Button(self.frame, text = "Cipher Decode", command = self.c_decode_window).grid(row=3, column=1)
        
        self.result_label = tkinter.Label(root, text = "")
        self.result_label.pack(pady =10)

        self.input_field = None
        self.action_button = None
        
    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
    # Create a class for morse enconding
    def m_encode_window(self):
        self.clear_frame()
        tkinter.Label(self.frame, text = "Enter text to encode: ").grid(row = 1, column = 0)
        
        # Create one entry fields
        self.input_field = tkinter.Entry(self.frame)
        self.input_field.grid(row = 1, column = 1)
        
        # Create button to convert the text into code
        self.action_button = tkinter.Button(self.frame, text = "Encode" , command = self.on_click_encode).grid(row = 2, column = 1)
        

    # Create a window for morse decoding
    def m_decode_window(self):
        self.clear_frame()
        tkinter.Label(self.frame, text="Enter morse code :").grid(row=1, column=0)

        # Create one entry fields
        self.input_field = tkinter.Entry(self.frame)
        self.input_field.grid(row = 1, column = 1)
        
        # Create button to convert the code into text
        self.action_button = tkinter.Button(self.frame, text = "Decode" , command = self.on_click_decode).grid(row = 2, column = 1)
        
    # Create a window for cipher encoding
    def c_encode_window(self):
        self.clear_frame()
        tkinter.Label(self.frame, text = "Enter text to encode: ").grid(row = 1, column = 0)
        tkinter.Label(self.frame, text = "Enter number of shift : ").grid(row = 2, column = 0)
        
        # Create one entry fields
        self.input_field_1 = tkinter.Entry(self.frame)
        self.input_field_1.grid(row = 1, column = 1)
        self.input_field_2 = tkinter.Entry(self.frame)
        self.input_field_2.grid(row = 2, column = 1)
        
        # Create button to convert the text into code
        self.action_button = tkinter.Button(self.frame, text = "Encode" , command = self.on_click_c_encode).grid(row = 3, column = 1)
        
    # Create a window for cipher decoding
    def c_decode_window(self):
        self.clear_frame()
        tkinter.Label(self.frame, text="Enter cipher code :").grid(row=1, column=0)
        tkinter.Label(self.frame, text="Enter number of shift :").grid(row=2, column=0)
        
        # Create one entry fields
        self.input_field_1 = tkinter.Entry(self.frame)
        self.input_field_1.grid(row = 1, column = 1)
        self.input_field_2 = tkinter.Entry(self.frame)
        self.input_field_2.grid(row = 2, column = 1)
        
        # Create button to convert the code into text
        self.action_button = tkinter.Button(self.frame, text = "Decode" , command = self.on_click_c_decode).grid(row = 3, column = 1)
        
    def on_click_c_encode(self):
        text = self.input_field_1.get()
        shift = int(self.input_field_2.get())
        result = cipher_text(text,shift)
        self.result_label.config(text=f"Encoded Text: {result}")
    def on_click_c_decode(self):
        cipher_code = self.input_field_1.get()
        shift = int(self.input_field_2.get())
        result = decipher_text(cipher_code,shift)
        self.result_label.config(text=f"Decoded Text: {result}")
    
    def on_click_decode(self):
        morse_code = self.input_field.get()
        result = decode_morse(morse_code)
        self.result_label.config(text=f"Decoded Text: {result}")
        
    def on_click_encode(self):
        text = self.input_field.get()
        result = encrypt_morse(text)
        self.result_label.config(text=f"Encoded Text: {result}")
        
if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(root)
    root.mainloop()