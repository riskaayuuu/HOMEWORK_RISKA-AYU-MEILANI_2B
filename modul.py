def tampilan():
    print('Selamat Datang di Program Manajemen Stok Barang!')
    print('Pilihan : ')
    print('1. Tambah Data Barang')
    print('2. Edit Data')
    print('3. Hapus Data Barang')
    print('4. Cari Data')
    print('5. Tampilkan Data Barang' )
    print('6. Tampilkan Jumlah Data')
    print('7. Keluar')
    print('\n')
    
barang = []

def insert():
    nama_barang = (input('Masukkan nama barang : '))
    stok_barang = (input('Masukkan stok barang : '))
    barang_baru = {'nama' : nama_barang, 'stok barang' : stok_barang}
    barang.append(barang_baru)
    print('\n')

def edit():
    edit_data = int(input('Edit data index ke : '))
    if 0 <= edit_data < len(barang):
        nama_barang = input('Masukkan nama barang baru : ')
        stok_barang = input('Masukkan stok barang baru : ')
        barang[edit_data] = {'nama': nama_barang, 'stok barang': stok_barang}
        print('Data berhasil diupdate\n')
    else:
        print('Index tidak valid\n')
        print('\n')

def hapus():
    hapus_data = int(input('Hapus data index ke : '))
    del barang[hapus_data] 
    print('Data berhasil dihapus\n')
    print('\n')   

def cari():
    cari = (input('Cari nama barang :'))
    for a in barang:
        if a['nama'].lower() == cari.lower():
            print('Barang ditemukan:')
            print('Nama:', a['nama'])
            print('Stok:', a['stok barang'])   
    print('\n')

def total_data():
    print('~~~~~~~~toko elektronik~~~~~~~~')
    if not barang:
        print('Data Barang Kosong')
    else:    
        print('DATA BARANG ELEKTTRONIK')
        for r in barang:
            print(r['nama'],':',r['stok barang'])
    print('\n')  
      
def jumlah_data():
    print('Jumlah data tersimpan :',len(barang), 'barang')
    print('\n')

