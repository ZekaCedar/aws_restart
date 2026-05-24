#Example 1
t = open('preproinsulin-seq.txt').read()
# delete ORIGIN, 1, 61, //, and the spaces and return carriages.
preproinsulin = t.replace('ORIGIN','').replace('61','').replace('//','').replace('1','').replace(' ','').replace('\n','').replace('\r','')
print(preproinsulin)
print(len(preproinsulin))
print("-------------------")
# In lsinsulin-seq-clean.txt, save amino acids 1–24. Verify that your file has 24 characters.
lsinsulin = preproinsulin[0:24]
print(lsinsulin)
print(len(lsinsulin))
print("-------------------")
# In binsulin-seq-clean.txt, save amino acids 25–54. Verify that your file has 30 characters
binsulin = preproinsulin[24:54]
print(binsulin)
print(len(binsulin))
print("-------------------")
# In cinsulin-seq-clean.txt, save amino acids 55–89. Verify that your file has 35 characters.
cinsulin = preproinsulin[54:89]
print(cinsulin)
print(len(cinsulin))
print("-------------------")
# In ainsulin-seq-clean.txt, save amino acids 90–110. Verify that your file has 21 characters.
ainsulin = preproinsulin[89:110]
print(ainsulin)
print(len(ainsulin))
print("-------------------")