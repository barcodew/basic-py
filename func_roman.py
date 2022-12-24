def roman(numbers):
  roman_dict = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X"
  }
  return roman_dict[numbers]

angka = int(input("Masukkan Angka   :"))

print(roman(angka))
