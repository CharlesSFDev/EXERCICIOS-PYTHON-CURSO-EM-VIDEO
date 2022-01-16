#CÓDIGO QUE RECEBE UM VALOR DE TEMPERATURA EM CELSIUS E A CONVERTE PARA FAHRENHEIT

tempCelsius = float(input('Digite o valor da temperatura em º Celsius: '))

tempFahrenheit = ((9/5)*tempCelsius) + 32

print('O valor digitado pelo usuário, equivalente a {}ºC, em ºF é igual a {}'.format(tempCelsius,tempFahrenheit))