# Stego_tool

Overview
Stego_tool is a Python-based tool for steganography, the art of hiding information within other non-secret data. This tool allows users to embed and extract hidden messages within image files using various steganographic techniques.

Features
Image Steganography: Embed secret messages within image files.
Multiple Techniques: Supports various steganographic techniques for hiding data.
User-Friendly Interface: Easy-to-use command-line interface for embedding and extracting messages.
Cross-Platform: Works on Windows, macOS, and Linux.

Installation
Clone the repository:
git clone https://github.com/JaydenS-53/Stego_tool.git

Navigate to the project directory:
cd Stego_tool

Install the required dependencies:
pip install -r requirements.txt

Usage:
Embedding a Message
To embed a message in an image file, use the following command:

python stego_tool.py embed -i input_image.jpg -m "Your secret message" -o output_image.png
Replace input_image.jpg with the path to your original image, "Your secret message" with the message you want to hide, and output_image.png with the desired name for the new image.

Extracting a Message
To extract a hidden message from an image file, use the following command:

python stego_tool.py extract -i stego_image.png -o extracted_message.txt
Replace stego_image.png with the path to the image containing the hidden message, and extracted_message.txt with the desired name for the extracted message file.

Supported Techniques
Least Significant Bit (LSB) Steganography
Trailer Based Steganography
