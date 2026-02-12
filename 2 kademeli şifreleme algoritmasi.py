text = ' ' + 'Herhangi bir metin'
pxval = 0

def encrypter(text):
    array = []
    arrayY = []

    for charX in text:
        array.append(ord(charX))

    for charY in array:
        locallst = []
        for itemX in str(charY):
            locallst.append(ord(itemX))
        locallst.insert(len(locallst),f'term: {len(locallst)}')
        for xER in locallst:
            arrayY.append(xER)

        locallst.clear()

    return arrayY

def decrypter(encrypted):
    enc_cache = []
    dec_array = []
    index = 0

    for encX in encrypted:
        if isinstance(encX,str):
            if index <= 0:
                enc_cache.append(encrypted[index - int(encX.split(':')[1].strip()) - 1:index])
            
            if index > int(encX.split(':')[1].strip()) - 1:
                enc_cache.append(encrypted[index - int(encX.split(':')[1].strip()) - 1:index])

        yield (enc_cache.copy())
        enc_cache.clear()

        index += 1

def decryptedTX(decrypted_enc):
    pX = []
    global pxval

    for vektör in decrypted_enc:
        if len(vektör.copy()) > 0:
            for chX in vektör.copy()[0]:
                if type(chX) != str:    
                    pX.append(chr(chX).strip())

            item = ''.join(pX.copy())
            if len(item) > 0:
                yield (chr(int(str(item))))
                pX.clear()


eX1,eX2,eX3 = None,None,None

encrypted_text = encrypter(text)
eX1 = encrypted_text.copy()

raw_decrypted_text = [tX for tX in decrypter(eX1) if len(tX) > 0]
eX2 = raw_decrypted_text

decrypted_text = [tX for tX in decryptedTX(eX2)]
eX3 = decrypted_text.copy()

print(f'Orjinal metin: {text}\n\n\n\nŞifrelenmiş metin: {eX1}\n\n\n\nHam çözülmüş metin:{eX2}\n\n\n\nÇözülmüş metin:{eX3}')



