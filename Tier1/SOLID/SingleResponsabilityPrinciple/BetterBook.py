#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import abstractmethod

# Responsabilidades:
# - Representar a un libro del mundo real
class Book(object):
    def __init__(self, title, author):
        self.title  = title
        self.author = author
        self.page = 1

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def turn_page(self):
        self.page += 1

    def get_current_page(self):
        return "The content of the current page"

class IHTMLFomater(object):
    @abstractmethod
    def html_formatter(self):
        pass

# Responsabilidades:
# - Transformar un Book en Html
class BookHTML(IHTMLFomater):
    def html_formatter(self, book):
        html = "<div class='author'>"
        html += book.get_author()
        html += "</div>"
        html += "<div class='title'>"
        html += book.get_title()
        html += "</div>"
        html += "<div class='content'>"
        html += book.get_current_page()
        html += "</div>"
        html += "<div class='page'>"
        html += str(book.page)
        html += "</div>"
        return html

class IPrinter(object):
    @abstractmethod
    def printPage(self, obj):
        pass

# Responsabilidades:
# - Formatear un objeto e imprimirlo
class HtmlPrinter(IPrinter):
    def __init__(self, formatter):
        self.formatter = formatter
    def printPage(self, obj):
        html = "<div>"
        html += self.formatter.html_formatter(obj)
        html += "</div>"
        print(html)

# Main
currentBook = Book('Un Mundo Feliz', 'Aldous Huxley')
bookHtmlFormatter = BookHTML()
htmlPrinter = HtmlPrinter(bookHtmlFormatter)
htmlPrinter.printPage(currentBook)
