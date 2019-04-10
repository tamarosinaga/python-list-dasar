def kalkulator():
        no=0
        jawab='y'
        while (jawab=='y'):
                print ('')
                print ('WELCOME TO MY PROJECT BROTHER')
                print ('======KALKULATOR======')
                print (' 1. Penjumlahan')
                print (' 2. pengurangan')
                print (' 3. Perkalian')
                print (' 4. pembagian')
                print (' 5. Exit')
                pil=int(input('>> Masukkan pilihan :'))
                a= input("Masukan bilangan pertama = ")
                b= input("Masukan bilangan kedua = ")
                if pil==1:
                        print ('')
                        print ("hasil penjumlahannya=",)
                        print (int(a)+int(b))
                        
                elif pil==2:
                        print ('')
                        print ("hasil pengurangannya=",)
                        print (int(a)-int(b))
                        
                elif pil==3:
                        print ('')
                        print ("hasil perkaliannya=",)
                        print (int(a)*int(b))
                        
                elif pil==4:
                        print ('')
                        print ("hasil pembagiannya=",)
                        print (int(a)/int(b))
                elif pil==5:
                        exit()

                else:
                        print("input yang anda masukan salah !")
                jawab=input("Tambah Data (y/t) ?")
                        
        no+=1

        
        print ('')
        print ('TERIMA KASIH KAWAN')

                
                        
                
                        
                       
                
        
