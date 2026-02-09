import cv2

image = cv2.imread("../Pexels/tiger.jpg")

if image is not None:
    resized_image = cv2.resize(image, (250, 250))
    cv2.imshow("Resized Image", resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found")