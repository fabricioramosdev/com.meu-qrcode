import qrcode
class FreeText():

    def __init__(self):
        qr = qrcode.QRCode(
            version = 2,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size =5,
            border=2,)
        qr.add_data('daiane ramos\nEstudando python\t a esta hora')
        qr.make(fit=True)
        img = qr.make_image(fill_color="#58b9c8", back_color="white")
        img.save('image.png')

if __name__ == '__main__':
    freetext = FreeText()