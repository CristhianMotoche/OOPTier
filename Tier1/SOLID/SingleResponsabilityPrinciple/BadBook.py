# Responsabilidades
# - Representar un libro del mundo real
# - Imprimir el contenido del Book en consola
# - Formatear el Book en HTML
class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 1

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def turn_page(self):
        self.page += 1

    # Si posteriormente se desea cambiar la forma en la cual se imprime el
    # contenido de la página actual, este método tendrá que cambiar, haciendo
    # que la clase cambie cuando no es su respondabilidad hacer eso.
    def print_current_page(self):
        print("The content of the current page")
        print(self.page)

    def html_formatter(self):
        html = "<div class='author'>"
        html += self.get_author()
        html += "</div>"
        html += "<div class='title'>"
        html += self.get_title()
        html += "</div>"
        html += "<div class='content'>"
        html += "The content of the current page"
        html += "</div>"
        html += "<div class='page'>"
        html += str(self.page)
        html += "</div>"
        return html

# Main
currentBook = Book('Un Mundo Feliz', 'Aldous Huxley')
print(currentBook.html_formatter())
