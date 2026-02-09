import cv2

img = cv2.imread("../Pexels/parrot.jpg")

if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("parrot_gray.jpg", gray)
    print("Grayscale image saved successfully")
else:
    print("Error: Image not found")
