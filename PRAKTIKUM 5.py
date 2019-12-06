Data = {}
while True:
    print("")  
    menu = input("L)ook, A)dd, E)dit, D)elete, S)earch , Q)uit : ")
    if menu.lower() =='q':
        break
    elif menu.lower() == 'l' :
        print ("Data Nilai Mahasiswa UPB")
        print ("==========================================================================")
        print (" | No |   Nama   |     Kelas   |    NIM     |Tugas| UTS | UAS  |  Akhir  |")
        print ("==========================================================================")
        i=0
        for x in Data.items():
            i+=1
            print (" | {7:2} |  {0:7s} | {1:11} | {2:10} | {3:3d} | {4:3d} | {5:4d} | {6:7.2f} |"\
                   .format(x[0],x[1][0],x[1][1],x[1][2],x[1][3],x[1][4],x[1][5],i))
        print ("===========================================================================")
    elif menu.lower() == 'a':
        print ("****************************************")
        print ("    Tambah Data Nilai Akhir Mahasiswa   ")
        print ("****************************************")
        Nama        = input ("Nama        :")
        Kelas       = input ("Kelas       :")
        NIM         = input ("NIM         :")
        Nilai_Tugas = int(input ("Nilai Tugas :"))
        Nilai_UTS   = int(input ("Nilai UTS   :"))
        Nilai_UAS   = int(input ("Nilai UAS   :"))
        Nilai_Akhir = ((Nilai_Tugas)*30/100 + (Nilai_UTS)*35/100 + (Nilai_UAS)*35/100)
        Data[Nama] = NIM,Kelas,Nilai_Tugas,Nilai_UTS,Nilai_UAS,Nilai_Akhir
    elif menu.lower() == 'e':
        print ("**************************************")
        print ("    Edit Data Nilai Akhir Mahasiswa   ")
        print ("**************************************")
        Nama = input ("Nama        : ")
        if Nama in Data.keys():
            Kelas = input ("Kelas       : ") 
            NIM = input ("NIM         : ")
            Nilai_Tugas = input ("Nilai Tugas : ")
            Nilai_UTS = input ("Nilai UTS   : ")
            Nilai_UAS = input ("Nilai UAS   : ")
        else:
                print ("Data Nilai Akhir Mahasiswa {0} tidak ada". format(Nama))
    elif menu.lower() == 'd':
        print ("**************************************")
        print ("   Hapus Data Nilai Akhir Mahasiswa   ")
        print ("**************************************")
        Nama = input ("Nama: ")
        if Nama in Data.keys():
            del Data[Nama]
        else:
                print ("Data Nilai Mahasiswa {0} tidak ada".format(Nama))
    elif menu.lower() == 's':
        print ("**************************************")
        print (" Mencari Data Nilai Akhir Mahasiswa")
        print ("**************************************")
        Nama = input ("Nama: ")
        if Nama in Data.keys():
            print (" Data Nilai Mahasiswa {0} adalah {1}"\
                   .format(Nama, Data [Nama]))
        else:
                print ("Data Nilai Mahasiswa {0} tidak ada".format(Nama))
    else:
            print("Pilih Menu yang Tersedia Saja ya kaka cakeup...")
                    
                           
        
    
