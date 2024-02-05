import numpy as np

class VSM:
  def __init__(self, freqvector, docfreqs):
    self.freqvector = freqvector
    self.docfreqs = docfreqs

  def search(self, q):
    # Calculamos los cosenos de todos los documentos.
    ranking = [(url, self.dotproduct(url, q) / self.module(url)) for url in self.freqvector]
    # Eliminamos los documentos con coseno = 0.
    ranking = [(url, cos) for url, cos in ranking if cos > 0]
    # Ordenamos.
    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking

  def dotproduct(self, url, q):
    '''
      Esta función se encarga de devolver el producto escalar entre el documento
      'url' y la consulta 'q'
    '''
    return [url[i] * q[i] for i in range(len(url))].sum()

  def module(self, url):
    '''
      Esta función se encarga de devolver el módulo del documento 'url'.
    '''
    return np.sqrt([url[i]^2 for i in range(len(url))].sum())

  def tf(self, word, url):
    '''
      Esta función se encarga de devolver el valor tf de la palabra 'word' del
      documento 'url'
    '''
    pass

  def idf(self,word):
    '''
      Esta función se encarga de devolver el valor 'idf' de la palabra 'word'
    '''
    pass