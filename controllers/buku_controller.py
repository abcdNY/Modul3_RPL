import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self):
        # Inisialisasi Model dan View
        self.model = BukuModel()
        self.view = BukuView()

        # Binding (mengikat) tombol di View dengan fungsi dari Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)  # Tambahan Tombol Update
        self.view.btn_hapus.configure(command=self.hapus_data)    # Tambahan Tombol Delete

        # Binding Event Klik pada Baris Tabel untuk Mengisi Form otomatis
        self.view.tabel.bind("<ButtonRelease-1>", self.select_data)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan isi tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (database)
        data_buku = self.model.get_all_buku()

        # Memasukkan data baru ke dalam tabel View
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def select_data(self, event):
        # Mengambil data dari baris tabel yang diklik dan menampilkannya ke form input
        selected_item = self.view.tabel.focus()
        if selected_item:
            values = self.view.tabel.item(selected_item, 'values')
            if values:
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_penulis.delete(0, 'end')
                self.view.entry_tahun.delete(0, 'end')
                
                self.view.entry_judul.insert(0, values[1])
                self.view.entry_penulis.insert(0, values[2])
                self.view.entry_tahun.insert(0, values[3])

    def simpan_data(self):
        # Mengambil teks dari kotak input di View
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        # Validasi Form Kosong
        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        # Mengirim data ke Model untuk disimpan
        berhasil = self.model.create_buku(judul, penulis, tahun)

        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan")
            # Bersihkan form input
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            # Muat ulang tabel agar data terbaru muncul
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def update_data(self):
        # Mengambil id_buku dari baris tabel yang dipilih lalu memperbarui datanya
        selected_item = self.view.tabel.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data buku dari tabel yang ingin diperbarui!")
            return

        values = self.view.tabel.item(selected_item, 'values')
        id_buku = values[0]  # Mengambil id_buku dari kolom pertama tabel[cite: 20]

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.update_buku(id_buku, judul, penulis, tahun)
        if berhasil:
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            # Bersihkan form
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def hapus_data(self):
        # Mengambil id_buku dari baris tabel yang dipilih lalu menghapusnya
        selected_item = self.view.tabel.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data buku dari tabel yang ingin dihapus!")
            return
        
        values = self.view.tabel.item(selected_item, 'values')
        id_buku = values[0]  # Mengambil id_buku dari kolom pertama tabel[cite: 20]

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data buku ini?")
        if konfirmasi:
            berhasil = self.model.delete_buku(id_buku)
            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                # Bersihkan form input secara langsung
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_penulis.delete(0, 'end')
                self.view.entry_tahun.delete(0, 'end')
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    # Fungsi untuk menjalankan aplikasi
    def run(self):
        self.view.mainloop()
    