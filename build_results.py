import os
from Bio import SeqIO
import sys

tam_min, tam_max = sys.argv[1:3]

sequences = {}
alignments = {}

#Trazendo as sequencias do fasta
with open("random_sequences.fasta",'r') as meu_fasta:
    input_file = SeqIO.parse(meu_fasta,'fasta')
    for read in input_file:
        sequences[read.id]=read.seq

#Validando o nome do resultado
counter = 1
log_file_name = f'result{counter}.log'

while os.path.exists(log_file_name):
    counter +=1
    log_file_name = f'result{counter}.log'

#Escrevendo o resultado do BLAST em um arquivo único
for num in range(8,18+1,2):
    valor = f'./OUTPUT_{num}/out/aligned.blast'
    with open(valor,'r') as meu_blast:
        lista_queries = []
        for i in meu_blast:
            lista_queries.append(i.split()[0])
        tipo_de_amostragem = {}
        tipo_de_amostragem[tam_min+'.cp'] = sum(1 for query in lista_queries if f'.type.{tam_min}.cp.' in query)
        tipo_de_amostragem[tam_max+'.cp'] = sum(1 for query in lista_queries if f'.type.{tam_max}.cp.' in query)
        tipo_de_amostragem[tam_min+'.cp.rev'] = sum(1 for query in lista_queries if f'.type.{tam_min}_rev.cp.' in query)
        tipo_de_amostragem[tam_max+'.cp.rev'] = sum(1 for query in lista_queries if f'.type.{tam_max}_rev.cp.' in query)
        tipo_de_amostragem[tam_min+'.cn'] = sum(1 for query in lista_queries if f'.type.{tam_min}.cn.' in query)
        tipo_de_amostragem[tam_max+'.cn'] = sum(1 for query in lista_queries if f'.type.{tam_max}.cn.' in query)
        tipo_de_amostragem[tam_min+'.cn.rev'] = sum(1 for query in lista_queries if f'.type.{tam_min}_rev.cn.' in query)
        tipo_de_amostragem[tam_max+'.cn.rev'] = sum(1 for query in lista_queries if f'.type.{tam_max}_rev.cn.' in query)
        tipo_de_amostragem[tam_min+'.random'] = sum(1 for query in lista_queries if f'random.{tam_min}' in query)
        tipo_de_amostragem[tam_max+'.random'] = sum(1 for query in lista_queries if f'random.{tam_max}' in query)
        alignments[num] = tipo_de_amostragem
    with open(log_file_name,'a') as log_file:
        log_file.write(f'Alignment with seed: {num}\n\n')
        for type_run, percentage in tipo_de_amostragem.items():
            log_file.write(f'Type of control: {str(type_run)}. Percentage of alignment reads: {str(percentage)}%\n')
        log_file.write('----------------------------------------------\n')
