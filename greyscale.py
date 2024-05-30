from PIL import Image
import os

def grayscale(input_image_path, output_folder):
    # Pastikan output folder tersedia
    os.makedirs(output_folder, exist_ok=True)
    
    # Buka gambar
    img = Image.open(input_image_path)
    
    # Konversi ke skala abu-abu
    img = img.convert('L')
    
    # Dapatkan nama file tanpa ekstensi
    filename_without_extension = os.path.splitext(os.path.basename(input_image_path))[0]
    
    # Simpan gambar yang sudah dikonversi
    output_image_path = os.path.join(output_folder, filename_without_extension + "_gray.jpg")
    img.save(output_image_path)
    
    print(f"Gambar berhasil dikonversi ke skala abu-abu dan disimpan sebagai {output_image_path}")
    
    # Tampilkan gambar yang telah disimpan
    img.show()

# Contoh penggunaan
input_image_path = r"D:/Semester 4/Pengolahan Citra/kemejagw.jpg"
output_folder = r"D:/Semester 4/Pengolahan Citra"

grayscale(input_image_path, output_folder)
