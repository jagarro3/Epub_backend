"""app.models.py"""
from typing import List
from ebooklib import epub

class EpubInfo(object):
    title = None
    creator = None
    identifier = None
    contributor = None
    rights = None
    coverage = None
    date = None
    description = None
    image = None

    def __init__(self, title, creator, identifier, contributor, rights, coverage, date, description, image):
        self.title = title
        self.creator = creator
        self.identifier = identifier
        self.contributor = contributor
        self.rights = rights
        self.coverage = coverage
        self.date = date
        self.description = description
        self.image = image

def make_epub_info(title, creator, identifier, contributor, rights, coverage, date, description, image):
    epub_info = EpubInfo(title, creator, identifier, contributor, rights, coverage, date, description, image)
    return epub_info