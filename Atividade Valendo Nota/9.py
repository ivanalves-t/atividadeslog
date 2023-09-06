premio = 780000.00

primeiro = premio * (46/100)
segundo = premio * (32/100)
terceiro = premio - primeiro - segundo

print(f"""
      
O primeiro ganhador levará para casa: R${primeiro}
O segundo ganhador levará para casa: R${segundo}
E o terceiro ganhador levará para casa R${terceiro}      
 
     """)
