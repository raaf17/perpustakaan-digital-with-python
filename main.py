import os
import CRUD as CRUD

if __name__=='__main__':
  sistem_operasi = os.name
  
  match sistem_operasi:
      case "posix": os.system("clear")
      case "nt": os.system("cls")
      
  print("Selamat Datang di Program Python")
  print("     Perpustakaan Digital")
  print("================================")
  
  # Check database ada atau tidak
  CRUD.init_console()
  
  while(True):
    match sistem_operasi:
      case "posix": os.system("clear")
      case "nt": os.system("cls")
    
    print("Selamat Datang di Program Python")
    print("     Perpustakaan Digital")
    print("================================")
  
    print(f"1. Lihat Data Buku")
    print(f"2. Tambah Data Buku")
    print(f"3. Update Data Buku")
    print(f"4. Hapus Data Buku\n")
    
    user_option = input("Masukkan pilihan anda : ")
    
    match user_option:
      case "1": CRUD.read_console()
      case "2": CRUD.create_console()
      case "3": CRUD.update_console()
      case "4": CRUD.delete_console()
      
    is_done = input("Apakah sudah selesai? (y/n)")
    if is_done == "y" or is_done == "Y":
      break
    
  print("Program berakhir, terima kasih sudah berkunjung")