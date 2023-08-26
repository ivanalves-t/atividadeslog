'''
4. As idades das pessoas de um determinado grupo são 10, 12, 15 e 17
anos. Calcule e exiba a média de idade do grupo, e a variação
percentual da média das idades caso uma pessoa de 16 anos se junte
ao grupo.
'''

age1 = 10
age2 = 12
age3 = 15
age4 = 17
age5 = 16

media_idade = (age1+age2+age3+age4)/4
media_idade2 = (age1+age2+age3+age4+age5)/5
percentual = ((media_idade2 - media_idade)/media_idade)*100

print(f'A média de idade do grupo é de {media_idade} anos')
print(f'A variação percentual da media, caso uma pessoa de 16 anos se unisse ao grupo é de {percentual:.1f}%')
