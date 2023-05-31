import os
os.system("cls")
#Variabel untuk menampung key dan values data
dataTampungan = [
    {
        'nama': 'Oza',
        'umur': 26,
        'jumlah buku': 1
    },
    {
        'nama': 'Fatar',
        'umur': 28,
        'jumlah buku': 2
    }
]

#Main Menu pada terminal
def menu_awal ():
    print('''
    ===== Perpustakaan Tersyahdu =====\n
    1. Lihat Data Peminjam Buku
    2. Pinjam Buku Perdana
    3. Perbarui Data Peminjam Buku
    4. Hapus Data Peminjam Buku
    5. Exit Menu''')

#Menu untuk melihat Data Peminjam pada Perpustakaan
def readData():
    print('''
    ===== Lihat Data Peminjam =====\n
    1. Lihat Seluruh Data Peminjam Buku
    2. Lihat Data Peminjam Buku dan jumlah Buku yang dipinjam
    3. Kembali ke Menu Utama\n''')
    menuReadData = input("Silahkan masukkan pilihan Sub menu Lihat Data di atas[1-3]: ")
    if menuReadData == "1":
        print("\nNo |   Nama Peminjam   |   Umur   |   Jumlah Buku")
        for i in dataTampungan:
            print(f"{dataTampungan.index(i)+1} \t{i.get('nama')}\t\t {i.get('umur')} Tahun\t{i.get('jumlah buku')} Buku")
        
        pilihanMenu = input("\nKembali ke Menu Utama? (y/n): ")
        if pilihanMenu == "y":
            return
        elif pilihanMenu == "n":
            readData()

    elif menuReadData == "2":
        print("\nNo |   Nama Peminjam   |   Umur   |   Jumlah Buku")
        for i in dataTampungan:
            print(f"{dataTampungan.index(i)+1} \t{i.get('nama')}\t\t {i.get('umur')} Tahun\t{i.get('jumlah buku')} Buku")               
        cariPeminjam = input("\nSilahkan masukkan Nama Peminjam Buku yang anda cari : ")
        if cariPeminjam:
            for i in dataTampungan:
                if i.get('nama') == cariPeminjam:
                    print("\nNo |   Nama Peminjam   |   Jumlah Buku")
                    print(f"{dataTampungan.index(i)+1}\t  {i.get('nama')}\t\t {i.get('jumlah buku')} Buku")
            
            pilihanMenu = input("\nKembali ke Menu Utama? (y/n): ")
            if pilihanMenu == "y":
                True
            elif pilihanMenu == "n":
                readData()
        else:
            print("Data tidak ditemukan!")
    elif menuReadData == "3":
        return

#Function untuk membuat Data Peminjam Perdana
def createData():
        print('''
        ===== Sub Menu Tambahkan Data =====\n
        1. Tambahkan Data Peminjam Buku
        2. Kembali ke Menu Utama''')
        pilihanCreate  = input('\nSilahkan pilih Sub Menu Create Data [1-2]:\n')

        if pilihanCreate == "1":
            nama = input('Masukkan nama: ')
            umur = input('Masukkan umur: ')
            jumlah_buku = input('Masukkan jumlah buku: ')
            daftarBuku = {"nama": nama, "umur": umur, "jumlah buku" : jumlah_buku}
            if jumlah_buku:
                # print(jumlah_buku.isnumeric())
                if jumlah_buku.isnumeric():
                    dataTampungan.append(daftarBuku)
                    print('''\n===== Data Perpurstakaan Tersyahdu =====\n''')
                    print(f'Nama :\t{nama}\nUmur :\t{umur}\nBuku: \t{jumlah_buku}')
                    print('\nData Peminjam Buku telah ditambahkan!\n')
                    createData()
                else:
                     print("Format Data tidak sesuai")
            else:
                print("Data belum dimasukkan!")
                createData()
        elif pilihanCreate == "2":
            True

#Function untuk menambahkan items dan melakukan update data pada peminjam buku
def updateData():
    global dataTampungan
    print('''
    ===== Sub Menu Update Data =====
    1. Update seluruh data peminjam buku
    2. Menambah jumlah buku yang baru dipinjam
    3. Kembali ke menu utama
    ''')

    pilihanUpdate  = input('\nSilahkan pilih Sub Menu Update Data [1-3]:\n')
    
     # variabel temporary
    foundData = False

    if pilihanUpdate == '1':
        print("\nNo |   Nama Peminjam   |   Umur   |   Jumlah Buku")
        for i in dataTampungan:
            print(f"{dataTampungan.index(i)+1} \t{i.get('nama')}\t\t {i.get('umur')} Tahun\t{i.get('jumlah buku')} Buku")
        
        nama = input('masukkan nama yang akan diupdate: ')
        if nama == '':
            print('mohon masukkan nama kembali')
            nama = input('masukkan nama yang akan diupdate: ')
        elif nama:
            for i in dataTampungan:
                if i.get('nama') == nama:
                    foundData = True
                
            if foundData:
                updatedNama = input('masukkan nama baru: ')
                umur = int(input('masukkan umur terkini: '))
                jumlah_buku = input('masukkan jumlah buku: ')
                updatedData = {'nama': updatedNama, 'umur': umur, 'jumlah buku' : jumlah_buku}
                
                if jumlah_buku:
                    if jumlah_buku.isnumeric():
                        updatedList = []
                        for i in dataTampungan:
                            if i.get('nama') != nama:
                                updatedList.append(i)
                        updatedList.append(updatedData)
                        
                        dataTampungan = updatedList
                        print('\nData telah update!\n')
                        print(f'Nama :\t{updatedNama}\nUmur :\t{umur}\nBuku:\t{jumlah_buku}')
                    else:
                        print("\nFormat Data tidak sesuai\n")
            else:
                print('data tidak ditemukan')

    elif pilihanUpdate == '2' :
        print("\nNo |   Nama Peminjam   |   Umur   |   Jumlah Buku")
        for i in dataTampungan:
            print(f"{dataTampungan.index(i)+1} \t{i.get('nama')}\t\t {i.get('umur')} Tahun\t{i.get('jumlah buku')} Buku")
        namaTambahBuku = input("Masukkan nama yang ingin ditambahkan jumlah buku:")
        jumlahTambahBuku = int(input("Masukkan jumlah buku yang ditambahkan: "))
        for i in dataTampungan:
            if i['nama'] == namaTambahBuku:
                i['jumlah buku'] += jumlahTambahBuku
        print("Jumlah buku berhasil ditambahkan !")

#Function untuk menghapus Data Peminjam
def hapusData():
    print('''
    =====Sub Menu Hapus Data Member Perpustakaan=====

    1. Hapus Data Peminjam Buku sesuai kriteria
    2. Kembali ke Menu Utama

    ''')
    pilihanHapus = input("Silahkan masukkan pilihan pada Sub Menu Hapus Data [1-2]:")

    if pilihanHapus == "1":
        if len(dataTampungan) == 0:
            print("Tidak ada data yang dapat dihapus")
        else:
            print("\nNo |   Nama Peminjam   |   Umur   |   Jumlah Buku")
            for i in dataTampungan:
                print(f"{ dataTampungan.index(i)+1} \t{i.get('nama')}\t\t {i.get('umur')} Tahun\t{i.get('jumlah buku')} Buku")      

        index = int(input("Masukkan nomor data yang ingin dihapus [1-1000]: ")) - 1 
        if index:
            deleted_data = dataTampungan.pop((index))
            print(f"\n\nData nomor {str(index+1)} Berhasil dihapus!\n")
            return deleted_data
        elif index < 0 or index >= len(dataTampungan):
            print("Nomor data tidak valid")
        else:
            deleted_data = dataTampungan.pop(index)
            print(f"\n\nData nomor {str(index+1)} berhasil dihapus!")
            return deleted_data
            # print("\nNo |   Nama Peminjam   |   Umur   |   Jumlah Buku")
            # print(f"{ dataTampungan.index(i)+1}\t  {i['nama']}\t\t {i['umur']} Tahun\t{i['jumlah buku']} Buku")
    elif pilihanHapus == "2":
        True

# Perulangan atau suatu kondisi dimana kita dapat memanggil fungsi sesuai input        
while True:
    menu_awal()
    pilihanMenuUtama = input('''
    Silahkan pilih menu di atas [1-5]: ''')
        
    if pilihanMenuUtama == "1":
        readData()
    elif pilihanMenuUtama == "2":
        createData()
    elif pilihanMenuUtama == "3":
        updateData()    
    elif pilihanMenuUtama == "4":
        hapusData()
    elif pilihanMenuUtama == "5":
        print("Terima kasih telah berkunjung ke Perpustakaan Tersyahdu!")
        break