nota_lab = float(input('Digite a nota do Laboratório '))
a_semestr = float(input('Digite a nota da Avaliação do Semestre '))
final_exam = float(input('Digite a nota do Exame Final '))

final_lab = nota_lab * 0.2
final_semestr = a_semestr * 0.3
f_final_exam = final_exam * 0.5

final_media = (final_lab+final_semestr+f_final_exam)

if final_media >=0 and final_media <= 2.9:
    print('Reprovado')
elif final_media >=3 and final_media <=4.9:
    print('Recuperação')
else:
    print('Aprovado')
