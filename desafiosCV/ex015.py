qt_dia = int(input("Digite quantos dias você alugou o carro: "))
qt_km_corrido = float(input("Digite quantos quilômetros foram percorridos: "))
vl_dia = 60
vl_km_corrido = 0.15
vl_pagmnt_dia = qt_dia * vl_dia
vl_pagmnt_km = qt_km_corrido * vl_km_corrido
vl_pagmnt_total = vl_pagmnt_dia + vl_pagmnt_km
print("Você deve pagar: ")
print("\tDias alugados:\t{} x R${:.2f} = \tR${:.2f}".format(qt_dia, vl_dia, vl_pagmnt_dia))
print("\tkm corridos:\t{:.1f}km x R${:.2f} = \tR${:.2f}".format(qt_km_corrido, vl_km_corrido, vl_pagmnt_km))
print("\tO total foi: \t \t \t \tR${:.2f}".format(vl_pagmnt_total))
