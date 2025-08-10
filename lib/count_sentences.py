#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value = ''):  
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    sentences = re.split(r'[.?!]', self.value)
    return len([s for s in sentences if s.strip()])

string = MyString()
string.value = "I am not a sentence"
print(string.is_sentence())
string.value = "I am a sentence."
print(string.is_sentence())

print(string.is_question())
string.value = "I am a qestion?"
print(string.is_question())

print(string.is_exclamation())
print(string.is_exclamation())
string.value = "I am an exclamation!"
print(string.is_exclamation())
print(string.count_sentences())


string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())
