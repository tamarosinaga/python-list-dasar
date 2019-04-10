def Gaji():
    from texttable import Texttable
    table = Texttable ()

    print ("\n\tPROGRAM PENGGAJIAN\n")
    print ("DAFTAR GAJI :\n")
    print ("1. programmer = 3000.000")
    print ("2. leader     = 3500.000")
    print ("3. operator   = 2000.000")
    print ("\n jika jabatan tidak ada, tidak ditemukan....\n")
    jawab = "y"
    no = 0
    nama = []
    jabatan = []
    gaji = []

    while (jawab == 'y'):
        nama.append(input("masukan nama: "))
        jab = input ("jabatan: ")
        jabatan.append(jab)
        if (jab == 'programmer' ):
            gaji.append(3000000)
            jawab = input("\n ada lagi? (y/t)")
        elif  (jab == 'leader' ):
            gaji.append(3500000)
            jawab = input("\n ada lagi? (y/t)")
        elif (jab == 'operator' ):
            gaji.append(2000000)
            jawab = input("\n ada lagi? (y/t)")
        else:
            print("jabatan yang ditulis tidak ditemukan")
            jawab = input("\n ada lagi? (y/t)")
            no += 1
    
    for i in range (no) :
        table.add_rows([['No','Nama','Jabatan','gaji'],[i+1,nama[i],jabatan[i],gaji[i]]])

    print (table.draw())

