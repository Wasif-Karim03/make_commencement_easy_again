import qrcode

# The local server URL
url = 'http://192.168.68.59:8000/qr_scanner.html'

# Generate QR code
qr = qrcode.make(url)
qr.save('qr_scanner_link.png')
print('QR code saved as qr_scanner_link.png') 