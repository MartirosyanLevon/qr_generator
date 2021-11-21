import pyqrcode

start = True
while start:
    s = input('Enter your link for creating qr code:')
    url = pyqrcode.create(s)

    url.svg('qr_generator.svg', scale=8)
    url.png('qr_generator.png', scale=6)
    print(f'Here is your qr code{url.terminal(quiet_zone=1)}')
    end = input("if you want to exit enter 'q' for continue 'enter'")
    if end == 'q':
        break
    else:
        continue
