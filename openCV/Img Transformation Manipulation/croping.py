import cv2

image = cv2.imread("../Pexels/python.jpg")
print(image.shape)

if image is not None:
    cropped = image[1000:2000, 3000:4000]
    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")