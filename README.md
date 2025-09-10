---


---

<h2 id="tugas-individu-2">Tugas Individu 2</h2>
<p><em><strong>by Christna Yosua Rotinsulu - 2406495691</strong></em></p>
<p><strong>URL Deployment PWS :</strong><br>
<a href="https://christna-yosua-houseofchampions.pbp.cs.ui.ac.id/">https://christna-yosua-houseofchampions.pbp.cs.ui.ac.id/</a></p>
<h2 id="implementasi-pengembangan-aplikasi-web-menggunakan-django"><strong>Implementasi Pengembangan Aplikasi Web Menggunakan Django</strong></h2>
<p><strong>Membuat Direktori dan Mengaktifkan <em>Virtual Environment</em></strong></p>
<ol>
<li>Tentu langkah pertama yang saya lakukan adalah membuat sebuah direktori baru bernama house-of-champions (<em>tema yang saya pilih</em>) dan masuk ke dalam folder tersebut.</li>
<li>Setelah itu, saya membuka terminal di vs code untuk membuat <em><strong>virtual environment</strong></em> di dalam direktori proyek yang saya buat dengan perintah <code>python -m venv env</code> yang nantinya akan membuat folder baru, yaitu env, yang berfungsi untuk mengisolasi <em>package</em> serta <em>dependencies</em> dari aplikasi yang saya buat agar tidak bertabrakan dengan versi lain di <em>device</em> yang saya gunakan. Setelah itu, <em>virtual environment</em> tersebut saya aktifkan dengan perintah <code>env\Scripts\activate</code>.</li>
</ol>
<p><strong>Menyiapkan <em>Dependencies</em> dan Membuat Proyek Django</strong></p>
<ol start="3">
<li>Lalu, saya mulai menyiapkan <em><strong>Dependencies</strong></em> yang menjadi komponen atau modul yang diperlukan oleh sebuah <em>software</em> untuk berfungsi, termasuk <em>library</em>, <em>framework</em>, atau <em>package</em> yang dibutuhkan. Dengan <em>Dependencies</em>, saya dapat melakukan proses pengembangan menjadi lebih efisien dan cepat, walaupun saya juga perlu berhati-hati untuk memastikan kompabilitas versi yang tepat. <em>virtual environment</em> yang telah saya buat dan aktifkan tadi berguna untuk mengisolasi <em>dependencies</em> antara proyek-proyek yang berbeda. Untuk menambahkan beberapa <em>dependencies</em> yang saya perlukan, saya membuat sebuah file khusus, yaitu <code>requirements.txt</code> yang berisi beberapa <em>dependencies</em>, yaitu <code>django, gunicorn, whitenoise, psycopg2-binary, requests, urllib3, dan python-dotenv</code>. Setelah itu, saya melakukan instalasi <em>dependecies</em> tersebut melalui perintah <code>pip install -r requirements.txt</code>.</li>
<li>Setelah mempersiapkan <em>dependencies</em> yang saya perlukan untuk proses pengembangan selanjutnya, saya mulai menyiapkan dan membuat proyek Django bernama <em>champions-store</em> melalui perintah <code>django-admin startproject champions_store .</code></li>
</ol>
<p><strong>Konfigurasi Environment Variables dan Proyek</strong></p>
<ol start="5">
<li>Selanjutnya, saya mulai melakukan <strong>konfigurasi environment variables dan proyek</strong>. Pertama, saya mulai membuat file <code>.env</code> untuk development lokal dan menambahkan konfigurasi <code>PRODUCTION=False</code> sehingga aplikasi web nanti akan menggunakan database SQLite yang lebih simple untuk melakukan testing dan development. Di sisi lain, saya juga membuat file <code>.env.prod</code> untuk production deployment dengan konfigurasi production sesuai dengan panduan, mulai dari <code>DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, SCHEMA, dan PRODUCTION</code> di mana <code>SCHEMA</code> yang digunakan adalah <code>tugas_individu</code>. Sebab <code>PRODUCTION=True</code>, aplikasi akan menggunakan PostgreSQL dengan kredensial yang akan disediakan oleh ITF Fasilkom UI.</li>
<li>Lalu, saya mulai melakukan modifikasi file <code>settings.py</code> untuk menggunakan environment variables yang telah saya konfigurasi melalui fungsi <code>load_dotenv()</code> yang diimpor dari <code>dotenv</code></li>
<li>Untuk keperluan deployment, saya menambahkan dua string, yaitu <code>"loaclhost, "127.0.0.1"</code> pada <code>ALLOWEB_HOSTS</code> di <code>settings.py</code> agar <em>host</em> tersebut diizinkan untuk mengakses aplikasi web, tetapi hanya bisa diakses dari jaringan saya saat ini saja (<em>host</em> lokal).</li>
<li>Setelah itu, saya menambahkan konfigurasi <code>PRODUCTION</code> di <code>settings.py</code> untuk mendapatkan konfigurasi <code>PRODUCTION</code> yang telah saya lakukan. Setelah itu, di file yang sama, saya menggunakan konfigurasi <code>DATABASES</code> sesuai dengan konfigurasi <code>PRODUCTION</code> di file <code>.env</code> dan <code>.env.prod</code></li>
</ol>
<p><strong>Menjalankan Server</strong></p>
<ol start="9">
<li>Untuk menjalankan server, saya perlu untuk melakukan migrasi database terlebih dahulu dengan perintah <code>python manage.py migrate</code>. Setelah berhasil melakukan migrasi, saya mulai menjalan server Django dengan perintah: <code>python manage.py runserver</code>. Untuk mengecek apakah proyek Django berhasil dibuat, saya dapat membuka <a href="http://localhost:8000">http://localhost:8000</a> di peramban web untuk mengetahui hal tersebut.</li>
</ol>
<p><strong>Menghentikan Server dan Menonaktifkan Virtual Environment serta Unggah Proyek ke Repositori GitHub</strong></p>
<ol start="11">
<li>Setelah proyek Django saya berhasil dibuat, saya menghentikan server dan menonaktifkan <em>virtual environment</em> untuk melakukan pengunggahan ke GitHub. Proyek Django yang saya buat, saya simpan di repositori GitHub bernama house-of-champions. Selain itu, saya menambahkan file <code>.gitignore</code> yang berisi konfigurasi untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git sehingga ketika saya melakukan <em>push</em>, file yang tercantum di file <code>.gitignore</code> tidak ikut ter-<em>push</em>. Berkas-berkas yang akan diabaikan dan tidak perlu dilacak oleh Git adalah berkas-berkas yang dihasilkan oleh proses kompilasi, berkas sementara, atau berkas konfigurasi pribadi. Dalam hal tersebut, file yang tidak akan ter-<em>push</em> ke GitHub, yaitu file <code>.env</code>, <code>.env.prod</code>, <code>db.sqlite3</code>, dan sebagainya, sebab mengandung konfigurasi pribadi dan proses kompilasi.</li>
</ol>
<p><strong>Pembuatan Akun dan Deployment melalui PWS (Pacil <em>Web Service</em>)</strong></p>
<ol start="12">
<li>Pacil Web Service adalah salah satu bentuk layanan <strong>PaaS</strong>, yaitu Platform as a Service, yang disediakan untuk membantu mahasiswa, termasuk saya, dalam melakukan pengembangan, pengelolaan, dan peluncuran aplikasi tanpa perlu mengkhawatirkan infrastruktur dasarnya. Untuk membuat project tersebut, saya perlu membuat akun sesuai dengan <em>SSO UI</em> milik saya. Lalu, saya membuat project baru bernama <em>houseofchampions</em> sesuai dengan tema aplikasi yang saya pilih. Setelah itu, saya perlu menyimpan kredensial yang diberikan sebelum menjalankan instruksi <em><strong>Project Command</strong></em>.  Setelah menyimpan kredensial tersebut, saya pergi ke tab Environs untuk mengonfigurasi <em>environment variables</em> yang telah saya konfigurasi di file <code>.env.prod</code>. Lalu, saya kembali ke proyek Django saya untuk menambahkan URL <em>deployment</em> pada <code>ALLOWED_HOSTS</code> sehingga proyek saya dapat diakses melalui URL <em>deployment</em> PWS dan dapat dilihat oleh user lain.</li>
<li>Setelah menambahkan <em>URL deployment</em>, saya melakukan <em>push</em> ke repositori GitHub saya dan mulai menjalankan perintah yang terdapat di <em>Project Command</em> pada halaman PWS. Lalu, akan muncul <em>pop-up</em> baru untuk memasukkan kredensial yang telah saya simpan tadi dan perlu menunggu beberapa detik hingga status deployment <em>Running</em>.</li>
</ol>
<p><strong>Membuat Aplikasi Django beserta Konfigurasi Model</strong></p>
<ol start="14">
<li>Untuk mengonfigurasi model, saya perlu mengaktifkan kembali <em>virtual environment</em>. Setelah itu, saya membuat aplikasi baru bernama <code>main</code> dalam proyek <em>house-of-champions</em> melalui perintah <code>python manage.py startapp main</code> yang nantinya akan membuat folder baru bernama <code>main</code>. Lalu, saya menambahkan <code>'main'</code> ke dalam daftar aplikasi pada <code>INSTALLED_APPS</code> di <code>settings.py</code>.</li>
</ol>
<p><strong>Implementasi Template Dasar</strong></p>
<ol start="15">
<li>Untuk memberikan tampilan teks, gambar, dan bahan lainnya secara visual maupun suara kepada user lain, saya perlu membuat file HTML yang akan menampilkan semua hal tersebut sesuai kebutuhan. Lalu, saya akan membuat direktori <code>templates</code> pada direktori <code>main</code>. Pada direktori tersebut, saya membuat berkas baru bernama <code>main.html</code> sesuai dengan data yang ingin saya tampilkan di aplikasi web.</li>
</ol>
<p><strong>Implementasi Model Dasar</strong></p>
<ol start="16">
<li>Setelah itu, saya mengonfigurasi <code>models.py</code> pada direktori <code>main</code> untuk mendefinisikan model baru sesuai kebutuhan saya. Attribute-attribute yang saya gunakan untuk proyek saya di antaranya, <code>id</code>, <code>name</code>, <code>price</code>, <code>description</code>, <code>thumbnail</code>, <code>category</code>, <code>is_featured</code>, <code>stock</code>, <code>rating</code>, <code>brand</code>, dan <code>created_at</code>.</li>
</ol>
<p><strong>Migrasi Model</strong></p>
<ol start="17">
<li>Agar Django dapat melacak perubahan pada model basis data saya, saya perlu melakukan migrasi agar struktur tabel basis data saya sesuai dengan perubahan yang telah saya definisikan sebelumnya melalui perintah <code>python manage.py makemigrations</code>. Perintah tersebut akan membuat berkas yang berisi perubahan model yang <strong>belum</strong> diaplikasikan ke dalam basis data. Untuk mengaplikasikan hal tersebut, saya menjalankan perintah <code>python manage.py migrate</code>.</li>
</ol>
<p><strong>Menghubungkan <em>View</em> dengan <em>Template</em></strong></p>
<ol start="18">
<li>Untuk menghubungkan komponen <em>view</em> dengan komponen <em>template</em>, saya perlu mengonfigurasi file <code>views.py</code> dengan mengimpor <code>render</code> dari modul <code>django.shortcuts</code>. Di dalam file ini juga, saya membuat fungsi <code>show_main</code> yang menerima parameter <code>request</code> untuk mengatur permintaan HTTP dari user dan mengembalikan tampilan yang sesuai. Oleh karena itu, <code>render</code> diperlukan agar dapat <code>render</code> tampilan HTML dengan menggunakan data yang saya berikan.</li>
<li>Setelah itu, saya dapat memodifikasi berkas <code>main.html</code> agar dapat menampilkan data yang telah diambil dari <em>model</em> dengan mengubahnya menjadi struktur kode Django yang sesuai untuk menampilkan data dengan format {{ data }}</li>
</ol>
<p><strong>Mengonfigurasi <em>Routing</em> URL</strong></p>
<ol start="20">
<li>Routing URL perlu dilakukan agar Django dapat mengetahui view dan argumen apa yang perlu dijalankan atau diteruskan ketika user membuka URL tertentu. Untuk melakukan hal tersebut, saya perlu mengonfigurasi berkas <code>urls.py</code> yang ada di direktori <code>champions-store</code> dengan mengimpor fungsi <code>include</code> dan menambahkan rute URL yang akan mengarah ke tampilan <code>main</code> di dalam list <code>urlpatterns</code>.</li>
<li>Untuk mengecek apakah routing berhasil, saya perlu menjalankan server terlebih dahulu dengan perintah <code>python manage.py runserver</code>, lalu, membuka [<a href="http://localhost:8000/">http://localhost:8000/</a> di peramban web saya.</li>
</ol>
<p><strong>Django Unit Testing</strong></p>
<ol start="22">
<li>Untuk mengetahui apakah kode yang telah saya buat bekerja sesuai dengan yang saya inginkan, saya perlu melakukan testing agar saya dapat mengecek apakah perubahan yang dilakukan dapat menimbulkan perilaku di luar keinginan saya. Dalam melakukan unit testing, saya perlu mengonfigurasi file <code>tests.py</code> pada direktori <code>main</code> dengan konfigurasi mengikuti panduan.</li>
<li>Setelah itu, saya perlu menjalankan testing dengan perintah <code>python manage.py test</code> dan melihat output yang dihasilkan untuk mengetahui apakah aplikasi web yang telah saya buat berjalan sesuai keinginan.</li>
<li>Setelah melakukan testing, saya <em>push</em> kembali ke repository GitHub saya beserta PWS agar perubahan yang saya lakukan dapat dilihat di URL <em>deployment</em> saya oleh user lain beserta kode programnya.</li>
</ol>
<h2 id="django-request-client">Django Request Client</h2>
<p><img src="https://drive.google.com/file/d/181tQWKWmVFIrM3CRBAeZY2-uogxq6EYM/view?usp=sharing" alt="Bagan.png"></p>

