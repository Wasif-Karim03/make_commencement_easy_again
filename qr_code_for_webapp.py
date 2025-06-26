import qrcode

url = 'https://wasif-karim03.github.io/make_commencement_easy_again/index.html'
qr = qrcode.make(url)
qr.save('webapp_qr.png')
print('QR code for web app saved as webapp_qr.png') 