# class de carro

class Carro:
  numero_de_rodas = 4
  quantidade_de_portas: 5
  lugares = 5
  
  def acelerar(self):
    print('acelerando..')
    
  def buzinar(self):
    print('Bibi..')
    
  def abrirPorta(self):
    print('abrindo portas..')
    
# estanciando carro a class Carro()
carro = Carro()

# chamando funções do carro
carro.acelerar()
carro.abrirPorta()
carro.buzinar()

# chamando atributos
print(carro.lugares)


# utilizando Herança - chamando a class Carro como paramentro na class Audi;

class Audi(Carro):
  modelo = 'hatch'
  marca = 'audi'
  portas = 2
  ano = 2020
  
audi = Audi()

print(audi.marca)
print(audi.ano)
print(audi.portas)
audi.acelerar()


