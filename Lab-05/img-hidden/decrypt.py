import os
import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""

    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))

            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]

                # Kiểm tra chuỗi kết thúc
                if len(binary_message) >= 16 and binary_message[-16:] == '1111111111111110':
                    # Chuyển đổi binary_message thành thông điệp
                    message = ""
                    for i in range(0, len(binary_message) - 16, 8):  # Loại bỏ chuỗi kết thúc
                        char = chr(int(binary_message[i:i+8], 2))
                        if char == '\0':
                            break
                        message += char
                    return message

    return "No hidden message found."

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return

    encoded_image_path = sys.argv[1]

    # Kiểm tra tệp tồn tại
    if not os.path.exists(encoded_image_path):
        print(f"Error: File '{encoded_image_path}' not found.")
        return

    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()