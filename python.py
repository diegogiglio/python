'''f = open('file2.txt', 'w')
primeiraLinha = f.readline()
segundaLinha = f.readline()

print(primeiraLinha, end='')
print(segundaLinha)

f.close()
'''
'''
f = open("file.txt", "r")
for line in f.readlines():
    print(line, end='')
'''
'''
f = open("file.txt", "a")
f.write("\n Oi eu fui adicionado")
'''
'''
fileInput = open("entrada.txt", "r")
fileOutput = open("saida.txt", "a")

msg = fileInput.read(10)

while len(msg):
    fileOutput.write(msg + '\n')
    msg = fileInput.read(10)

fileInput.close()
fileOutput.close()
'''
