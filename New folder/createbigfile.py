text = """
Ini adalah file besar untuk menguji Zlib Compression dan Base64 Encoding.
Tujuan file ini adalah mengisi ruang dengan teks-teks panjang agar hasil kompresi terasa signifikan.
Kita akan mengulang paragraf ini berkali-kali untuk mencapai ukuran yang besar.
Semangat terus belajar dan bereksperimen dengan Python, Zlib, dan sistem jaringan!
"""

with open("large_file.txt", "w", encoding="utf-8") as f:
    for _ in range(5000):  
        f.write(text + "\n")
