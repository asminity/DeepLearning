import cv2

img = cv2.imread("../Pexels/parrot.jpg",0)

if img is None:
    print("Error: Image not found") 
else:
    print("Image loaded successfully")
    print(img.shape)