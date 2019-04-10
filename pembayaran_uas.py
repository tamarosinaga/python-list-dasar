from texttable import Texttable

def pembayaran_UAS():
    jawab ="y"
    no=0
    nama=[]
    kelas=[]
    nim=[]
    uang_UAS=[]
    total_bulanan=[]
    uang_seminar=[]
    uang_kas=[]
    uang_admin=[]
    table = Texttable ()
    while(jawab =="y"):
        print ("\n\tprogram Pembayaran mahasiswa\n")
        nama.append(input("\nMasukkan Nama :"))
        nim.append(input("\nMasukkan Nim :"))
        kelas.append(input("\nMasukkan Kelas :"))

#----------------------------------------------------------------------#

        pilih_UAS = (input("\nbayaran UAS (y/t)?"))
        if  pilih_UAS=='y':
            uang_UAS.append(2500000)
        else:
            uang_UAS.append(0)

#----------------------------------------------------------------------#
        pilih_bulanan= (input("\nbayaran bulanan (y/t)?"))
        if pilih_bulanan== 'y':
            total_bulanan.append(500000)
        else:
            total_bulanan.append(0)

#-----------------------------------------------------------------------#
        pilih_seminar = (input("\nbayar Seminar (y/t)?"))
        if  pilih_seminar=='y':
            uang_seminar.append(100000)

        else:
            uang_seminar.append(0)

#---------------------------------------------------------------------------#
        pilih_kas= (input("\nbayar kas (y/t)?"))
        if pilih_kas=='y':
           uang_kas.append(20000)

        else:
            uang_kas.append(0)

        print("\n\nbiaya admin 5000")
        uang_admin.append(5000)

#-----------------------------------------------------------------------------------#
        jawab=input("Tambah data (y/t) ?")
        no+=1
    for i in range(no):
        UAS=int(uang_UAS[i])    
        SPP=int(total_bulanan[i])
        seminar=int(uang_seminar[i])
        kas=int(uang_kas[i])
        admin=int(uang_admin[i])
        grand_total =UAS+SPP+seminar+kas+admin
        table.set_cols_dtype(['a','i','i','i','i','i','i','i','i','i'])
        table.add_rows([['NO','NAMA','NIM','KELAS','UAS','BULANAN','SEMINAR','KAS','ADMIN','TOTAL'],
                    [i+1,nama[i],nim[i],kelas[i],uang_UAS[i],total_bulanan[i],uang_seminar[i],uang_kas[i],uang_admin[i],grand_total]])
    print (table.draw())


                
    
