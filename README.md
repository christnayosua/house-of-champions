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
Penyampaian data tidak hanya terbatas pada keakuratan data yang didapatkan, tetapi juga bagaimana <em>impact</em> yang diberikan data tersebut mampu membuat keputusan yang lebih baik.</li>
<li><strong>Akses Data Tepat Waktu</strong><br>
Memiliki akses ke data kapan pun yang kita butuhkan sangatlah penting sehingga dapat menyesuaikan permintaan atau <em>feedback</em> dari <em>user</em> atau <em>client</em>. Hal tersebut memampukan kita, sebagai <em>developer</em> untuk merespons lebih cepat terhadap perubahan sehingga dapat unggul dibandingkan pesaing.</li>
<li><strong>Wawasan Berbasis Data</strong><br>
Wawasan dalam berbasis data akan memampukan <em>developer</em> untuk menyimpan data dengan cara yang lebih efektif dan efisien. Hal ini akan mengoptimalkan strategi untuk ke depannya dan mencapai hasil yang lebih baik.</li>
</ol>
<p>Berdasarkan hal tersebut, <em>data delivery</em> berperan sebagai mekanisme yang memastikan pertukaran informasi antara berbagai komponen sistem berjalan lebih efektif. <em>Centralized</em> data platform tersebut memungkinkan penyimpanan, pengelolaan, dan pengiriman data dalam volume besar, baik terstruktur maupun tidak terstruktur. Platform seperti inilah yang akan memberikan infrastruktur untuk menyimpan dan memproses data dari berbagai sumber secara <em>seamless</em> yang sangat krusial dalam lingkungan bisnis modern di mana data menjadi aset strategis yang tak ternilai pada saat ini.</p>
<h2 id="kenapa-json-lebih-unggul-🔝2">Kenapa JSON Lebih Unggul? 🔝[2]</h2>
<p>JSON adalah turunan dari JavaScript yang digunakan sebagai alat untuk transfer dan penyimpanan data. Saat ini, bahasa JSON sering digunakan dalam pembuatan aplikasi website. Di sisi lain, XML adalah <em>markup language</em> yang sering digunakan untuk membuat suatu format informasi umum dan nantinya akan digunakan sebagai sarana membagikan format dan data pada halaman www. Lalu, kenapa JSON lebih unggul dan menjadi pilihan <em>developer</em> untuk menyimpan dan transfer data?</p>
<p>JSON memiliki kecepatan <em>parsing</em> yang lebih cepat dibandingkan XML. <em>Parsing</em> sendiri adalah pengenalan bagian terkecil dari sebuah dokumen JSON atau XML. Selain itu, JSON hemat resource dibandingkan XML dalam menyimpan data. Sebab JSON adalah turunan dari JavaScript, struktur data native JavaScript yang disediakan membantu dalam melakukan integrasi. Selain itu, JSON menampilkan data dalam format yang lebih ringkas dan mudah dibaca oleh manusia awam serta mendukung data types secara langsung, seperti <em>number</em>, <em>string</em>, dan <em>boolean</em>, sehingga <em>programmer</em> tingkat mana pun dapat lebih mudah untuk memahami data yang tersimpan dan akan ditransfer.</p>
<h2 id="is_valid-pada-form-django-✅3">is_valid() pada Form Django ✅[3]</h2>
<p>Method <code>is_valid()</code> yang saya gunakan dalam aplikasi web saya mempunyai peran untuk melakukan validasi input terhadap <em>contstraints</em> yang telah didefinisikan sebelumnya (format, required field, dll). Ketika method ini mengembalikan nilai <code>True</code>, maka objek yang akan dibuat dengan data formulir dapat dilakukan dan disimpan setelahnya. Di sisi lain, apabila output yang dikeluarkan adalah<code>False</code>, maka akan memberikan informasi error messages sehingga <em>developer</em> dapat mengetahui <em>field input</em> yang tidak sesuai dengan kriteria. <code>is_valid()</code> tidak hanya berperan sebagai validators saja, tetapi juga sebagai <em>cleaners</em>. Peran tersebut membantu <em>developer</em> untuk mencegah data yang tidak sesuai masuk ke dalam database sehingga melindungi sistem dari potensi <em>security vulnerabilities</em>.</p>
<h2 id="kebutuhan-csrf_token-dalam-form-django🥷🧑‍💻4">Kebutuhan csrf_token dalam Form Django🥷🧑‍💻[4]</h2>
<p>CSRF atau <em>Cross-Site Request Forgery</em> adalah sebuah token yang diperlukan untuk mencegah serangan CSRF di mana penyerang akan memanipulasi <em>suspect</em> untuk menjalankan aksi yang tidak diinginkan sehingga token unik perlud= dibuat untuk setiap <em>session user</em> yang nantinya akan divalidasi oleh server.</p>
<p>Lalu, apa bahayanya apabila tidak menggunakan CSRF token?  Seperti yang sudah dijelaskan, CSRF berperan untuk mencegah serangan CSRF sehingga apabila tidak menggunakan CSRF token, penyerang dapat membuat <em>request</em> palsu untuk menggunakan identitas korban, memanipulasi data tanpa persetujuan <em>user</em>, atau mengeksploitasi aksi privileged, seperti transfer dana (misal, top-up game) atau ubah password.</p>
<p>Bagaimana penyerang melakukan serangan CSRF? Penyerang umumnya akan membuat link/form jahat dan mengelabui korban untuk mengkliknya ketika korban melakukan login ke aplikasi target sehingga biasanya penyerang akan membuat konten menarik yang dapat mengundang korban untuk masuk ke perangkapnya. Lalu, ketika korban mengklik link/form tersebut, sebuah <em>request</em> baru akan dikirim ke pihak server dengan kredensial korban yang aktif dan tentu server berkemungkinan akan memvalidasi serta menjalankan *request *tersebut. Setelah pihak server menyetujui dan memproses <em>request</em> tersebut, maka di saat itulah penyerang akan melakukan operasi pencurian identitas atau hal lainnya sebab server tidak dapat membedakan <em>request</em> tersebut apakah <em>legitimate</em> atau <em>malicious</em>.</p>
<h2 id="checklist-step-by-step-🎯-5">Checklist Step-By-Step 🎯 [5]</h2>
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
<h3>Push ke PWS dan GitHub</h3><hr>
<ol start="14">
<li>Setelah selesai untuk mengembalikan data dalam bentuk XML dan JSON, saya melakukan push ke GitHub dan PWS agar perubahan yang saya lakukan dapat tersimpan dan terlihat di URL <em>deployment</em> saya.</li>
</ol>
<h2 id="feedback-untuk-tutorial-2-👍">Feedback untuk Tutorial 2 👍</h2>
<p>Asdos sangat membantu saya untuk memahami dan mengerjakan tutorial 2 kemarin melalui panduan dan komunikasi melalui <em>Discord</em>. Selain itu, penjelasan-penjelasan bagian yang harus dikonfigurasi dan ditambahkan turut disertai penjelasan sehingga saya tidak hanya mengimplementasikan saja, tetapi juga memahami maksud dari hal tersebut. Dari hal tersebutlah, saya dapat mengerjakan tugas individu 3 dengan lebih mudah terutama jawaban-jawabannya sudah disediakan pada panduan tutorial 2 kemarin. Saya berharap agar hal ini terus konsisten terjadi untuk ke depannya. Great Job, kakak Asdos 💓!</p>
<h2 id="screenshot-hasil-akses-url-pada-postman-🔗">Screenshot Hasil Akses URL pada Postman 🔗</h2>
<h3>XML</h3>
<p><img src="https://drive.google.com/file/d/1AK5E92Usf5qrHREjBmvNRYrhTAz65c07/view?usp=sharing" alt="XML"><br>
<a href="https://drive.google.com/file/d/1AK5E92Usf5qrHREjBmvNRYrhTAz65c07/view?usp=sharing">Link Alternatif - XML</a></p>
<h3>JSON</h3>
<p><img src="https://drive.google.com/file/d/1J1xealYy1xaZobEFIv8eHIesyhQN2Sl-/view?usp=sharing" alt="JSON"><br>
<a href="https://drive.google.com/file/d/1J1xealYy1xaZobEFIv8eHIesyhQN2Sl-/view?usp=sharing">Link Alternatif - JSON</a></p>
<h3>XML by ID</h3>
<p><img src="https://drive.google.com/file/d/1lchB-xxdxK1Ez-ygXanylS6KiuGI2mik/view?usp=sharing" alt="XML by ID"><br>
<a href="https://drive.google.com/file/d/1lchB-xxdxK1Ez-ygXanylS6KiuGI2mik/view?usp=sharing">Link Alternatif - XML by ID</a></p>
<h3>JSON by ID</h3>
<p><img src="https://drive.google.com/file/d/1NmxHzjtEGwWF7LDSee7fse21lJOtEnd-/view?usp=sharing" alt="JSON by ID"><br>
<a href="https://drive.google.com/file/d/1NmxHzjtEGwWF7LDSee7fse21lJOtEnd-/view?usp=sharing">Link Alternatif - JSON by ID</a></p>
<h2 id="referensi-🔎">Referensi 🔎</h2>
<p>[1] Sean. (2024, 23 October). <em>Data Delivery</em>. Retrieved from <a href="https://www.fanruan.com/en/glossary/big-data/data-delivery">https://www.fanruan.com/en/glossary/big-data/data-delivery</a><br>
[2] Binar. (n.d.). <em>JSON: Pengertian, Fungsi, Jenis-Jenis, Kelebihan dan Kekurangannya</em>. Retrieved from <a href="https://www.binar.co.id/blog/json-adalah">https://www.binar.co.id/blog/json-adalah</a><br>
[3] Ansel, J. (2022, Juny 1). <em>Working with Django Model Forms</em>. Retrieved from <a href="https://medium.com/@jansel358/working-with-django-model-forms-77afe017e2cc">https://medium.com/@jansel358/working-with-django-model-forms-77afe017e2cc</a><br>
[4] Django Documentation. (n.d.). <em>How to Use Django’s CSRF Protection</em>. Retrieved from <a href="https://docs.djangoproject.com/id/5.2/howto/csrf/">https://docs.djangoproject.com/id/5.2/howto/csrf/</a><br>
[5] Tim Dosen dan Asisten Dosen PBP 2024-2025. (2025, August 27). <em>Tutorial 2 : Form dan Data Delivery</em>. Retrieved from  <a href="https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-2#tutorial-implementasi-skeleton-sebagai-kerangka-views">https://pbp-fasilkom-ui.github.io/ganjil-2026/docs/tutorial-2#tutorial-implementasi-skeleton-sebagai-kerangka-views</a></p>
<h2 id="tugas-individu-4">Tugas Individu 4</h2>
<p><em><strong>by Christna Yosua Rotinsulu-2406495691</strong></em></p>
<h3>Django's AuthenticationForm</h3>
<hr>
<p><code>AuthenticationForm</code> adalah form bawaan dari Django yang disediakan untuk mengautentikasi <em>user</em>. <code>AuthenticationForm</code> dapat diimport dari library <code>django.contrib.auth.forms</code>. Form ini nantinya akan memvalidasi username dan password yang dimasukkan pada halaman login terhadap database pengguna. Apabila ditemukan kecocokan/validasi sukses, maka Django akan mengembalikan objek <code>User</code> yang sesuai melalui method <code>get_user()</code>.</p>
<p>Lalu, apa kelebihan dan kekurangan dari <code>AuthenticationForm</code> pada Django? Berikut adalah kelebihan dan kekurangan dari form tersebut:</p>
<p><strong>Kelebihan</strong></p>
<ol>
<li>Sudah terintegrasi dengan sistem autentikasi Django (backends, <code>login()/logout()</code>)</li>
<li>Dapat melakukan validasi secara otomatis, tanpa perlu didefinisikan oleh <em>developer</em> (<em>Ready-to-use)</em></li>
<li>Mudah untuk dikustomisasi sesuai kebutuhan (<em>subclass atau override fields/label</em>)</li>
<li>Mendukung <em>error handling</em> bawaan (ex. kredensial tidak valid)</li>
<li>Terintegrasi dengan sistem <em>permissions</em> Django</li>
</ol>
<p><strong>Kekurangan</strong></p>
<ol>
<li>Masih terbatas pada autentikasi username/password standar sehingga perlu kustomisasi apabila ingin login via email (protokol keamanan lebih ketat)</li>
<li>Perlu penyesuaian lebih lanjut untuk kebutuhan kustom yang lebih kompleks, seperti membuat custom backend atau form apabila ada kebutuhan logic autentikasi khusus, seperti SSO.</li>
<li>Tampilan default perlu disesuaikan dengan desain aplikasi sehingga perlu styling dan i18n</li>
<li>Tidak otomatis menangani fitur lanjutan (2FA, <em>rate-limiting</em>, <em>captcha</em>, dan <em>account lockout</em>)</li>
</ol>
<h3>Autentikasi vs Otorisasi: Butuh Keduanya atau Salah Satu?</h3>
<hr>
<p><strong>Autentikasi</strong> atau <em>authentication</em> adalah proses memverifikasi identitas, seperti <em>username, password, token, 2FA, dsb</em>. <strong>Autentikasi</strong> sama halnya dengan pertanyaan <em>siapa kamu?</em> Melalui <em>authentication</em>, <em>server-side</em> mengetahui <em>user</em> mana yang sedang berinteraksi atau dia seorang anonim.</p>
<p>Di sisi lain, <strong>otorisasi</strong> atau <em>authorization</em> adalah proses memeriksa hak akses/izin, seperti <em>permissions</em>, <em>roles</em>, atau <em>groups</em>. <strong>Otorisasi</strong> sama halnya dengan pertanyaan <em>apa yang boleh kamu lakukan?</em> <strong>Otorisasi</strong> dilakukan setelah <strong>autentikasi</strong> sehingga setelah mengetahui <em>siapa dia</em>, <em>server-side</em> dapat mengetahui hak akses yang dimiliki <em>user</em> tersebut, seperti membaca/mengubah/menjalankan aksi tertentu.</p>
<p>Lalu, bagaimana cara Django mengimplementasikan kedua hal tersebut?</p>
<ul>
<li><strong>Autentikasi</strong></li>
</ul>
<ol>
<li>Django, menyediakan model <code>User</code> yang dapat diimport dari <code>django.contrib.auth.models.User</code> yang berfungsi untuk menyimpan identitas <em>user</em> dalam sebuah model/objek. Selain itu, data <em>user</em> juga dapat disimpan melalui custom user via <code>AUTH_USER_MODEL</code>.</li>
<li>Django juga menyediakan function <code>authenticate()</code> untuk memeriksa kredensial milik <em>user</em> melalui <em>authentication backends</em> (<code>AUTHENTICATION_BACKENDS)</code> untuk bisa menambahkan backend custom, seperti login via email, LDAP, OAuth, SSO, dsb. Apabila ditemukan kecocokan/tervalidasi, maka Django akan mengembalikan objek <code>User</code> tersebut.</li>
<li>Django sendiri saat ini sudah menyediakan sistem password hashing secara otomatis sehingga protokol keamanannya menjadi lebih ketat dan sulit diserang <em>attacker</em>.</li>
<li>Untuk menyimpan <em>session</em> ID <em>user</em> ke cookie dan menandai bahwa user terautentikasi, Django menyediakan function <code>login(request, user)</code>. Hal ini akan membantu <em>user</em> agar state selama sesi interaksi dengan aplikasi web dapat terjaga sehingga tidak perlu melakukan prosedur login kembali, walaupun cukup beresiko jika tidak dilindungi.</li>
<li>Django juga menyediakan beberapa tools bawaan juga, seperti <code>AuthenticationForm</code>, <code>LoginView</code>, <code>LogoutView</code>, password hashing yang tadi sudah dijelaskan, dan password reset flows.</li>
</ol>
<ul>
<li><strong>Otorisasi</strong><br>
Django, dalam hal otorisasi, menawarkan beberapa lapisan kontrol akses berupa dekorator, seperti <code>@login_required</code> (<em>yang digunakan dalam tutorial</em>) yang akan membatasi akses berdasarkan status login, <code>@permission_required</code> untuk izin akses yang lebih spesifik, dan pengecekan langsung di kode melalui <code>user.has_perm()</code>. Sistem otorisasi ini turut diperkuat dengan pembagian peran yang terstruktur dan hierarkis yang terdiri dari <em>superuser</em>, <em>staff</em>, dan <em>regular user</em> dan manajemen <em>group permission</em> di mana semua proses akan dilakukan setelah identitas <em>user</em> terautentikasi yang akan menciptakan alur keamanan yang berlapis dan sistematis.</li>
</ul>
<h3>Session vs Cookies: Penyimpan Jejak di Aplikasi Web</h3>
<p><strong>Session</strong> atau <em>Penyimpanan Server-Side</em> adalah mekanisme untuk menyimpan data setiap <em>user</em> di antara <em>request</em> HTTP yang bersifat <em>stateless</em> sehingga <em>client</em> hanya menerima sessionid saja. Di sisi lain, <strong>cookie</strong> adalah penyimpanan <em>client-side</em> dalam bentuk file kecil berupa data yang disimpan di browser <em>user</em> atas permintaan website.</p>
<p>Lalu, apa kelebihan dan kekurangan dari <code>session</code> dan <code>cookies</code>?</p>
<ul>
<li>✅<strong>Kelebihan Cookies</strong></li>
</ul>
<ol>
<li><strong>Ringan untuk Server</strong>: cookies tidak butuh storage di sisi server sebab semua data disimpan di browser <em>user</em>. Hal tersebut menyebabkan server tetap <em>stateless</em> sehingga lebih mudah diskalakan, terutama pada arsitektur <em>microservices</em> yang mengutamakan kemandirian antar layanan.</li>
<li><strong>Performa Tinggi</strong>: server tidak perlu melakukan <em>lookup</em> ke database atau chace untuk mencari data <em>user</em> sebab sudah tersedia langsung di setiap <em>request</em> yang dilakukan. Hal ini tentu akan mengurangi latensi dan meningkatkan performa aplikasi, terutama untuk data kecil yang sering diakses.</li>
<li><strong>Persistensi Data</strong>: cookies dapat memiliki waktu kadaluwarsa yang panjang sehingga data tetap dapat tersimpan meskipun browser ditutup oleh <em>user</em>. Hal ini akan memungkinkan pengguna untuk kembali ke state atau preferensi sebelumnya tanpa perlu mengatur ulang, seperti login.</li>
<li><strong>Simplicity</strong>: cookies sangat mudah diimplementasikan karena sudah didukung secara <em>built-in</em> oleh semua browser sehingga <em>developer</em> tidak perlu mengonfigurasi atau setup tambahan yang kompleks untuk dimanfaatkan.</li>
<li><strong>Client Independence</strong>: setiap client tentu dapat menyimpan state-nya masing-masing di browser sehingga tidak ada penggunaan <em>resource</em> secara bersamaan di server. Hal ini akan mengurangi risiko <em>bottleneck</em> pada penyimpanan di sisi server.</li>
</ol>
<hr>
<ul>
<li>👎<strong>Kekurangan Cookies</strong></li>
</ul>
<ol>
<li><strong>Keamanan Rendah</strong>: cookies memungkinkan <em>user</em> untuk memanipulasi data sebab berada di sisi browser. Selain itu, cookies sangat rentan terhadap serangan, seperti XSS (<em>Cross-Site Scripting</em>) dan CSRF (<em>Cross-Site Request Forgery</em>) jika tidak dikonfigurasi dengan benar oleh <em>developer</em>.</li>
<li><strong>Ukuran Terbatas</strong>: cookies umumnya hanya mampu menyimpan sekitar 4KB per cookie dan biasanya hanya 20 cookie per domain yang didukung (tergantung browser). Hal tersebut tentu tidak cocok digunakan jika digunakan untuk menyimpan data yang lebih besar dan kompleks.</li>
<li><strong>Privacy Concerns</strong>: cookies umumnya sering digunakan untuk melacak perilaku pengguna, misalnya oleh iklan atau layanan pihak ketiga. Dari hal tersebut, regulasi seperti GDPR mewajibkan adanya persetujuan pengguna sebelum menyimpan cookies (biasanya akan muncul pop-up). Akan tetapi, sebagian pengguna, termasuk saya, sering memilih untuk memblokir cookies karena alasan privasi.</li>
<li><strong>Data Exposure</strong>: isi dari cookies dapat dilihat dengan mudah melalui <em>developer</em> tools yang ada di browser sehingga sangat beresiko apabila menyimpan data sensitif. Berdasarkan hal tersebut, cookies tidak menjadi pilihan utama untuk menyimpan informasi penting, seperti password atau data-data finansial.</li>
<li><strong>Dependency on Client</strong>: cookies sangat bergantung pada browser client, tetapi <em>user</em> bisa saja menonaktifkan cookies, dan perilaku cookies di setiap browser maupun perangkat mobile pun bisa berbeda-beda. Hal ini akan menimbulkan keterbatasan dan inkonsistensi dalam pengalaman pengguna untuk ke depannya.</li>
</ol>
<hr>
<ul>
<li>✅<strong>Kelebihan Session</strong></li>
</ul>
<ol>
<li><strong>Keamanan Tinggi</strong>: berbeda dengan cookies, session menyimpan data di server sehingga <em>client</em> tidak dapat langsung memanipulasinya sebab hanya <em>session ID</em> yang dikirimkan ke browser. Hal tersebut akan mengurangi resiko manipulasi dan eksposur data secara langsung.</li>
<li><strong>Kapasitas Besar dan Tidak Terbatas</strong>: seesion dapat menampung objek yang lebih kompleks, seperti array, atau data yang relatif besar dan kompleks tanpa batasan ukuran ketat seperti cookie yang umumnya hanya bisa menampung sekitar 4KB untuk setiap cookie. Hal ini memungkinkan untuk menyimpan profil pengguna, preferensi, isi keranjang belanja, atau struktur data yang lebih kompleks.</li>
<li><strong>Kontrol Penuh oleh Server</strong>: session hanya bisa dikelola di sisi server sehingga administrator atau aplikasi mempunyai hak akses tinggi, seperti mengahapus/invalidasi sesi kapan saja, mengatur timeout, dan menerapkan kebijakan pengelola sesi yang lebih terpadu. Hal ini akan memudahkan protokol keamanan dan manajemen <em>lifecycle</em> sesi untuk semua klien.</li>
<li><strong>Privacy Better</strong>: data pengguna yang disimpan di sisi server membantu mengurangi eksposur pada perangkat pengguna dan memudahkan kepatuhan terhadap regulasi privasi, seperti GDPR/CCPA. Hal ini akan mengurangi potensi kebocoran data melalui perangkat klien.</li>
<li><strong>Reliability</strong>: session tidak bergantung pada pengaturan browser milik klien sehingga <em>user</em> tidak bisa menonaktifkan session seperti cookie. Hal ini tentu akan meingkatkan reliabilitas mekanisme state karena server tetap mampu mempertahankan state meski ada variasi perilaku browser.</li>
</ol>
<hr> 
<ul>
<li><strong>👎Kekurangan Session</strong></li>
</ul>
<ol>
<li><strong>Beban Server</strong>: session memerlukan ruang penyimpanan dan sumber daya lebih pada server terlebih sistem dengan banyak pengguna simultan, storgae dan I/O akan mempengaruhi performa aplikasi. Hal ini tentu memerlukan mekanisme <em>cleanup</em> untuk sesi-sesi yang sudah kedaluwarsa agar tidak menumpuk di server.</li>
<li><strong>Scalability Issues</strong>: berbeda dengan cookie, session yang tersimpan di lokal suatu server akan menyebabkan inkonsistensi jika <em>request</em> yang di-post diarahkan ke server lain pada <em>environment</em> yang menggunakan <em>load balancer</em> dan banyak <em>instance</em> aplikasi. Hal tersebut membutuhkan <em>shared storage</em> atau <em>distributed chace</em> sehingga menambah kompleksitas infrastruktur.</li>
<li><strong>Complexity</strong>: konfigurasi session biasanya lebih kompleks dibandingkan cookies sehingga membutuhkan pengaturan backend, seperti database atau chace, strategi eviction, backup/replikasi, dan kadang pengaturan keamanan tambahan. Hal ini akan menambah beban pengembangan dan operasional dibanding solusi <em>client-only</em>.</li>
<li><strong>Statefulness</strong>: session membuat server menjadi stateful yang bertentangan dengan prinsip <em>RESTful</em> yang mengutamakan <em>statelessness</em>. Hal ini akan membuat layanan yang sepenuhnya <em>stateless</em> atau <em>microservice</em> yang mudah diskalakan menjadi lebih menantang tanpa arsitektur tambahan.</li>
</ol>
<h3>Data Aman, Hati Tenang: Strategi Django dalam Mengendalikan Cookies</h3> 
<hr>
<p>Penggunaan cookies, secara <em>default</em>, tidak aman digunakan dalam pengembangan aplikasi web. Hal ini disebabkan oleh risiko keamanan yang dapat ditimbulkan dari penggunaan cookies tanpa konfigurasi keamanan lebih lanjut. Berikut adalah beberapa serangan yang berpontesi terjadi pada penggunaan cookies:</p>
<ol>
<li><strong>Cross-Site Scripting (XSS)</strong>: <em>attacker</em> akan mencuri cookies melalui kode JavaScript “jahat”. Hal ini memungkinkan <em>attacker</em> untuk mencuri data-data sensitif yang tersimpan di browser, seperti session ID, melalui manipulasi DOM atau akses langsung ke document.cookie.</li>
<li><strong>Cross-Site Request Forgery (CSRF)</strong>: <em>attacker</em> akan melakukan manipulasi cookies untuk melakukan aksi yang tidak sah atas nama <em>user</em> di mana korban akan membujuk pengguna yang sudah login untuk mengunjungi situs-situs “perangkap” yang mengirim <em>request</em> tertenu ke aplikasi web target. Dari hal tersebut, perubahan data dapat terjadi tanpa sepengetahuan <em>user</em>.</li>
<li><strong>Session Hijacking</strong>: <em>attacker</em> akan mencuri session ID <em>user</em> untuk menyamar sebagai pengguna yang sah. Hal ini tentu akan mengakibatkan akses tidak sah ke akun pengguna.</li>
<li><strong>Data Tempering</strong>: cookies yang disimpan di client-side dan dapat dimodifikasi melalui browser developer tools, terlebih data yang tidak divalidasi dengan baik di sisi server, seperti ID pengguna, dapat dimanipulasi oleh <em>attacker</em> untuk mendapatkan keuntungan secara ilegal atau akses yang tidak terotorisasi.</li>
</ol>
<p>Lalu, bagaimana peran Django dalam menghadapi hal tersebut?</p>
<p><strong>Django</strong> secara proaktif akan menangani risiko keamanan cookies tersebut melalui berbagai mekanisme <em>built-in</em> yang dilakukan secara <em>layered</em>, dimulai dengan proteksi CSRF yang otomatis disertakan token unik pada setiap form untuk mencegah serangan CSRF, pengaturan secure flags pada cookies (<em>HttpOnly, Secure, and SameSite</em>) yang akan membatasi akses JavaScript dan memastikan transmisi data hanya dapat dilakukan melalui HTTPS, serta sistem session management yang akan membantu penyimpanan data-data yang sensitif di <em>server-side</em> dan <em>user</em> diberikan <em>session ID</em> yang sudah terenkripsi, dan fitur signed cookies untuk menyimpan data yang harus disimpan di <em>client side</em>. Melalui prosedur tersebut, aplikasi web yang dibangun dapat terlindungi oleh <em>multilayered defense system</em> yang efektif untuk mengurangi kerentanan tradisional pada cookies web.</p>
<h3>Checklist Step-by-Step</h3>
<hr>
<h2>Function dan Form Registrasi</h2><h2>
</h2><ol>
<li>Saya mengimport <code>UserCreationForm</code> dan <code>messages</code> pada <code>views.py</code> untuk mengimplementasikan fungsi dan form registrasi akun. <code>UserCreationForm</code> adalah form bawaan dari Django untuk prosedur registrasi sehingga dapat langsung saya gunakan dalam aplikasi web saya. Lalu, saya menambahkan fungsi <code>register</code> pada <code>views.py</code> untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data sudah di-<em>submit</em> dari form tersebut.</li>
<li>Pada function <code>register</code> juga, saya menambahkan alur untuk melakukan validasi input yang dimasukkan oleh <em>user</em> pada form yang telah disediakan melalui perintah <code>form.is_valid()</code>. Sesudah divalidasi, isian form tersebut akan disimpan melalui perintah <code>form.save()</code>dan menampilkan pesan kepada <em>user</em> bahwa registrasi berhasil dan kembali ke halaman login.</li>
<li>Pada subdirektori <code>templates</code>, saya menambahkan berkas HTML bernama <code>register.html</code> untuk memberikan visual kepada <em>user</em> untuk halaman registrasi.</li>
<li>Setelah menambahkan views kepada <em>user</em>, saya mengintegrasikan fungsi <code>register</code> tadi pada <code>urls.py</code> untuk ditambahkan <code>urlpatterns</code> agar dapat menampilkan halaman <em>register</em> dan fungsinya sesuai <em>request</em> dari <em>user</em>.</li>
</ol>
<h3>Fungsi Login</h3>
<hr>
<ol start="5">
<li>Setelah melakukan prosedur registrasi, saya membuat fungsi login pada <code>views.py</code> dengan menambahkan import <code>authenticate</code>, <code>login</code>, dan <code>AuthenticationForm</code> yang sudah disediakan oleh Django untuk mendukung proses login dan autentikasi.</li>
<li>Pada berkas yang sama, saya menambahkan fungsi <code>login_user</code> untuk mengautentikasi pengguna yang ingin melakukan proses login. <em>User</em> nanti akan memasukkan <em>username</em> dan <em>password</em> serta di-<em>submit</em> sehingga mengirimkan request POST kepada aplikasi. Nantinya, aplikasi, dengan bantuan Django, akan melakukan proses autentikasi terhadap input yang dimasukkan oleh <em>user</em>. Apabila ditemukan kecocokan dengan data di <em>database</em>, maka fungsi ini akan membuat session untuk <em>user</em> tersebut.</li>
<li>Setelah itu, pada subdirektori <code>templates</code>, saya menambahkan berkas HTML baru bernama <code>login.html</code> yang akan menampilkan halaman login kepada user. Lalu, saya membuka berkas <code>urls.py</code> untuk menambahkan <code>urlpatterns</code> agar dapat mengakses fungsi <code>login_user</code>.</li>
</ol>
<h3>Fungsi Logout</h3> 
<hr>
<ol start="8">
<li>Sama seperti fungsi login, saya membuka kembali berkas <code>views.py</code> untuk mengimport <code>logout</code> untuk mekanisme logout pada aplikasi web, Setelah itu, saya menambahkan fungsi <code>logout_user</code> yang berfungsi untuk mendukung prosedur logout pada aplikasi web.</li>
<li>Setelah itu, saya menambahkan views baru pada berkas <code>main.html</code>, yaitu tombol <em>Logout</em> agar ketika <em>user</em> menekan tombol tersebut, maka <em>user</em> akan logout dari aplikasi web. Lalu, pada berkas <code>urls.py</code>, saya menambahkan <code>urlpatterns</code> untuk mengakses fungsi <code>logout_user</code> yang telah dibuat agar dapat diakses.</li>
</ol>
<h3>Merestriksi Akses Halaman Main dan Products Detail</h3> 
<hr>
<ol start="10">
<li>Untuk merestriksi akses halaman, saya perlu melakukan import <code>login_required</code> pada berkas <code>views.py</code> sebagai decorator untuk menambahkan fungsionalitas ke suatu fungsi tanpa mengubah isi dari kode fungsi tersebut. decorator tersebut saya letakkan pada bagian atas fungsi <code>show_main</code> dan <code>show_products</code>sehingga hanya <em>user</em> yang sudah terautentikasi saja yang dapat mengakses halaman tersebut.</li>
</ol>
<h3>Menggunakan Data dari Cookies</h3>
<hr>
<ol start="11">
<li>Untuk menggunakan data dari cookies, saya perlu mengimport <code>HttpResponseRedirect</code>, <code>reverse</code>, dan <code>datetime</code> pada berkas <code>views.py</code>. Setelah itu, pada fungsi <code>login_user</code>, saya menambahkan konfigurasi untuk menyimpan cookie baru bernama <code>last_login</code> yang berisi <em>timestamp</em> terakhir melakukan <em>login</em>.</li>
<li>Lalu, pada function <code>show_main</code>, saya menambahkan variabel baru bernama <code>last_login</code> yang akan menyimpan <em>timestamp</em> dari aktivitas <em>user</em>. Hal ini juga berlaku ketika <em>user</em> menekan tombol logout, maka cookie tersebut dihapus sehingga dapat diperbarui ketika <em>user</em> melakukan login.</li>
<li>Untuk melihat aktivitas terakhir login <em>user</em>, saya menambahkan konfigurasi pada berkas <code>main.html</code> untuk menambahkan view baru yang berisi informasi <em>timestamp</em> terakhir dari <em>user</em> setelah melakukan login.</li>
</ol>
<h3>Menghubungkan Model Prodcts dengan User</h3>
<hr>
<ol start="14">
<li>Untuk menghubungkan model <code>Products</code> kepada <em>user</em>,  peru mengimport model <code>User</code> yang sudah disediakan oleh Django. Pada model <code>Products</code>, saya menambahkan variabel baru yaitu <code>user</code> yang akan menyimpan data user dalam bentuk model <code>User</code>. Agar Django dapat mendeteksi perubahan yang terjadi pada <code>models.py</code>, saya perlu melakukan migrasi agar perubahan model yang saya lakukan terdeteksi dan tersimpan.</li>
<li>Setelah itu, pada berkas <code>views.py</code>, saya menambahkan konfigurasi tambahan pada fungsi <code>create_products</code> agar objek hasil form yang dimasukkan <em>user</em> tidak langsung tersimpan di <em>database</em> sehingga dapat melakukan modifikasi terlebih dahulu. Selain itu, nilai dari <code>request.user</code> akan membuat setiap objek secara otomatis terhubunga kepada pengguna yang membuatnya.</li>
<li>Lalu, pada function <code>show_main</code>, saya menambahkan konfigurasi untuk melakukan filter berdasarkan <em>author</em> yang menambahkan produk-produk tertentu di mana filter tersebut diambil dari query parameter <code>filter</code> pada URL. Agar fungsionalitas tersebut dapat dilihat, saya menambahkan view tambahan pada berkas <code>main.html</code> untuk menambahkan tombol filter My dan All. Lalu, pada berkas <code>products_detail.html</code>, saya juga menambahkan nama <em>author</em> yang menambahkan produk tertentu ke dalam aplikasi web.</li>
</ol>

