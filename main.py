import modul as md
while True:
    md.tampilan()
    pilihan = int(input('Masukkan pilihan : '))

    if pilihan == 1:
        md.insert()

    elif pilihan == 2:
        md.edit()

    elif pilihan == 3:
        md.hapus()

    elif pilihan == 4:
        md.cari()

    elif pilihan == 5:
        md.total_data()

    elif pilihan == 6:
        md.jumlah_data()

    elif pilihan == 7:
        print('~'*30)
        print('   Terimakasih telah mencoba   ')    
        print('~'*30)
        exit()

    else:
        print('~'*30)
        print('   Pilihan tidak tersedia, silahkan pilih antara angka 1 sampai 7   ')    
        print('~'*30)
    
        


