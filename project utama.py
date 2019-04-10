from perhitungan.penggajian import Gaji
from perhitungan.nilai import nilai
from perhitungan.Kalkulator import kalkulator
from perhitungan.pembayaran_uas import pembayaran_UAS
from perhitungan.pembayaran_uts import pembayaran_UTS

import getpass
def Login():
        print("\nlogin in system") ; user = input("username :") ;password = getpass.getpass("password :")
        if user == "tamaro" and password == "sinaga1998":
           pilih()
        else :            
            print (("\n         !!! WARNING !!!             "),
                   ("\n!!! username atau password yang anda masukkan salah !!!"))
            login ()

def pilih():
    print ("SELAMAT DATANG DI PROJECT SAYA TAMARO SINAGA")
    print ("program yang tersedia : ")
    print ("1. nilai ")
    print ("2. Gaji ")
    print ("3. kalkulator")
    print ("4. pembayaran_UAS")
    print ("5. pembayaran_UTS")
    print ("6. exit ")

    pilih = int(input("\nmasukan pilihan anda : "))
    
    if pilih == 1:
        nilai ()
        lagi ()
        
    elif pilih == 2:
        Gaji ()
        lagi ()

    elif pilih == 3:
        kalkulator ()
        lagi()

    elif pilih == 4:
        pembayaran_UAS ()
        lagi()

    elif pilih == 5:
        pembayaran_UTS ()
        lagi()
   

    elif pilih== 6:
        exit
        print("\n\t---------terima kasih---------")

    else:
        print("\n\t---------terima kasih---------")

def lagi ():
    tanya = input("\nkembali ke menu utama(y/t)?")
    if tanya == "y":
        pilih()

    elif tanya == "t":
        print ("\n\t----------terima kasih--------")
        exit

    else:
        print("\n\tsalah input........!")
        lagi()

Login()
