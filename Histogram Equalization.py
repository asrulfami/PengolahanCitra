import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image_path):
    # Membaca citra dalam mode grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Menghitung histogram asli
    hist, bins = np.histogram(image.flatten(), 256, [0, 256])
    
    # Menghitung histogram kumulatif
    cdf = hist.cumsum()
    
    # Normalisasi histogram kumulatif
    cdf_normalized = cdf * hist.max() / cdf.max()
    
    # Masking nilai 0
    cdf_m = np.ma.masked_equal(cdf, 0)
    
    # Normalisasi cdf
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    
    # Mengisi kembali nilai 0 yang di-mask dengan 0
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    
    # Menerapkan transformasi ke citra asli
    image_equalized = cdf[image]
    
    # Menampilkan hasil
    plt.figure(figsize=(12, 6))
    
    # Plot citra asli
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Citra Asli')
    plt.axis('off')
    
    # Plot histogram citra asli
    plt.subplot(2, 2, 2)
    plt.plot(hist, color='black')
    plt.title('Histogram Citra Asli')
    
    # Plot citra hasil equalization
    plt.subplot(2, 2, 3)
    plt.imshow(image_equalized, cmap='gray')
    plt.title('Citra Hasil Histogram Equalization')
    plt.axis('off')
    
    # Plot histogram citra hasil equalization
    hist_eq, bins_eq = np.histogram(image_equalized.flatten(), 256, [0, 256])
    plt.subplot(2, 2, 4)
    plt.plot(hist_eq, color='black')
    plt.title('Histogram Citra Hasil Equalization')
    
    plt.tight_layout()
    plt.show()

# Panggil fungsi dengan path ke citra Anda
histogram_equalization('man.png')
