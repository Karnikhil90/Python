import qrcode
import name

def createQR(data:str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    file_name = "qrcode.png"
    file = name.get_name(file_name)
    
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    image.save(file)
    print(f"file='{file}' data='{data}'")
    
createQR(input("Enter the data:"))