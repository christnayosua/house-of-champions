## Tugas Individu 2
 ***by Christna Yosua Rotinsulu - 2406495691***

**URL Deployment PWS :** 
https://christna-yosua-houseofchampions.pbp.cs.ui.ac.id/

## **Implementasi Pengembangan Aplikasi Web Menggunakan Django** 💻[1][2]

**Membuat Direktori dan Mengaktifkan *Virtual Environment*** 
 1. Tentu langkah pertama yang saya lakukan adalah membuat sebuah direktori baru bernama house-of-champions (*tema yang saya pilih*) dan masuk ke dalam folder tersebut.
 2. Setelah itu, saya membuka terminal di vs code untuk membuat ***virtual environment*** di dalam direktori proyek yang saya buat dengan perintah `python -m venv env` yang nantinya akan membuat folder baru, yaitu env, yang berfungsi untuk mengisolasi *package* serta *dependencies* dari aplikasi yang saya buat agar tidak bertabrakan dengan versi lain di *device* yang saya gunakan. Setelah itu, *virtual environment* tersebut saya aktifkan dengan perintah `env\Scripts\activate`.

**Menyiapkan *Dependencies* dan Membuat Proyek Django**

 3. Lalu, saya mulai menyiapkan ***Dependencies*** yang menjadi komponen atau modul yang diperlukan oleh sebuah *software* untuk berfungsi, termasuk *library*, *framework*, atau *package* yang dibutuhkan. Dengan *Dependencies*, saya dapat melakukan proses pengembangan menjadi lebih efisien dan cepat, walaupun saya juga perlu berhati-hati untuk memastikan kompabilitas versi yang tepat. *virtual environment* yang telah saya buat dan aktifkan tadi berguna untuk mengisolasi *dependencies* antara proyek-proyek yang berbeda. Untuk menambahkan beberapa *dependencies* yang saya perlukan, saya membuat sebuah file khusus, yaitu `requirements.txt` yang berisi beberapa *dependencies*, yaitu `django, gunicorn, whitenoise, psycopg2-binary, requests, urllib3, dan python-dotenv`. Setelah itu, saya melakukan instalasi *dependecies* tersebut melalui perintah `pip install -r requirements.txt`. 
 4. Setelah mempersiapkan *dependencies* yang saya perlukan untuk proses pengembangan selanjutnya, saya mulai menyiapkan dan membuat proyek Django bernama *champions-store* melalui perintah `django-admin startproject champions_store .`
 
 **Konfigurasi Environment Variables dan Proyek**
 
 5. Selanjutnya, saya mulai melakukan **konfigurasi environment variables dan proyek**. Pertama, saya mulai membuat file `.env` untuk development lokal dan menambahkan konfigurasi `PRODUCTION=False` sehingga aplikasi web nanti akan menggunakan database SQLite yang lebih simple untuk melakukan testing dan development. Di sisi lain, saya juga membuat file `.env.prod` untuk production deployment dengan konfigurasi production sesuai dengan panduan, mulai dari `DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, SCHEMA, dan PRODUCTION` di mana `SCHEMA` yang digunakan adalah `tugas_individu`. Sebab `PRODUCTION=True`, aplikasi akan menggunakan PostgreSQL dengan kredensial yang akan disediakan oleh ITF Fasilkom UI.
 6. Lalu, saya mulai melakukan modifikasi file `settings.py` untuk menggunakan environment variables yang telah saya konfigurasi melalui fungsi `load_dotenv()` yang diimpor dari `dotenv`
 7. Untuk keperluan deployment, saya menambahkan dua string, yaitu `"loaclhost, "127.0.0.1"` pada `ALLOWEB_HOSTS` di `settings.py` agar *host* tersebut diizinkan untuk mengakses aplikasi web, tetapi hanya bisa diakses dari jaringan saya saat ini saja (*host* lokal).
 8. Setelah itu, saya menambahkan konfigurasi `PRODUCTION` di `settings.py` untuk mendapatkan konfigurasi `PRODUCTION` yang telah saya lakukan. Setelah itu, di file yang sama, saya menggunakan konfigurasi `DATABASES` sesuai dengan konfigurasi `PRODUCTION` di file `.env` dan `.env.prod`

**Menjalankan Server**
 
 9. Untuk menjalankan server, saya perlu untuk melakukan migrasi database terlebih dahulu dengan perintah `python manage.py migrate`. Setelah berhasil melakukan migrasi, saya mulai menjalan server Django dengan perintah: `python manage.py runserver`. Untuk mengecek apakah proyek Django berhasil dibuat, saya dapat membuka http://localhost:8000 di peramban web untuk mengetahui hal tersebut.

**Menghentikan Server dan Menonaktifkan Virtual Environment serta Unggah Proyek ke Repositori GitHub** 

 11. Setelah proyek Django saya berhasil dibuat, saya menghentikan server dan menonaktifkan *virtual environment* untuk melakukan pengunggahan ke GitHub. Proyek Django yang saya buat, saya simpan di repositori GitHub bernama house-of-champions. Selain itu, saya menambahkan file `.gitignore` yang berisi konfigurasi untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git sehingga ketika saya melakukan *push*, file yang tercantum di file `.gitignore` tidak ikut ter-*push*. Berkas-berkas yang akan diabaikan dan tidak perlu dilacak oleh Git adalah berkas-berkas yang dihasilkan oleh proses kompilasi, berkas sementara, atau berkas konfigurasi pribadi. Dalam hal tersebut, file yang tidak akan ter-*push* ke GitHub, yaitu file `.env`, `.env.prod`, `db.sqlite3`, dan sebagainya, sebab mengandung konfigurasi pribadi dan proses kompilasi. 

**Pembuatan Akun dan Deployment melalui PWS (Pacil *Web Service*)**

 12. Pacil Web Service adalah salah satu bentuk layanan **PaaS**, yaitu Platform as a Service, yang disediakan untuk membantu mahasiswa, termasuk saya, dalam melakukan pengembangan, pengelolaan, dan peluncuran aplikasi tanpa perlu mengkhawatirkan infrastruktur dasarnya. Untuk membuat project tersebut, saya perlu membuat akun sesuai dengan *SSO UI* milik saya. Lalu, saya membuat project baru bernama *houseofchampions* sesuai dengan tema aplikasi yang saya pilih. Setelah itu, saya perlu menyimpan kredensial yang diberikan sebelum menjalankan instruksi ***Project Command***.  Setelah menyimpan kredensial tersebut, saya pergi ke tab Environs untuk mengonfigurasi *environment variables* yang telah saya konfigurasi di file `.env.prod`. Lalu, saya kembali ke proyek Django saya untuk menambahkan URL *deployment* pada `ALLOWED_HOSTS` sehingga proyek saya dapat diakses melalui URL *deployment* PWS tersebut dan dapat dilihat oleh user lain. 
 13. Setelah menambahkan *URL deployment*, saya melakukan *push* ke repositori GitHub saya dan mulai menjalankan perintah yang terdapat di *Project Command* pada halaman PWS. Lalu, akan muncul *pop-up* baru untuk memasukkan kredensial yang telah saya simpan tadi dan perlu menunggu beberapa detik hingga status deployment *Running*.

**Membuat Aplikasi Django beserta Konfigurasi Model**

14. Untuk mengonfigurasi model, saya perlu mengaktifkan kembali *virtual environment*. Setelah itu, saya membuat aplikasi baru bernama `main` dalam proyek *house-of-champions* melalui perintah `python manage.py startapp main` yang nantinya akan membuat folder baru bernama `main`. Lalu, saya menambahkan `'main'` ke dalam daftar aplikasi pada `INSTALLED_APPS` di `settings.py`.

**Implementasi Template Dasar**

15. Untuk memberikan tampilan teks, gambar, dan bahan lainnya secara visual maupun suara kepada user lain, saya perlu membuat file HTML yang akan menampilkan semua hal tersebut sesuai kebutuhan. Lalu, saya akan membuat direktori `templates` pada direktori `main`. Pada direktori tersebut, saya membuat berkas baru bernama `main.html` sesuai dengan data yang ingin saya tampilkan di aplikasi web. 

**Implementasi Model Dasar**

16. Setelah itu, saya mengonfigurasi `models.py` pada direktori `main` untuk mendefinisikan model baru sesuai kebutuhan saya. Attribute-attribute yang saya gunakan untuk proyek saya di antaranya, `id`, `name`, `price`, `description`, `thumbnail`, `category`, `is_featured`, `stock`, `rating`, `brand`, dan `created_at`.

**Migrasi Model**

17. Agar Django dapat melacak perubahan pada model basis data saya, saya perlu melakukan migrasi agar struktur tabel basis data saya sesuai dengan perubahan yang telah saya definisikan sebelumnya melalui perintah `python manage.py makemigrations`. Perintah tersebut akan membuat berkas yang berisi perubahan model yang **belum** diaplikasikan ke dalam basis data. Untuk mengaplikasikan hal tersebut, saya menjalankan perintah `python manage.py migrate`.

**Menghubungkan *View* dengan *Template*** 

18. Untuk menghubungkan komponen *view* dengan komponen *template*, saya perlu mengonfigurasi file `views.py` dengan mengimpor `render` dari modul `django.shortcuts`. Di dalam file ini juga, saya membuat fungsi `show_main` yang menerima parameter `request` untuk mengatur permintaan HTTP dari user dan mengembalikan tampilan yang sesuai. Oleh karena itu, `render` diperlukan agar dapat `render` tampilan HTML dengan menggunakan data yang saya berikan.
19. Setelah itu, saya dapat memodifikasi berkas `main.html` agar dapat menampilkan data yang telah diambil dari *model* dengan mengubahnya menjadi struktur kode Django yang sesuai untuk menampilkan data dengan format {{ data }}

**Mengonfigurasi *Routing* URL**

20. Routing URL perlu dilakukan agar Django dapat mengetahui view dan argumen apa yang perlu dijalankan atau diteruskan ketika user membuka URL tertentu. Untuk melakukan hal tersebut, saya perlu mengonfigurasi berkas `urls.py` yang ada di direktori `champions-store` dengan mengimpor fungsi `include` dan menambahkan rute URL yang akan mengarah ke tampilan `main` di dalam list `urlpatterns`.
21. Untuk mengecek apakah routing berhasil, saya perlu menjalankan server terlebih dahulu dengan perintah `python manage.py runserver`, lalu, membuka [http://localhost:8000/ di peramban web saya. 

**Django Unit Testing**

22. Untuk mengetahui apakah kode yang telah saya buat bekerja sesuai dengan yang saya inginkan, saya perlu melakukan testing agar saya dapat mengecek apakah perubahan yang dilakukan dapat menimbulkan perilaku di luar keinginan saya. Dalam melakukan unit testing, saya perlu mengonfigurasi file `tests.py` pada direktori `main` dengan konfigurasi mengikuti panduan. 
23. Setelah itu, saya perlu menjalankan testing dengan perintah `python manage.py test` dan melihat output yang dihasilkan untuk mengetahui apakah aplikasi web yang telah saya buat berjalan sesuai keinginan. 
24. Setelah melakukan testing, saya *push* kembali ke repository GitHub saya beserta PWS agar perubahan yang saya lakukan dapat dilihat di URL *deployment* saya oleh user lain beserta kode programnya.

## Django Request Client 👤 [3]
![Bagan Client Request](https://www.canva.com/design/DAGyiKER53U/Uamgjs_Id0nyOQUwImMSJA/view?utm_content=DAGyiKER53U&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h07a9e4acb9)
[Bagan Request Client Alternative](https://www.canva.com/design/DAGyiKER53U/Uamgjs_Id0nyOQUwImMSJA/view?utm_content=DAGyiKER53U&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h07a9e4acb9)
hubungan antara `urls.py`, `views.py`, `models.py`, dan berkas `main.html` adalah sebagai berikut. `urls.py` berperan sebagai router yang memetakan URL ke function view yang sesuai dengan *request client*. Di sisi lain, `views.py` berperan untuk menerjemahkan dan mengelola *request client* lalu akan berinteraksi dengan `models.py` apabila diperlukan untuk mengakses database. `models.py` berperan untuk melakukan operasi database dan mendefinisikan struktur data tertentu di mana merepresentasikan tabel di database. Lalu, `main.html` berperan untuk menampilkan data yang telah diproses dalam format yang *user-friendly*. 

Secara lebih ringkas, `urls.py` akan memilih `views.py` dan `models.py` (*apabila diperlukan*),  lalu `models.py` akan memproses database yang ada sesuai kebutuhan dan *request client*, sedangkan `views.py` akan melakukan *render* ke `main.html`. Lalu, `main.html` akan dikirim sebagai `HTTP response`. 

## Peran setting.py Dalam Django 🎮
Berkas settings.py berperan sebagai berkas utama untuk mengontrol berbagai aspek proyek Django. Melalui file ini, saya dapat melakukan berbagai konfigurasi, mulai dari aplikasi, database, *middleware*, template, *Internationalization*, security, dan *authentication*, walaupun saat ini hanya beberapa konfigurasi yang baru diimplementasikan sepenuhnya dalam proyek saya. Sebagai contoh, ketika saya ingin melakukan deployment di Pacil Web Service, saya mendaftarkan URL *deployment* tersebut pada `ALLOWED_HOST` sehingga proyek Django saya dapat diakses melalui URL tersebut dan dapat dilihat oleh user lain.

## Migrasi Database di Django 📚[4] 
Agar Django dapat melacak perubahan pada model basis data yang dilakukan, hal yang perlu dilakukan adalah melakukan migrasi database tersebut. Jadi, migrasi adalah instruksi untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kode terbaru. Untuk melakukan migrasi, saya perlu menjalankan perintah `python manage.py makemigrations`. Apa yang akan dilakukan perintah tersebut? Django awalnya akan membandingkan model versi sekarang dengan versi sebelumnya. Lalu, Django akan membuat file migrasi khusus untuk menjalankan operasi database yang diperlukan dan nanti akan disimpan di berkas `migrations`. Setelah membuat migrasi, saya perlu menerapkan migrasi tersebut melalui perintah `python manage.py migrate` yang nantinya akan meminta Django untuk menjalankan operasi database yang tercantum di file migrasi yang tadi telah dibuat. Lalu riwayat migration tadi akan disimpan di tabel `django_migrations`. Django pun dapat melacak migrasi yang telah dilakukan sehingga mungkin dapat *rollback* ke versi sebelumnya. Selain itu, Django dapat menangani *dependencies* antara migrasi dan aplikasi yang berbeda.

## Alasan Django Dijadikan Permulaan Pembelajaran 😁 [5] 
1. ***Ridiculously fast.***
Django membantu *developer* dalam mengembangkan aplikasi dari konsep hingga siap untuk didistrbusikan secepat mungkin sehingga sangat ramah untuk pengguna yang baru belajar Django. 

2. ***Fully Loaded***
Django menyediakan banyak fitur tambahan yang dapat dimanfaatkan oleh *developer* sehingga mempermudah pengembangan aplikasi web, terutama dalam menyelesaikan tugas-tugas web umum. Django menangani user authentication, content administration, site maps, RSS feeds, dan sebagainya. 

3. **Reassuringly secure**
Django menganggap serius keamanan dan membantu pengembang menghindari berbagai kesalahan keamanan umum, seperti injeksi SQL, skrip lintas situs, pemalsuan permintaan lintas situs, dan *clickjacking*. Sistem autentikasi yang telah disediakan untuk membantu pengguna mengelola akun dan kata sandi pengguna dengan aman.

4. **Exceedingly scalable**
Beberapa situs tersibuk saat ini sebagian besar menggunakan kemampuan Django untuk menyesuaikan skala secara cepat dan fleksibel untuk memenuhi permintaan *traffic* terberat sebab semakin banyak *user* maka sumber daya di web tersebut yang ada semakin terkuras.

5. **Incredibly versatile**
Perusahaan, organisasi, dan pemerintahan telah menggunakan Django untuk membangun segala macam hal — mulai dari sistem manajemen konten hingga jejaring sosial hingga platform komputasi ilmiah.

## Feedback 👍
Saya sangat menghargai dan mengapresiasi bagaimana asisten dosen membantu saya selama pengerjaan lab dan tugas individu. Selain itu, panduan yang diberikan sangat lengkap, sistematis, dan mudah dipahami sehingga membantu saya dalam memahami materi serta menyelesaikan tugas lab dan individu, terlebih saya baru menggunakan Django untuk pertama kali. 👍

## Referensi 🔗
[1] Tim Dosen dan Asisten Dosen PBP 2025 dan 2024. (21 Agustus 2025). *Tutorial 1: Pengenalan Aplikasi Django dan  _Model-View-Template_  (MVT) pada Django*. Retrieved from https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-1

[2] Tim Dosen dan Asisten Dosen PBP 2025 dan 2024. (27 Agustus 2025). *Tutorial 0: Konfigurasi dan Instalasi Git dan Djang*. Retrieved from https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-0

[3] Django. (n.d.). *Request and response objects*. Retrieved from https://docs.djangoproject.com/en/5.2/ref/request-response/

[4] Django. (n.d.). *Migrations*. Retrieved from https://docs.djangoproject.com/en/5.2/topics/migrations/

[5] Django. (n.d.). *Why Django?*. Retrieved from https://www.djangoproject.com/start/overview/

## Tugas Individu 3
***by Christna Yosua Rotinsulu - 2406495691***

## Peran Krusial Data Delivery 🚚[1]
 *data delivery* sangat diperlukan sebab platform saat ini umumnya menggunakan arsitektur yang terdistribusi (misal, **client-server**). Oleh sebab itu, pertukaran data antara bagian forntend dan backend harus dilakukan secara sistematis sehingga memastikan ketepatan informasi. Dilansir dari fanruan, berikut adalah alasan kenapa *data delivery* itu penting, yaitu sebagai berikut:
 
 1. **Memastikan Akurasi Data**
Data yang akurat akan menjadi tulang punggung setiap proses pengambilan keputusan yang berhasil, terlebih hal ini sangat diperlukan ketika sedang memulai bisnis atau bekerja di sebuah perusahaan. Dari hal tersebut, kita harus memercayai informasi yang akan digunakan. 
2. **Deteksi Kesalahan**
Kesalahan dalam data dapat terjadi di tahap mana pun sehingga mendeteksi kesalahan sejak dini akan membantu mencegah kesalahan dalam mengambil keputusan. Misal, ketika hasil penjualan item di House Of Champions terdapat kesalahan dalam pendataan, maka kesimpulan hasil penjualan bisa saja sangat meleset, yang harusnya untung menjadi rugi, atau sebaliknya. 
3. **Validasi Data**
Memastikan data akurat dan valid akan membantu dalam proyek dan keputusan untuk ke depannya. Langkah ini dapat membantu untuk memeriksa kualitas informasi dari sebuah platform sehingga data yang digunakan menjadi lebih andal dan siap untuk dianalisis lebih jauh.
4. **Meningkatkan Pengambilan Keputusan**
Penyampaian data tidak hanya terbatas pada keakuratan data yang didapatkan, tetapi juga bagaimana *impact* yang diberikan data tersebut mampu membuat keputusan yang lebih baik. 
5. **Akses Data Tepat Waktu**
Memiliki akses ke data kapan pun yang kita butuhkan sangatlah penting sehingga dapat menyesuaikan permintaan atau *feedback* dari *user* atau *client*. Hal tersebut memampukan kita, sebagai *developer* untuk merespons lebih cepat terhadap perubahan sehingga dapat unggul dibandingkan pesaing. 
6. **Wawasan Berbasis Data**
Wawasan dalam berbasis data akan memampukan *developer* untuk menyimpan data dengan cara yang lebih efektif dan efisien. Hal ini akan mengoptimalkan strategi untuk ke depannya dan mencapai hasil yang lebih baik. 

Berdasarkan hal tersebut, *data delivery* berperan sebagai mekanisme yang memastikan pertukaran informasi antara berbagai komponen sistem berjalan lebih efektif. *Centralized* data platform tersebut memungkinkan penyimpanan, pengelolaan, dan pengiriman data dalam volume besar, baik terstruktur maupun tidak terstruktur. Platform seperti inilah yang akan memberikan infrastruktur untuk menyimpan dan memproses data dari berbagai sumber secara *seamless* yang sangat krusial dalam lingkungan bisnis modern di mana data menjadi aset strategis yang tak ternilai pada saat ini.

## Kenapa JSON Lebih Unggul? 🔝[2]
JSON adalah turunan dari JavaScript yang digunakan sebagai alat untuk transfer dan penyimpanan data. Saat ini, bahasa JSON sering digunakan dalam pembuatan aplikasi website. Di sisi lain, XML adalah *markup language* yang sering digunakan untuk membuat suatu format informasi umum dan nantinya akan digunakan sebagai sarana membagikan format dan data pada halaman www. Lalu, kenapa JSON lebih unggul dan menjadi pilihan *developer* untuk menyimpan dan transfer data? 

JSON memiliki kecepatan *parsing* yang lebih cepat dibandingkan XML. *Parsing* sendiri adalah pengenalan bagian terkecil dari sebuah dokumen JSON atau XML. Selain itu, JSON hemat resource dibandingkan XML dalam menyimpan data. Sebab JSON adalah turunan dari JavaScript, struktur data native JavaScript yang disediakan membantu dalam melakukan integrasi. Selain itu, JSON menampilkan data dalam format yang lebih ringkas dan mudah dibaca oleh manusia awam serta mendukung data types secara langsung, seperti *number*, *string*, dan *boolean*, sehingga *programmer* tingkat mana pun dapat lebih mudah untuk memahami data yang tersimpan dan akan ditransfer.  

## is_valid() pada Form Django ✅[3]
Method `is_valid()` yang saya gunakan dalam aplikasi web saya mempunyai peran untuk melakukan validasi input terhadap *contstraints* yang telah didefinisikan sebelumnya (format, required field, dll). Ketika method ini mengembalikan nilai `True`, maka objek yang akan dibuat dengan data formulir dapat dilakukan dan disimpan setelahnya. Di sisi lain, apabila output yang dikeluarkan adalah`False`, maka akan memberikan informasi error messages sehingga *developer* dapat mengetahui *field input* yang tidak sesuai dengan kriteria. `is_valid()` tidak hanya berperan sebagai validators saja, tetapi juga sebagai *cleaners*. Peran tersebut membantu *developer* untuk mencegah data yang tidak sesuai masuk ke dalam database sehingga melindungi sistem dari potensi *security vulnerabilities*. 

## Kebutuhan csrf_token dalam Form Django🥷🧑‍💻[4]
CSRF atau *Cross-Site Request Forgery* adalah sebuah token yang diperlukan untuk mencegah serangan CSRF di mana penyerang akan memanipulasi *suspect* untuk menjalankan aksi yang tidak diinginkan sehingga token unik perlud= dibuat untuk setiap *session user* yang nantinya akan divalidasi oleh server. 

Lalu, apa bahayanya apabila tidak menggunakan CSRF token?  Seperti yang sudah dijelaskan, CSRF berperan untuk mencegah serangan CSRF sehingga apabila tidak menggunakan CSRF token, penyerang dapat membuat *request* palsu untuk menggunakan identitas korban, memanipulasi data tanpa persetujuan *user*, atau mengeksploitasi aksi privileged, seperti transfer dana (misal, top-up game) atau ubah password. 

Bagaimana penyerang melakukan serangan CSRF? Penyerang umumnya akan membuat link/form jahat dan mengelabui korban untuk mengkliknya ketika korban melakukan login ke aplikasi target sehingga biasanya penyerang akan membuat konten menarik yang dapat mengundang korban untuk masuk ke perangkapnya. Lalu, ketika korban mengklik link/form tersebut, sebuah *request* baru akan dikirim ke pihak server dengan kredensial korban yang aktif dan tentu server berkemungkinan akan memvalidasi serta menjalankan *request *tersebut. Setelah pihak server menyetujui dan memproses *request* tersebut, maka di saat itulah penyerang akan melakukan operasi pencurian identitas atau hal lainnya sebab server tidak dapat membedakan *request* tersebut apakah *legitimate* atau *malicious*.

## Checklist Step-By-Step 🎯 [5]
Berikut adalah checklist yang saya lakukan dalam melakukan dan menyelesaikan tugas individu 3 : 

<h3> Implementasi Skeleton Sebagai Kerangka Views</h3> <hr>

1. **Membuat base.html**
Pada *root folder*, saya membuat sebuah direktori baru bernama `templates` yang berisi file `base.html` yang akan menjadi *template* dasar yang digunakan sebagai kerangka umum untuk halaman lainnya di dalam proyek saya. Dalam *template* ini terdapat block `{% block %}` untuk mendefinisikan area dalam template yang dapat diganti oleh template turunannya. Template turunan tersebut akan me-*extend* template dasar dan mengganti konten di dalam block ini sesuai dengan kebutuhan saya. 
2. Setelah membuat kerangka umum tersebut, saya perlu mengonfigurasi `settings.py` agar `base.html` yang telah dibuat dapat terdeteksi sebagai berkas template. Lalu, pada subdirektori `templates`, saya melakukan modifikasi untuk menampilkan attribute yang telah saya definisikan pada berkas `views.py`. 

<h3> Form Input Data dan Menampilkan Data pada HTML </h3><hr>

3. Setelah membuat kerangka umum dan berbagai konfigurasi yang dilakukan, saya melanjutkan tahap saya berikutnya, yaitu membuat sebuah *form* yang menjadi *field input* data pada *House-Of-Champions* pada aplikasi web saya sehingga nantinya saya dapat menambahkan data baru untuk ditampilkan di halaman utama web. Saya perlu membuat berkas baru, yaitu `forms.py` untuk membuat struktur *form* yang dapat menerima data *Items* baru. *Fields input* yang saya gunakan untuk penambahan data, antara lain *name, description, category, thumbnail, is_feautured, price, stock, rating, dan brand* sesuai dengan *attribute* yang telah saya definisikan di berkas `models.py`. 
4. Lalu, saya melakukan konfigurasi pada berkas `views.py` untuk mengimpor modul-modul yang diperlukan dan membuat *functions* yang akan membuat dan menampilkan item yang akan dibuat oleh *user*. `create_items` bertujuan untuk membuat item yang akan ditambahkan dan disimpan dalam database di mana *function* ini akan mendeteksi apakah form yang diajukan valid dan *request* yang dikirimkan adalah `"POST"`. Apabila kedua kriteria tersebut terpenuhi, maka objek `item` baru akan dibuat dan disimpan. Di sisi lain, `show_items` berperan untuk menampilkan objek `item` yang telah dibuat sebelumnya dan menaikkan jumlah *visitors* setiap kali *user* mengunjungi item yang terdaftar. 
5. Setelah membuat konfigurasi tersebut, saya perlu menambahkan *path* URL ke variable `urlpatterns` di berkas `urls.py` agar dapat menuju ke tampilan halaman yang sesuai. 
6. Pada berkas `main.html`, saya membuat tambahan tampilan untuk menampilkan list yang berisi objek `item` yang telah dibuat dan disimpan. Informasi yang ditampilkan akan membantu mengundang perhatian *calon pembeli* serta memberikan rekomendasi *item* sesuai dengan rating dan jumlah pembeli item tersebut (belum ditambahkan). 
7. Selain berkas `main.html`, saya membuat dua berkas baru pada direktori yang sama untuk halaman form input dan detail item yang dijual, yaitu `create_items.html` dan `items_detail.html`. Pada berkas `create_items.html`, saya menambahkan block `{% csrf_token %}` yang bertindak sebagai *security* agar *user* tidak terserang serangan CSRF. Di sisi lain, terdapat block `{{% form.as_table %}}` yang menjadi *template tag* untuk menampilkan *fields* form yang sudah dibuat pada berkas `forms.py` sebagai `table`.
8. Setelah itu, saya melakukan konfigurasi pada berkas `settings.py` untuk menambahkan URL *deployment* aplikasi web saya pada *attribute* `CSRF_TRUSTED_ORIGINS` agar hanya melalui token tersebut, data dan *request* yang dikirimkan diterima oleh aplikasi web. 

<h3>Mengembalikan Data dalam Bentuk XML dan JSON</h3><hr>

9. Setelah membuat form input data dan menampilkannya, saya akan mengembalikan data yang tersimpan dalam bentuk XML dan JSON untuk kebutuhan analisis ke depannya. Pada file `views.py`,  saya mengimpor modul `HttpResponse` dan `Serializer` untuk menyusun respon yang ingin dikembalikan oleh *server* kepada *user*. 
10. Lalu, saya membuat *function* baru untuk menerima parameter *request* dengan nama `show_xml` dan `show_json` dan membuat variabel `items_list` yang menyimpan hasil *query* dari seluruh data pada `Items`.  Setelah itu, *function* tersebut akan me-*return* HTTPResponse dengan parameter hasil *query* yang sudah diserialisasi dalam bentuk XML atau JSON dan parameter `content_type="application/xml"`. Setelah itu, saya menambahkan *path url* ke dalam `urlpatterns` untuk mengakses *function* yang sudah diimpor tadi. 

<h3>Mengembalikan Data Berdasarkan ID dalam bentuk XML dan JSON</h3><hr>

11. Setelah selesai dapat mengembalikan data dalam bentuk XML dan JSON, saya membuat *function* baru untuk mengembalikan data yang tersimpan dalam *query* berdasarkan ID. Pertama, saya membuat dua *function* baru yang menerima parameter `request` dan `items_id`, yaitu `show_xml_by_id` dan `show_json_by_id` di mana di dalam kedua *function* tersebut terdapat variabel `items_list` yang menyimpan hasil *query* dari data dengan id tertentu.
12. Lalu, saya menambahkan *return function* berupa `HttpResponse` yang menerima parameter data hasil *query* yang sudah diserialisasi menjadi JSON atau XML dan parameter `content_type` dengan *value* `"application/xml"` atau `"application/json"`. Pada *function* tersebut, saya juga menambahkan block `try except` untuk mengantisipasi kondisi ketika data dengan `items_id` tertentu ternyata tidak ditemukan dalam basis data di mana akan mengembalikan `HttpResponse` dengan status 404 sebagai tanda bahwa data tersebut tidak ada. 
13. Setelah itu, saya menambahkan *path url* pada berkas `urls.py` untuk mengimpor fungsi yang sudah ada dan menambahkan akses fungsi yang sudah dibuat tadi. 

<h3>Push ke PWS dan GitHub</h3><hr>

14. Setelah selesai untuk mengembalikan data dalam bentuk XML dan JSON, saya melakukan push ke GitHub dan PWS agar perubahan yang saya lakukan dapat tersimpan dan terlihat di URL *deployment* saya. 

## Feedback untuk Tutorial 2 👍
Asdos sangat membantu saya untuk memahami dan mengerjakan tutorial 2 kemarin melalui panduan dan komunikasi melalui *Discord*. Selain itu, penjelasan-penjelasan bagian yang harus dikonfigurasi dan ditambahkan turut disertai penjelasan sehingga saya tidak hanya mengimplementasikan saja, tetapi juga memahami maksud dari hal tersebut. Dari hal tersebutlah, saya dapat mengerjakan tugas individu 3 dengan lebih mudah terutama jawaban-jawabannya sudah disediakan pada panduan tutorial 2 kemarin. Saya berharap agar hal ini terus konsisten terjadi untuk ke depannya. Great Job, kakak Asdos 💓!

## Screenshot Hasil Akses URL pada Postman 🔗
<h3>XML</h3>

![XML](https://drive.google.com/file/d/1AK5E92Usf5qrHREjBmvNRYrhTAz65c07/view?usp=sharing)
[Link Alternatif - XML](https://drive.google.com/file/d/1AK5E92Usf5qrHREjBmvNRYrhTAz65c07/view?usp=sharing)

<h3>JSON</h3>

![JSON](https://drive.google.com/file/d/1J1xealYy1xaZobEFIv8eHIesyhQN2Sl-/view?usp=sharing)
[Link Alternatif - JSON](https://drive.google.com/file/d/1J1xealYy1xaZobEFIv8eHIesyhQN2Sl-/view?usp=sharing)

<h3>XML by ID</h3>

![XML by ID](https://drive.google.com/file/d/1lchB-xxdxK1Ez-ygXanylS6KiuGI2mik/view?usp=sharing)
[Link Alternatif - XML by ID](https://drive.google.com/file/d/1lchB-xxdxK1Ez-ygXanylS6KiuGI2mik/view?usp=sharing)

<h3>JSON by ID</h3>

![JSON by ID](https://drive.google.com/file/d/1NmxHzjtEGwWF7LDSee7fse21lJOtEnd-/view?usp=sharing)
[Link Alternatif - JSON by ID](https://drive.google.com/file/d/1NmxHzjtEGwWF7LDSee7fse21lJOtEnd-/view?usp=sharing)

## Referensi 🔎
[1] Sean. (2024, 23 October). *Data Delivery*. Retrieved from https://www.fanruan.com/en/glossary/big-data/data-delivery
[2] Binar. (n.d.). *JSON: Pengertian, Fungsi, Jenis-Jenis, Kelebihan dan Kekurangannya*. Retrieved from https://www.binar.co.id/blog/json-adalah
[3] Ansel, J. (2022, Juny 1). *Working with Django Model Forms*. Retrieved from https://medium.com/@jansel358/working-with-django-model-forms-77afe017e2cc
[4] Django Documentation. (n.d.). *How to Use Django's CSRF Protection*. Retrieved from https://docs.djangoproject.com/id/5.2/howto/csrf/
[5] Tim Dosen dan Asisten Dosen PBP 2024-2025. (2025, August 27). *Tutorial 2 : Form dan Data Delivery*. Retrieved from  https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-2#tutorial-implementasi-skeleton-sebagai-kerangka-views

## Tugas Individu 4
***by Christna Yosua Rotinsulu-2406495691***

<h3>👤 Django's AuthenticationForm [1]</h3> 
<hr>

`AuthenticationForm` adalah form bawaan dari Django yang disediakan untuk mengautentikasi *user*. `AuthenticationForm` dapat diimport dari library `django.contrib.auth.forms`. Form ini nantinya akan memvalidasi username dan password yang dimasukkan pada halaman login terhadap database pengguna. Apabila ditemukan kecocokan/validasi sukses, maka Django akan mengembalikan objek `User` yang sesuai melalui method `get_user()`.

Lalu, apa kelebihan dan kekurangan dari `AuthenticationForm` pada Django? Berikut adalah kelebihan dan kekurangan dari form tersebut:

**Kelebihan**

1. Sudah terintegrasi dengan sistem autentikasi Django (backends, `login()/logout()`)
2. Dapat melakukan validasi secara otomatis, tanpa perlu didefinisikan oleh *developer* (*Ready-to-use)*
3. Mudah untuk dikustomisasi sesuai kebutuhan (*subclass atau override fields/label*)
4. Mendukung *error handling* bawaan (ex. kredensial tidak valid)
5. Terintegrasi dengan sistem *permissions* Django

**Kekurangan**

1. Masih terbatas pada autentikasi username/password standar sehingga perlu kustomisasi apabila ingin login via email (protokol keamanan lebih ketat)
2. Perlu penyesuaian lebih lanjut untuk kebutuhan kustom yang lebih kompleks, seperti membuat custom backend atau form apabila ada kebutuhan logic autentikasi khusus, seperti SSO. 
3. Tampilan default perlu disesuaikan dengan desain aplikasi sehingga perlu styling dan i18n
4. Tidak otomatis menangani fitur lanjutan (2FA, *rate-limiting*, *captcha*, dan *account lockout*)

<h3>🪪 Autentikasi vs Otorisasi: Butuh Keduanya atau Salah Satu? [2]</h3>
<hr>

**Autentikasi** atau *authentication* adalah proses memverifikasi identitas, seperti *username, password, token, 2FA, dsb*. **Autentikasi** sama halnya dengan pertanyaan *siapa kamu?* Melalui *authentication*, *server-side* mengetahui *user* mana yang sedang berinteraksi atau dia seorang anonim. 

Di sisi lain, **otorisasi** atau *authorization* adalah proses memeriksa hak akses/izin, seperti *permissions*, *roles*, atau *groups*. **Otorisasi** sama halnya dengan pertanyaan *apa yang boleh kamu lakukan?* **Otorisasi** dilakukan setelah **autentikasi** sehingga setelah mengetahui *siapa dia*, *server-side* dapat mengetahui hak akses yang dimiliki *user* tersebut, seperti membaca/mengubah/menjalankan aksi tertentu.

Lalu, bagaimana cara Django mengimplementasikan kedua hal tersebut? 

- **Autentikasi**
1. Django, menyediakan model `User` yang dapat diimport dari `django.contrib.auth.models.User` yang berfungsi untuk menyimpan identitas *user* dalam sebuah model/objek. Selain itu, data *user* juga dapat disimpan melalui custom user via `AUTH_USER_MODEL`. 
2. Django juga menyediakan function `authenticate()` untuk memeriksa kredensial milik *user* melalui *authentication backends* (`AUTHENTICATION_BACKENDS)` untuk bisa menambahkan backend custom, seperti login via email, LDAP, OAuth, SSO, dsb. Apabila ditemukan kecocokan/tervalidasi, maka Django akan mengembalikan objek `User` tersebut.
3. Django sendiri saat ini sudah menyediakan sistem password hashing secara otomatis sehingga protokol keamanannya menjadi lebih ketat dan sulit diserang *attacker*. 
4. Untuk menyimpan *session* ID *user* ke cookie dan menandai bahwa user terautentikasi, Django menyediakan function `login(request, user)`. Hal ini akan membantu *user* agar state selama sesi interaksi dengan aplikasi web dapat terjaga sehingga tidak perlu melakukan prosedur login kembali, walaupun cukup beresiko jika tidak dilindungi. 
5. Django juga menyediakan beberapa tools bawaan juga, seperti `AuthenticationForm`, `LoginView`, `LogoutView`, password hashing yang tadi sudah dijelaskan, dan password reset flows. 

- **Otorisasi**
Django, dalam hal otorisasi, menawarkan beberapa lapisan kontrol akses berupa dekorator, seperti `@login_required` (*yang digunakan dalam tutorial*) yang akan membatasi akses berdasarkan status login, `@permission_required` untuk izin akses yang lebih spesifik, dan pengecekan langsung di kode melalui `user.has_perm()`. Sistem otorisasi ini turut diperkuat dengan pembagian peran yang terstruktur dan hierarkis yang terdiri dari *superuser*, *staff*, dan *regular user* dan manajemen *group permission* di mana semua proses akan dilakukan setelah identitas *user* terautentikasi yang akan menciptakan alur keamanan yang berlapis dan sistematis.

<h3>🍪 Session vs Cookies: Penyimpan Jejak di Aplikasi Web [3]</h3>

**Session** atau *Penyimpanan Server-Side* adalah mekanisme untuk menyimpan data setiap *user* di antara *request* HTTP yang bersifat *stateless* sehingga *client* hanya menerima sessionid saja. Di sisi lain, **cookie** adalah penyimpanan *client-side* dalam bentuk file kecil berupa data yang disimpan di browser *user* atas permintaan website. 

Lalu, apa kelebihan dan kekurangan dari `session` dan `cookies`?

- ✅**Kelebihan Cookies**
1. **Ringan untuk Server**: cookies tidak butuh storage di sisi server sebab semua data disimpan di browser *user*. Hal tersebut menyebabkan server tetap *stateless* sehingga lebih mudah diskalakan, terutama pada arsitektur *microservices* yang mengutamakan kemandirian antar layanan. 
2. **Performa Tinggi**: server tidak perlu melakukan *lookup* ke database atau chace untuk mencari data *user* sebab sudah tersedia langsung di setiap *request* yang dilakukan. Hal ini tentu akan mengurangi latensi dan meningkatkan performa aplikasi, terutama untuk data kecil yang sering diakses. 
3. **Persistensi Data**: cookies dapat memiliki waktu kadaluwarsa yang panjang sehingga data tetap dapat tersimpan meskipun browser ditutup oleh *user*. Hal ini akan memungkinkan pengguna untuk kembali ke state atau preferensi sebelumnya tanpa perlu mengatur ulang, seperti login. 
4. **Simplicity**: cookies sangat mudah diimplementasikan karena sudah didukung secara *built-in* oleh semua browser sehingga *developer* tidak perlu mengonfigurasi atau setup tambahan yang kompleks untuk dimanfaatkan. 
5. **Client Independence**: setiap client tentu dapat menyimpan state-nya masing-masing di browser sehingga tidak ada penggunaan *resource* secara bersamaan di server. Hal ini akan mengurangi risiko *bottleneck* pada penyimpanan di sisi server. 

<hr>

- 👎**Kekurangan Cookies**
1.  **Keamanan Rendah**: cookies memungkinkan *user* untuk memanipulasi data sebab berada di sisi browser. Selain itu, cookies sangat rentan terhadap serangan, seperti XSS (*Cross-Site Scripting*) dan CSRF (*Cross-Site Request Forgery*) jika tidak dikonfigurasi dengan benar oleh *developer*. 
2. **Ukuran Terbatas**: cookies umumnya hanya mampu menyimpan sekitar 4KB per cookie dan biasanya hanya 20 cookie per domain yang didukung (tergantung browser). Hal tersebut tentu tidak cocok digunakan jika digunakan untuk menyimpan data yang lebih besar dan kompleks. 
3.  **Privacy Concerns**: cookies umumnya sering digunakan untuk melacak perilaku pengguna, misalnya oleh iklan atau layanan pihak ketiga. Dari hal tersebut, regulasi seperti GDPR mewajibkan adanya persetujuan pengguna sebelum menyimpan cookies (biasanya akan muncul pop-up). Akan tetapi, sebagian pengguna, termasuk saya, sering memilih untuk memblokir cookies karena alasan privasi.
4. **Data Exposure**: isi dari cookies dapat dilihat dengan mudah melalui *developer* tools yang ada di browser sehingga sangat beresiko apabila menyimpan data sensitif. Berdasarkan hal tersebut, cookies tidak menjadi pilihan utama untuk menyimpan informasi penting, seperti password atau data-data finansial.
5. **Dependency on Client**: cookies sangat bergantung pada browser client, tetapi *user* bisa saja menonaktifkan cookies, dan perilaku cookies di setiap browser maupun perangkat mobile pun bisa berbeda-beda. Hal ini akan menimbulkan keterbatasan dan inkonsistensi dalam pengalaman pengguna untuk ke depannya. 

<hr>

- ✅**Kelebihan Session**

1. **Keamanan Tinggi**: berbeda dengan cookies, session menyimpan data di server sehingga *client* tidak dapat langsung memanipulasinya sebab hanya *session ID* yang dikirimkan ke browser. Hal tersebut akan mengurangi resiko manipulasi dan eksposur data secara langsung. 
2. **Kapasitas Besar dan Tidak Terbatas**: seesion dapat menampung objek yang lebih kompleks, seperti array, atau data yang relatif besar dan kompleks tanpa batasan ukuran ketat seperti cookie yang umumnya hanya bisa menampung sekitar 4KB untuk setiap cookie. Hal ini memungkinkan untuk menyimpan profil pengguna, preferensi, isi keranjang belanja, atau struktur data yang lebih kompleks. 
3. **Kontrol Penuh oleh Server**: session hanya bisa dikelola di sisi server sehingga administrator atau aplikasi mempunyai hak akses tinggi, seperti mengahapus/invalidasi sesi kapan saja, mengatur timeout, dan menerapkan kebijakan pengelola sesi yang lebih terpadu. Hal ini akan memudahkan protokol keamanan dan manajemen *lifecycle* sesi untuk semua klien.
4. **Privacy Better**: data pengguna yang disimpan di sisi server membantu mengurangi eksposur pada perangkat pengguna dan memudahkan kepatuhan terhadap regulasi privasi, seperti GDPR/CCPA. Hal ini akan mengurangi potensi kebocoran data melalui perangkat klien. 
5. **Reliability**: session tidak bergantung pada pengaturan browser milik klien sehingga *user* tidak bisa menonaktifkan session seperti cookie. Hal ini tentu akan meingkatkan reliabilitas mekanisme state karena server tetap mampu mempertahankan state meski ada variasi perilaku browser.

<hr> 

- **👎Kekurangan Session**
1. **Beban Server**: session memerlukan ruang penyimpanan dan sumber daya lebih pada server terlebih sistem dengan banyak pengguna simultan, storgae dan I/O akan mempengaruhi performa aplikasi. Hal ini tentu memerlukan mekanisme *cleanup* untuk sesi-sesi yang sudah kedaluwarsa agar tidak menumpuk di server. 
2. **Scalability Issues**: berbeda dengan cookie, session yang tersimpan di lokal suatu server akan menyebabkan inkonsistensi jika *request* yang di-post diarahkan ke server lain pada *environment* yang menggunakan *load balancer* dan banyak *instance* aplikasi. Hal tersebut membutuhkan *shared storage* atau *distributed chace* sehingga menambah kompleksitas infrastruktur. 
3. **Complexity**: konfigurasi session biasanya lebih kompleks dibandingkan cookies sehingga membutuhkan pengaturan backend, seperti database atau chace, strategi eviction, backup/replikasi, dan kadang pengaturan keamanan tambahan. Hal ini akan menambah beban pengembangan dan operasional dibanding solusi *client-only*.
4. **Statefulness**: session membuat server menjadi stateful yang bertentangan dengan prinsip *RESTful* yang mengutamakan *statelessness*. Hal ini akan membuat layanan yang sepenuhnya *stateless* atau *microservice* yang mudah diskalakan menjadi lebih menantang tanpa arsitektur tambahan.

<h3>👮 Data Aman, Hati Tenang: Strategi Django dalam Mengendalikan Cookies [4]</h3> 

<hr>

Penggunaan cookies, secara *default*, tidak aman digunakan dalam pengembangan aplikasi web. Hal ini disebabkan oleh risiko keamanan yang dapat ditimbulkan dari penggunaan cookies tanpa konfigurasi keamanan lebih lanjut. Berikut adalah beberapa serangan yang berpontesi terjadi pada penggunaan cookies:

1. **Cross-Site Scripting (XSS)**: *attacker* akan mencuri cookies melalui kode JavaScript "jahat". Hal ini memungkinkan *attacker* untuk mencuri data-data sensitif yang tersimpan di browser, seperti session ID, melalui manipulasi DOM atau akses langsung ke document.cookie. 
2. **Cross-Site Request Forgery (CSRF)**: *attacker* akan melakukan manipulasi cookies untuk melakukan aksi yang tidak sah atas nama *user* di mana korban akan membujuk pengguna yang sudah login untuk mengunjungi situs-situs "perangkap" yang mengirim *request* tertenu ke aplikasi web target. Dari hal tersebut, perubahan data dapat terjadi tanpa sepengetahuan *user*. 
3. **Session Hijacking**: *attacker* akan mencuri session ID *user* untuk menyamar sebagai pengguna yang sah. Hal ini tentu akan mengakibatkan akses tidak sah ke akun pengguna.
4. **Data Tempering**: cookies yang disimpan di client-side dan dapat dimodifikasi melalui browser developer tools, terlebih data yang tidak divalidasi dengan baik di sisi server, seperti ID pengguna, dapat dimanipulasi oleh *attacker* untuk mendapatkan keuntungan secara ilegal atau akses yang tidak terotorisasi. 

Lalu, bagaimana peran Django dalam menghadapi hal tersebut?

**Django** secara proaktif akan menangani risiko keamanan cookies tersebut melalui berbagai mekanisme *built-in* yang dilakukan secara *layered*, dimulai dengan proteksi CSRF yang otomatis disertakan token unik pada setiap form untuk mencegah serangan CSRF, pengaturan secure flags pada cookies (*HttpOnly, Secure, and SameSite*) yang akan membatasi akses JavaScript dan memastikan transmisi data hanya dapat dilakukan melalui HTTPS, serta sistem session management yang akan membantu penyimpanan data-data yang sensitif di *server-side* dan *user* diberikan *session ID* yang sudah terenkripsi, dan fitur signed cookies untuk menyimpan data yang harus disimpan di *client side*. Melalui prosedur tersebut, aplikasi web yang dibangun dapat terlindungi oleh *multilayered defense system* yang efektif untuk mengurangi kerentanan tradisional pada cookies web. 

<h3>🎯 Checklist Step-by-Step</h3>
<hr>

<h3>Function dan Form Registrasi 📄<h3>
<hr>

1. Saya mengimport `UserCreationForm` dan `messages` pada `views.py` untuk mengimplementasikan fungsi dan form registrasi akun. `UserCreationForm` adalah form bawaan dari Django untuk prosedur registrasi sehingga dapat langsung saya gunakan dalam aplikasi web saya. Lalu, saya menambahkan fungsi `register` pada `views.py` untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data sudah di-*submit* dari form tersebut.
2. Pada function `register` juga, saya menambahkan alur untuk melakukan validasi input yang dimasukkan oleh *user* pada form yang telah disediakan melalui perintah `form.is_valid()`. Sesudah divalidasi, isian form tersebut akan disimpan melalui perintah `form.save()`dan menampilkan pesan kepada *user* bahwa registrasi berhasil dan kembali ke halaman login. 
3. Pada subdirektori `templates`, saya menambahkan berkas HTML bernama `register.html` untuk memberikan visual kepada *user* untuk halaman registrasi. 
4. Setelah menambahkan views kepada *user*, saya mengintegrasikan fungsi `register` tadi pada `urls.py` untuk ditambahkan `urlpatterns` agar dapat menampilkan halaman *register* dan fungsinya sesuai *request* dari *user*.

<h3>Fungsi Login 📄</h3>

<hr>

5. Setelah melakukan prosedur registrasi, saya membuat fungsi login pada `views.py` dengan menambahkan import `authenticate`, `login`, dan `AuthenticationForm` yang sudah disediakan oleh Django untuk mendukung proses login dan autentikasi.
6. Pada berkas yang sama, saya menambahkan fungsi `login_user` untuk mengautentikasi pengguna yang ingin melakukan proses login. *User* nanti akan memasukkan *username* dan *password* serta di-*submit* sehingga mengirimkan request POST kepada aplikasi. Nantinya, aplikasi, dengan bantuan Django, akan melakukan proses autentikasi terhadap input yang dimasukkan oleh *user*. Apabila ditemukan kecocokan dengan data di *database*, maka fungsi ini akan membuat session untuk *user* tersebut. 
7. Setelah itu, pada subdirektori `templates`, saya menambahkan berkas HTML baru bernama `login.html` yang akan menampilkan halaman login kepada user. Lalu, saya membuka berkas `urls.py` untuk menambahkan `urlpatterns` agar dapat mengakses fungsi `login_user`. 

<h3>Fungsi Logout 📤</h3> 
<hr>

8. Sama seperti fungsi login, saya membuka kembali berkas `views.py` untuk mengimport `logout` untuk mekanisme logout pada aplikasi web, Setelah itu, saya menambahkan fungsi `logout_user` yang berfungsi untuk mendukung prosedur logout pada aplikasi web. 
9. Setelah itu, saya menambahkan views baru pada berkas `main.html`, yaitu tombol *Logout* agar ketika *user* menekan tombol tersebut, maka *user* akan logout dari aplikasi web. Lalu, pada berkas `urls.py`, saya menambahkan `urlpatterns` untuk mengakses fungsi `logout_user` yang telah dibuat agar dapat diakses. 

<h3>Merestriksi Akses Halaman Main dan Products Detail 👕</h3> 
<hr>

10. Untuk merestriksi akses halaman, saya perlu melakukan import `login_required` pada berkas `views.py` sebagai decorator untuk menambahkan fungsionalitas ke suatu fungsi tanpa mengubah isi dari kode fungsi tersebut. decorator tersebut saya letakkan pada bagian atas fungsi `show_main` dan `show_products`sehingga hanya *user* yang sudah terautentikasi saja yang dapat mengakses halaman tersebut. 

<h3>Menggunakan Data dari Cookies 🍪</h3>
<hr>

11. Untuk menggunakan data dari cookies, saya perlu mengimport `HttpResponseRedirect`, `reverse`, dan `datetime` pada berkas `views.py`. Setelah itu, pada fungsi `login_user`, saya menambahkan konfigurasi untuk menyimpan cookie baru bernama `last_login` yang berisi *timestamp* terakhir melakukan *login*. 
12. Lalu, pada function `show_main`, saya menambahkan variabel baru bernama `last_login` yang akan menyimpan *timestamp* dari aktivitas *user*. Hal ini juga berlaku ketika *user* menekan tombol logout, maka cookie tersebut dihapus sehingga dapat diperbarui ketika *user* melakukan login. 
13. Untuk melihat aktivitas terakhir login *user*, saya menambahkan konfigurasi pada berkas `main.html` untuk menambahkan view baru yang berisi informasi *timestamp* terakhir dari *user* setelah melakukan login. 

<h3>Menghubungkan Model Prodcts dengan User 👟</h3>
<hr>

14. Untuk menghubungkan model `Products` kepada *user*,  peru mengimport model `User` yang sudah disediakan oleh Django. Pada model `Products`, saya menambahkan variabel baru yaitu `user` yang akan menyimpan data user dalam bentuk model `User`. Agar Django dapat mendeteksi perubahan yang terjadi pada `models.py`, saya perlu melakukan migrasi agar perubahan model yang saya lakukan terdeteksi dan tersimpan.
15. Setelah itu, pada berkas `views.py`, saya menambahkan konfigurasi tambahan pada fungsi `create_products` agar objek hasil form yang dimasukkan *user* tidak langsung tersimpan di *database* sehingga dapat melakukan modifikasi terlebih dahulu. Selain itu, nilai dari `request.user` akan membuat setiap objek secara otomatis terhubunga kepada pengguna yang membuatnya. 
16. Lalu, pada function `show_main`, saya menambahkan konfigurasi untuk melakukan filter berdasarkan *author* yang menambahkan produk-produk tertentu di mana filter tersebut diambil dari query parameter `filter` pada URL. Agar fungsionalitas tersebut dapat dilihat, saya menambahkan view tambahan pada berkas `main.html` untuk menambahkan tombol filter My dan All. Lalu, pada berkas `products_detail.html`, saya juga menambahkan nama *author* yang menambahkan produk tertentu ke dalam aplikasi web.  

## Referensi 🔎
[1] Django Documentation. (n.d.). * Using the Django authentication system*. Retrieved from https://docs.djangoproject.com/en/5.2/topics/auth/default/
[2] MDN Web Docs. (n.d.). *Django Tutorial Part 8: User authentication and permissions*. Retrieved from https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Authentication
[3] GeeksforGeeks. (2025, July 23). *Difference Between Session and Cookies*. Retrieved from https://www.geeksforgeeks.org/javascript/difference-between-session-and-cookies/
[4] Django Documentation. (n.d.). *Security in Django*. Retrieved from https://docs.djangoproject.com/en/5.2/topics/security/
[5] Tim Dosen dan Asisten Dosen PBP 2024 dan 2025. (n.d). *Tutorial 3: Autentikasi, Session, Cookies dan Selenium*. Retrieved from https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-3

## Tugas Individu 5
***by Christna Yosua Rotinsulu-2406495691***

<h3>Urutan Prioritas Pengambilan CSS 🎨[1]</h3>
<hr>
Dalam mengambil dan menerapkan style CSS yang dibuat *developer* untuk aplikasi web, urutan yang akan menjadi fokus browser adalah sebagai berikut:

1.  **Importance** : deklarasi dengan `!important` akan menjadi pilihan pertama browser untuk memilih style CSS yang ingin diterapkan. Lalu, bagaimana jika terdapat dua rules tersebut? Dalam mengatasi hal tersebut, browser akan melihat ***specificity*** mana yang lebih tinggi. Lalu, bagaimana jika ***specifity*-nya** sama? Browser akan melihat *source order* yang muncul paling akhir. 
2. **Inline styles (`style="...")`**: *inline style* mempunyai *specificity* yang sangat tinggi sehingga ketika *style CSS* didefinisikan secara *inline* (*mengabaikan deklarasi `!mportant`*), maka hal tersebut akan menjadi prioritas browser untuk memutuskan dan menerapkan *style* tersebut.
3. **ID Selector (`#id`)** mempunyai *specifity* tinggi dalam CSS *Style*, terlebih id harus unik. Biasanya, *developer* menggunakan hal ini untuk desain bagian yang lebih spesifik.
4. **Class, attribute, pseudo-class (`.class, [attribute], :hover`)** mempunyai *specificity* yang sedang sehingga prioritas untuk menerapkannya bergantung pada prioritas yang lebih tinggi. *Developer* umumnya menggunakan selector ini untuk desain bagian spesifik dalam jumlah banyak, seperti desain `div` dan `button` dengan className yang sama. 
5. **Element and pseudo-element (`div, p, ::after`)** mempunyai *specificity* yang rendah. Hal ini perlu diperhatikan sebab semua element yang dipilih dalam berkas HTML akan menerapkan style tersebut sehingga untuk desain lebih spesifik dapat menggunakan selector dengan *specificity* yang lebih tinggi.
6. **Source Order**: lalu, bagaimana jika tidak menggunakan selector `.class`, `#id`, dsb? atau ada dua *selector* dengan rules yang sama? Untuk menangani hal tersebut, browser akan melihat urutan rules yang ditulis dan akan memilih *rules* yang ditulis paling terakhir/bawah (terbaru). 
7. **Origin**: dalam praktiknya, *developer* lebih memilih untuk menggunakan *eksternal style* sehingga lebih mudah dalam mengatur desain yang ingin digunakan, terlebih jika kode terlalu banyak, maka jika *rules* langsung didefinisikan di berkas yang sama akan merepotkan *developer* untuk *develop* desain browser menjadi lebih menarik.

<h3>Mengapa Responsive Design Penting? 📲 [2]</h3>
<hr>

Alasan kenapa *responsive design* perlu menjadi perhatian utama *developer* dalam mengembangkan sebuah aplikasi adalah sebagai berikut:

1. **Tidak Bergantung Pada Device**: *user* dapat membuka aplikasi melalui peramban web dari ponsel, laptop, atau TV sehingga *developer* perlu memperhatikan agar *layout* menjadi lebih adaptif di semua *device*.
2. **UX  & Konversi**: tata letak yang baik pada semua perangkat akan memberikan kenyamanan kepada *user* dalam mengakses aplikasi web tersebut. Selain itu, hal ini akan membantu menurunkan *bounce* sehingga menaikkan konversi antara *user* dengan aplikasi, seperti pendaftaran atau pembelian produk.
3. **SEO atau Search Engine Optimazion** akan membantu menarik perhatian *user* untuk mengunjungi aplikasi yang dibuat. Tetapi, SEO lebih memprioritaskan *mobile-friendly pages* sehingga tata letak harus lebih adaptif untuk device mobile.
4. **Aksesibilitas**: salah satu hal yang perlu diperhatikan *user* adalah target pemasaran. Oleh sebab itu, apabila target pemasaran ditujukan kepada orang tua dan lansia akan lebih baik jika *responsive design + breakpoints* yang masuk akal diterapkan dalam aplikasi, seperti pembesaran ukuran teks, sehingga membantu *user* dalam mengakses aplikasi.

Salah satu contoh aplikasi yang sudah menerapkan *responsive design* adalah **Tokopedia/Shopee**. Aplikasi tersebut mempunyai layout yang adaptif terhadap semua device, elemen CTA besar, dan navigasi tab bawah sangat membantu *user* melakukan pembelian produk, transaksi, pelacakan barang, menyampaikan keluhan, dsb. 

Di sisi lain, ada beberapa aplikasi yang belum atau kurang menerapkan *responsive design* yang umumnya digunakan di beberapa **portal pemerintahan lama atau aplikasi intranet perusahaan lawas** yang masih dirancang untuk *desktop only*, tabel yang melebar, dan tombol kecil. Biasanya aplikasi tersebut masih menggunakan codebase lama, depedensi UI lawas, atau tidak ada prioritas bisnis untuk redesign, seperti *e-commerce* modern saat ini. 

<h3>Box Model 📦 [3]</h3>
<hr>

Dalam CSS Style, Box model dibagi menjadi 4 bagian, yaitu **Content**, **Padding**, **Border**,  dan **Margin**.

1. **Content**: box atau area untuk menaruh teks/gambar.
2. **Padding**: space di dalam box yang terletak di antara *content dan border*. (Background juga dapat melekat sampai padding).
3. **Border**: garis yang berada di sekitar *padding dan content*.
4. **Margin**: space yang berada di luar border dan memisahkan elemen dari elemen lain. (Note: margin dapat *collapse* untuk *vertical margins*).

Contoh implementasi:

    .card{
        content-box;
        width: 300px; 
        padding: 20px;              
        border: 2px solid #00000;  
        margin: 16px;               
        box-sizing: border-box;     
    }
   **Penjelasan**
   
   1. Padding 20px -> memberi space di bagian atas, bawah, kanan, dan kiri sebesar 20 pixels
   2. Border 2px solid #00000 -> memberi garis pada box **card** setebal 2 pixels dan tidak putus putus dengan warna hitam (bisa menggunakan RGB dan hsl juga untuk mengatur lightness atau saturation)
   3. Margin 16px -> Memberi space di luar box (kanan, kiri, atas, dan bawah) **card** sebesar 16 pixels. 
 
<h3>Flexbox vs Grid : Mana yang Lebih Bagus? 💪 [4]</h3>
<hr>

Flexbox adalah konsep layout di mana menaruh box layout menjadi satu dimensi (baris atau kolom). Hal ini sangat baik apabila diterapkan pada bar navigasi, card row, center-align vertical/horizontal, komponen UI yang linear. Flexbox akan menjadi lebih adaptif di semua device karena box layout tidak akan menghimpit satu dengan yang lain pada ukuran screen device yang lebih kecil. Beberapa properti utama di flexbox: `display: flex; flex-direction; justify-content; align-items; gap; flex-wrap; flex-grow/shrink/basis`.

Di sisi lain, Grid adalah konsep layout di mana menaruh box layout menjadi dua dimensi (baris dan kolom) sehingga cocok untuk layout halaman, gallery, complex card layout, asymmetrical layouts, dsb. Beberapa properti utama dalam CSS Grid meliputi `display: grid; grid-template-columns/rows; gap; grid-auto-flow; grid-area`.

Lalu, mana yang lebih bagus? Konsep layout tersebut perlu dikatikan dengan kebutuhan aplikasi. Apabila layout utamanya baris/kolom sederhana, maka gunakan **Flexbox**. Lalu, apabila butuh kontrol baris dan kolom kompleks, maka gunakan **Grid**. Atau, bisa menggunakan kedua konsep layout tersebut untuk halaman (**Grid**) atau komponen internal (**Flexbox**)

<h3>Checklist Step by Step</h3>
<hr>

1. **Menambah tailwind ke aplikasi**: membuka berkas `base.html` yang telah dibuat sebelumnya dan menambahkan tag `<meta name="viewport>` agar halaman web menjadi adaptif terhadap ukuran dan perilaku *mobile device*.
2. Menambahkan script CDN (*Content Delivery Network*) Tailwind di bagian head pada berkas `base.html`.
3. **Menambahkan fitur edit_products** pada berkas `views.py` yang menerima parameter `request` dan `id` agar toko dapat mengedit produk mereka di aplikasi web secara langsung tanpa perlu `create_product` kembali. 
4. **Menambahkan tampilan edit_product** dengan menambahkan berkas baru bernama `edit_products.html` dan mengintegrasikan tampilan tersebut melalui `urls.py` agar dapat diakses. Lalu, mengimport function `create_products` dan path ke function tersebut.
5. **Melakukan pembaruan `main.html`** untuk menambahkan tombol `edit` yang dapat di-*click* toko untuk memperbarui produk mereka.
6. **Menambahkan fitur `delete_products`** dengan menambahkan function `delete_products` yang menerima parameter `request` dan `id` pada berkas `views.py` agar toko dapat menghapus produk mereka dari aplikasi (sebelumnya belum tersedia). Lalu, mengintegrasikan fungsi tersebut pada berkas `urls.py` dan menambahkan url untuk mengakses fungsi tersebut. 
7. **Memunculkan tombol `delete` pada berkas `main.html`** dengan mengubah bagian loop `product_list` yang dapat di-*click* untuk mengakses fungsi tersebut.
8. **Menambahkan navigation bar** pada direktori `templates` di root directory. Navigation bar ini akan membantu aplikasi dalam menavigasi berbagai halaman atau fitur yang ada di aplikasi web. 
9. **Menambahkan konfigurasi static files pada aplikasi** dengan menambahkan *middleware* WhiteNoise pada berkas `settings.py` agar Django dapat mengelola berkas statis secara otomatis dalam mode produksi tanpa perlu konfigurasi yang kompleks. Lalu, menambahkan konfigurasi variabel `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL`.
10.**Costum styling halaman login, register, navbar, home, dan product details** menggunakan Tailwind.

## Referensi 🔎
[1] MDN Web Docs. (n.d.). *Basic CSS selectors*. Retrieved from https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors
[2] w3schools. (n.d.). *HTML  Responsive Web Design*. Retrieved from https://www.w3schools.com/html/html_responsive.asp
[3] w3schools. (n.d.). *CSS  Box Model*. Retrieved from https://www.w3schools.com/css/css_boxmodel.asp
[4] Codepolitan. (2018, July 10). *CSS Grid vs Flexbox*. Retrieved from https://www.codepolitan.com/blog/css-grid-vs-flexbox-5b4336849183d/
[5] Tim Dosen dan Asdos PBP 2025. (n.d.) *Tutorial 4: Desain Web Menggunakan HTML dan CSS3 & Metode Update dan Delete pada Data*. Retrieved from https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-4

## Tugas Individu 6
***by Christna Yosua Rotinsulu - 2406495691***

<h3>Synchronous Request vs Asynchronous Request [1] 💥</h3>
<hr>

Synchronous dan asynchronous *request* adalah dua model pemograman yang berbeda dalam hal menangani operasi dalam sebuah aplikasi, terutama yang membutuhkan waktu seperti *request* jaringan.

**Synchronous request** adalah *request* yang mencegah DOM atau browser mengeksekusi kode tambahan sampai server memberikan respons. Apabila *request* tersebut diterima, maka hanya bagian kode berikutnya yang akan dieksekusi, sebaliknya, peramban web/DOM akan menunggu respons tersebut.

Di sisi lain, **asynchronous request** adalah *request* yang tidak akan mencegah DOM atau peramban untuk mengeksekusi kode tambahan sampai server memberikan respons sehingga sisa kode akan langsung dieksekusi. 

Dari definisi tersebut, saya dapat menjelaskan 3 hal yang menjadi pembeda antara kedua model pemograman tersebut sebagai berikut:

1. **Synchronous** akan membuat peramban web ter-refresh seluruhnya setiap kali melakukan request, sedangkan **asynchronous** akan membuat peramban web memperbarui halaman yang dimaskud pada bagian tertentu saja tanpa perlu refresh seluruh halaman. 
2. **Synchronous** menyebabkan *user experience* menjadi terputus karena harus menuggu loading halaman yang baru di-*update*, sedangkan **asynchronous** tetap mempertahankan komunikasi antara *user* dengan aplikasi walaupun proses *request* sedang berjalan di belakang layar.
3. Berdasarkan poin 1 dan 2, **synchronous** menggunakan pola komunikasi linear dan *blocking*, sedangkan **asynchronous** menggunakan pola komunikasi non-*blocking* dan parallel.

<h3>Alur Kerja AJAX di Django [2] ⚙️</h3>
<hr>

Cara AJAX memberikan response terhadap request yang diberikan *user* melalui aplikasi web dapat saya jelaskan melalui poin-poin berikut:

1. **Trigger dari Sisi Client**: ketika *client* men-*trigger* sebuah event JavaScript, seperti click, input, dsb, maka hal terebut akan memicu AJAX call.
2. **AJAX  Request**: AJAX call yang dipicu tadi akan membuat JavaScript mengirim HTTP *request* ke bagian *endpoint* Django. 
3. **Django Processing Request**: *request* yang tersebut akan memicu URL *routing* untuk mengarahkan ke *view* yang sesuai permintaan *user*. Di *view* tersebut, *logic* dan interaksi yang di-*fetch* akan diproses dengan models/database sesuai kebutuhan. Lalu, setelah selesai diproses, Django akan mengembalikan *response* dalam format JSON/XML. 
4. **Update di Sisi Client**: *response* yang dikirim Django akan diterima oleh JavaScript dan memperbarui DOM secara dinamis sehingga tidak mengganggu interaksi *user* saat itu.
5. **Update UI**: peramban web atau aplikasi web akan melakukan pembaruan halaman di bagian tertentu tanpa perlu melakukan reload di keseluruhan halaman. 

<h3>AJAX vs Render Biasa: Mana yang Lebih Baik? [3] 👮</h3>
<hr>

Setelah membahas cara kerja AJAX dalam menangani *request*, saya dapat mendeskripsikan keuntungan AJAX dalam aplikasi web melalui poin-poin berikut:

1. **User Experience Lebih Interaktif**: AJAX memberikan kesempatan kepada *user* untuk terus melakukan interaksi yang cepat dan responsif dengan aplikasi web sehingga interaksi akan terus meningkat seiring berjalannya waktu.
2. **Bandwidth Berkurang**: sebab hanya beberapa data yang perlu ditransfer berdasarkan kebutuhan sesuai *request* yang diberikan sehingga bandwidth atau kapasitas maksimum transfer data menjadi semakin berkurang. 
3. **Mirip Desktop**: interaksi real-time dan fluid (terus mengalir) menjadikan aplikasi web menjadi mirip dengan desktop. 
4. **Preservasi State**: AJAX mampu mempertahankan kondisi form data, scroll position, dan UI state yang saat ini *user* lakukan sehingga *user* menjadi lebih mudah dalam mengakses aplikasi, seperti tidak perlu lagi mengisi form dari awal atau scroll dari bagian *header*. 
5. **Processing secara Parallel**: AJAX mampu menerima berbagai *request* dan memproses hal tersebut secara bersamaan karena sifatnya yang **asynchronous**. Hal ini akan meningkatkan kecepatan eksekusi kode, menangani masalah kompleks, pengurangan biaya dalam jangka panjang, dsb.
6. **Feedback Instan**: AJAX mampu dalam melakukan validasi form dan notifikasi langsung sehingga tidak perlu diproses dengan waktu yang lama di belakang layar. Hal ini tentu akan membantu *user* dalam mengakses aplikasi web. 

Berdasarkan kelebihan-kelebihan hal tersebut, saya dapat membandingkannya dengan render biasa melalui poin-poin berikut:

1. Render biasa akan membuat halaman selalu reload seluruhnya selama *request* terus dikirim sehingga akan menurunkan *user experience* dalam aplikasi tersebut atau terfragmentasi. 
2. Sebab render biasa perlu men-*transfer* semua data, beban bandwidth akan menjadi semakin tinggi sehingga kecepatan akses aplikasi menjadi menurun.
3. Render biasa akan membuat *user* menunggu lebih lama sebab menunggu *response* dari aplikasi web sampai disetujui dan dikembalikan. 

<h3>Apakah AJAX Aman? [4] 🤔</h3>
<hr>

Tentu penggunaan AJAX mempunyai celah-celah keamanan, oleh karena itu, *developer* perlu memperhatikan beberapa aspek dalam mengamankan data-data yang ada di aplikasi. Berikut adalah beberapa contoh yang dapat saya jelaskan untuk menjamin keamanan aplikasi web dalam menggunakan AJAX melalui poin-poin berikut:

1. Selalu menyertakan token CSRF dalam AJAX *request*
2. Wajib menggunakan **HTTPS** sehingga komunikasi login/register/pembelian dapat terenkripsi dan sulit dibaca secara langsung
3. Melakukan validasi ketat di sisi server untuk semua input yang dimasukkan oleh *user*
4. Memberikan batas percobaan login untuk menghindari *brute force attacks* sehingga *user* 'palsu' tidak dapat sembarangan login ke dalam aplikasi web (sertakan opsi *forget password* sehingga *user* 'asli' dapat memperbarui password akun mereka)
5. Mengatur session timeout yang aman 
6. Melakukan restriksi *cross-origin request* (opsional)
7. Sanitasi output yang dihasilkan dan menggunakan *content security policy* sehingga data yang ditampilkan lebih aman dan terhindar dari kode berbahaya, seperti serangan XSS
8. Menggunakan header keamanan seperti HSTS atau *HTTP Strict Transport Security* sehingga aplikasi web hanya dapat berjalan menggunakan koneksi HTTPS yang lebih aman. 

<h3>Bagaimana Peran AJAX dalam User Experience [5] 👤</h3>
<hr>

Penggunaan AJAX secara signifikan meningkatkan pengalaman pengguna melalui beberapa aspek yang dapat saya jelaskan melalui poin-poin berikut:

1. **Responsivitas Tinggi**: aplikasi web menjadi lebih cepat dan halus sebab AJAX membuat halaman tidak perlu memuat ulang sepenuhnya setiap kali pengguna melakukan interaksi (mengirimkan *request*)
2. **Interaksi Real-Time seperti Desktop**: AJAX membuat transfer data dan proses data di belakang layar tidak mengganggu aktivitas pengguna selama proses tersebut sehingga tercipta sensasi seperti menggunakan aplikasi native
3. **Progressive Feedback**: aplikasi dapat memberikan notifikasi pembaruan melalui indikator loading atau pembaruan status sehingga *user* dapat memahami bahwa sistem saat ini sedang memproses permintaan mereka atau memperbarui tampilan
4. **Single-page Feel**: navigasi antar konten menjadi lebih mulus dan tanpa jeda ketika menggunakan AJAX sehingga *user* dapat terus melakukan interaksi tanpa perlu menunggu waktu pemrosesan yang lama
5. **Preservasi Context**: AJAX memungkinkan *user* untuk kembali ke state sebelumnya, seperti form data, posisi halaman, dsb, sehingga *user* mudah dalam melakukan akses aplikasi, seperti tidak perlu mengisi form dari awal atau scroll ke halaman terakhir. 


## Referensi 🔎
[1] Geeksforgeeks. (2025, July 23). *Difference between synchronous and asynchronous requests in jQuery Ajax*. Retrieved from https://www.geeksforgeeks.org/jquery/difference-between-synchronous-and-asynchronous-requests-in-jquery-ajax/
[2] Geeksforgeeks. (2025, July 23). *Handling Ajax request in Django*. Retrieved from https://www.geeksforgeeks.org/python/handling-ajax-request-in-django/
[3] Jagoan Hosting. (2022, May 19). *AJAX: Pengertian, Cara Kerja, Fungsi dan Kurang Lebih*. Retrieved from https://www.jagoanhosting.com/blog/ajax-adalah/
[4] Django Documentation. (n.d.). *How to use Django's CSRF protection*. Retrieved from https://docs.djangoproject.com/id/5.2/howto/csrf/
[5] Harvianti, A. (2025, May 22). *Apa Itu AJAX? Definisi, Fungsi, Cara Kerja, dan Kelebihan*. Retrieved from https://www.sekawanmedia.co.id/blog/apa-itu-ajax/

## Tugas Individu 9
***by Christna Yosua Rotinsulu - 2406495691***

<h3>Mengapa Perlu Model Dart dan Konsekuensi Tanpanya 🤔</h3>
<hr>

Membuat model Dart untuk merepresentasikan data JSON dari aplikasi mobile saya tentu akan memberikan beberapa keuntungan bagi seorang *developer*. Keuntungan pertama membuat modelDart adalah model Dart mampu memberikan **type safety &** keuntungan bahasa statis sehingga compiler dapat menangkap error jenis daat saat melakukan kompilasi. Tidak hanya **type safety**, model Dart mendukung **null safety** di mana ketika ada field yang dapat dideklarasikan nullable (`?`) atau required (`required`). Salah satu alasan utama kenapa model Dart harus dibuat adalah ketika aplikasi mobile memiliki skala besar dan proyek yang terstruktur sebab mempermudah pengelolaan kode aplikasi sebab perubahan struktur JSON hanya perlu diadaptasi pada satu tempat saja. Fitur IDE, seperti *autocompletion* yang sering digunakan, saat ini, sudah mendukung proses pembuatan model Dart sehingga membantu *developer* untuk bekerja secara lebih optimal. 

**Lalu, bagaimana ketika tidak menggunakan model Dart?** Apabila tidak menggunakan model Dart, maka representasi data JSON akan menggunakan **pemetaan langung** menggunakan `Map<String, dynamic>`. Lalu, apa bedanya dengan menggunakan model Dart? Pemetaan secara langsung tidak mendukung **type safety** seperti model Dart sehingga ketika ada data `dynamic` yang error, seperti salah tipe data, hanya ketahuan ketika runtime yang tentu dapat memperlambat pekerjaan. Selain itu, pemetaan langsung tidak mendukung **null safety** sehingga tidak ada jaminan keamanan data null dan dapat menyebabkan **crash**. Berbeda dengan model Dart, ketika terjadi perubahan struktur JSON, maka *developer* perlu melakukan perubahan di banyak tempat sehingga sangat rentan terhadap *human error*, terlebih untuk aplikasi yang sudah berskala besar dan kompleks. Selain itu, fitur IDE tidak mendukung autocompletion untuk pemetaan langsung sehingga sangat rawan terhadap typo apabila tidak mengingat key JSON yang dibuat. 

Berikut adalah contoh implementasi di Flutter:
```dart
import 'package:json_annotation/json_annotation.dart';

part 'product.g.dart';

@JsonSerializable()
class Product {
  final int id;
  final String name;
  final int price;
  final String description;
  final int user;

  Product({
    required this.id,
    required this.name,
    required this.price,
    required this.description,
    required this.user,
  });

  factory Product.fromJson(Map<String, dynamic> json) => _$ProductFromJson(json);
  Map<String, dynamic> toJson() => _$ProductToJson(this);
}
```

<h3>HTTP vs CookieRequest 🔥</h3>
<hr>

Dalam proyek kali ini, saya menggunakan package **http** dan **CookieRequest** untuk melakukan beberapa fungsionalitas tertentu. Package **http** membantu saya untuk melakukan **HTTP request** dasar, seperti GET, POST, PUT, dan DELETE ke web server Django untuk menangani pertukaran data mentah secara asynchronous. Di sisi lain, package **CookieRequest** digunakan sebagai **layer autentikasi** yang membungkus fungsionalitas **http**. Package ini akan secara otomatis mengelola dan menyertakan cookie, yang berisi session ID, di setiap request yang dikirimkan ke Django sehingga aplikasi Flutter dapat mempertahankan status login user. 

<h3>Membagikan Instance CookieRequest 🍪</h3>
<hr>

Instance `CookieRequest` perlu dibgaikan ke semua komponen yang ada di dalam aplikasi dan umumnya dibagikan dengan `Provider` untuk memastikan bahwa **status autentikasi** secara konsisten terjadi di seluruh bagian aplikasi. Melalui pembagian instance yang sama tersebut, komponen di setiap bagian yang sedang melakukan `request`, seperti mengambil data item produk baru, akan menggunakan **session** yang sama. Di sisi lain, apabila tidak membagikan instance yang sama, maka Django akan menganggap komponen tersebut **tidak terautentikasi**. 

<h3>Konvigurasi Konektivitas Flutter-Django</h3>
<hr>

Dengan melakukan konvigurasi konektivitas, Flutter dapat berkomunikasi dengan server Django yang berjalan di lokal. Oleh sebab itu, pada proyek ini, saya menambahkan konvigurasi `ALLOWED_HOSTS` pada `settings.py` Django, yaitu `10.0.2.2` di mana alamat tersebut adalah **alias khusus** dari emulator Android untuk `localhost` di komputer saya. Di sisi lain, agar Flutter dan Django dianggap sebagai origin berbeda, saya perlu mengaktifkan package `django-cors-headers` yang akan memberikan middleware **CORS (Cross-Origin Resource Sharing)** sehingga brower atau aplikasi Flutter tidak akan memblokir respons yang diberikan oleh Django. Selain itu, agar cookie dapat dikirim dalam konteks cross-site yang aman, saya perlu melakukan **pengaturan Cookie (SameSite & Secure)**, yaitu mengatur `CSRF_COOKIE_SAMSITE` dan `SESSION_COOKIE_SAMSISTE` menjadi `'None'` dan `CSRF_COOKIE_SECURE` dan `SESSION_COOKIE_SECURE` menjadi `True`. Agar applikasi Flutter dapat membuat koneksi jaringan, saya menambahkan **izin akses internet di bagian Android**, yaitu menambahkan baris `<uses-permission android:name="android.permission.INTERNET" />` di berkas `android/app/src/main/AndroidManifest.xml`.

<h3>Mekanisme Pengiriman dan Penampilan Data</h3>
<hr>

Mekanisme pengiriman dan penampilan data, dapat saya jelaskan melalui diagram berikut:

```mermaid
flowchart TD
    A[User Input Data Login<br>di Flutter] --> B[Flutter Kirim Request<br>ke Endpoint Django]
    B --> C{Django Verifikasi<br>Kredensial}
    C -- Sukses --> D[Django Buat Session<br>& Kirim Cookie]
    C -- Gagal --> E[Kembali ke Login<br>dengan Pesan Error]
    D --> F[Flutter Terima Cookie<br>& Simpan dengan CookieRequest]
    F --> G[Arahkan ke Menu Utama]
    G --> H[Request Data dengan<br>Cookie yang Tersimpan]
 ```

Berdasarkan diagram tersebut, mekanisme pengiriman dan penampilan data dapat saya jelaskan sebagai berikut:

1. **Input & Request**: *User* nantinya akan memasukkan data produk di UI Flutter, misalnya form tambah produk baru. Nantinya, data yang dimasukkan tersebut di-*decode* menjadi JSON dan dikirimkan via **POST request** menggunakan package yang sudah diaktifkan tadi, yaitu `http` dan `CookieRequest` ke endpoint Django. 
2. **Proses di Django**: Data yang dikirimkan dalam bentuk `request` tadi akan diterima oleh server Django dan divalidasi serta disimpan ke dalam database. 
3. **Fetch Data**: Ketika data sudah disimpan dalam database, layar daftar produk di Flutter akan mengirimkan `GET` ke endpoint JSON Django untuk mendapatkan data mentah yang diperlukan. 
4. **Parsing Django ke Model**: Respons JSON dari Django yang diterima akan di-*decode* dan dikonversi menjadi list objek Dart menggunakan method `fromJson` yang ada pada model yang dibuat. 
5. **Menampilkan di UI Flutter**: Setelah objek tersebut dibuat, maka widget `FutureBuilder` akan membangun UI, seperti `ListView.builder`, saat data future berhasil di-fetch dan di-parse.

<h3>Mekanisme Autentikasi Aplikasi</h3>
<hr>

Mekanisme autentikasi pada aplikasi Flutter dapat saya jelaskan melalui diagram berikut:

```mermaid
flowchart TD
    A[User Input Data Login<br>di Flutter] --> B[Flutter Kirim Request<br>ke Endpoint Django]
    B --> C{Django Verifikasi<br>Kredensial}
    C -- Sukses --> D[Django Buat Session<br>& Kirim Cookie]
    C -- Gagal --> E[Kembali ke Login<br>dengan Pesan Error]
    D --> F[Flutter Terima Cookie<br>& Simpan dengan CookieRequest]
    F --> G[Arahkan ke Menu Utama]
    G --> H[Request Data dengan<br>Cookie yang Tersimpan]
```

Ketika *user* melakukan login dengan memasukkan username dan password pada form login, maka Flutter akan mengirimkan *username* dan *password* ke endpoint Django untuk diverifikasi apakah terdaftar di database. Ketika *user* terautentikasi, maka Django akan membuat session baru dan mengirimkan **id session** tersebut ke aplikasi *client* untuk disimpan sebagai **CookieRequest**. Lalu, Flutter akan mengarahkan halaman ke menu utama atau `homepage`. *User* dapat melakukan interaksi melalui fitur-fitur yang ada dan setiap interaksi akan mengirimkan `request` data dengan cookie yang tersimpan. Hal ini juga berlaku untuk proses **registrasi** akun baru di mana Flutter akan mengirimkan data *username* dan *password* ke endpoint Django untuk dibuatkan akun baru. **Lalu, bagaimana dengan fitur Logout?** Sama seperti tugas aplikasi web berbasis Django, aplikasi Flutter akan mengirimkan `request` baru ke endpoint logout di Django untuk melakukan `logout`. Lalu, Django akan menerima dan memberikan response ke aplikasi Flutter serta menghapus `session` yang tadi sudah disimpan. Selain itu, Flutter juga akan menghapus cookie yang disimpan, berisi id session, menggunakan instance `CookieRequest`. Hal ini perlu dilakukan agar terhindar dari pencurian data di mana melalui session id **attacker** dapat mengetahui interaksi yang sedang terjadi dan itu sangat berbahaya, terutama yang berkaitan dengan data sensitif dan proses transaksi.

<h3>Implementasi Checklist Step-by-Step</h3>
<hr>

Dalam mengerjakan proyek saya kali ini, berikut adalah checklist yang saya lakukan dalam mengembangkan aplikasi mobile saya, mulai dari implementasi tutorial dan modifikasi kode sesuai kebutuhan.