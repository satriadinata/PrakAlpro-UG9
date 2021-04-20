# perpustakaan menyimpan data dalam sebuah list yang
# di generate dari sebuah database seperti berikut
data=[['Mtk','Suryanto','2017'],['IPA','Ade','2015']]
print("Menu :\n1. Tambah data\n2. Lihat data\n3. Exit")
menu=True
while True:
    pilihan=input('Masukkan pilihan menu: ')
    if pilihan=='1':
        judul=input('Masukkan Judul: ')
        penulis=input('Nama Penulis: ')
        tahun=input('Masukkan Tahun: ')
        store=[judul,penulis,tahun]
        data.append(store)
        print(data)
    elif pilihan=='2':
        print('Judul\t\tpenulis\t\ttahun')
        for i in data:
            # for j in range(len(i)):
            print(i[0],end='\t\t')
            print(i[1],end='\t\t')
            print(i[2])
    elif pilihan=='3':
        break