print("lütfen yönlendirmelere uygun hareket ediniz. \n Öğrenci bilgi girişini bitirmek için son notu girdikten sonra öğrenci ad-soyad kısmına 'tamam' yazınız.")
isim = list()
ara_sinav = list()
final = list()
ev_odevi = list()
not_ort = list()
d = {}

while True:
    g = input("Girişi bitirmek için TAMAM yazın \nÖğrencinin adı soyadı:\n")
    if g == "TAMAM":
        break
    else:
        isim.append(g)
    ara_sinav.append(int(input("Öğrencinin ara sınav notunu giriniz.\n")))
    final.append(int(input("Öğrencinin final notunu giriniz.\n")))
    ev_odevi.append(int(input("Öğrencinin ev ödevi sınav notunu giriniz.\n")))

print(isim)
print(len(isim))
for j in range(len(isim)):
    not_ort.append((ara_sinav[j] + final[j] + ev_odevi[j])/3)

d["isimler"] = isim
d["ort_notlar"] = not_ort

max_not_index = d["ort_notlar"].index(max(d["ort_notlar"]))

print("Sayın {} Tebrikler! \nNot ortalamanız {} \nEn yüksek nota sahipsiniz. \n Eğitim hayatında başarılar..".format(d["isimler"][max_not_index],max(d["ort_notlar"])))