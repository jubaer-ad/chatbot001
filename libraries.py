import nltk



from inspect import currentframe, getframeinfo
frameinfo = getframeinfo(currentframe())
print("--------------------")
print("ALL OK TILL: " + frameinfo.filename, frameinfo.lineno+3)
print("--------------------")
