# Stego_tool

This project is a toolbox of different steganography methods, beginning with trailer based and then moving to LSB (least significant bit) and then pallette based steganography. For each technique I have encapsulated a class to hold the functions that input/extract text, images and files.

I decided to write this in python due to its huge range of libraries and how easy it is to read/write from files.

Trailer based:
This is where the data is written to or read from the end of the image, after the magic bytes.

Least Significant bit:
This is where data is embedded into the last bit of the 8 bit binary patterns of the image.

Pallette Based:
This changes the images pixel colours slightly to store the data, the changes are litle enough to be hidden from the human eye, but with larger files this can be noticable.
