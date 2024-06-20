import cv2
import numpy as np
from matplotlib import pyplot as plt

# Membaca gambar
image = cv2.imread('macan.jpg', 0)  # Membaca gambar dalam mode grayscale

# Menerapkan filter Gaussian
kernel_size = (5, 5)  # Ukuran kernel (bisa disesuaikan)
sigma = 1  # Deviasi standar Gaussian (bisa disesuaikan)
blurred_image = cv2.GaussianBlur(image, kernel_size, sigma)

# Menampilkan gambar asli dan gambar yang telah difilter
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(blurred_image, cmap='gray'), plt.title('Gaussian Blurred Image')
plt.show()
