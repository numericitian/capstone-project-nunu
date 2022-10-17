import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats

st.set_page_config(layout = "wide")

st.title("Apakah Kecenderungan Membaca Berhubungan pada Penggunaan Media Sosial?")

st.header("Pendahuluan")

st.write("Menurut data dari Digital 2022, "
        "penggunaan media sosial telah mencapai lebih dari 50 persen jumlah penduduk dari 26 negara. "
         "Tercatat bahwa dari 5,06 miliar penduduk terdapat 3,15 miliar penduduk yang merupakan pengguna aktif media sosial. "
         "Angka tersebut terbilang mencengangkan untuk saat ini. "
         "Sementara durasi rata-rata penggunaan media sosial per orang selama 1 pekan tercatat paling tinggi di Filipina, "
         "yaitu 1785 menit dan terendah di Jepang, yaitu 357 menit. "
         "Apabila dibandingkan dengan durasi rata-rata membaca buku per orang selama 1 pekan hal ini akan berbeda jauh. "
         "Menurut data dari Books of Brilliance 2022, "
         "durasi tertinggi tercatat sebesar 642 menit (India) dan terendah tercatat sebesar 186 menit (Korea Selatan). "
         "Hal ini menjadi pertanyaan bukan? Apakah durasi membaca buku itu mempunyai hubungan dengan banyaknya pengguna aktif media sosial? "
         "atau durasi membaca itu mempunyai hubungan dengan waktu seseorang yang dihabiskan di media sosial? "
         "Oleh karena itu, mari kita bahas perlahan-lahan.")

st.header("Dataset")

st.subheader("Berikut ini beberapa data disajikan dalam bentuk tabel")

df = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vQWWTMl8xYI_Ket7jIEr_C9UP0b7haqRH8CjLh5QKELHdRBmCHnWUjXp0mkkwZqxw/pub?output=xlsx")
st.dataframe(df)

st.write("Dalam tabel tersebut, belum terdapat kolom persentase jumlah pengguna aktif media sosial "
         "serta jumlah penduduk dan jumlah pengguna aktif media sosial belum dalam satuan juta. "
         "Untuk menambahkan hal itu, lakukan langkah berikut.")

df['Jumlah Penduduk_Juta'] = df['Jumlah Penduduk']/1000000
df['Jumlah Pengguna Aktif Media Sosial_Juta'] = df['Jumlah Pengguna Aktif Media Sosial']/1000000
df['Pengguna Aktif Media Sosial_Persen'] = (df['Jumlah Pengguna Aktif Media Sosial']/df['Jumlah Penduduk']) * 100

st.code("df['Jumlah Penduduk_Juta'] = df['Jumlah Penduduk']/1000000")
st.code("df['Jumlah Pengguna Aktif Media Sosial_Juta'] = df['Jumlah Pengguna Aktif Media Sosial']/1000000")
st.code("df['Pengguna Aktif Media Sosial_Persen'] = (df['Jumlah Pengguna Aktif Media Sosial']/df['Jumlah Penduduk']) * 100")

st.write("Sehingga akan menampilkan tabel baru berikut ini:")

st.dataframe(df)

st.subheader("Statistika Deskriptif")

st.dataframe(df.describe())

st.write("Dari tabel statistika deskriptif di atas, rata-rata dari durasi rata-rata membaca buku ke-26 negara sebesar 381.69 menit dengan durasi tertinggi sebesar 642 menit dan terendah sebesar 186 menit. "
         "Rata-rata dari durasi rata-rata penggunaan media sosial, yakni 1018.15 menit. Tertinggi sebesar 1785 menit dan terendah dengan durasi 357 menit. "
         "Sedangkan rata-rata persentase dari jumlah pengguna aktif media sosial sebesar 76.76%. Persentase terendah sebesar 33.35% dan tertinggi sebesar 91.21%.")

st.write("Sekarang, hal yang menjadi pertanyaan adalah negara apa saja yang memiliki durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial tertinggi?, "
         "negara apa saja yang memiliki durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial terendah? "
         "serta negara apa saja yang berada di bawah dan di atas rata-rata apabila ditinjau dari durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial?")
st.write("Oleh karena itu, di bawah ini akan ditampilkan beberapa chart untuk menjawab pertanyaan tersebut.")

st.header("Horizontal Bar Chart")

st.subheader("Horizontal Bar Chart Berdasarkan Durasi Membaca Buku")

def show_values(axs, orient="v", space=.01):
    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height()*0.01)
                value = '{:.1f}'.format(p.get_height())
                ax.text(_x, _y, value, ha="center") 
        elif orient == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height()*0.5)
                value = '{:.0f}'.format(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)

st.set_option('deprecation.showPyplotGlobalUse', False)

plt.figure(figsize=(12, 9))
g_membaca = sns.barplot(x = 'Durasi Membaca',
            y = 'Negara',
            data = df.sort_values('Durasi Membaca', ascending = False))
g_membaca.set_xlabel('Durasi Membaca Buku (Menit)')
g_membaca.set_ylabel('')
show_values(g_membaca, "h", space=1)
st.pyplot()

st.write("Dari bar chart, terlihat bahwa India merupakan negara tertinggi yang memiliki durasi rata-rata membaca buku per orang dalam sepekan "
         "dan terendah diduduki oleh Korea Selatan dengan durasi 186 menit. "
         "Lalu, negara mana saja yang menempati posisi di atas rata-rata dan di bawah rata-rata dari durasi rata-rata membaca buku? "
         "Berikut ini akan ditampilkan 2 bar chart yang akan menjawab pertanyaan tersebut.")

plt.figure(figsize=(8, 3))
p = sns.barplot(x = 'Durasi Membaca',
            y = 'Negara',
            data = df[df['Durasi Membaca'] > 381.69].sort_values('Durasi Membaca', ascending = False))
p.set_xlabel('Durasi Membaca Buku (Menit)', size = 8)
p.set_ylabel('')
for label in (p.get_xticklabels() + p.get_yticklabels()):
    label.set_fontsize(8)
show_values(p, "h", space=1)
st.pyplot()

st.write("Bar Chart di atas menunjukkan bahwa ada 11 negara yang memiliki durasi membaca buku di atas rata-rata dari 26 negara yang ada. "
         "Terdapat negara (1) India, (2) Thailand, (3) China, (4) Filipina, (5) Mesir, (6) Rusia "
         "(7) Perancis, (8) Swedia, (9) Saudi Arabia, (10) Hongkong, dan (11) Polandia.")

st.write("Berarti, terdapat 15 negara yang memiliki durasi membaca buku di bawah rata-rata. Negara apa saja itu? "
         "Berikut ini negara-negara yang memiliki nilai di bawah rata-rata dari durasi rata-rata membaca buku per orang dalam sepekan.")

plt.figure(figsize=(9, 5))
a = sns.barplot(x = 'Durasi Membaca',
            y = 'Negara',
            data = df[df['Durasi Membaca'] < 381.69].sort_values('Durasi Membaca', ascending = False))
a.set_xlabel('Durasi Membaca Buku (Menit)', size = 9)
a.set_ylabel('')
for label in (a.get_xticklabels() + a.get_yticklabels()):
    label.set_fontsize(9)
show_values(a, "h", space=1)
st.pyplot()

st.write("Negara-negara yang dimaksud adalah Australia, Afrika Selatan, Indonesia, Turki, Kanada, Spanyol, "
         "United States, Jerman, Italia, Meksiko, United Kingdom, Brazil, Taiwan, Jepang, dan Korea Selatan dengan durasi masing-masing dapat dilihat melalui bar chart di atas.")

st.subheader("Horizontal Bar Chart Berdasarkan Durasi Penggunaan Media Sosial")

plt.figure(figsize=(12, 8))
b = sns.barplot(x = 'Durasi Media Sosial',
            y = 'Negara',
            data = df.sort_values('Durasi Media Sosial', ascending = False))
b.set_xlabel('Penggunaan Media Sosial (Menit)')
b.set_ylabel('')
show_values(b, "h", space=1)
st.pyplot()

st.write("Berbeda dengan negara yang memiliki durasi tertinggi dan terendah dari rata-rata membaca buku, Filipina menduduki posisi pertama untuk durasi penggunaan media sosial per orang selama 1 pekan, "
         "sedangkan Jepang yang terendah dengan masing-masing durasi, yaitu 1785 menit dan 357 menit.")
st.write("Negara yang memiliki durasi penggunaan media sosial di atas rata-rata adalah sebagai berikut.")

plt.figure(figsize=(10, 3))
c = sns.barplot(x = 'Durasi Media Sosial',
            y = 'Negara',
            data = df[df['Durasi Media Sosial'] > 1018.15].sort_values('Durasi Media Sosial', ascending = False))
c.set_xlabel('Penggunaan Media Sosial (Menit)', size = 10)
c.set_ylabel('')
for label in (c.get_xticklabels() + c.get_yticklabels()):
    label.set_fontsize(10)
show_values(c, "h", space=1)
st.pyplot()

st.write("Adapun beberapa negara yang memiliki durasi rata-rata penggunaan media sosial per orang selama sepekan di bawah rata-rata jika membandingkan dari 26 negara tersebut adalah sebagai berikut.")

plt.figure(figsize=(11, 5))
d = sns.barplot(x = 'Durasi Media Sosial',
            y = 'Negara',
            data = df[df['Durasi Media Sosial'] < 1018.15].sort_values('Durasi Media Sosial', ascending = False))
d.set_xlabel('Penggunaan Media Sosial (Menit)', size = 11)
d.set_ylabel('')
for label in (d.get_xticklabels() + d.get_yticklabels()):
    label.set_fontsize(11)
show_values(d, "h", space=1)
st.pyplot()

st.write("Negara-negara dengan durasi penggunaan media sosial di atas rata-rata, yaitu "
         "Filipina, Brazil, Afrika Selatan, Meksiko, Indonesia, Korea Selatan, Saudi Arabia, Mesir, Turki, Thailand, dan Rusia. "
         "Sedangkan negara selain 11 di atas merupakan negara yang memiliki durasi di bawah rata-rata, seperti India, United States, China, hingga Jepang.")

st.subheader("Horizontal Bar Chart Berdasarkan Persentase Jumlah Pengguna Aktif Media Sosial")

def show_values(axs, orient="v", space=.01):
    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height()*0.01)
                value = '{:.1f}'.format(p.get_height())
                ax.text(_x, _y, value, ha="center") 
        elif orient == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height()*0.5)
                value = '{:.2f}'.format(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)

plt.figure(figsize=(13, 9))
g_pengguna = sns.barplot(x = 'Pengguna Aktif Media Sosial_Persen',
            y = 'Negara',
            data = df.sort_values('Pengguna Aktif Media Sosial_Persen', ascending = False))
g_pengguna.set_xlabel('Persentase Pengguna Aktif Media Sosial')
g_pengguna.set_ylabel('')

show_values(g_pengguna, "h", space=1)
st.pyplot()

st.write("Chart di atas menampilkan bahwa Korea Selatan memiliki persentase tertinggi, yaitu 91.21% dibandingkan dengan negara lainnya, "
         "sedangkan India memiliki persentase terendah, yaitu sebesar 33.36%.")
st.write("Lalu, negara-negara mana saja yang termasuk negara yang memiliki persentase jumlah pengguna aktif media sosial di atas rata-rata?. "
         "Berikut ini ditampilkan bar chart untuk menjawab pertanyaan tersebut.")

plt.figure(figsize=(12, 5))
g_pengguna1 = sns.barplot(x = 'Pengguna Aktif Media Sosial_Persen',
            y = 'Negara',
            data = df[df['Pengguna Aktif Media Sosial_Persen'] > 76.76].sort_values('Pengguna Aktif Media Sosial_Persen', ascending = False))
g_pengguna1.set_xlabel('Persentase Pengguna Aktif Media Sosial', size = 12)
g_pengguna1.set_ylabel('')
for label in (g_pengguna1.get_xticklabels() + g_pengguna1.get_yticklabels()):
    label.set_fontsize(12)
show_values(g_pengguna1, "h", space=1)
st.pyplot()

st.write("Ternyata ada banyak negara yang termasuk ke dalam negara yang memiliki persentase jumlah pengguna aktif media sosial di atas rata-rata. "
         "Total negara yang termasuk dimulai dari Korea Selatan (91.21%), Swedia (90.78%), Taiwan (89.44%), Hongkong (88.13%), hingga terbawah yakni Meksiko (78.30%).")

st.write("Kemudian, negara-negara yang memiliki persentase jumlah pengguna aktif media sosial di bawah rata-rata adalah sisa dari 18 negara pada bar chart sebelumnya.")

plt.figure(figsize=(6, 2))
g_pengguna2 = sns.barplot(x = 'Pengguna Aktif Media Sosial_Persen',
            y = 'Negara',
            data = df[df['Pengguna Aktif Media Sosial_Persen'] < 76.76].sort_values('Pengguna Aktif Media Sosial_Persen', ascending = False))
g_pengguna2.set_xlabel('Persentase Pengguna Aktif Media Sosial', size = 6)
g_pengguna2.set_ylabel('')
for label in (g_pengguna2.get_xticklabels() + g_pengguna2.get_yticklabels()):
    label.set_fontsize(6)
show_values(g_pengguna2, "h", space=1)
st.pyplot()

st.write("Negara-negara tersebut adalah Rusia, Polandia, Italia, Indonesia, China, Mesir, Afrika Selatan, dan India. Sekarang, hal yang menjadi pertanyaan adalah "
         "negara apa saja yang memiliki durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial di atas angka rata-rata dari ketiga parameter tersebut?")

membaca_atas = df["Durasi Membaca"] > 381.69
medsos_atas = df["Durasi Media Sosial"] > 1018.15
pengguna_atas = df['Pengguna Aktif Media Sosial_Persen'] > 76.76
data_atas = df[membaca_atas & medsos_atas & pengguna_atas].set_index("Negara")
st.dataframe(data_atas)

st.write("Dari 26 negara yang terdapat di dataset, hanya ada 3 negara yang memiliki durasi membaca, durasi penggunaan media sosial, "
         "dan persentase jumlah pengguna aktif media sosial di atas rata-rata, yaitu Saudi Arabia, Filipina, dan Thailand.")
st.write("Pertanyaan selanjutnya adalah bagaimana perbandingan jumlah penduduk dengan jumlah pengguna aktif media sosial?. Berikut ini disajikan 5 negara teratas dan terbawah berdasarkan jumlah penduduknya.")

st.subheader("Horizontal Bar Chart Jumlah Penduduk vs Jumlah Pengguna Aktif Media Sosial")

st.write("5 Negara Tertinggi Berdasarkan Jumlah Penduduk")
f, ax = plt.subplots(figsize = (28,6))
sns.set_color_codes('pastel')
sns.barplot(x = 'Jumlah Penduduk_Juta', y = 'Negara', data = df.sort_values('Jumlah Penduduk_Juta', ascending = False).head(5),
            label = 'Jumlah Penduduk', color = 'b', edgecolor = 'w')
sns.set_color_codes('muted')
sns.barplot(x = 'Jumlah Pengguna Aktif Media Sosial_Juta', y = 'Negara', 
            data = df.sort_values('Jumlah Penduduk_Juta', ascending = False).head(5),
            label = 'Jumlah Pengguna Aktif Media Sosial', color = 'b', edgecolor = 'w')
ax.legend(ncol = 2, loc = 'lower right')
sns.despine(left = True, bottom = True)

ax.set_xlabel('Juta (Orang)', size = 15)
ax.set_ylabel('')

for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontsize(15)

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    ax.text(x+width/1.010, 
            y+height/2, 
            '{:.0f}'.format(width), 
            horizontalalignment='center', 
            verticalalignment='center',
            color='black',
            fontsize=15,
            **{'fontname' : 'Arial'})

plt.show()
st.pyplot()

st.write("5 Negara Terendah Berdasarkan Jumlah Penduduk")
fig, ax = plt.subplots(figsize = (28,6))
sns.set_color_codes('pastel')
sns.barplot(x = 'Jumlah Penduduk_Juta', y = 'Negara', data = df.sort_values('Jumlah Penduduk_Juta', ascending = False).tail(5),
            label = 'Jumlah Penduduk', color = 'b', edgecolor = 'w')
sns.set_color_codes('muted')
sns.barplot(x = 'Jumlah Pengguna Aktif Media Sosial_Juta', y = 'Negara', 
            data = df.sort_values('Jumlah Penduduk_Juta', ascending = False).tail(5),
            label = 'Jumlah Pengguna Aktif Media Sosial', color = 'b', edgecolor = 'w')
ax.legend(ncol = 2, loc = 'lower right')
sns.despine(left = True, bottom = True)

ax.set_xlabel('Juta (Orang)', size = 15)
ax.set_ylabel('')

for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontsize(15)

for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    x, y = p.get_xy() 
    ax.text(x+width/1.010, 
            y+height/2, 
            '{:.2f}'.format(width), 
            horizontalalignment='center', 
            verticalalignment='center',
            color='black',
            fontsize=15,
            **{'fontname' : 'Arial'})
plt.show()

st.pyplot()

st.write("Berdasarkan kedua bar chart di atas, jumlah pengguna aktif media sosial jika dibandingkan dengan jumlah penduduk di 10 negara tersebut "
         "hampir semuanya memiliki perbandingan lebih dari separuh penduduknya aktif dalam bermedia sosial.")

st.write("Terakhir, bar chart akan menampilkan durasi membaca dengan durasi penggunaan media sosial di setiap negara.")

st.subheader("Horizontal Bar Chart Durasi Membaca vs Durasi Penggunaan Media Sosial")

# convert to long form
data_akhir1= df[['Negara', 'Durasi Membaca', 'Durasi Media Sosial']]
data_akhir2 = (data_akhir1.melt(id_vars='Negara', var_name='Durasi', value_name='Jumlah')
       .sort_values('Jumlah', ascending=False).reset_index(drop=True))
data_akhir2['Durasi'] = data_akhir2['Durasi'].replace(['Durasi Media Sosial','Durasi Membaca'],
                                     ['Durasi Penggunaan Media Sosial','Durasi Membaca Buku'])
# plot
fig, ax = plt.subplots(figsize=(16, 10))
sns.barplot(x='Jumlah', y='Negara', data=data_akhir2, hue='Durasi', ax=ax)
ax.set_yticklabels(ax.get_yticklabels(), rotation=0)

for c in ax.containers:
    # set the bar label
    ax.bar_label(c, fmt='%.0f', label_type='edge', padding=1)
    
# pad the spacing between the number and the edge of the figure
ax.margins(x=0.1)

# set x label and y label
ax.set_xlabel('Durasi (Menit)')
ax.set_ylabel('')

st.pyplot()

st.write("Berdasarkan bar chart di atas, 26 negara semuanya memiliki durasi rata-rata penggunaan media sosial paling lama jika dibandingkan dengan durasi rata-rata membaca buku per orang dalam 1 pekan. "
         "Hal ini mungkin disebabkan orang-orang di tiap negara lebih intens dalam melakukan komunikasi, mencari informasi, dsb setiap harinya. "
         "Terlepas dari alasan apapun itu, mari selanjutnya melihat plot sebaran data antara durasi membaca dan durasi penggunaan media sosial, "
         "serta durasi membaca dan persentase jumlah pengguna aktif media sosial.")

st.header("Hubungan antar 2 Variabel")

st.subheader("Durasi Membaca vs Persentase Pengguna Aktif Media Sosial")

c1, c2 = st.columns(2)
with c1:
        a = sns.scatterplot(x = 'Pengguna Aktif Media Sosial_Persen',
                y = 'Durasi Membaca',
                data = df)
        a.set_xlabel('Pengguna Aktif Media Sosial (Persen)')
        a.set_ylabel('Durasi Membaca Buku (Menit)')
        plt.show()
        st.pyplot()
with c2:
        st.write("Dari scatter plot di samping, hubungan 2 variabel tersebut menunjukkan plot memiliki hubungan yang negatif, "
                 "berarti bahwa semakin berkurang pengguna aktif media sosial, maka semakin lama durasi seseorang untuk menghabiskan waktunya dalam membaca buku. "
                 "Sebaliknya, semakin meningkat pengguna aktif media sosial, maka semakin sedikit durasi membacanya.")

d1,d2 = st.columns(2)
with d1:
        corr1 = df[["Pengguna Aktif Media Sosial_Persen", "Durasi Membaca"]].corr()
        st.table(corr1)
        st.write("Besar korelasi (hubungan) antar 2 variabel ini sebesar 0.56. Hal ini menandakan bahwa hubungan antar 2 variabel ini cukup kuat untuk menentukan ada tidaknya hubungan yang terjadi. "
                 "Selanjutnya, kita akan mencari besar nilai signifikansi (p-value) untuk memastikan benar atau tidaknya terdapat hubungan antar 2 variabel ini.")
        hub1 = scipy.stats.pearsonr(df['Pengguna Aktif Media Sosial_Persen'], df['Durasi Membaca'])
        st.text(hub1)
with d2:
        sns.heatmap(corr1, annot = True)
        st.pyplot()
        
st.write("Nilai signifikansi sebesar 0.002 menunjukkan bahwa variabel durasi membaca buku dan persentase pengguna aktif media sosial terdapat hubungan yang signifikan antar satu dengan yang lainnya.")

st.subheader("Durasi Membaca vs Durasi Penggunaan Media Sosial")

c1, c2 = st.columns(2)
with c1:
        a = sns.scatterplot(x = 'Durasi Media Sosial',
                y = 'Durasi Membaca',
                data = df)
        a.set_xlabel('Durasi Penggunaan Media Sosial (Menit)')
        a.set_ylabel('Durasi Membaca Buku (Menit)')
        plt.show()
        st.pyplot()
with c2:
        st.write("Dari scatter plot di samping, hubungan 2 variabel tersebut menunjukkan plot memiliki hubungan yang positif, "
                 "berarti bahwa semakin lama durasi menggunakan media sosial, maka semakin lama durasi seseorang untuk menghabiskan waktunya dalam membaca buku. "
                 "Sebaliknya, semakin singkat durasi menggunakan media sosial, maka semakin singkat juga durasi membacanya. "
                 "Kalau secara logika, simpulan itu tentu tidak masuk dinalar kita. Akan tetapi, mari kita cek besar hubungan dan nilai signifikansi dari 2 variabel tersebut agar lebih meyakinkan dari simpulan yang ditetapkan di awal.")

d1,d2 = st.columns(2)
with d1:
        corr2 = df[["Durasi Media Sosial", "Durasi Membaca"]].corr()
        st.table(corr2)
        st.write("Besar korelasi (hubungan) antar 2 variabel ini sebesar 0.14. Hal ini menandakan bahwa hubungan antar 2 variabel ini cukup lemah untuk menentukan ada tidaknya hubungan yang terjadi. "
                 "Selanjutnya, kita akan mencari besar nilai signifikansi (p-value) untuk memastikan benar atau tidaknya terdapat hubungan antar 2 variabel ini.")
        hub2 = scipy.stats.pearsonr(df['Durasi Media Sosial'], df['Durasi Membaca'])
        st.text(hub2)
with d2:
        sns.heatmap(corr2, annot = True)
        st.pyplot()
        
st.write("Nilai signifikansi sebesar 0.48 menunjukkan bahwa variabel durasi membaca buku dan durasi penggunaan media sosial tidak terdapat hubungan yang signifikan satu dengan yang lainnya.")

st.header("Simpulan")

st.write("1. Rata-rata dari masing-masing durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial, yaitu "
         "381.69 menit, 1018.15 menit, dan 76.76%")
st.write("2. Negara yang memiliki durasi membaca, durasi penggunaan media sosial, dan persentase jumlah pengguna aktif media sosial di atas angka rata-rata dari ketiga parameter, "
         "yaitu Saudi Arabia, Filipina, dan Thailand")
st.write("3. Variabel durasi membaca dengan persentase jumlah pengguna aktif media sosial memiliki hubungan yang signifikan dengan besar korelasi (hubungan) 0.56% "
         "dan berkorelasi negatif, artinya semakin berkurang pengguna aktif media sosial, maka semakin lama durasi seseorang untuk menghabiskan waktunya dalam membaca buku. Sebaliknya, semakin meningkat pengguna aktif media sosial, maka semakin sedikit durasi membacanya.")
st.write("4. Variabel membaca buku dan durasi penggunaan media sosial tidak terdapat hubungan yang signifikan.")

st.header("Sumber Data")
st.write("https://booksofbrilliance.com/2022/09/14/which-country-reads-the-most-books/")
st.write("https://datareportal.com/reports/digital-2022")
        