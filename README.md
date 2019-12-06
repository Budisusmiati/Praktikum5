#Praktikum5
Penjelasan Program Praktikum5 :
1.Pertama buatlah Data dictionary kosong (Data = {}).
2.Gunakan perulangan while. Masukkan inputan menu ( Quit, Look, Add, Edit, Delete, Search).
3.Gunakan kondisi if, elif, dan else untuk mengeksekusi perintah.
4.Untuk menu yang pertama adalah perintah Quit (keluar).  Gunakan kondisi if untuk mengeksekusi perintah, jika hasilnya True maka program akan berhenti, tetapi jika hasilnya False / selain yang ada di menu , maka Anda akan diminta memasukkan inputan menu lagi ( yang ada pada menu).
5.Menu selanjutnya adalah perintah Look. Gunakan looping for ( for x in Data.items() ), lalu masukkan perintah print data dictionary.
6.Untuk perintah Add (menambahkan), inputkan data yang ingin Anda masukkan, seperti: Nama, Kelas, NIM, Nilai Tugas, Nilai UTS, Nilai UAS. Nilai Akhir dihitung dengan menggunakan rumus (Nilai Tugas * 30%) + (Nilai UTS * 35%) + (Nilai UAS * 35%).
7.Lalu menu untuk perintah Edit (mengubah). Inputkan Data[Nama] yang akan diedit. Gunakan kondisi if lagi ( if Nama in Data.keys() ), jika hasil adalah True maka Anda akan disuruh menginputkan data perubahannya. Tetapi jika hasilnya False, maka akan tercetak “Data ... tidak ada” dan  muncul perintah untuk memasukkan inputan menu lagi.
8.Menu dengan perintah Delete (menghapus). Inputkan Data[Nama] yang akan di hapus,dengan menggunakan kondisi if, jika hasil True maka data akan terhapus dengan menggunakan perintah del Data[Nama], dan jika hasilnya False maka akan tercetak “Data ... tidak ada” dan  muncul perintah untuk memasukkan inputan menu lagi.
9.Yang terakhir adalah menu dengan perintah search (mencari). Inputkan Data[Nama] yang akan dicari. Gunakan kondisi if , jika hasilnya True maka akan tercetak data yang dicari dengan menggunakan perintah print Data (Nama, Data[Nama]). Dan jika hasilnya False maka akan tercetak “Data ... tidak ada” dan  muncul perintah untuk memasukkan inputan menu lagi.
10.Kondisi yang terakhir menggunakan else, jika menu yang Anda inputkan tidak ada pada menu maka Anda akan disuruh untuk menginputkan menu pilihan yang ada saja pada Data.
11.Berikut Hasil program ketika di Run:

Gambar (1):
=====================================================================================================================
![Screenshot (108)](https://user-images.githubusercontent.com/57002773/70346352-bb014000-1890-11ea-8855-4d624d24bf6d.png)
=====================================================================================================================
Gambar (2):
=====================================================================================================================
![Screenshot (109)](https://user-images.githubusercontent.com/57002773/70346369-c6546b80-1890-11ea-8add-4f47db3ddf3d.png)
=====================================================================================================================
Gambar (3):
=====================================================================================================================
![Screenshot (112)](https://user-images.githubusercontent.com/57002773/70345837-8345c880-188f-11ea-8316-28f47dc1869f.png)
=====================================================================================================================
*********************************************** SEMOGA BERMANFAAT ***************************************************
