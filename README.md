# LAPORAN UTS STRUKTUR DATA
## Nama Anggota :
1. I Kadek Brahadya Praja Nugraha (2501010093)
2. Wayan Andhika Darma Putra (2501010070)
3. Dewa Ngakan Made Rasta Baladika Ak (2501010074)
## I. Rumusan masalah serta solusi
1. Bagaimana konsep queue (antrian) dapat diterapkan untuk mengelola sistem antrian parkir kendaraan secara efektif?
2. Bagaimana implementasi struktur data array dalam membangun sistem antrian parkir sederhana?
3. Bagaimana sistem yang dibuat dapat mensimulasikan kondisi nyata dalam pengelolaan parkir kendaraan?
Solusi yang ditawarkan dalam proyek ini adalah dengan merancang dan mengimplementasikan sistem antrian parkir berbasis queue menggunakan array. Adapun solusi yang diberikan meliputi:
1. Penerapan konsep Queue (FIFO)
Sistem dirancang agar kendaraan yang pertama masuk akan menjadi kendaraan pertama yang keluar, sehingga tercipta keteraturan dalam parkiran.
2. Penggunaan Array sebagai Struktur Data
Data kendaraan disimpan dalam array (list Python) yang memungkinkan pengolahan data secara sederhana dan efisien.
3. Penyediaan Operasi Dasar Queue
Sistem menyediakan operasi utama seperti Enqueue untuk menambah kendaraan, Dequeue untuk mengeluarkan kendaraan, Peek untuk melihat kendaraan terdepan, serta Display untuk menampilkan seluruh antrian.
## II. Landasan teori
Struktur data adalah cara untuk mengelola data dalam komputer agar dapat digunakan secara efisien(Kadir, 2021). Struktur data memungkinkan proses pengolahan data seperti pencarian, penambahan, dan penghapusan dapat dilakukan dengan lebih optimal. Jadi struktur data merupakan cara untuk menyimpan, mengorganisasi, serta mengelola data agar bisa digunakan kembali dengan mudah dan efisisen.
Pada Struktur data terdapat juga konsep queue. Queue adalah struktur data yang memungkinkan kita menyimpan dan mengambil elemen dalam urutan First-In-First-Out (FIFO). Artinya, elemen yang pertama dimasukkan ke dalam queue akan menjadi elemen pertama yang dikeluarkan dari queue seperti pada sistem antrian parkir. Operasi dasar pada queue meliputi Enqueue yang menambahkan elemen ke bagian belakang antrian, Dequeue yang menghapus elemen dari bagian depan antrian, Peek yang melihat elemen paling depan tanpa menghapusnya, dan terakhir ada Display yang menampilkan seluruh isi antrian.
Pada awalnya antrian berada dalam keadaan kosong atau tidak ada satupun elemen di dalamnya. Pada keadaan ini tidak dapat dilakukan penghapusan elemen karena akan meyebabkan kesalahan yang disebut underflow. Elemen baru dapat ditambahkan ketika antrian berada dalam keadaan tidak penuh. Jika antrian dalam keadaan penuh maka elemen baru tidak dapat ditambahkan, karena jika dilakukan penambahan elemen baru maka akan terjadi kesalahan atau yang disebut overflow. Dengan demikian elemen tersebut harus menunggu sampai antrian berada dalam keadaan bisa menambahkan elemen baru. Ada beberapa kelebihan dalam penggunaan array seperti Mudah diimplementasikan, Sederhana, dan cocok untuk pemula. Tetapi hal ini juga terdapat kekurangan seperti operasi dequeue memiliki kompleksitas waktu yang lebih tinggi karena pergeseran elemen.
## III. Desain Sistem dan Implementasi
Sistem yang dibuat merupakan sistem antrian parkir sederhana yang menerapkan konsep Queue (antrian) dengan prinsip FIFO (First In First Out), yaitu kendaraan yang pertama masuk akan menjadi kendaraan pertama yang keluar. Pada sistem ini, struktur data yang digunakan adalah array (list Python) untuk menyimpan data kendaraan berupa nomor plat. Sistem dirancang berbasis menu interaktif yang memungkinkan pengguna memilih operasi yang diinginkan. Berikut dalam bentuk pseucodenya:
Berdasarkan pseucode tersebut, alur kerja sistem adalah:

<img width="565" height="729" alt="image" src="https://github.com/user-attachments/assets/d9374fe0-9897-4c5e-b5a5-31e37a4057bc" />

1. Program dimulai,
2. Sistem menampilkan menu pilihan,
3. Pengguna memilih menu,
4. Sistem menjalankan proses sesuai pilihan:
5. Jika memilih Enqueue, kendaraan ditambahkan ke antrian
6. Jika memilih Dequeue, kendaraan terdepan dikeluarkan
7. Jika memilih Peek, sistem menampilkan kendaraan paling depan
8. Jika memilih Display, sistem menampilkan seluruh antrian
9. Jika memilih Keluar, program berhenti
10. Setelah proses selesai, sistem kembali ke menu utama,
11. Program berakhir saat pengguna memilih keluar

Sistem menggunakan variabel antrian parkir untuk menyimpan data kendaraan serta kapasitas untuk membatasi jumlah kendaraan dalam parkiran. Operasi yang digunakan pada program ini merupakan operasi queue dengan fungsi sebagai berikut:
1. Enqueue (Tambah Kendaraan)
Fungsi ini digunakan untuk menambahkan kendaraan ke dalam antrian parkir.
Kendaraan akan dimasukkan ke posisi paling belakang menggunakan append().
2. Dequeue (Kendaraan Keluar)
Fungsi ini digunakan untuk menghapus kendaraan dari antrian.
Kendaraan yang keluar adalah kendaraan paling depan menggunakan pop(0).
3. Peek (Melihat Antrian Depan)
Fungsi ini digunakan untuk melihat kendaraan yang berada di posisi paling depan tanpa menghapusnya.
4. Display (Menampilkan Antrian)
Fungsi ini digunakan untuk menampilkan seluruh kendaraan dalam antrian parkir.
## IV Kesimpulan
Berdasarkan hasil perancangan dan implementasi sistem antrian parkir menggunakan struktur data queue, dapat disimpulkan bahwa seluruh rumusan masalah yang telah diajukan sebelumnya berhasil diselesaikan dengan baik. Penerapan konsep queue dengan prinsip FIFO (First In First Out) terbukti mampu mengelola antrian kendaraan secara teratur, di mana kendaraan yang pertama masuk akan menjadi yang pertama keluar. Implementasi sistem menggunakan array (list Python) juga berjalan sesuai dengan teori yang telah dipelajari, khususnya dalam menjalankan operasi dasar queue seperti enqueue, dequeue, peek, dan display. Selain itu, sistem yang dibangun mampu mensimulasikan kondisi nyata dalam pengelolaan parkir secara sederhana namun efektif. Dengan demikian, dapat disimpulkan bahwa penggunaan struktur data queue memberikan manfaat yang signifikan dalam menciptakan sistem yang terstruktur, efisien, dan mudah dipahami, khususnya dalam kasus pengelolaan antrian parkir kendaraan.
## V Link Canva
https://canva.link/qphsivjhogzgk0w
