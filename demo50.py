
file1 = open('data\\Python_Introduction.txt', encoding='UTF-8')

readme_txt = file1.read()
print(type(readme_txt), len(readme_txt), readme_txt[:100])

file1.close()

file2 = open('data\\Clone1', 'w', encoding='UTF-8')
file2.write(readme_txt)
file2.close()

with open('data\\Python_Introduction.txt', encoding='UTF-8') as file3:
    readme_txt2 = file3.read()
print(type(readme_txt2), len(readme_txt2), readme_txt2[:500])

with open('data\\Clone2','w', encoding='UTF-8') as file4:
    file4.write(readme_txt2)