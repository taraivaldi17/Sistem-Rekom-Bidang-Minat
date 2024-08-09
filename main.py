import streamlit as st
import pandas as pd

matkul = {
    "Kode MK": [
        "21521010", "21521003", "21521004", "21521005", "21521006", "21521007", "21521008", "21521009", "21521011", "21522001",
        "21522002", "21522003", "21522004", "21522005", "21522006", "21522008", "21522009", "21523001", "21523002", "21523003",
        "21523004", "21523005", "21523006", "21523007", "21524001", "21524002", "21524003", "21524004", "21524005", "21524006",
        "21524007", "21524008", "21525001", "21525002", "21525003", "21525004", "21525005", "21525006", "21525007"],
    "Nama MK": [
        "PENDIDIKAN PANCASILA", "PENDIDIKAN AGAMA I", "BAHASA INGGRIS", "KALKULUS I", "PENGANTAR TEKNOLOGI INFORMASI",
        "ALGORITMA & PEMOGRAMAN I", "LOGIKA MATEMATIKA", "BAHASA INDONESIA", "DESAIN GRAFIS DAN ANIMASI", "PENDIDIKAN AGAMA II",
        "KALKULUS II", "STATISTIKA & PROBABILITAS", "ALGORITMA & PEMOGRAMAN II", "TEKNIK DIGITAL", "SISTEM OPERASI", "SISTEM BERKAS",
        "KEWARGANEGARAAN", "MATEMATIKA DISKRIT", "ALJABAR LINIER & MATRIK", "ARSITEKTUR & ORGANISASI KOMPUTER I",
        "JARINGAN KOMPUTER", "STRUKTUR DATA", "SISTEM BASIS DATA", "PEMOGRAMAN BERORIENTASI OBJEK", "TEORI BAHASA & AUTOMATA",
        "PENGOLAHAN CITRA DIGITAL", "ARSITEKTUR & ORGANISASI KOMPUTER II", "ANALISA ALGORITMA", "METODE NUMERIK", "PEMOGRAMAN WEB",
        "JARINGAN KOMPUTER LANJUT", "TEKNOLOGI WIRELESS DAN SISTEM BERGERAK", "RISET OPERASIONAL", "REKAYASA PERANGKAT LUNAK",
        "KECERDASAN BUATAN", "INTERAKSI MANUSIA & KOMPUTER", "MULTIMEDIA", "PEMOGRAMAN VISUAL", "ANALISA DESIGN SI"],
    "Bidang Peminatan": [
        None, None, None, "SI, SC", "SI, SC, JK",
        "SI", "SC", None, "SI, JK", None,
        "SC", "SI, SC", "SI", "JK", "JK", "SI, JK",
        None, "SC", "SC", "SI, JK",
        "JK", "SI, SC", "SI, SC", "SI", "SI, JK",
        "SC", "SI, JK", "SI, SC", "SC", "SI",
        "JK", "SI, JK", "SC", "SI, SC, JK",
        "SC", "SI", "SI", "SI", "SI, SC"],
    "Kode Fakta dan Aturan": [
        None, None, None, "M001", "M002",
        "M003", "M004", None, "M005", None,
        "M006", "M007", "M008", "M009", "M010", "M011",
        None, "M012", "M013", "M014",
        "M015", "M016", "M017", "M018", "M019",
        "M020", "M021", "M022", "M023", "M024",
        "M025", "M026", "M027", "M028",
        "M029", "M030", "M031", "M032", "M033"],
    "Semester": [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5],
    "SKS": [3,3,2,2,2,3,3,2,2,2,3,3,3,3,2,3,2,2,3,2,3,3,4,3,3,3,2,2,2,4,3,2,2,4,3,3,3,3,3],
    "Prasyarat": [
        "", "", "", "", "", "", "", "", "", "21521003",
        "", "", "21521007", "", "", "", "", "", "21522002", "21522005",
        "21522006", "21522004", "", "21522004", "", "21523002", "21523003", "21521007", "21521005", "21523006, 21521007",
        "21523004", "", "", "21523006, 21523007", "21521008", "", "21521011", "21523007", ""],
    "Jenis Mata Kuliah": [
        "Universitas", "Universitas", "Universitas", "Fakultas", "Jurusan", "Jurusan", "Fakultas", "Universitas", "Jurusan", "Universitas",
        "Fakultas", "Fakultas", "Jurusan", "Jurusan", "Jurusan", "Jurusan", "Universitas", "Fakultas", "Fakultas", "Jurusan",
        "Jurusan", "Jurusan", "Jurusan", "Jurusan", "Jurusan", "Jurusan", "Jurusan", "Jurusan", "Jurusan", "Jurusan",
        "Jurusan", "Jurusan", "Fakultas", "Jurusan", "Jurusan", "Jurusan", "Jurusan", "Jurusan", "Jurusan"]
}

peminatan = {
    "Kode Bidang Minat": ["SI", "SC", "JK"],
    "Bidang Minat": ["Sistem Informasi", "Sistem Cerdas", "Jaringan Komputer"]
}

nilai_matkul = {
    "Nilai Huruf": ["A", "AB", "B", "BC", "C", "D", "E"],
    "Nilai Angka": [4.00, 3.50, 3.00, 2.50, 2.00, 1.00, 0.00],
    "Nilai Normalisasi": [1.0000, 0.8750, 0.7500, 0.6250, 0.5000, 0.2500, 0.0000]
}

fcRule = {
    "Kode Rule": [
        "R001", "R002", "R003", "R004", "R005", "R006", "R007", "R008", "R009", "R010",
        "R011", "R012", "R013", "R014", "R015", "R016", "R017", "R018", "R019", "R020",
        "R021", "R022", "R023", "R024", "R025", "R026", "R027", "R028", "R029", "R030",
        "R031", "R032", "R033", "R034", "R035", "R036"],
    "Kondisi": [
        "IF M001 THEN M007", "IF M001 AND M028 THEN M007", "IF M002 THEN M028", "IF M003 THEN SI", "IF M004 AND M033 THEN M006",
        "IF M004 THEN SC", "IF M005 THEN M011", "IF M005 AND M028 THEN M011", "IF M006 THEN SC", "IF M007 THEN M016",
        "IF M008 THEN SI", "IF M009 AND M026 THEN M010", "IF M009 THEN JK", "IF M010 THEN JK", "IF M011 THEN M014",
        "IF M012 THEN SC", "IF M013 THEN SC", "IF M014 THEN M019", "IF M015 THEN JK", "IF M016 THEN M017",
        "IF M017 THEN M022", "IF M018 THEN SI", "IF M019 THEN M021", "IF M020 THEN SC", "IF M021 THEN M026",
        "IF M022 THEN M033", "IF M023 THEN SC", "IF M024 THEN SI", "IF M025 THEN JK", "IF M026 AND M033 THEN M003",
        "IF M027 THEN SC", "IF M028 THEN M003", "IF M029 THEN SC", "IF M030 THEN SI", "IF M031 THEN SI", "IF M032 THEN SI"]
}

# Fungsi untuk menampilkan halaman dashboard
def dashboard():
    st.title("Dashboard")
    st.write("""
    ### Selamat Datang di Sistem Rekomendasi Bidang Minat Teknik Informatika

    Website ini adalah sistem pakar yang dirancang untuk membantu mahasiswa Program Studi Teknik Informatika di Universitas Madura dalam menentukan bidang minat yang sesuai. 

    Dengan menggunakan penalaran **Forward Chaining** dan metode **Dempster-Shafer**, sistem ini akan merekomendasikan bidang minat yang paling cocok berdasarkan mata kuliah yang telah ditempuh dan nilai yang diperoleh.

    ### Fitur Utama
    - **Bidang Minat**: Jelajahi bidang minat yang tersedia dalam Program Studi Teknik Informatika.
    - **Informasi Mata Kuliah**: Dapatkan informasi detail mengenai mata kuliah yang ditawarkan.
    - **Rule Sistem Pakar**: Lihat dan pahami aturan yang digunakan oleh sistem pakar untuk inferensi.
    - **Perhitungan Dempster-Shafer**: Input nilai mata kuliah Anda dan dapatkan rekomendasi bidang minat.

    Selamat menggunakan, dan semoga sistem ini dapat membantu Anda dalam menentukan jalur studi yang sesuai dengan minat dan kemampuan Anda.
    """)

# Fungsi untuk menampilkan halaman bidang minat
def bidang_minat():
    st.title("Bidang Minat")
    st.write("Berikut adalah daftar bidang minat yang tersedia dalam Program Studi Teknik Informatika di Universitas Madura:")

    # Membuat dataframe dari data bidang minat
    df = pd.DataFrame(peminatan)

    # Menampilkan tabel
    st.table(df)

# Fungsi untuk menampilkan halaman informasi mata kuliah
def informasi_mata_kuliah():
    st.title("Informasi Mata Kuliah")
    st.write("Berikut adalah daftar mata kuliah wajib semester 1-5 di Program Studi Teknik Informatika:")
 
    # Membuat dataframe dari data mata kuliah
    df = pd.DataFrame(matkul)
    selected_columns = ["Kode MK", "Nama MK", "Semester", "SKS", "Prasyarat", "Jenis Mata Kuliah"] # mengambil data pada kolom untuk ditampilkan
    st.table(df[selected_columns])

# Fungsi untuk menampilkan nilai mata kuliah dan nilai normalisasinya
def nilai_mata_kuliah():
    st.title("Nilai Normalisasi")
    st.write("Berikut adalah nilai pada mata kuliah di Program Studi Teknik Informatika di Universitas Madura dan nilai normalisasinya")
    
    df = pd.DataFrame(nilai_matkul)
    st.table(df)

# Fungsi untuk menampilkan halaman tabel fakta dan aturan
def fakta_aturan():
    st.title("Fakta dan Aturan")
    st.write("Berikut adalah tabel fakta dan aturan terkait mata kuliah dan bidang peminatan:")

    df = pd.DataFrame(matkul)
    df_filtered = df[df["Kode Fakta dan Aturan"].notnull()] # memfilter / mengambil data berdasarkan kode fakta dan aturan yang tidak kosong
    selected_columns = ["Kode MK", "Kode Fakta dan Aturan", "Nama MK", "Bidang Peminatan"] # mengambil data pada kolom untuk ditampilkan
    st.table(df_filtered[selected_columns].reset_index(drop=True))

# Fungsi untuk menampilkan halaman rule sistem pakar
def rule_fc():
    st.title("Rule Forward Chaining")
    st.write("Berikut adalah tabel rule sistem pakar yang digunakan dalam penentuan bidang minat:")

    # Membuat DataFrame
    df = pd.DataFrame(fcRule)

    # Menampilkan tabel
    st.table(df)

# Fungsi untuk menggabungkan massa keyakinan
def kombinasi_massa_keyakinan(m1, m2):
    hasil = {}
    for key1, value1 in m1.items():
        for key2, value2 in m2.items():
            if key1 and key2:
                key_himpunan = tuple(sorted(set(key1) & set(key2), key=lambda x: ['SI', 'SC', 'JK']))
            elif not key1:
                key_himpunan = key2
            elif not key2:
                key_himpunan = key1
            else:
                key_himpunan = ()
            nilai_himpunan = value1 * value2
            if key_himpunan in hasil:
                hasil[key_himpunan] += nilai_himpunan
            else:
                hasil[key_himpunan] = nilai_himpunan
    
    total = sum(hasil.values())
    
    for key in hasil:
        hasil[key] /= total
    return hasil

# Fungsi untuk menampilkan halaman perhitungan Dempster Shafer
def halaman_ds():
    st.title("Perhitungan Dempster Shafer")
    st.write("Masukkan nilai mata kuliah untuk perhitungan:")
    
    df_nilai = pd.DataFrame(nilai_matkul)
    matkul_terpilih = {}
    matkul_bidang_minat = {}
    total_sks = 0
    
    for nama_mk, kode_mk, bidang_minat, sks in zip(matkul["Nama MK"], matkul["Kode MK"], matkul["Bidang Peminatan"], matkul["SKS"]):
        # Checkbox mata kuliah
        if st.checkbox(f"Apakah Anda telah mengambil {nama_mk} ({kode_mk}) ?"):
            # Input nilai mata kuliah
            nilai_huruf = st.selectbox(f"Nilai untuk {nama_mk}", ["A", "AB", "B", "BC", "C", "D", "E"], key=f"{kode_mk}_nilai")
            # Normalisasi nilai
            nilai_normalisasi = df_nilai[df_nilai["Nilai Huruf"] == nilai_huruf]["Nilai Normalisasi"].values[0]
            
            # Jika matakuliah memiliki bidang minat, simpan ke matkul_bidang_minat
            if bidang_minat:
                # Ambil bidang minat dan memecahnya
                daftar_bidang_minat = bidang_minat.split(', ')
                # Simpan data nilai mata kuliah dan bidang minatnya untuk perhitungan DS
                matkul_bidang_minat[nama_mk] = (nilai_normalisasi, daftar_bidang_minat)
            else:
                daftar_bidang_minat = []

            # Simpan data nilai mata kuliah dan bidang minatnya untuk ditampilkan
            matkul_terpilih[nama_mk] = (nilai_normalisasi, daftar_bidang_minat)
            
            # Jika nilai bukan E, tambahkan SKS ke total
            if nilai_huruf != "E":
                total_sks += sks
    
    st.write("Nilai Mata Kuliah yang telah diambil:")
    for mk, (nilai, bidang) in matkul_terpilih.items():
        st.write(f"{mk}: {nilai}, Bidang Peminatan: {', '.join(bidang)}")
    
    if st.button("Hitung Rekomendasi Bidang Minat"):
        if total_sks < 100:
            st.write("Tidak dapat melakukan rekomendasi bidang minat! SKS yang diambil tidak mencukupi 100 SKS.")
        else:
            # Urutkan mata kuliah berdasarkan jumlah bidang peminatan (dari terbanyak ke tersedikit)
            matkul_bidang_minat = dict(sorted(matkul_bidang_minat.items(), key=lambda item: len(item[1][1]), reverse=True))
            massa_keyakinan = [{tuple(bidang): nilai, (): 1 - nilai} for nilai, bidang in matkul_bidang_minat.values()]

            while len(massa_keyakinan) > 1:
                m1 = massa_keyakinan.pop(0)
                m2 = massa_keyakinan.pop(0)
                hasil_kombinasi = kombinasi_massa_keyakinan(m1, m2)
                massa_keyakinan.insert(0, hasil_kombinasi)
            
            # Hasil akhir setelah semua kombinasi
            if massa_keyakinan:
                st.write("Rekomendasi Bidang Minat:")
                rekomendasi_akhir = massa_keyakinan[0]
                for bidang, nilai in rekomendasi_akhir.items():
                    if bidang:
                        bidang_str = ', '.join(bidang)
                    else:
                        bidang_str = "Tidak Spesifik"
                    st.write(f"Bidang: {bidang_str} dengan keyakinan {nilai:.4f}")

# Fungsi untuk mengeksekusi forward chaining
def forward_chaining(known_facts, rules):
    new_facts = known_facts.copy()
    while True:
        added = False
        for rule in rules["Kondisi"]:
            if "THEN" in rule:
                condition, result = rule.split(" THEN ")
                conditions = condition.replace("IF ", "").split(" AND ")
                if all(cond in new_facts for cond in conditions):
                    if result not in new_facts:
                        new_facts.append(result)
                        added = True
        if not added:
            break
    return new_facts

# Fungsi untuk menampilkan halaman forward chaining
def halaman_fc():
    st.title("Penalaran Forward Chaining")
    st.write("Pilih mata kuliah untuk penalaran:")

    df = pd.DataFrame(matkul)
    df_filtered = df[df["Kode Fakta dan Aturan"].notnull()] # memfilter / mengambil data berdasarkan kode fakta dan aturan yang tidak kosong

    selected_courses = st.multiselect("Mata Kuliah", options=df_filtered["Nama MK"])

    if st.button("Hitung Bidang Minat"):
        selected_facts = [matkul["Kode Fakta dan Aturan"][matkul["Nama MK"].index(course)] for course in selected_courses]
        inferred_facts = forward_chaining(selected_facts, fcRule)

        bidang_minat = set()
        for fact in inferred_facts:
            if fact in ["SI", "SC", "JK"]:
                bidang_minat.add(fact)

        st.write("Bidang Minat yang Direkomendasikan:", ", ".join(bidang_minat))

# Streamlit layout
st.set_page_config(page_title="Sistem Pakar Penentuan Bidang Minat", layout="wide")
st.title("Sistem Pakar Penentuan Bidang Minat")

# Sidebar untuk navigasi halaman
st.sidebar.title("Navigasi")
page = st.sidebar.selectbox("Pilih halaman", ["Dashboard", "Bidang Minat", "Informasi Mata Kuliah", "Nilai Mata Kuliah", "Fakta dan Aturan", "Rule Forward Chaining", "Perhitungan Dempster Shafer", "Penalaran Forward Chaining"])

# Menampilkan halaman berdasarkan pilihan di sidebar
if page == "Dashboard":
    dashboard()
elif page == "Bidang Minat":
    bidang_minat()
elif page == "Informasi Mata Kuliah":
    informasi_mata_kuliah()
elif page == "Nilai Mata Kuliah":
    nilai_mata_kuliah()
elif page == "Fakta dan Aturan":
    fakta_aturan()
elif page == "Rule Forward Chaining":
    rule_fc()
elif page == "Perhitungan Dempster Shafer":
    halaman_ds()
elif page == "Penalaran Forward Chaining":
    halaman_fc()