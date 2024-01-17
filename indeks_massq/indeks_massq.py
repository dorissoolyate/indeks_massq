print("Tere! Olen sinu uus sõber - Python!")
nimi=input("sisesta nimi")
print(nimi + (",oi kui ilus nimi"))
indeks_massq=input(nimi + ("! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if indeks_massq=="1":
    pikkus=int(input("sisesta pikkus"))
    mass=float(input("sisesta mass"))
    indeks=mass/(0.01*pikkus)**2
    print(nimi + "! sinu keha indeks on : {:.1f}" .format(indeks))
else:
    print("Kahju! See on väga kasulik info!")
    print()
    print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")