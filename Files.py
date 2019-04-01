#Read from file
file = open('MyData','r')
print(file.read())

#Write from file
fw = open('abc','w')
fw.write('Something')

#Append to file
fw = open('abc','a')
fw.write('Something')

# Read as lines
for data in fw:
    print(fw)