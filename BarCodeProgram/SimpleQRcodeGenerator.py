import pyqrcode
def qrcode(x):
	if(x==""):
		x='Code written by Bharat Rawat'
	try:
		qr=pyqrcode.create(x)
		qr.png('abc.png',scale=10)
		print('QR Code genratoed...')
	except:
		print("Something went wrong check may be you install modules")
if __name__=='__main__':
    x=input()
    qrcode(x)





