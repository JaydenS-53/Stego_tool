import PIL.Image
import io
# Class to hold all functions of trailer based steganography, this appends teh data to the end of the image file
# Advantages: Simple, Easy to extract, Doesn't affect image quality, Large capacity, Low chance of detection
# Disadvantages: Vulnerable to forensic analysis, No encyrption, Corrupts if any compression occurs, Limited secrecy
class trailer_stego:

    # function to insert text at the end of the file
    def insert_text(img, string):
        with open(img, 'ab') as i:
            string_in_bytes = string.encode('utf-8')
            i.write(string_in_bytes)
    
    # function to extract text at the end of the file
    def extract_text(img):
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
    
    # function to insert image at the end of the file
    def insert_image(dummie_img, hidden_img):
        hidden_img = PIL.image.open('image.png') # open image and save as png
        byte_arr = io.BytesIO()
        hidden_img.save(byte_arr, format='PNG')
        with open(dummie_img, 'ab') as i: # open dummie image (image that the hidden image hides in)
            i.write(byte_arr.getvalue()) # write hidden image to dummie image
        
        return "Image inserted."
    
    # function to extract image at the end of the file
    def extract_image(img):
        with open(img, 'rb') as i:
            content = i.read()[::-1]  # Read content in reverse
            ff_d9_marker = b'\xFF\xD9' # Set marker at end of file

            try:
                offset = content.index(ff_d9_marker[::-1])  # Find the position of FF D9 marker
                extracted_data = content[:offset][::-1].decode('latin-1')  # Convert bytes to string
                extracted_data.save("hidden_img.png")
                return "Image saved as hidden_img.png"
            except ValueError as e:
                print(f"Error: {e}. End of Image marker not found.") # Print error if FF D9 not present
                return None
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return None
            
    # function to insert exe file at the end of the file
    def insert_exe(img, exe):
        with open(img, 'ab') as i, open(exe, 'rb') as e: # open image and exe file
            exe = e.encode('utf-8') # encode exe file
            i.write(exe) # write to image file
        return ".exe file inserted."
    
    # function to extract exe file at the end of the file
    def extract_exe(img):
        with open(img, 'rb') as i:
            content = i.read()[::-1]  # Read content in reverse
            ff_d9_marker = b'\xFF\xD9' # Set marker at end of file

            try:
                offset = content.index(ff_d9_marker[::-1])  # Find the position of FF D9 marker
                extracted_data = content[:offset][::-1].decode('latin-1')  # Convert bytes to string
                extracted_data.save("file.exe")
                return ".exe saved as file.exe"
            except ValueError as e:
                print(f"Error: {e}. End of Image marker not found.") # Print error if FF D9 not present
                return None
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return None
    
# Class to hold all functions of LSB stegonography, this is where information is embedded into the least significant bits of the pixel values of the image.
# Advantages: can hide large amounts of data, fast encoding/decoding, preserves image quality, harder to see than trailer based
# Disadvantages: sensitive to lossy compression, widely known technique so can be cracked, easy to detect in digital forensics
class LSB:

    # insert text using LSB modification
    def insert_text():
        pass
    
    # extract text using LSB modification
    def extract_text():
        pass

# testing
# trailer_stego.insert_text('img.jpeg', 'hello world')
extracted_data = trailer_stego.extract_text('img.jpeg')

if extracted_data is not None:
    print(extracted_data)  
