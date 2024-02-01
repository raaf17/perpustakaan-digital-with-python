from . import Operasi

def delete_console():
  read_console()
  while(True):
    print("Silahkan pilih nomor buku yang ingin anda delete")
    no_buku = int(input("Nomor Buku : "))
    data_buku = Operasi.read(index=no_buku)
    
    if data_buku:
      data_break = data_buku.split(',')
      pk = data_break[0]
      data_add = data_break[1]
      penulis = data_break[2]
      judul = data_break[3]
      tahun = data_break[4][:-1]
      
      print("\n" + "=" * 100)
      print("Data yang ingin anda hapus")
      print(f"1. Judul\t : {judul:.40}")
      print(f"1. Penulis Buku\t : {penulis:.40}")
      print(f"1. Tahun Terbit\t : {tahun:4}")
        
      is_done = input("Yakin akan dihapus? (y/n)")
      if is_done == "y" or is_done == "Y":
        Operasi.delete(no_buku)
        break
    else:
      print("Nomor yang anda masukkan tidak valid")
      
  print("Data berhasil dihapus")

def update_console():
  read_console()
  while(True):
    print("Silahkan pilih nomor buku yang ingin anda update")
    no_buku = int(input("Nomor Buku : "))
    data_buku = Operasi.read(index=no_buku)
    data_break = data_buku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]
    
    if data_buku:
      break
    else:
      print("Nomor yang anda masukkan tidak valid")
      
  data_break = data_buku.split(',')
  pk = data_break[0]
  data_add = data_break[1]
  penulis = data_break[2]
  judul = data_break[3]
  tahun = data_break[4][:-1]
  
  while(True):
    # Data yang ingin diubah
    print("\n" + "=" * 100)
    print("Silahkan pilih data apa yang ingin anda ubah")
    print(f"1. Judul\t : {judul:.40}")
    print(f"1. Penulis Buku\t : {penulis:.40}")
    print(f"1. Tahun Terbit\t : {tahun:4}")
    
    # Memilih mode untuk ubah
    user_option = input("Pilih data [1,2,3] : ")
    print("\n" + "=" * 100)
    
    match user_option:
      case "1": judul = input("Judul\t : ")
      case "2": penulis = input("Penulis Buku\t : ")
      case "3": 
        while(True):
          try:
            tahun = int(input("Tahun Terbit\t : "))
            if len(str(tahun)) == 4:
              break
            else:
              print("Tahun yang anda masukkan maksimal harus 4 angka")
          except:
            print("Tahun yang anda masukkan harus angka (yyyy)")
      case _: print("Index tidak cocok")
      
    print("Data baru anda")
    print(f"1. Judul\t : {judul:.40}")
    print(f"1. Penulis Buku\t : {penulis:.40}")
    print(f"1. Tahun Terbit\t : {tahun:4}")
      
    is_done = input("Apakah sudah selesai update? (y/n)")
    if is_done == "y" or is_done == "Y":
      break
    
  Operasi.update(no_buku, pk, data_add, tahun, judul, penulis)

def create_console():
  print("\n\n" + "=" * 50)
  print("Silahkan tambah data buku\n")
  penulis = input("Penulis\t : ")
  judul = input("Judul Buku\t : ")
  while(True):
    try:
      tahun = int(input("Tahun Terbit\t : "))
      if len(str(tahun)) == 4:
        break
      else:
        print("Tahun yang anda masukkan maksimal harus 4 angka")
    except:
      print("Tahun yang anda masukkan harus angka (yyyy)")
      
  Operasi.create(tahun, judul, penulis)
  print("\nBerikut adalah data baru anda")
  read_console()

def read_console():
  # print("      Lihat Data Buku")
  data_file = Operasi.read()
  
  index = "No"
  judul = "Judul"
  penulis = "Penulis"
  tahun = "Tahun"
  
  # Header
  print("\n" + "=" * 100)
  print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
  print("-" * 100)
  
  # Data
  for index, data in enumerate(data_file):
    data_break = data.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4]
    print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:5}", end="")
  
  # Footer
  print("=" * 100 + "\n")