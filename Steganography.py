#Steganography

import cv2
import time
from os import stat
HEADER_SIZE = 30
FILE_NAME = 20
FILE_SIZE = 10

def splitByte(val):
    #104 ---> [011, 010, 00]
    bits =[]
    bits.append((val & 0xE0)>>5)
    bits.append((val & 0x1C)>>2)
    bits.append((val & 0x3))
    return bits

def mergeBits(bits):
    #[011, 010, 00] ---> 104
    return (((bits[0] << 3) | bits[1]) << 2) | bits[2]

def getsize(document):
    try:
        # using os.stat to find the size of the file in bytes
        return stat(document).st_size
    except:
        return -1


def processDocumentName(document):
    # document: 'd:/rahulcomp/images/kids.jpg'
    fname = document.split('/')[-1]
    if len(fname) > FILE_NAME:
        # slice the fname
        return fname[len(fname)-FILE_NAME:]
    else:
        # left pad with _
        return fname.rjust(FILE_NAME, '_')


def processDocumentSize(document):
    size = getsize(document)
    if size == -1:
        return None

    s_size = str(size)
    if len(s_size) > FILE_SIZE:
        return None
    return s_size.rjust(FILE_SIZE, '_')


def embed(imageFile, document, resultantFile):
    start_time = time.time()
    # read the source image
    arr_img = cv2.imread(imageFile, cv2.IMREAD_COLOR)
    # if imageFile exists then src_img is a 3D numpy array (h,w,(b,g,r))
    # otherswise src_img is None

    if arr_img is None:
        print('Source Image Not Found')
        return

    w = arr_img.shape[1]
    h = arr_img.shape[0]
    capacity = w*h
    print('Embedding Capacity : ', capacity)

    doc_size = getsize(document)
    if doc_size == -1:
        print(document, 'not found')
        return

    print('Required Capacity : ', doc_size)

    if doc_size + HEADER_SIZE > capacity:
        print('Cannot embed', document , 'in', imageFile)
        return

    header = processDocumentName(document) + processDocumentSize(document)

    #open the document
    fh = open(document, 'rb')

    #Embedding
    i=cnt= 0
    flag = True

    while i < h and flag:
        j=0
        while j < w:
            if cnt < HEADER_SIZE:
                #data comes from the header
                data = ord(header[cnt])
            else:
                #data comes from the file in byte object form
                #and it is None at EOF
                data = fh.read(1)

                if data:
                    #fetched, now convert the byte object to int
                    data = int.from_bytes(data, byteorder='big')
                else:
                    #EOF : stop embedding
                    fh.close()
                    flag = False
                    break

            #data available now
            bits = splitByte(data)

            #LSB overwriting
            arr_img[i,j,0] = (arr_img[i,j,0] & ~0x7) | bits[0] #b
            arr_img[i,j,1] = (arr_img[i,j,1] & ~0x7) | bits[1] #g
            arr_img[i,j,2] = (arr_img[i,j,2] & ~0x3) | bits[2] #r

            cnt+=1
            j+=1
        i+=1
    #save back the image
    cv2.imwrite(resultantFile, arr_img)
    print('embedding done in ', time.time()- start_time, 'seconds')

def extract(imageFile, resultantFolder):
    start_time = time.time()
    # read the source image
    arr_img = cv2.imread(imageFile, cv2.IMREAD_COLOR)
    # if imageFile exists then src_img is a 3D numpy array (h,w,(b,g,r))
    # otherswise src_img is None

    if arr_img is None:
        print('Source Image Not Found')
        return

    w = arr_img.shape[1]
    h = arr_img.shape[0]

    #Extraction
    i=cnt= 0
    flag = True

    header = ''
    while i < h and flag:
        j=0
        while j < w:
            #extract bits from the pixel
            b1 = arr_img[i,j,0] & 0x7
            b2 = arr_img[i,j,1] & 0x7
            b3 = arr_img[i,j,2] & 0x3

            #form the byte by merging the bits
            data = mergeBits([b1,b2,b3])

            if cnt < HEADER_SIZE:
                #recreate the header
                header = header + chr(data)
            else:
                if cnt == HEADER_SIZE:
                    #extract content and recreate the document
                    doc_name = resultantFolder + '/' + header[:FILE_NAME].strip('_')
                    doc_size = int(header[FILE_NAME:].strip('_')) + cnt
                    fh = open(doc_name, 'wb')


                if cnt < doc_size:
                    #binary writing requires byte objects and not the ASCII, hence convert.
                    fh.write(int.to_bytes(int(data), 1, byteorder='big'))
                else:
                    fh.close()
                    print('Extraction Complete in ', time.time()- start_time, 'seconds')
                    print('See: ' , doc_name)
                    flag = False
                    break

            cnt+=1
            j+=1
        i+=1



embed('d:/rahulcomp/images/work.jpg', 'd:/rahulcomp/images/kids.jpg', 'd:/rahulcomp/images/result.png')
extract('d:/rahulcomp/images/result.png', 'd:/rahulcomp/temp')


