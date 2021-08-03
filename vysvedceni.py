schoolReport = {
  "Český jazyk": 1,
  "Anglický jazyk": 1,
  "Matematika": 1,
  "Přírodopis": 2,
  "Dějepis": 1,
  "Fyzika": 2,
  "Hudební výchova": 4,
  "Výtvarná výchova": 2,
  "Tělesná výchova": 3,
  "Chemie": 4,
}

sum = 0

print("Jednicku dostal z: ")

for key, value in schoolReport.items():
    sum += value
    if value == 1:
        print(key)

avrg = sum / len(schoolReport)

print("Prumerna znamka je ", avrg)