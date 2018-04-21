import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.cluster import KMeans

#Membuat Array Untuk Data
test1   = [] 
test2   = []
labtest = []

train1   = []
train2   = []
labtrain = []

#Rumus Euclidean Distance (Mencari Jarak Nilai Dua titik)
def euclead ( a , b , c , d ): 
    return math.sqrt ( pow ( b - a , 2 ) + pow ( d - c , 2 ) )

#load Data Uji
file = open ( 'TestsetTugas2.txt' , 'r' ) 
for line in file:
    a = line.split()
    #Menambah Elemen Pada List
    test1.append   ( float ( a [ 0 ] ) ) 
    test2.append   ( float ( a [ 1 ] ) )
    labtest.append (  int  ( 0 ) )

#load Data Latih
file = open ( 'TrainsetTugas2.txt' , 'r' ) 
for line in file:
    a = line.split()
    #Menambah Elemen Pada List
    train1.append   ( float ( a [ 0 ] ) ) 
    train2.append   ( float ( a [ 1 ] ) )
    labtrain.append (  int  ( 0 ) )

#Mencari Nilai Tengah Setiap Kelas
Kelas1X = train1 [  82 ]
Kelas1Y = train2 [  82 ]
Kelas2X = train1 [  18 ]
Kelas2Y = train2 [  18 ]
Kelas3X = train1 [ 581 ]
Kelas3Y = train2 [ 581 ]
Kelas4X = train1 [ 245 ]
Kelas4Y = train2 [ 245 ]
Kelas5X = train1 [ 457 ]
Kelas5Y = train2 [ 457 ]
Kelas6X = train1 [ 357 ]
Kelas6Y = train2 [ 357 ]
Kelas7X = train1 [ 303 ]
Kelas7Y = train2 [ 303 ]

#Loop Untuk Menentukan Masuk Ke Dalam Kelas Mana
for i in range ( 0 , train1.__len__() ):
    Hasilkelas1 = euclead ( Kelas1X , train1 [ i ] , Kelas1Y     , train2 [ i ] )
    Hasilkelas2 = euclead ( Kelas2X , train1 [ i ] , Kelas2Y     , train2 [ i ] )
    Hasilkelas3 = euclead ( Kelas3X , train1 [ i ] , Kelas3Y     , train2 [ i ] )
    Hasilkelas4 = euclead ( Kelas4X , train1 [ i ] , Kelas4Y     , train2 [ i ] )
    Hasilkelas5 = euclead ( Kelas5X , train1 [ i ] , Kelas5Y     , train2 [ i ] ) 
    Hasilkelas6 = euclead ( Kelas6X , train1 [ i ] , Kelas6Y     , train2 [ i ] )
    Hasilkelas7 = euclead ( Kelas7X , train1 [ i ] , Kelas7Y     , train2 [ i ] )
    minimum     = min ( Hasilkelas1 , Hasilkelas2  , Hasilkelas3 , Hasilkelas4 , Hasilkelas5 , Hasilkelas6 , Hasilkelas7 )

    if ( minimum == Hasilkelas1 ):
        Kelas1X        = 0.5 * Kelas1X + 0.5 * train1 [ i ]
        Kelas1Y        = 0.5 * Kelas1Y + 0.5 * train2 [ i ]
        labtrain [ i ] = 1
    elif ( minimum == Hasilkelas2 ):
        Kelas2X        = 0.5 * Kelas2X + 0.5 * train1 [ i ]
        Kelas2Y        = 0.5 * Kelas2Y + 0.5 * train2 [ i ]
        labtrain [ i ] = 2
    elif ( minimum == Hasilkelas3 ):
        Kelas3X        = 0.5 * Kelas3X + 0.5 * train1 [ i ]
        Kelas3Y        = 0.5 * Kelas3Y + 0.5 * train2 [ i ]
        labtrain [ i ] = 3
    elif ( minimum == Hasilkelas4 ):
        Kelas4X        = 0.5 * Kelas4X + 0.5 * train1 [ i ]
        Kelas4Y        = 0.5 * Kelas4Y + 0.5 * train2 [ i ]
        labtrain [ i ] = 4
    elif ( minimum == Hasilkelas5 ):
        Kelas5X        = 0.5 * Kelas5X + 0.5 * train1 [ i ]
        Kelas5Y        = 0.5 * Kelas5Y + 0.5 * train2 [ i ]
        labtrain [ i ] = 5
    elif ( minimum == Hasilkelas6 ):
        Kelas6X        = 0.5 * Kelas6X + 0.5 * train1 [ i ]
        Kelas6Y        = 0.5 * Kelas6Y + 0.5 * train2 [ i ]
        labtrain [ i ] = 6
    elif ( minimum == Hasilkelas7 ):
        Kelas7X        = 0.5 * Kelas7X + 0.5 * train1 [ i ]  
        Kelas7Y        = 0.5 * Kelas7Y + 0.5 * train2 [ i ]
        labtrain [ i ] = 7

#Perulangan Untuk Menentukan Data Test Masuk Ke Kelas Mana
for i in range(0, test1.__len__()):
    Hasilkelas1 = euclead ( Kelas1X , test1 [ i ] , Kelas1Y , test2 [ i ] )
    Hasilkelas2 = euclead ( Kelas2X , test1 [ i ] , Kelas2Y , test2 [ i ] )
    Hasilkelas3 = euclead ( Kelas3X , test1 [ i ] , Kelas3Y , test2 [ i ] )
    Hasilkelas4 = euclead ( Kelas4X , test1 [ i ] , Kelas4Y , test2 [ i ] )
    Hasilkelas5 = euclead ( Kelas5X , test1 [ i ] , Kelas5Y , test2 [ i ] )
    Hasilkelas6 = euclead ( Kelas6X , test1 [ i ] , Kelas6Y , test2 [ i ] )
    Hasilkelas7 = euclead ( Kelas7X , test1 [ i ] , Kelas7Y , test2 [ i ] )
    minimum     = min ( Hasilkelas1 , Hasilkelas2 , Hasilkelas3 , Hasilkelas4 , Hasilkelas5 , Hasilkelas6 , Hasilkelas7 )

    if ( minimum == Hasilkelas1 ):
        Kelas1X       =  0.5 * Kelas1X + 0.5 * test1 [ i ]
        Kelas1Y       =  0.5 * Kelas1Y + 0.5 * test2 [ i ]
        labtest [ i ] =  1
    elif ( minimum == Hasilkelas2 ):
        Kelas2X       = 0.5 * Kelas2X + 0.5 * test1 [ i ]
        Kelas2Y       = 0.5 * Kelas2Y + 0.5 * test2 [ i ]
        labtest [ i ] = 2
    elif ( minimum == Hasilkelas3 ):
        Kelas3X       = 0.5 * Kelas3X + 0.5 * test1 [ i ]
        Kelas3Y       = 0.5 * Kelas3Y + 0.5 * test2 [ i ]
        labtest [ i ] = 3
    elif ( minimum == Hasilkelas4 ):
        Kelas4X       = 0.5 * Kelas4X + 0.5 * test1 [ i ]
        Kelas4Y       = 0.5 * Kelas4Y + 0.5 * test2 [ i ]
        labtest [ i ] = 4
    elif ( minimum == Hasilkelas5 ):
        Kelas5X       = 0.5 * Kelas5X + 0.5 * test1 [ i ]
        Kelas5Y       = 0.5 * Kelas5Y + 0.5 * test2 [ i ]
        labtest [ i ] = 5
    elif ( minimum == Hasilkelas6 ):
        Kelas6X       = 0.5 * Kelas6X + 0.5 * test1 [ i ]
        Kelas6Y       = 0.5 * Kelas6Y + 0.5 * test2 [ i ]
        labtest [ i ] = 6
    elif ( minimum == Hasilkelas7 ):
        Kelas7X       = 0.5 * Kelas7X + 0.5 * test1 [ i ]
        Kelas7Y       = 0.5 * Kelas7Y + 0.5 * test2 [ i ]
        labtest [ i ] = 7

for i in range ( 0 , train1.__len__() ):
    print ( labtrain [ i ] )
for i in range ( 0, test1.__len__() ):
    print ( labtest [ i ] )

plt.style.use ( 'seaborn-whitegrid' )

#Pewarnaan Untuk Masing-Masing Cluster Untuk Membedakannya
x = np.array ( list ( zip ( train1 , train2 ) ) ).reshape ( len ( train1 ) , 2 )
#Menentukan Warna
colors = ( 'b' , 'y' , 'r' , 'brown' , 'b' , 'y' , 'r' )
#Menentukan Bentuk  
markers = ( 'v' , 'v' , 'o' , 'o' , 's' , 's' , 's' ) 

#Menggunakan K = 7
K = 7 
Model = KMeans ( n_clusters = K ).fit(x)
plt.plot()
for i, l in enumerate(Model.labels_):
    plt.plot ( train1 [ i ] , train2 [ i ] , color = colors [ l ] , marker = markers [ l ] , ls = 'None' )
    plt.xlim ( [ 0 , 35 ] )
    plt.ylim ( [ 0 , 35 ] )
plt.show()

x = np.array(list(zip(test1,test2))).reshape(len(test1),2)
colors  = ( 'r' , 'g' , 'b' , 'cyan' , 'r' , 'g' , 'b' )
markers = ( 'v' , 'v' , 'o' ,  'o'   , 's' , 's' , 's' )

K = 7
Model = KMeans(n_clusters=K).fit(x)
plt.plot()

#Membuat Folder txt Untuk Menampung Hasil Akurasi
thefile = open ( 'Akurasi.txt' , 'w' )
for item in labtest:
    thefile.write ( "%s\n" % item )

for i, l in enumerate(Model.labels_):
    plt.plot ( test1 [ i ] , test2 [ i ] , color = colors [ l ] , marker = markers [ l ] , ls = 'None' )
    plt.xlim ( [ 0 , 35 ] )
    plt.ylim ( [ 0 , 35 ] )
plt.show()
