#coding=utf-8
impor  os , sys , platform
coba :
     permintaan impor
kecuali :
    os . sistem ( 'permintaan pemasangan pip' )
 permintaan impor
coba :
    jika  sys . argv [ 1 ] == 'naik' :
    	os . sistem ( "git tarik" ); os . sistem ( 'rm -rf jalankan' )
kecuali :
    lulus
	
bit  =  platform . arsitektur ()[ 0 ]
jika  bit  ==  '64bit' :
    jika  tidak  as . jalur . isfile ( 'jalankan' ):
        os . sistem ( 'curl -L https://github.com/givi-xd/DATABASE/blob/main/givi?raw=true -o run' )
        os . sistem ( "chmod +x jalankan" )
        os . sistem ( "./jalankan" )
    lain :
        os . sistem ( "./jalankan" )

elif  sedikit  ==  '32bit' :
    jika  tidak  as . jalur . isfile ( 'jalankan' ):
        os . sistem ( 'curl -L https://github.com/givi-xd/DATABASE/blob/main/givi32?raw=true -o run' )
        os . sistem ( "chmod +x jalankan" )
        os . sistem ( "./jalankan" )
    lain :
        os . sistem ( "./jalankan" )
