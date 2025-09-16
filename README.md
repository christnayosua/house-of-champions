---


---

<h2 id="tugas-individu-2">Tugas Individu 2</h2>
<p><em><strong>by Christna Yosua Rotinsulu - 2406495691</strong></em></p>
<p><strong>URL Deployment PWS :</strong><br>
<a href="https://christna-yosua-houseofchampions.pbp.cs.ui.ac.id/">https://christna-yosua-houseofchampions.pbp.cs.ui.ac.id/</a></p>
<h2 id="implementasi-pengembangan-aplikasi-web-menggunakan-django-💻12"><strong>Implementasi Pengembangan Aplikasi Web Menggunakan Django</strong> 💻[1][2]</h2>
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
<li>Pacil Web Service adalah salah satu bentuk layanan <strong>PaaS</strong>, yaitu Platform as a Service, yang disediakan untuk membantu mahasiswa, termasuk saya, dalam melakukan pengembangan, pengelolaan, dan peluncuran aplikasi tanpa perlu mengkhawatirkan infrastruktur dasarnya. Untuk membuat project tersebut, saya perlu membuat akun sesuai dengan <em>SSO UI</em> milik saya. Lalu, saya membuat project baru bernama <em>houseofchampions</em> sesuai dengan tema aplikasi yang saya pilih. Setelah itu, saya perlu menyimpan kredensial yang diberikan sebelum menjalankan instruksi <em><strong>Project Command</strong></em>.  Setelah menyimpan kredensial tersebut, saya pergi ke tab Environs untuk mengonfigurasi <em>environment variables</em> yang telah saya konfigurasi di file <code>.env.prod</code>. Lalu, saya kembali ke proyek Django saya untuk menambahkan URL <em>deployment</em> pada <code>ALLOWED_HOSTS</code> sehingga proyek saya dapat diakses melalui URL <em>deployment</em> PWS tersebut dan dapat dilihat oleh user lain.</li>
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
<h2 id="django-request-client-👤-3">Django Request Client 👤 [3]</h2>
<p><img src="https://www.canva.com/design/DAGyiKER53U/Uamgjs_Id0nyOQUwImMSJA/view?utm_content=DAGyiKER53U&amp;utm_campaign=designshare&amp;utm_medium=link2&amp;utm_source=uniquelinks&amp;utlId=h07a9e4acb9" alt="Bagan Client Request"><br>
<a href="https://www.canva.com/design/DAGyiKER53U/Uamgjs_Id0nyOQUwImMSJA/view?utm_content=DAGyiKER53U&amp;utm_campaign=designshare&amp;utm_medium=link2&amp;utm_source=uniquelinks&amp;utlId=h07a9e4acb9">Bagan Request Client Alternative</a><br>
hubungan antara <code>urls.py</code>, <code>views.py</code>, <code>models.py</code>, dan berkas <code>main.html</code> adalah sebagai berikut. <code>urls.py</code> berperan sebagai router yang memetakan URL ke function view yang sesuai dengan <em>request client</em>. Di sisi lain, <code>views.py</code> berperan untuk menerjemahkan dan mengelola <em>request client</em> lalu akan berinteraksi dengan <code>models.py</code> apabila diperlukan untuk mengakses database. <code>models.py</code> berperan untuk melakukan operasi database dan mendefinisikan struktur data tertentu di mana merepresentasikan tabel di database. Lalu, <code>main.html</code> berperan untuk menampilkan data yang telah diproses dalam format yang <em>user-friendly</em>.</p>
<p>Secara lebih ringkas, <code>urls.py</code> akan memilih <code>views.py</code> dan <code>models.py</code> (<em>apabila diperlukan</em>),  lalu <code>models.py</code> akan memproses database yang ada sesuai kebutuhan dan <em>request client</em>, sedangkan <code>views.py</code> akan melakukan <em>render</em> ke <code>main.html</code>. Lalu, <code>main.html</code> akan dikirim sebagai <code>HTTP response</code>.</p>
<h2 id="peran-setting.py-dalam-django-🎮">Peran <a href="http://setting.py">setting.py</a> Dalam Django 🎮</h2>
<p>Berkas <a href="http://settings.py">settings.py</a> berperan sebagai berkas utama untuk mengontrol berbagai aspek proyek Django. Melalui file ini, saya dapat melakukan berbagai konfigurasi, mulai dari aplikasi, database, <em>middleware</em>, template, <em>Internationalization</em>, security, dan <em>authentication</em>, walaupun saat ini hanya beberapa konfigurasi yang baru diimplementasikan sepenuhnya dalam proyek saya. Sebagai contoh, ketika saya ingin melakukan deployment di Pacil Web Service, saya mendaftarkan URL <em>deployment</em> tersebut pada <code>ALLOWED_HOST</code> sehingga proyek Django saya dapat diakses melalui URL tersebut dan dapat dilihat oleh user lain.</p>
<h2 id="migrasi-database-di-django-📚4">Migrasi Database di Django 📚[4]</h2>
<p>Agar Django dapat melacak perubahan pada model basis data yang dilakukan, hal yang perlu dilakukan adalah melakukan migrasi database tersebut. Jadi, migrasi adalah instruksi untuk mengubah struktur tabel basis data sesuai dengan perubahan model yang didefinisikan dalam kode terbaru. Untuk melakukan migrasi, saya perlu menjalankan perintah <code>python manage.py makemigrations</code>. Apa yang akan dilakukan perintah tersebut? Django awalnya akan membandingkan model versi sekarang dengan versi sebelumnya. Lalu, Django akan membuat file migrasi khusus untuk menjalankan operasi database yang diperlukan dan nanti akan disimpan di berkas <code>migrations</code>. Setelah membuat migrasi, saya perlu menerapkan migrasi tersebut melalui perintah <code>python manage.py migrate</code> yang nantinya akan meminta Django untuk menjalankan operasi database yang tercantum di file migrasi yang tadi telah dibuat. Lalu riwayat migration tadi akan disimpan di tabel <code>django_migrations</code>. Django pun dapat melacak migrasi yang telah dilakukan sehingga mungkin dapat <em>rollback</em> ke versi sebelumnya. Selain itu, Django dapat menangani <em>dependencies</em> antara migrasi dan aplikasi yang berbeda.</p>
<h2 id="alasan-django-dijadikan-permulaan-pembelajaran-😁-5">Alasan Django Dijadikan Permulaan Pembelajaran 😁 [5]</h2>
<ol>
<li>
<p><em><strong>Ridiculously fast.</strong></em><br>
Django membantu <em>developer</em> dalam mengembangkan aplikasi dari konsep hingga siap untuk didistrbusikan secepat mungkin sehingga sangat ramah untuk pengguna yang baru belajar Django.</p>
</li>
<li>
<p><em><strong>Fully Loaded</strong></em><br>
Django menyediakan banyak fitur tambahan yang dapat dimanfaatkan oleh <em>developer</em> sehingga mempermudah pengembangan aplikasi web, terutama dalam menyelesaikan tugas-tugas web umum. Django menangani user authentication, content administration, site maps, RSS feeds, dan sebagainya.</p>
</li>
<li>
<p><strong>Reassuringly secure</strong><br>
Django menganggap serius keamanan dan membantu pengembang menghindari berbagai kesalahan keamanan umum, seperti injeksi SQL, skrip lintas situs, pemalsuan permintaan lintas situs, dan <em>clickjacking</em>. Sistem autentikasi yang telah disediakan untuk membantu pengguna mengelola akun dan kata sandi pengguna dengan aman.</p>
</li>
<li>
<p><strong>Exceedingly scalable</strong><br>
Beberapa situs tersibuk saat ini sebagian besar menggunakan kemampuan Django untuk menyesuaikan skala secara cepat dan fleksibel untuk memenuhi permintaan <em>traffic</em> terberat sebab semakin banyak <em>user</em> maka sumber daya di web tersebut yang ada semakin terkuras.</p>
</li>
<li>
<p><strong>Incredibly versatile</strong><br>
Perusahaan, organisasi, dan pemerintahan telah menggunakan Django untuk membangun segala macam hal — mulai dari sistem manajemen konten hingga jejaring sosial hingga platform komputasi ilmiah.</p>
</li>
</ol>
<h2 id="feedback-👍">Feedback 👍</h2>
<p>Saya sangat menghargai dan mengapresiasi bagaimana asisten dosen membantu saya selama pengerjaan lab dan tugas individu. Selain itu, panduan yang diberikan sangat lengkap, sistematis, dan mudah dipahami sehingga membantu saya dalam memahami materi serta menyelesaikan tugas lab dan individu, terlebih saya baru menggunakan Django untuk pertama kali. 👍</p>
<h2 id="referensi-🔗">Referensi 🔗</h2>
<p>[1] Tim Dosen dan Asisten Dosen PBP 2025 dan 2024. (21 Agustus 2025). <em>Tutorial 1: Pengenalan Aplikasi Django dan  <em>Model-View-Template</em>  (MVT) pada Django</em>. Retrieved from <a href="https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-1">https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-1</a></p>
<p>[2] Tim Dosen dan Asisten Dosen PBP 2025 dan 2024. (27 Agustus 2025). <em>Tutorial 0: Konfigurasi dan Instalasi Git dan Djang</em>. Retrieved from <a href="https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-0">https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-0</a></p>
<p>[3] Django. (n.d.). <em>Request and response objects</em>. Retrieved from <a href="https://docs.djangoproject.com/en/5.2/ref/request-response/">https://docs.djangoproject.com/en/5.2/ref/request-response/</a></p>
<p>[4] Django. (n.d.). <em>Migrations</em>. Retrieved from <a href="https://docs.djangoproject.com/en/5.2/topics/migrations/">https://docs.djangoproject.com/en/5.2/topics/migrations/</a></p>
<p>[5] Django. (n.d.). <em>Why Django?</em>. Retrieved from <a href="https://www.djangoproject.com/start/overview/">https://www.djangoproject.com/start/overview/</a></p>
<h2 id="tugas-individu-3">Tugas Individu 3</h2>
<p><em><strong>by Christna Yosua Rotinsulu - 2406495691</strong></em></p>
<h2 id="peran-krusial-data-delivery-🚚1">Peran Krusial Data Delivery 🚚[1]</h2>
<p><em>data delivery</em> sangat diperlukan sebab platform saat ini umumnya menggunakan arsitektur yang terdistribusi (misal, <strong>client-server</strong>). Oleh sebab itu, pertukaran data antara bagian forntend dan backend harus dilakukan secara sistematis sehingga memastikan ketepatan informasi. Dilansir dari fanruan, berikut adalah alasan kenapa <em>data delivery</em> itu penting, yaitu sebagai berikut:</p>
<ol>
<li><strong>Memastikan Akurasi Data</strong><br>
Data yang akurat akan menjadi tulang punggung setiap proses pengambilan keputusan yang berhasil, terlebih hal ini sangat diperlukan ketika sedang memulai bisnis atau bekerja di sebuah perusahaan. Dari hal tersebut, kita harus memercayai informasi yang akan digunakan.</li>
<li><strong>Deteksi Kesalahan</strong><br>
Kesalahan dalam data dapat terjadi di tahap mana pun sehingga mendeteksi kesalahan sejak dini akan membantu mencegah kesalahan dalam mengambil keputusan. Misal, ketika hasil penjualan item di House Of Champions terdapat kesalahan dalam pendataan, maka kesimpulan hasil penjualan bisa saja sangat meleset, yang harusnya untung menjadi rugi, atau sebaliknya.</li>
<li><strong>Validasi Data</strong><br>
Memastikan data akurat dan valid akan membantu dalam proyek dan keputusan untuk ke depannya. Langkah ini dapat membantu untuk memeriksa kualitas informasi dari sebuah platform sehingga data yang digunakan menjadi lebih andal dan siap untuk dianalisis lebih jauh.</li>
<li><strong>Meningkatkan Pengambilan Keputusan</strong><br>
Penyampaian data tidak hanya</li>
</ol>
<h2 id="kenapa-json-lebih-unggul-🔝2">Kenapa JSON Lebih Unggul? 🔝[2]</h2>
<p>JSON adalah turunan dari JavaScript yang digunakan sebagai alat untuk transfer dan penyimpanan data. Saat ini, bahasa JSON sering digunakan dalam pembuatan aplikasi website. Di sisi lain, XML adalah <em>markup language</em> yang sering digunakan untuk membuat suatu format informasi umum dan nantinya akan digunakan sebagai sarana membagikan format dan data pada halaman www. Lalu, kenapa JSON lebih unggul dan menjadi pilihan <em>developer</em> untuk menyimpan dan transfer data?</p>
<p>JSON memiliki kecepatan <em>parsing</em> yang lebih cepat dibandingkan XML. <em>Parsing</em> sendiri adalah pengenalan bagian terkecil dari sebuah dokumen JSON atau XML. Selain itu, JSON hemat resource dibandingkan XML dalam menyimpan data. Sebab JSON adalah turunan dari JavaScript, struktur data native JavaScript yang disediakan membantu dalam melakukan integrasi. Selain itu, JSON menampilkan data dalam format yang lebih ringkas dan mudah dibaca oleh manusia awam serta mendukung data types secara langsung, seperti <em>number</em>, <em>string</em>, dan <em>boolean</em>, sehingga <em>programmer</em> tingkat mana pun dapat lebih mudah untuk memahami data yang tersimpan dan akan ditransfer.</p>
<h2 id="is_valid-pada-form-django-✅3">is_valid() pada Form Django ✅[3]</h2>
<p>Method <code>is_valid()</code> yang saya gunakan dalam aplikasi web saya mempunyai peran untuk melakukan validasi input terhadap <em>contstraints</em> yang telah didefinisikan sebelumnya (format, required field, dll). Ketika method ini mengembalikan nilai <code>True</code>, maka objek yang akan dibuat dengan data formulir dapat dilakukan dan disimpan setelahnya. Di sisi lain, apabila output yang dikeluarkan adalah<code>False</code>, maka akan memberikan informasi error messages sehingga <em>developer</em> dapat mengetahui <em>field input</em> yang tidak sesuai dengan kriteria. <code>is_valid()</code> tidak hanya berperan sebagai validators saja, tetapi juga sebagai <em>cleaners</em>. Peran tersebut membantu <em>developer</em> untuk mencegah data yang tidak sesuai masuk ke dalam database sehingga melindungi sistem dari potensi <em>security vulnerabilities</em>.</p>
<h2 id="kebutuhan-csrf_token-dalam-form-django🥷🧑‍💻4">Kebutuhan csrf_token dalam Form Django🥷🧑‍💻[4]</h2>
<p>CSRF atau <em>Cross-Site Request Forgery</em> adalah sebuah token yang diperlukan untuk mencegah serangan CSRF di mana penyerang akan memanipulasi <em>suspect</em> untuk menjalankan aksi yang tidak diinginkan sehingga token unik perlud= dibuat untuk setiap <em>session user</em> yang nantinya akan divalidasi oleh server.</p>
<p>Lalu, apa bahayanya apabila tidak menggunakan CSRF token?  Seperti yang sudah dijelaskan, CSRF berperan untuk mencegah serangan CSRF sehingga apabila tidak menggunakan CSRF token, penyerang dapat membuat <em>request</em> palsu untuk menggunakan identitas korban, memanipulasi data tanpa persetujuan <em>user</em>, atau mengeksploitasi aksi privileged, seperti transfer dana (misal, top-up game) atau ubah password.</p>
<p>Bagaimana penyerang melakukan serangan CSRF? Penyerang umumnya akan membuat link/form jahat dan mengelabui korban untuk mengkliknya ketika korban melakukan login ke aplikasi target sehingga biasanya penyerang akan membuat konten menarik yang dapat mengundang korban untuk masuk ke perangkapnya. Lalu, ketika korban mengklik link/form tersebut, sebuah <em>request</em> baru akan dikirim ke pihak server dengan kredensial korban yang aktif dan tentu server berkemungkinan akan memvalidasi serta menjalankan *request *tersebut. Setelah pihak server menyetujui dan memproses <em>request</em> tersebut, maka di saat itulah penyerang akan melakukan operasi pencurian identitas atau hal lainnya sebab server tidak dapat membedakan <em>request</em> tersebut apakah <em>legitimate</em> atau <em>malicious</em>.</p>
<h2 id="checklist-step-by-step">Checklist Step-By-Step</h2>
<p>Berikut adalah checklist yang saya lakukan dalam melakukan dan menyelesaikan tugas individu 3 :</p>
<h3> Implementasi Skeleton Sebagai Kerangka Views</h3> <hr>
<ol>
<li><strong>Membuat base.html</strong><br>
Pada <em>root folder</em>, saya membuat sebuah direktori baru bernama <code>templates</code> yang berisi file <code>base.html</code> yang akan menjadi <em>template</em> dasar yang digunakan sebagai kerangka umum untuk halaman lainnya di dalam proyek saya. Dalam <em>template</em> ini terdapat block <code>{% block %}</code> untuk mendefinisikan area dalam template yang dapat diganti oleh template turunannya. Template turunan tersebut akan me-<em>extend</em> template dasar dan mengganti konten di dalam block ini sesuai dengan kebutuhan saya.</li>
<li>Setelah membuat kerangka umum tersebut, saya perlu mengonfigurasi <code>settings.py</code> agar <code>base.html</code> yang telah dibuat dapat terdeteksi sebagai berkas template. Lalu, pada subdirektori <code>templates</code>, saya melakukan modifikasi untuk menampilkan attribute yang telah saya definisikan pada berkas <code>views.py</code>.</li>
</ol>
<h3> Form Input Data dan Menampilkan Data pada HTML </h3><hr>
<ol start="3">
<li>Setelah membuat kerangka umum dan berbagai konfigurasi yang dilakukan, saya melanjutkan tahap saya berikutnya, yaitu membuat sebuah <em>form</em> yang menjadi <em>field input</em> data pada <em>House-Of-Champions</em> pada aplikasi web saya sehingga nantinya saya dapat menambahkan data baru untuk ditampilkan di halaman utama web. Saya perlu membuat berkas baru, yaitu <code>forms.py</code> untuk membuat struktur <em>form</em> yang dapat menerima data <em>Items</em> baru. <em>Fields input</em> yang saya gunakan untuk penambahan data, antara lain <em>name, description, category, thumbnail, is_feautured, price, stock, rating, dan brand</em> sesuai dengan <em>attribute</em> yang telah saya definisikan di berkas <code>models.py</code>.</li>
<li>Lalu, saya melakukan konfigurasi pada berkas <code>views.py</code> untuk mengimpor modul-modul yang diperlukan dan membuat <em>functions</em> yang akan membuat dan menampilkan item yang akan dibuat oleh <em>user</em>. <code>create_items</code> bertujuan untuk membuat item yang akan ditambahkan dan disimpan dalam database di mana <em>function</em> ini akan mendeteksi apakah form yang diajukan valid dan <em>request</em> yang dikirimkan adalah <code>"POST"</code>. Apabila kedua kriteria tersebut terpenuhi, maka objek <code>item</code> baru akan dibuat dan disimpan. Di sisi lain, <code>show_items</code> berperan untuk menampilkan objek <code>item</code> yang telah dibuat sebelumnya dan menaikkan jumlah <em>visitors</em> setiap kali <em>user</em> mengunjungi item yang terdaftar.</li>
<li>Setelah membuat konfigurasi tersebut, saya perlu menambahkan <em>path</em> URL ke variable <code>urlpatterns</code> di berkas <code>urls.py</code> agar dapat menuju ke tampilan halaman yang sesuai.</li>
<li>Pada berkas <code>main.html</code>, saya membuat tambahan tampilan untuk menampilkan list yang berisi objek <code>item</code> yang telah dibuat dan disimpan. Informasi yang ditampilkan akan membantu mengundang perhatian <em>calon pembeli</em> serta memberikan rekomendasi <em>item</em> sesuai dengan rating dan jumlah pembeli item tersebut (belum ditambahkan).</li>
<li>Selain berkas <code>main.html</code>, saya membuat dua berkas baru pada direktori yang sama untuk halaman form input dan detail item yang dijual, yaitu <code>create_items.html</code> dan <code>items_detail.html</code>. Pada berkas <code>create_items.html</code>, saya menambahkan block <code>{% csrf_token %}</code> yang bertindak sebagai <em>security</em> agar <em>user</em> tidak terserang serangan CSRF. Di sisi lain, terdapat block <code>{{% form.as_table %}}</code> yang menjadi <em>template tag</em> untuk menampilkan <em>fields</em> form yang sudah dibuat pada berkas <code>forms.py</code> sebagai <code>table</code>.</li>
<li>Setelah itu, saya melakukan konfigurasi pada berkas <code>settings.py</code> untuk menambahkan URL <em>deployment</em> aplikasi web saya pada <em>attribute</em> <code>CSRF_TRUSTED_ORIGINS</code> agar hanya melalui token tersebut, data dan <em>request</em> yang dikirimkan diterima oleh aplikasi web.</li>
</ol>
<h3>Mengembalikan Data dalam Bentuk XML dan JSON</h3><hr>
<ol start="9">
<li>Setelah membuat form input data dan menampilkannya, saya akan mengembalikan data yang tersimpan dalam bentuk XML dan JSON untuk kebutuhan analisis ke depannya. Pada file <code>views.py</code>,  saya mengimpor modul <code>HttpResponse</code> dan <code>Serializer</code> untuk menyusun respon yang ingin dikembalikan oleh <em>server</em> kepada <em>user</em>.</li>
<li>Lalu, saya membuat <em>function</em> baru untuk menerima parameter <em>request</em> dengan nama <code>show_xml</code> dan <code>show_json</code> dan membuat variabel <code>items_list</code> yang menyimpan hasil <em>query</em> dari seluruh data pada <code>Items</code>.  Setelah itu, <em>function</em> tersebut akan me-<em>return</em> HTTPResponse dengan parameter hasil <em>query</em> yang sudah diserialisasi dalam bentuk XML atau JSON dan parameter <code>content_type="application/xml"</code>. Setelah itu, saya menambahkan <em>path url</em> ke dalam <code>urlpatterns</code> untuk mengakses <em>function</em> yang sudah diimpor tadi.</li>
</ol>
<h3>Mengembalikan Data Berdasarkan ID dalam bentuk XML dan JSON</h3><hr>
<ol start="11">
<li>Setelah selesai dapat mengembalikan data dalam bentuk XML dan JSON, saya membuat <em>function</em> baru untuk mengembalikan data yang tersimpan dalam <em>query</em> berdasarkan ID. Pertama, saya membuat dua <em>function</em> baru yang menerima parameter <code>request</code> dan <code>items_id</code>, yaitu <code>show_xml_by_id</code> dan <code>show_json_by_id</code> di mana di dalam kedua <em>function</em> tersebut terdapat variabel <code>items_list</code> yang menyimpan hasil <em>query</em> dari data dengan id tertentu.</li>
<li>Lalu, saya menambahkan <em>return function</em> berupa <code>HttpResponse</code> yang menerima parameter data hasil <em>query</em> yang sudah diserialisasi menjadi JSON atau XML dan parameter <code>content_type</code> dengan <em>value</em> <code>"application/xml"</code> atau <code>"application/json"</code>. Pada <em>function</em> tersebut, saya juga menambahkan block <code>try except</code> untuk mengantisipasi kondisi ketika data dengan <code>items_id</code> tertentu ternyata tidak ditemukan dalam basis data di mana akan mengembalikan <code>HttpResponse</code> dengan status 404 sebagai tanda bahwa data tersebut tidak ada.</li>
<li>Setelah itu, saya menambahkan <em>path url</em> pada berkas <code>urls.py</code> untuk mengimpor fungsi yang sudah ada dan menambahkan akses fungsi yang sudah dibuat tadi.</li>
</ol>

