import os

#main.py
#encoding: utf-8

__author__      = "Muhamad Zulfan Taqiyudin Baehaki", "Muhammad Rafif Fadlurahman"
__version__     = 0.1
__contact__     = {
                    "Rafif" :{
                        "Name"          :   "Muhammad Rafif Fadlurahman",
                        "Email"         :   "rafif.fadlurahman20@mhs.uinjkt.ac.id",
                        "University"    :   "UIN SYARIF HIDAYATULLAH JAKARTA"

                    },
                    "Zulfan":{
                        "Name"          :   "Muhamad Zulfan Taqiyudin Baehaki",
                        "Email"         :   "muhamad.zulfan20@mhs.uinjkt.ac.id",
                        "University"    :   "UIN SYARIF HIDAYATULLAH JAKARTA"
                    }    
} 


menu = {
    1:  "Pensil",
    2:  "Buku",
    3:  "Bebek"
}

harga = {
    1:  1_000,
    2:  3_500,
    3:  20_000
}

def menuKita():
    print("+----------------------+")
    print("|         menu         |")
    print("+----------------------+")
    for i  in range (1, len(menu)+1):
        print(f"{i}. {menu[i]} \t harga: {harga[i]}")
    print("0.total")

def payment():
    menuKita()
    total = 0
    buffer = 0
    x = 1
    while(x==1):
        quantity = 0
        inputMenu = int(input("Input:"))
        if (inputMenu == 0):
            print("Masuk")
            print("total harga:" + str(total))
            break
        elif (inputMenu > 0 or inputMenu <= 3):
            print(menu[inputMenu] + "\t harga: " + str(harga[inputMenu]))
            quantity= int(input("quantity: "))
            buffer = harga[inputMenu] * quantity
        else:
            print("wrong input code!")

        total += buffer
    
    print("test")

    return total

def bayar():
    total = payment()
    x = True
    while x is True:
        uangAnda = int(input("masukkan uang anda: "))
        if uangAnda >= total:
            x = False
        elif(uangAnda < total):
            print("Uang anda tidak cukup!")
    
    kembalian = total - uangAnda
    if(kembalian == 0 ):
        print("Uang anda pas!")
    elif(kembalian > 0 ):
        print(f"kembalian anda: {kembalian}")
    
    print("\n")

    print("ingin belanja lagi?(y/n)")
    ulangi = str(input("y untuk ya, dan n untuk tidak: "))
    if(ulangi == 'y'):
        bayar()
    elif(ulangi == 'n'):
        os.system("cls")
        run()





def run():
    print("====== WARUNG BAROKAH  =======")
    print("1. Payment")
    print("2. history")
    print("0. quit")
    pilih = str(input("input: "))

    if(pilih == "1"):
        bayar()
    elif(pilih == "2"):
        history()
    elif(pilih == "0"):
        quit()
    else:
        os.system('cls')
        run()
        
run()