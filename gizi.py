import streamlit as st
from streamlit_option_menu import option_menu

#navigasi sidebar
with st.sidebar:
    selected = option_menu(
        menu_title = 'Main Menu',
        options = ['Beranda', 'Gizi Harianmu'],
    )

#halaman beranda
if (selected == 'Beranda') :
    st.title('Nutri-Cal')
    st.markdown(':orange[Hi, Nutri-Calen]. :wave:')
    st.write('Kenapa sih kita harus menghitung kebutuhan gizi?')
    st.write('Apakah sepenting itu?')
    st.write('Nutri-calen, Menurut FAO (Organisasi Pangan dan Pertanian) mengacu pada data estimasi rata-rata jumlah penduduk kurang gizi di Asia Tenggara periode 2019-2021 Indonesia tercatat sebagai negara dengan jumlah penduduk kurang gizi tertinggi di kawasan Asia Tenggara dengan jumlah 17,7 juta orang. Data ini menunjukan bahwa kebutuhan gizi sangat penting bagi tubuh kita, dengan mengetahui kebutuhan gizi  nutri-calen dapat mengetahui jumlah kontribusi suatu makanan atau minuman terhadap kebutuhan gizi harian, sehinggaa dapat menghindarkan kita dari risiko malnutrisi (kekurangan gizi) dan risiko overnutrition (kelebihan nutrisi)  maupun penyakit khususnya yang disebabkan oleh asupan gizi yang tidak akurat dari makanan dan minuman kita sehari-hari.')
    st.write('Bagaimana cara menghitung kebutuhan gizi harian? :thinking_face:')
    st.write('tenang, kami hadir untuk anda.')
    st.write('Aplikasi ini adalah aplikasi yang memudahkan nutri-calen untuk menghitung kebutuhan gizi tubuh. Nutri-calen dapat menentukan kebutuhan harian gizi dengan detail, karena dalam aplikasi ini kami memberikan hasil kebutuhan kalori harian, protein, lemak dan karbohidrat yang diperluka oleh tubuh anda. Aplikasi ini mengacu pada rumus Harris-Benedict sehingga hasil yang akan tampilkan 100% akurat.')
        
if (selected == 'Gizi Harianmu') :
    
    # fungsi untuk menghitung kebutuhan kalori harian
    def hitung_kebutuhan_kalori(jenis_kelamin, berat_badan, tinggi_badan, usia, aktivitas):
        if jenis_kelamin == 'Laki-laki':
            bmr = 66.5 + (13.7 * berat_badan) + (5 * tinggi_badan) - (6.8 * usia)
        else:
            bmr = 655 + (9.6 * berat_badan) + (1.8 * tinggi_badan) - (4.7 * usia)
        if aktivitas == 'Sangat jarang olahraga':
            faktor = 1.2
        elif aktivitas == 'Jarang olahraga (1-3 hari/minggu)':
            faktor = 1.375
        elif aktivitas == 'Normal olahraga (3-5 hari/minggu)':
            faktor = 1.55
        elif aktivitas == 'Sering olahraga (6-7 hari/minggu)':
            faktor = 1.725
        else:
            faktor = 1.9
        kebutuhan_kalori = round(bmr * faktor)
        return kebutuhan_kalori

    # fungsi untuk menghitung kebutuhan gizi harian
    def hitung_kebutuhan_gizi(kebutuhan_kalori):
        protein = round(kebutuhan_kalori * 0.15 / 4)
        lemak = round(kebutuhan_kalori * 0.15 / 9)
        karbohidrat = round(kebutuhan_kalori * 0.6 / 4)
        return protein, lemak, karbohidrat

    # tampilan form input
    st.header('Kalkulator Kebutuhan Gizi Harian')
    jenis_kelamin = st.selectbox('Jenis Kelamin', [' ','Laki-laki', 'Perempuan'])
    berat_badan = st.number_input('Berat Badan (kg)', min_value=0, max_value=200)
    tinggi_badan = st.number_input('Tinggi Badan (cm)', min_value=0, max_value=300)
    usia = st.number_input('Usia (tahun)', min_value=0, max_value=120)
    aktivitas = st.selectbox('Aktivitas Fisik', [' ','Sangat jarang olahraga', 'Jarang olahraga (1-3 hari/minggu)', 'Normal olahraga (3-5hari/minggu)', 'Sering olahraga (6-7 hari/minggu)', 'Sangat sering olahraga (setiap hari bisa dua kali olahraga)'])
    submit_button = st.button('cek status gizi')

    # jika tombol submit ditekan, hitung kebutuhan gizi dan tampilkan hasil
    if submit_button:
        kebutuhan_kalori = hitung_kebutuhan_kalori(jenis_kelamin, berat_badan, tinggi_badan, usia, aktivitas)
        protein, lemak, karbohidrat = hitung_kebutuhan_gizi(kebutuhan_kalori)
        st.subheader('Kebutuhan Gizi Harian')
        st.write(f'Kebutuhan kalori: {kebutuhan_kalori} kalori')
        st.write(f'Protein: {protein} gram')
        st.write(f'Lemak: {lemak} gram')
        st.write(f'Karbohidrat: {karbohidrat} gram')
