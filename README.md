### Wireless DOS with Scapy

Kablosuz ağlara DOS saldırı gerçekleştirmek amacı ile Scapy ile gerliştirilmiş bir araçtır.

<a href="#" rel="some text">![scapydos](https://github.com/besimaltnok/wifiDOS/blob/master/wifidos.png)</a>

##### Kullanılabilir Parametreler 

* -m Mode   : Saldırı modunu tanımlamak için kullanılmalıdır. (b: Tüm istemcilere saldırı - c : Sadece bir istemciye yönelik)
* -c Client : Saldırı düzenlenecek istemcinin mac adres bilgisi
* -i iface  : Saldırıda kullanılacak ve monitor mod durumunda olacak ağ kartı
* -a AP_mac : Saldırı düzenlenecek erişim noktasının mac adres bilgisi
* --help    : Yardım görüntülemek amacı ile kullanılabilir.


##### Örnek Kullanım

* python wifiDOS.py -m b -a AP_mac -i wlan0
* python wifiDOs.py -m c -a AP_mac -c Client_mac -i wlan0


NOT : Erişim noktası ile saldırıyı düzenlemek amacı ile kullandığımız ağ kartı aynı kanalda olmalıdır.
Bunun için : 
- iwconfig wlan0 channel kanal_numarası konutu kullanabiliriz.
