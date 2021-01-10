# import re
# xx = "guru99,education is fun"
# r1 = re.findall(r"[x]",xx)
# print(r1)
#------------------------------------------------
import re
n = input().lower()
dic = {'g':'c',
       'c':'g',
       't':'a',
       'a':'u'}
# check = len(re.findall(r"[bd-fh-su-z]",n))
# print(check)
if re.findall(r"[bd-fh-su-z]",n) :
  print('Invalid Input')
else:
  # print('good')
  print (re.sub(r'[gcat]', lambda x: dic[x.group()], n).upper())
  

#------------------------------------------------
# import re 

# def multiple_replace(dict, text):
#   # Create a regular expression  from the dictionary keys
#   regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

#   # For each match, look-up corresponding value in dictionary
#   return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text) 

# if __name__ == "__main__": 

#   text = "Larry Wall is the creator of Perl"

#   dict = {
#     "Larry Wall" : "Guido van Rossum",
#     "creator" : "Benevolent Dictator for Life",
#     "Perl" : "Python",
#   } 

#   print (multiple_replace(dict, text))
#--------------------------------------
# import re

# number_mapping = {'g': 'c',
#                   'c': 'g',
#                   't': 'a',
#                   'a': 'u'}
# s = "gctagtac"

# print (re.sub(r'[gcat]', lambda x: number_mapping[x.group()], s))

