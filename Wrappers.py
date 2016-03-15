#!/usr/bin/env python

'''
Wrapper objects for mac osx dictionary entries.
'''
from collections import defaultdict

class DictionaryEntry(defaultdict):
    '''
    Wrapper for a dictionary entry in mac osx
    '''
    def __init__(self, word):
        super(DictionaryEntry, self).__init__(list)
        self.word = word

    def add_definition(self, part_of_speech, definition):
        self[part_of_speech].append(definition)

    def __str__(self):
        # TODO: understand why this works
        # TODO: Add conversion method to html
        string = self.word + '<br>'
        for part_of_speech, definitions in self.iteritems():
            string += part_of_speech + '<br>'
            for definition in definitions:
                string += definition.__str__().decode('utf-8')
            string += '<br>'
        return string.encode('utf-8')

class Definition(object):
    '''
    Wrapper for a definition, which consists of a description and usages.
    '''
    def __init__(self, description, usages):
        self.description = description
        self.usages = usages

    def __str__(self):
        description_string = unicode(self.description).encode('utf-8')
        usage_string = '<br>'.join(self.usages)
        definition = 'defn:<br>{} <br>usage:<br>{}<br>'.format(description_string, unicode(usage_string).encode('utf-8'))
        return definition
