import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        # Binding Tombol ke Fungsi Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.update_data)
        self.view.btn_hapus.configure(command=self.hapus_data)
        
        # Binding Event Klik pada Baris Tabel untuk Mengisi Form Otomatis
        self.view.tabel.bind("<ButtonRelease-1>", self.select_data)

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()
        for anggota in data_anggota:
            self.view.tabel.insert("", "end", values=(anggota['id_anggota'], anggota['nama'], anggota['alamat']))

    def select_data(self, event):
        """Mengambil data dari baris tabel yang diklik dan menampilkannya ke form input"""
        selected_item = self.view.tabel.focus()
        if selected_item:
            values = self.view.tabel.item(selected_item, 'values')
            if values:
                self.view.entry_nama.delete(0, 'end')
                self.view.entry_alamat.delete(0, 'end')
                
                self.view.entry_nama.insert(0, values[1])
                self.view.entry_alamat.insert(0, values[2])

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.create_anggota(nama, alamat)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.clear_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def update_data(self):
        """Mengambil id_anggota dari baris tabel yang dipilih lalu memperbarui datanya"""
        selected_item = self.view.tabel.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data anggota dari tabel yang ingin diperbarui!")
            return
        
        values = self.view.tabel.item(selected_item, 'values')
        id_anggota = values[0]  # Mengambil id_anggota dari kolom pertama

        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        berhasil = self.model.update_anggota(id_anggota, nama, alamat)
        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.clear_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def hapus_data(self):
        """Mengambil id_anggota dari baris tabel yang dipilih lalu menghapusnya"""
        selected_item = self.view.tabel.focus()
        if not selected_item:
            messagebox.showwarning("Peringatan", "Pilih data anggota dari tabel yang ingin dihapus!")
            return
        
        values = self.view.tabel.item(selected_item, 'values')
        id_anggota = values[0]  # Mengambil id_anggota dari kolom pertama

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data anggota ini?")
        if konfirmasi:
            berhasil = self.model.delete_anggota(id_anggota)
            if berhasil:
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
                self.clear_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    def clear_form(self):
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')

    def run(self):
        self.view.mainloop()