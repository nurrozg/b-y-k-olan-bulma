#Girilen 3 sayıyı büyüklük olarak karşılaştıran python uygulamasını yapınız.
sayi1 =int(input('1. sayı : '))
sayi2 = int(input('2. sayı: '))
sayi3 = int(input('3. sayı: '))
if ( sayi1 > sayi2 ) and (sayi1 > sayi3):
    print(f'sayi1 en büyük sayıdır')
elif (sayi2 > sayi1) and (sayi2 > sayi3):
    print(f'sayi2 en büyük sayıdır')
elif(sayi3 > sayi1) and (sayi3 > sayi1):
    print(f' sayi3 en büyüktür')