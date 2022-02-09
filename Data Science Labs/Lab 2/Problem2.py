# Question 2
# Name:Satyen Sabnis, ssabnis2@student.gsu.com, 2/4/2022, DSCI 1302

def clean(doc):
  cleaned_doc = ""
  bad_things = ["(", ")", ",", ".", "!", "?", "\'", "/", "[", "]","*", "\""]
  for char in doc:
    if char not in bad_things:
      cleaned_doc += char

  return cleaned_doc

def isNumber(word):
  for char in word:
    if not char.isdigit():
      return False
  return True

def wordcount(user_string):
  word_count = dict()
  user_string = user_string.lower().split(" ")
  for element in user_string:
    if isNumber(element):
      pass
    else:
      if element in word_count:
        word_count[element]+=1
      else:
        word_count[element] = 1
  print(word_count)

user_string = input("Enter your text: ")
wordcount(clean(user_string))