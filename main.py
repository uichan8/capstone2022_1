#object class
from LightUtil.Ceilling import Ceilling
from LightUtil.Sign import Sign
#database class

def main():
    a = Ceilling([18],[23],[24])
    a.on_mode()
    
    b = Sign([16],[20])
    b.on_mode()
    #b.eco_mode()

if __name__ == "__main__":
    main()

