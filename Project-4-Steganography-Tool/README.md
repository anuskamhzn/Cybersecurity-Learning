# Image Steganography Tool (Python)

## Overview
This project is a Python-based image steganography tool that hides a secret text
message inside an image using the Least Significant Bit (LSB) technique and
extracts it back without visibly altering the image.

## How It Works
- The secret message is converted into binary
- Binary data is embedded into the least significant bits of image pixels
- The modified image looks visually unchanged
- The hidden message can be extracted by reading the LSBs

## Features
- User-defined secret message
- Supports PNG images
- Simple command-line interaction
- Reliable message extraction

## Tools & Technologies
- Python 3
- Pillow (PIL)
- Kali Linux / Windows

## Usage

### Install dependency
```bash
pip install pillow

Encode a message:
```bash
python encode.py
```
```bash
Example input:
Enter image name: sample_image.png
Enter secret message: Hello from steganography
Enter output image name: output.png
```
Decode the message:
```bash
python decode.py
```

```bash
Example output:
Hidden Message: Hello from steganography
```

Use Case:

- This project demonstrates fundamental concepts used in:
- Digital forensics
- Covert communication
- Data hiding techniques in cybersecurity