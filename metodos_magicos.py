"""
POO - Métodos Mágicos

Métodos Mágicos são todos os métodos que utilizam dunder.

dunder <- Double Underscore


"""

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)


print(livro1) 
print(livro2)