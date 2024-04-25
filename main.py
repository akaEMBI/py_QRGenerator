import qrcode  # Mengimpor modul qrcode untuk membuat QR code

def generate_qr_code(data, filename, version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                     box_size=10, border=4, fill_color="black", back_color="white"):
    # Fungsi untuk menghasilkan QR code dari data yang diberikan
    qr = qrcode.QRCode(  # Membuat objek QRCode
        version=version,  # Versi QR code (default: 1)
        error_correction=error_correction,  # Tingkat koreksi error (default: LOW)
        box_size=box_size,  # Ukuran kotak dalam QR code
        border=border,  # Lebar border QR code
    )
    qr.add_data(data)  # Menambahkan data ke QR code
    qr.make(fit=True)  # Membuat QR code dengan ukuran yang sesuai
    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)  # Membuat gambar QR code dengan warna yang ditentukan
    qr_img.save(filename)  # Menyimpan gambar QR code dengan nama file yang ditentukan
    print(f"QR code generated and saved as {filename}")  # Menampilkan pesan bahwa QR code telah berhasil dibuat dan disimpan

def main():
    while True:  # Loop utama program
        print("\nMenu:")
        print("1. Generate QR CODE")  # Opsi untuk membuat QR code
        print("2. EXIT")  # Opsi untuk keluar dari program

        choice = input("Enter your choice: ")  # Meminta input pilihan dari pengguna

        if choice == '1':  # Jika pilihan adalah 1, mulai proses pembuatan QR code
            print("\nChoose data type:")  # Meminta pengguna untuk memilih jenis data untuk QR code
            print("1. Link (URL)")  # Pilihan untuk membuat QR code dari link (URL)
            print("2. Text")  # Pilihan untuk membuat QR code dari teks
            print("3. Back to Main Menu")  # Pilihan untuk kembali ke menu utama

            data_choice = input("Enter your data type choice: ")  # Meminta input jenis data dari pengguna

            if data_choice == '1':  # Jika pilihan adalah 1, meminta input link (URL) dari pengguna
                data = input("Enter the link (URL) for QR code: ")
                if not data.startswith("http://") and not data.startswith("https://"):
                    print("Invalid link format. Please enter a valid URL.")  # Validasi format link
                    continue
            elif data_choice == '2':  # Jika pilihan adalah 2, meminta input teks dari pengguna
                data = input("Enter the text for QR code: ")
            elif data_choice == '3':  # Jika pilihan adalah 3, kembali ke menu utama
                continue
            else:
                print("Invalid data type choice. Please enter 1, 2, or 3.")  # Pesan jika pilihan tidak valid
                continue

            filename = input("Enter the filename to save the QR code (e.g., example.png): ")  # Meminta input nama file untuk menyimpan QR code
            if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):  # Validasi ekstensi file
                print("Invalid file format. Please use .png or .jpg extension.")
                continue

            generate_qr_code(data, filename)  # Panggil fungsi untuk membuat QR code
        elif choice == '2':  # Jika pilihan adalah 2, keluar dari program
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")  # Pesan jika pilihan tidak valid

if __name__ == "__main__":
    main()  # Panggil fungsi main() untuk menjalankan program
