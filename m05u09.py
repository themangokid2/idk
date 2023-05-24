# läs filen och spara innehållet i en variabel med read()
with open("provpoäng2.txt", "r") as file:
    content = file.read()

# splitta innehållet till varje lina och dela varje lina till ett namn och poäng
lines = content.split('\n')

# spara namnen och resultaten som en tuple i en lista
names_scores = []
for line in lines:
    name, score = line.split('|')
    names_scores.append((name, int(score)))

# sorterar listan baserad på resultaten
names_scores.sort(key=lambda x: x[1])

# printar resultatet
for student, score in names_scores:
    print(f"{student}|{score}")


# tar sifforna ur listan med en for loop
scores = []

for line in lines:
    if line:
        student, score = line.split("|")
        scores.append(int(score))

# enkel beräkning
medelvarde = sum(scores) / len(scores)

#enkel print
print("medelvärdet är ", medelvarde)

worst_student, worst_score = names_scores[0] # tar första namnet i listan då listan är redan sorterad

best_student, best_score = names_scores[-1] # tar sista namnet i listan då listan är redan sorterad

print(f"den sämsta eleven är {worst_student} som fick {worst_score}")
print(f"den bästa eleven är {best_student} som fick {best_score}")