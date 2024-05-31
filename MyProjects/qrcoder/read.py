import cv2
from pyzbar import pyzbar

# Load the image containing the QR code
def readQR(filename):
    if not filename.endswith(".png"):
        filename = filename + ".png"
    
    image = cv2.imread(filename)

    # Decode the QR code
    decoded_objects = pyzbar.decode(image)

    # Print the decoded information
    for obj in decoded_objects:
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"))

    if not decoded_objects:
        print("No QR code found in the image.")

readQR(input("Enter the file name: "))