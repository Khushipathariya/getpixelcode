import cv2

# Load the image
img = cv2.imread("download.jpg")   # change "test.jpg" to your image name

if img is None:
    print("Error: Image not found!")
    exit()

# Get image size
height, width = img.shape[:2]
print("Width:", width)
print("Height:", height)

# Get pixel at (x, y)
x = 100
y = 50

b, g, r = img[y, x]   # OpenCV = BGR
print(f"Pixel at ({x},{y}) -> R={r}, G={g}, B={b}")
