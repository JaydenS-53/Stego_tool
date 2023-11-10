import PIL.Image
import io
from PIL import Image
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

    # function to generate the binary data for each pixel that will be modified
    def gen_data(self, data):
        # list of binary codes of given data
        new_data = []
        # generate binary data for each pixel
        for d in data:
            new_data.append(format(ord(d), '08b'))
        return new_data
    
    # function to modify each pixels least significant bit
    def modPix(self, pixels, data):
        
        # generate list of pixels that will have data embedded into them
        datalist = LSB.gen_data(data)
        length_of_data = len(datalist)
        imdata = iter(pixels)
 
        for i in range(length_of_data):
    
            # extract 3 pixels at a time
            pixels = [value for value in imdata.__next__()[:3] +
                                    imdata.__next__()[:3] +
                                    imdata.__next__()[:3]]
    
            # pixel values are 1 for odd and 0 for even
            for j in range(0, 8):
                if (datalist[i][j] == '0' and pixels[j]% 2 != 0):
                    pixels[j] -= 1
    
                elif (datalist[i][j] == '1' and pixels[j] % 2 == 0):
                    if(pixels[j] != 0):
                        pixels[j] -= 1
                    else:
                        pixels[j] += 1
                    
    
            # if eight pixel is 0 we need to keep reading, if it is 1 then the message is over
            if (i == length_of_data - 1):
                if (pixels[-1] % 2 == 0):
                    if(pixels[-1] != 0):
                        pixels[-1] -= 1
                    else:
                        pixels[-1] += 1
            # if it isn't the last set of pixels ...
            else:
                # checks the LSB to see if we need to continue processing or not
                if (pixels[-1] % 2 != 0):
                    pixels[-1] -= 1
            # convert pixels back to a tupel ready for yielding
            pixels = tuple(pixels)
            # turns function to a generator so that the execution can pause and generate values one at a time rather than all at once
            yield pixels[0:3]
            yield pixels[3:6]
            yield pixels[6:9]

    # function to encode pixels
    def encode_enc(img, data):
        size = img.size[0]
        (x, y) = (0, 0)
        # iterate through pixels and run through modifying pixel function
        for pixel in LSB.modPix(img.getdata(), data):
    
            # inserting modified pixels in the new image
            img.putpixel((x, y), pixel)
            if (x == size - 1):
                x = 0
                y += 1
            else:
                x += 1
    
    # function to encode data into image
    def encode():
        # receive input from user to get filename and data to encode
        img = input("Enter img name (with extension) : ")
        image = Image.open(img, 'r')
        data = input("Enter text to be encoded : ")
        if (len(data) == 0):
            raise ValueError('Data is empty')
        # create new image with modified pixels inserted
        newimg = image.copy()
        LSB.encode_enc(newimg, data)
        # saving new image
        new_img_name = input("Enter the name of new img (with extension) : ")
        newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

    # function to decode the data in the image
    def decode():
        # get image and open, open string to append extracted data to
        img = input("Enter img name (with extension) : ")
        image = Image.open(img, 'r')
        data = ''
        imgdata = iter(image.getdata())
        # iterate through LSB of pixels
        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3] +
                                    imgdata.__next__()[:3]]
    
            # string of binary data
            binstr = ''
            # store each LSB to the data string
            for i in pixels[:8]:
                if (i % 2 == 0):
                    binstr += '0'
                else:
                    binstr += '1'
            # return data
            data += chr(int(binstr, 2))
            if (pixels[-1] % 2 != 0):
                return data
            

# testing
# trailer_stego.insert_text('img.jpeg', 'hello world')
#extracted_data = trailer_stego.extract_text('img.jpeg')

#if extracted_data is not None:
    # print(extracted_data)  
