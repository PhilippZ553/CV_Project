import cv2

img = cv2.imread('test.jpg')

if img is None:
    print("img not found")
else:
    width = 600
    ratio = width / img.shape[1]
    height = int(img.shape[0] * ratio)
    img_small = cv2.resize(img, (width, height))

    gray = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('original)', img_small)
    cv2.imshow('gray', gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()