class Animal():

    def emitir_som(self):
      print('Som emitido...')
      

# class Cachorro - que herda herança Animal
class Cachorro(Animal):
  
  def emitir_som(self):
    print('Au Au..')
    
cachorro = Cachorro()
cachorro.emitir_som()


# class gato - que herda herança Animal
class Gato(Animal):
  
  # aqui eu pego função emitir_som da class Animal e sobre Escrevo
  def emitir_som(self):
    print('Miau Miau...')

gato = Gato()
gato.emitir_som()