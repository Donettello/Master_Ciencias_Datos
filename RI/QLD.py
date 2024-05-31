import numpy as np
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter

class QLD:
  def __init__(self, freqvector, wordfreqs, mu):
    self.freqvector = freqvector
    self.wordfreqs = wordfreqs
    self.mu = mu
    #self.D

  def search(self, q):
    ranking = []

    for url in self.freqvector.keys():
      rank = 1.0

      # Obtenemos el tamaño del documento
      len_doc = sum(self.freqvector[url].values())
      for w in q:
        # Calculamos el valor p-gorro de la palabra
        p_w = self.p_c(w)

        # Obtenemos la frecuencia de la palabra en el documento
        frec_w_d = self.freqvector[url].get(w, 0)

        # Calculamos su rango con suavizado Dirichlet
        rank *= (frec_w_d + self.mu * p_w)/(len_doc + self.mu)
      ranking.append([url, rank])

    # Eliminamos los documentos con valor menor que cero
    ranking = [(url, cos) for url, cos in ranking if cos > 0]

    # Ordensmos por orden de rango
    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking

  def p_c(self, w):
    '''
      Función que devuelve la probabilidad de la palabra 'w'.
      Necesaria para el suavizado de Dirichlet
    '''
    sum_freq = np.array([self.freqvector[url].get(w, 0) for url in self.freqvector.keys()]).sum()
    len_total = 0
    for url in self.freqvector.keys():
      for w in self.freqvector[url].keys():
        len_total += self.freqvector[url][w]

    return sum_freq / len_total

# La colección: una pequeña lista de URLs web.
urls = ["https://en.wikipedia.org/wiki/Age_of_Enlightenment",
        "https://en.wikipedia.org/wiki/Rationalism",
        "https://en.wikipedia.org/wiki/Scientific_Revolution",
        "https://en.wikipedia.org/wiki/French_Revolution",
        "https://en.wikipedia.org/wiki/Winner%27s_curse",
        "https://en.wikipedia.org/wiki/Simpson%27s_paradox",
        "https://en.wikipedia.org/wiki/Friendship_paradox",
        "https://en.wikipedia.org/wiki/Condorcet_paradox",
        "https://en.wikipedia.org/wiki/Paradox_of_value",
        "https://en.wikipedia.org/wiki/Ship_of_Theseus"
       ]

# Leemos los documentos y quitamos las marcas HTML.
texts = [BeautifulSoup(urlopen(url).read(), "lxml").text.lower() for url in urls]

# Una lista ad-hoc de stopwords.
stoplist = ["also", "could", "p", "pp", "th", "however", "one", "two", "many", "i", "de", "la", "me", "my", "myself", "the", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Nos abstraemos de los detalles reales de indexación, y utilizaremos un manejo muy simplificado del texto.

# Vector de frecuencias para todos los documentos de la colección, usando la subclase de diccionario collections.Counter.
# Para cada documento, separamos el texto en lista de palabras, y Counter genera un diccionario palabra:frecuencia.
# Se construye un diccionario url -> word -> count (se denomina un "índice forward").
freqvector = {url:Counter([word for word in re.findall(r"[^\W\d_]+|\d+", text) if word not in stoplist]) for url, text in zip(urls, texts)}

# Guardamos el vocabulario (el conjunto de todas las palabras que apaercen en los documentos de la colección).
vocabulary = set()
for word in freqvector.values(): vocabulary.update(word)

# Document frequency de cada palabra del vocabulario: nº de documentos que contienen la palabra.
docfreqs = {word:len([url for url in freqvector if word in freqvector[url]]) for word in vocabulary}

# Frecuencia total para cada palabra del vocabulario: nº total de apariciones en la colección.
wordfreqs = {word:sum([freqvector[url][word] for url in freqvector if word in freqvector[url]]) for word in vocabulary}

# Probamos tres consultas.
for q in [['descartes', 'montesquieu'], ['thought', 'experiment', 'identity'], ['market', 'paradox']]:
  print('\n------------------------------')
  print('Query:', q)
  print('\nQuery likelihood + Dirichlet')
  for url, score in QLD(freqvector, wordfreqs, mu=3000).search(q):
    print(score, url)