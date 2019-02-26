def ocr(img):
    import cv2

    import pytesseract
  
    #from matplotlib import pyplot as plt
    # Uncomment the line below to provide path to tesseract manuall
    pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
    # Define config parameters.
      
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    config = ('-l eng --oem 1 --psm 3')


    # Our operations on the frame come here
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 

    # Run tesseract OCR on image
    text = pytesseract.image_to_string(img, config=config)
    # Print recognized text
    return (text)


