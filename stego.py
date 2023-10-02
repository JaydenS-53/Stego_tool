# Holds all functions of trailer based steganography, this appends teh data to the end of the image file
# Advantages: Simple, Easy to extract, Doesn't affect image quality, Large capacity, Low chance of detection
# Disadvantages: Vulnerable to forensic analysis, No encyrption, Corrupts if any compression occurs, Limited secrecy
class trailer_stego:

    # function to insert text at the end of the file
    def insert_text(img, string):
        with open(img, 'ab') as i:
            string_in_bytes = string.encode('utf-8')
            i.write(string_in_bytes)
    
    # function to extract text at the end of the file
    def extract_data_after_ffd9(img):
        with open(img, 'rb') as i:
            content = i.read()[::-1]  # Read content in reverse
            ff_d9_marker = b'\xFF\xD9'# Set marker at end of file

            try:
                offset = content.index(ff_d9_marker[::-1])  # Find the position of FF D9 marker
                extracted_data = content[:offset][::-1].decode('latin-1')  # Convert bytes to string
                return extracted_data
            except ValueError as e:
                print(f"Error: {e}. End of Image marker not found.") # Print error if FF D9 not present
                return None
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return None


# testing
# trailer_stego.insert_text('img.jpeg', 'hello world')
extracted_data = trailer_stego.extract_data_after_ffd9('img.jpeg')

if extracted_data is not None:
    print(extracted_data)  
