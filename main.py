#main.py
#encoding: utf-8

__author__      = "Muhamad Zulfan Taqiyudin Baehaki", "Muhammad Rafif Fadlurahman"
__version__     = 0.1
__contact__     = {
                    "Rafif" :{
                        "Name"          :   "Muhammad Rafif Fadlurahman",
                        "Email"         :   "rafif.fadlurahman20@mhs.uinjkt.ac.id",
                        "University"    :   "UIN SYARI FHIDAYATULLAH JAKARTA"

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
    print("======== menu ========")

    for i  in range (1, len(menu)+1):
        print(menu[i] + "\t" + str(harga[i]) )

menuKita()