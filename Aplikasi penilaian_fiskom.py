import tkinter as tk
from tkinter import ttk, messagebox

class CyberCampusApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cyber Campus - Universitas Airlangga")
        self.geometry("1200x750")
        self.configure(bg="#e8ecef")

        # Database Dosen (Kode: (Nama, NIP))
        self.dosen_data = {
            "FR": ("Febdian", "197902062008011004"),
            "NU": ("Nuril", "197004141999032001"),
            "AZ": ("Zaidan", "198304222006041001"),
            "IS": ("Imam", "197201181999031001"),
            "JA": ("Jan Ady", "197201262002121002"),
            "YG": ("Yhosep", "197309042006041001"),
            "Am": ("Aminatun", "196810281993032003"),
            "Wn": ("Winarno", "198109122015041001"),
            "DH": ("Dyah", "196911281994032001"),
            "SS": ("Soegi", "197001251993031003"),
            "DI": ("Djony Izak", "196802011993031004"),
            "EE": ("Edo", "198706042018083101"),
            "Sn": ("Samian", "196706211998021001"),
            "Sw": ("Siswanto", "196403051989031003"),
            "Pj": ("Puji", "196103251987101001"),
            "HT": ("Herri", "197712282003121003"),
            "RA": ("Retna", "196806261993032003"),
            "Si": ("Supadi", "197209181998021001"),
            "AS": ("Adri", "195603031986011002")
        }

        # Database Mahasiswa (NIM: Nama)
        self.mahasiswa_data = [
            ("182241001", "Salsabila Ramadhani Putri Riadi"),
            ("182241002", "Astri Dwi Pratiwi"),
            ("182241003", "Naela Halimatus Sa'diyah"),
            ("182241004", "Muhammad Zaki Farishul Haq"),
            ("182241005", "Lailatul Mufidah"),
            ("182241006", "Ahmad Najib Zaki"),
            ("182241007", "Rahel Tasyana Tambunan"),
            ("182241008", "Ahmad Ihfan Khoiri Habib"),
            ("182241009", "Sarah Hafidhah"),
            ("182241010", "Naila Zhafira Qurrotu 'Aini"),
            ("182241011", "Riska Elvina Putri Muslimah"),
            ("182241012", "Aisah"),
            ("182241013", "Neisya Salsabila Nasywa Fuad"),
            ("182241014", "Pradithya Putra Galang Islami"),
            ("182241015", "Naufal Lutfian Hakim"),
            ("182241017", "Salsabila Aliyah Wirawan"),
            ("182241018", "Hamidah Hasan"),
            ("182241019", "Nayla Izzati"),
            ("182241020", "Muhammad Febry Rahardian"),
            ("182241022", "Fifi Wardani"),
            ("182241023", "Abdurrahman Rafif"),
            ("182241024", "M. Farhan Fauzan"),
            ("182241025", "Dwi Safaatin"),
            ("182241026", "Gita Fajriyatin Puspa Rinjani"),
            ("182241027", "Alvin Firdausy"),
            ("182241028", "Jonatan Aditia Sihombing"),
            ("182241029", "Zuanida Indri Agustin"),
            ("182241030", "Diajeng Putri Imaya"),
            ("182241031", "Tiana Afiska Gianta Putri"),
            ("182241032", "Nabilah Wiedama Putri"),
            ("182241033", "Nanda Dwi Alfikri"),
            ("182241034", "Rijal Hadhari"),
            ("182241036", "Muhammad Abiyu Khansa"),
            ("182241037", "Lubaabindra M. Dzakwan"),
            ("182241038", "Dina Renanti Sitompul"),
            ("182241039", "Adelia Dwi Yuanita"),
            ("182241040", "Farras Atha Pandita"),
            ("182241041", "Tenia Cestri Azmiyanti"),
            ("182241042", "Ilham Putra Yuliawan"),
            ("182241043", "Hendra Maulana"),
            ("182241045", "Airin Khairunnisa Nur Raerah"),
            ("182241046", "Thomas Aquino Brilliant Aryawardhana"),
            ("182241047", "Pinkan Anjelita Isnamartandya"),
            ("182241048", "Aufa Dhiya Murtadlo"),
            ("182241049", "Mayta Rahmawati"),
            ("182241050", "Muhammad Nawvall Arya Tedy Herwanto"),
            ("182241051", "Putri Balqish Prita Aulia"),
            ("182241052", "Caroline Putri Kadri"),
            ("182241053", "Alexandria Putri Indriani Tutuko"),
            ("182241054", "Mohammad Akhsan Zaaky"),
            ("182241055", "Eva Khoirun Nisa"),
            ("182241056", "Moh. Nazril Ilham Adzani"),
            ("182241057", "Jazila Assafar Aswatul Mukaromah"),
            ("182241058", "Keyro Trisna Nugraha"),
            ("182241059", "Biema Mahawijaya Nawasetya"),
            ("182241060", "Gandani Putri Lunagustama"),
            ("182241062", "Dea Ayu Kisstia")
        ]

        # Daftar Mata Kuliah Baru
        self.mata_kuliah_list = [
            "Fisika Atomik dan Molekuler",
            "Fisika Eksperimental (Praktikum)",
            "Fisika Komputasi II",
            "Fisika Komputasi (Praktikum)",
            "Fisika Statistik",
            "Listrik dan Magnet",
            "Listrik dan Magnet (Praktikum)",
            "Sensor dan Pengukuran",
            "Sistem Pengaturan"
        ]

        # Struktur Penyimpanan Nilai per MK: {nim: {mk: {"tugas": x, "uts": y, "uas": z, "akhir": w, "huruf": h}}}
        self.nilai_data = {
            m[0]: {mk: {"tugas": "-", "uts": "-", "uas": "-", "akhir": "-", "huruf": "-"} for mk in self.mata_kuliah_list}
            for m in self.mahasiswa_data
        }

        self.setup_ui()

    def setup_ui(self):
        # Header Utama Cyber Campus
        header_frame = tk.Frame(self, bg="#002b5c", height=80)
        header_frame.pack(fill=tk.X, side=tk.TOP)

        title_label = tk.Label(
            header_frame, 
            text="CYBER CAMPUS\nUniversitas Airlangga", 
            font=("Helvetica", 16, "bold"), 
            fg="gold", bg="#002b5c", justify=tk.LEFT
        )
        title_label.pack(side=tk.LEFT, padx=20, pady=10)

        slogan_label = tk.Label(
            header_frame, 
            text="Excellence with Morality", 
            font=("Times New Roman", 14, "italic"), 
            fg="white", bg="#002b5c"
        )
        slogan_label.pack(side=tk.RIGHT, padx=20, pady=10)

        # Tab Menu Utama
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tab_dosen = tk.Frame(self.notebook, bg="white")
        self.tab_mahasiswa = tk.Frame(self.notebook, bg="white")
        self.tab_admin = tk.Frame(self.notebook, bg="white")
        self.tab_prodi = tk.Frame(self.notebook, bg="white")
        self.tab_keuangan = tk.Frame(self.notebook, bg="white")

        self.notebook.add(self.tab_dosen, text="  Menu Dosen  ")
        self.notebook.add(self.tab_mahasiswa, text="  Menu Mahasiswa  ")
        self.notebook.add(self.tab_admin, text="  Menu Admin  ")
        self.notebook.add(self.tab_prodi, text="  Menu Pengurus Prodi  ")
        self.notebook.add(self.tab_keuangan, text="  Menu Keuangan  ")

        self.build_dosen_menu()
        self.build_mahasiswa_menu()
        self.build_admin_menu()
        self.build_prodi_menu()
        self.build_keuangan_menu()

    # ------------------------------------------------------------------
    # 1. MENU DOSEN (Pusat Pengisian Nilai dengan Tugas, UTS, UAS)
    # ------------------------------------------------------------------
    def build_dosen_menu(self):
        info_banner = tk.Label(
            self.tab_dosen, 
            text="✔ Jadwal Penilaian Aktif | Komposisi: Tugas (30%), UTS (35%), UAS (35%)",
            bg="#fff3cd", fg="#856404", font=("Arial", 9, "bold"), anchor="w", padx=10, pady=5
        )
        info_banner.pack(fill=tk.X, padx=10, pady=5)

        top_frame = tk.Frame(self.tab_dosen, bg="white")
        top_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(top_frame, text="Pilih Dosen Pengajar:", font=("Arial", 9, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=2)
        dosen_list = [f"[{k}] {v[0]} - NIP. {v[1]}" for k, v in self.dosen_data.items()]
        self.combo_dosen = ttk.Combobox(top_frame, values=dosen_list, width=50)
        self.combo_dosen.current(0)
        self.combo_dosen.grid(row=0, column=1, padx=10, pady=2, sticky="w")

        tk.Label(top_frame, text="Mata Kuliah:", font=("Arial", 9, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=2)
        self.combo_mk = ttk.Combobox(top_frame, values=self.mata_kuliah_list, width=50, state="readonly")
        self.combo_mk.current(0)
        self.combo_mk.grid(row=1, column=1, padx=10, pady=2, sticky="w")
        self.combo_mk.bind("<<ComboboxSelected>>", lambda e: self.refresh_tabel_dosen())

        banner = tk.Label(self.tab_dosen, text="FORM INPUT KOMPONEN NILAI MAHASISWA", bg="#002b5c", fg="white", font=("Arial", 10, "bold"), anchor="w", padx=10)
        banner.pack(fill=tk.X, padx=10, pady=(10, 0))

        # Tabel Pengisian Nilai
        table_frame = tk.Frame(self.tab_dosen, bg="white")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        columns = ("no", "nim", "nama", "tugas", "uts", "uas", "akhir", "huruf")
        self.tree_dosen = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
        
        headers = {
            "no": ("NO", 40),
            "nim": ("NIM", 110),
            "nama": ("NAMA MAHASISWA", 270),
            "tugas": ("TUGAS (30%)", 100),
            "uts": ("UTS (35%)", 90),
            "uas": ("UAS (35%)", 90),
            "akhir": ("NILAI AKHIR", 100),
            "huruf": ("HURUF", 70)
        }
        for col, (text, width) in headers.items():
            self.tree_dosen.heading(col, text=text)
            anchor = "center" if col != "nama" else "w"
            self.tree_dosen.column(col, width=width, anchor=anchor)

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree_dosen.yview)
        self.tree_dosen.configure(yscroll=scrollbar.set)
        
        self.tree_dosen.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Panel Input Form Nilai (Tugas, UTS, UAS)
        entry_frame = tk.Frame(self.tab_dosen, bg="#f8f9fa", bd=1, relief=tk.SOLID)
        entry_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(entry_frame, text="Input Nilai:", bg="#f8f9fa", font=("Arial", 9, "bold")).pack(side=tk.LEFT, padx=5, pady=8)
        
        tk.Label(entry_frame, text="Tugas:", bg="#f8f9fa").pack(side=tk.LEFT, padx=2)
        self.entry_tugas = tk.Entry(entry_frame, width=6)
        self.entry_tugas.pack(side=tk.LEFT, padx=2)

        tk.Label(entry_frame, text="UTS:", bg="#f8f9fa").pack(side=tk.LEFT, padx=2)
        self.entry_uts = tk.Entry(entry_frame, width=6)
        self.entry_uts.pack(side=tk.LEFT, padx=2)

        tk.Label(entry_frame, text="UAS:", bg="#f8f9fa").pack(side=tk.LEFT, padx=2)
        self.entry_uas = tk.Entry(entry_frame, width=6)
        self.entry_uas.pack(side=tk.LEFT, padx=2)

        btn_simpan = tk.Button(entry_frame, text="Simpan & Hitung Nilai", bg="#002b5c", fg="white", font=("Arial", 9, "bold"), command=self.simpan_nilai)
        btn_simpan.pack(side=tk.LEFT, padx=15, pady=5)

        self.refresh_tabel_dosen()

    def refresh_tabel_dosen(self):
        for item in self.tree_dosen.get_children():
            self.tree_dosen.delete(item)
        
        current_mk = self.combo_mk.get()
        for idx, (nim, nama) in enumerate(self.mahasiswa_data, 1):
            val = self.nilai_data[nim][current_mk]
            self.tree_dosen.insert("", tk.END, values=(
                idx, nim, nama, val["tugas"], val["uts"], val["uas"], val["akhir"], val["huruf"]
            ))

    def simpan_nilai(self):
        selected = self.tree_dosen.selection()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih mahasiswa dari tabel terlebih dahulu!")
            return
        
        t_str = self.entry_tugas.get().strip()
        uts_str = self.entry_uts.get().strip()
        uas_str = self.entry_uas.get().strip()

        try:
            tugas = float(t_str) if t_str else 0.0
            uts = float(uts_str) if uts_str else 0.0
            uas = float(uas_str) if uas_str else 0.0
        except ValueError:
            messagebox.showerror("Error", "Nilai komponen harus berupa angka!")
            return

        if not (0 <= tugas <= 100 and 0 <= uts <= 100 and 0 <= uas <= 100):
            messagebox.showerror("Error", "Setiap nilai komponen harus berada di antara 0 dan 100!")
            return

        # Perhitungan Nilai Akhir Berdasarkan Bobot
        nilai_akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        na_rounded = round(nilai_akhir, 2)

        # Penentuan Nilai Huruf
        if na_rounded >= 85: huruf = "A"
        elif na_rounded >= 75: huruf = "AB"
        elif na_rounded >= 70: huruf = "B"
        elif na_rounded >= 65: huruf = "BC"
        elif na_rounded >= 60: huruf = "C"
        elif na_rounded >= 50: huruf = "D"
        else: huruf = "E"

        item = self.tree_dosen.item(selected)
        nim = item["values"][1]
        current_mk = self.combo_mk.get()

        self.nilai_data[nim][current_mk] = {
            "tugas": str(tugas),
            "uts": str(uts),
            "uas": str(uas),
            "akhir": str(na_rounded),
            "huruf": huruf
        }

        self.refresh_tabel_dosen()
        self.refresh_tabel_mahasiswa()
        
        # Kosongkan form input
        self.entry_tugas.delete(0, tk.END)
        self.entry_uts.delete(0, tk.END)
        self.entry_uas.delete(0, tk.END)
        messagebox.showinfo("Sukses", f"Nilai untuk NIM {nim} pada matakuliah {current_mk} berhasil disimpan!")

    # ------------------------------------------------------------------
    # 2. MENU MAHASISWA (Pusat Melihat KHS & Hasil Penilaian)
    # ------------------------------------------------------------------
    def build_mahasiswa_menu(self):
        top_frame = tk.Frame(self.tab_mahasiswa, bg="white")
        top_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(top_frame, text="Pilih Akun Mahasiswa:", font=("Arial", 9, "bold"), bg="white").pack(side=tk.LEFT, padx=5)
        
        mhs_options = [f"{m[0]} - {m[1]}" for m in self.mahasiswa_data]
        self.combo_mhs_login = ttk.Combobox(top_frame, values=mhs_options, width=45, state="readonly")
        self.combo_mhs_login.current(50)  # Default: Eva Khoirun Nisa
        self.combo_mhs_login.pack(side=tk.LEFT, padx=5)
        self.combo_mhs_login.bind("<<ComboboxSelected>>", lambda e: self.refresh_tabel_mahasiswa())

        banner = tk.Label(self.tab_mahasiswa, text="KARTU HASIL STUDI (KHS) MAHASISWA", bg="#002b5c", fg="white", font=("Arial", 10, "bold"), anchor="w", padx=10)
        banner.pack(fill=tk.X, padx=10, pady=(5,0))

        table_frame = tk.Frame(self.tab_mahasiswa, bg="white")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        columns = ("mk", "sks", "tugas", "uts", "uas", "akhir", "huruf", "status")
        self.tree_mhs = ttk.Treeview(table_frame, columns=columns, show="headings", height=12)
        
        headers_mhs = {
            "mk": ("MATA KULIAH", 230),
            "sks": ("SKS", 50),
            "tugas": ("TUGAS", 80),
            "uts": ("UTS", 80),
            "uas": ("UAS", 80),
            "akhir": ("NILAI AKHIR", 90),
            "huruf": ("HURUF", 70),
            "status": ("STATUS", 90)
        }
        for col, (text, width) in headers_mhs.items():
            self.tree_mhs.heading(col, text=text)
            anchor = "center" if col != "mk" else "w"
            self.tree_mhs.column(col, width=width, anchor=anchor)

        self.tree_mhs.pack(fill=tk.BOTH, expand=True)
        self.refresh_tabel_mahasiswa()

    def refresh_tabel_mahasiswa(self):
        for item in self.tree_mhs.get_children():
            self.tree_mhs.delete(item)

        selected_str = self.combo_mhs_login.get()
        nim = selected_str.split(" - ")[0] if selected_str else self.mahasiswa_data[0][0]
        mhs_dict_nilai = self.nilai_data.get(nim, {})

        for mk in self.mata_kuliah_list:
            val = mhs_dict_nilai.get(mk, {"tugas": "-", "uts": "-", "uas": "-", "akhir": "-", "huruf": "-"})
            huruf = val["huruf"]
            status = "LULUS" if huruf in ["A", "AB", "B", "BC", "C"] else ("BELUM DIISI" if huruf == "-" else "TIDAK LULUS")
            
            self.tree_mhs.insert("", tk.END, values=(
                mk, "3", val["tugas"], val["uts"], val["uas"], val["akhir"], huruf, status
            ))

    # ------------------------------------------------------------------
    # 3. MENU ADMIN (Pengelolaan Akun & Data Akademik)
    # ------------------------------------------------------------------
    def build_admin_menu(self):
        banner = tk.Label(self.tab_admin, text="PANEL KELOLA DATA AKADEMIK & AKUN", bg="#002b5c", fg="white", font=("Arial", 10, "bold"), anchor="w", padx=10)
        banner.pack(fill=tk.X, padx=10, pady=10)

        admin_sub = ttk.Notebook(self.tab_admin)
        admin_sub.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Sub-tab 1: Data Dosen
        f_dosen = tk.Frame(admin_sub, bg="white")
        admin_sub.add(f_dosen, text="Data Dosen")
        tree_dosen_admin = ttk.Treeview(f_dosen, columns=("kode", "nama", "nip"), show="headings")
        tree_dosen_admin.heading("kode", text="KODE DOSEN")
        tree_dosen_admin.heading("nama", text="NAMA DOSEN")
        tree_dosen_admin.heading("nip", text="NIP")
        tree_dosen_admin.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        for k, v in self.dosen_data.items():
            tree_dosen_admin.insert("", tk.END, values=(k, v[0], v[1]))

        # Sub-tab 2: Data Mahasiswa
        f_mhs = tk.Frame(admin_sub, bg="white")
        admin_sub.add(f_mhs, text="Data Mahasiswa")
        tree_mhs_admin = ttk.Treeview(f_mhs, columns=("no", "nim", "nama"), show="headings")
        tree_mhs_admin.heading("no", text="NO")
        tree_mhs_admin.heading("nim", text="NIM")
        tree_mhs_admin.heading("nama", text="NAMA MAHASISWA")
        tree_mhs_admin.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        for idx, (nim, nama) in enumerate(self.mahasiswa_data, 1):
            tree_mhs_admin.insert("", tk.END, values=(idx, nim, nama))

    # ------------------------------------------------------------------
    # 4. MENU PENGURUS PRODI (Monitoring Laporan & Rekap)
    # ------------------------------------------------------------------
    def build_prodi_menu(self):
        banner = tk.Label(self.tab_prodi, text="MONITORING & REKAP NILAI PROGRAM STUDI", bg="#002b5c", fg="white", font=("Arial", 10, "bold"), anchor="w", padx=10)
        banner.pack(fill=tk.X, padx=10, pady=10)

        stat_frame = tk.Frame(self.tab_prodi, bg="#e9ecef", bd=1, relief=tk.RIDGE)
        stat_frame.pack(fill=tk.X, padx=10, pady=5)

        lbl_info = tk.Label(
            stat_frame, 
            text="Total Mahasiswa: 57 | Total Dosen: 19 | Total Mata Kuliah: 9 | Status: Synchronized", 
            font=("Arial", 10, "bold"), bg="#e9ecef", fg="#002b5c", pady=10
        )
        lbl_info.pack()

        btn_export = tk.Button(self.tab_prodi, text="📄 Cetak / Export Rekapitulasi Laporan (PDF/Excel)", bg="#28a745", fg="white", font=("Arial", 9, "bold"), command=lambda: messagebox.showinfo("Export", "Laporan Rekapitulasi Nilai berhasil di-export!"))
        btn_export.pack(padx=10, pady=10)

    # ------------------------------------------------------------------
    # 5. MENU KEUANGAN (Pengelolaan Tagihan UKT)
    # ------------------------------------------------------------------
    def build_keuangan_menu(self):
        banner = tk.Label(self.tab_keuangan, text="PENGELOLAAN TAGIHAN & KEUANGAN (UKT)", bg="#002b5c", fg="white", font=("Arial", 10, "bold"), anchor="w", padx=10)
        banner.pack(fill=tk.X, padx=10, pady=10)

        table_frame = tk.Frame(self.tab_keuangan, bg="white")
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        columns = ("nim", "nama", "tagihan", "status_bayar")
        tree_keu = ttk.Treeview(table_frame, columns=columns, show="headings", height=12)
        
        tree_keu.heading("nim", text="NIM")
        tree_keu.heading("nama", text="NAMA MAHASISWA")
        tree_keu.heading("tagihan", text="TAGIHAN UKT")
        tree_keu.heading("status_bayar", text="STATUS PEMBAYARAN")

        tree_keu.column("nim", width=120, anchor="center")
        tree_keu.column("nama", width=280)
        tree_keu.column("tagihan", width=150, anchor="center")
        tree_keu.column("status_bayar", width=150, anchor="center")

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree_keu.yview)
        tree_keu.configure(yscroll=scrollbar.set)

        tree_keu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        for nim, nama in self.mahasiswa_data:
            tree_keu.insert("", tk.END, values=(nim, nama, "Rp 6.000.000", "LUNAS"))

if __name__ == "__main__":
    app = CyberCampusApp()
    app.mainloop()