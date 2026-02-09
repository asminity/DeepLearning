import cv2

img = cv2.imread("../Pexels/parrot.jpg",1)

if img is None:
    print("Error: Image not found") 
else:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
