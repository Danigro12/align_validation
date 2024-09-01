from criar_db import criar_banco_aleatorio
from reverse_complement import generate_reverse_complement
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import random
import sys

tamanho_min_read, tamanho_max_read = map(int, sys.argv[1:3])
cp_ref_dir,cn_ref_dir = map(str, sys.argv[3:5])

criar_banco_aleatorio(cp_ref_dir,'cp')
criar_banco_aleatorio(cn_ref_dir,'cn')

fasta_final = {}
bases = 'actg'

def gerar_read_aleatoria(tam_seq,banco_de_dados_dir,reverse=False):

    #Parseando o arquivo
    with open(banco_de_dados_dir,'r') as banco_de_dados:
        records = list(SeqIO.parse(banco_de_dados,'fasta'))

    #selecionar registro aleatorio
    registro_aleatorio = random.choice(records)
    #pegar o id e sequencia do registro aleatorio
    id_sequencia = registro_aleatorio.id
    sequencia = str(registro_aleatorio.seq)
    #pegar um pedaço aleatório da sequência
    if len(sequencia) <= tam_seq:
        pedaco_da_seq = sequencia
    else:
        inicio = random.randint(0, len(sequencia) - tam_seq)
        pedaco_da_seq = sequencia[inicio:inicio + tam_seq]
    
    pedaco_da_seq = pedaco_da_seq.replace('U','T')

    if reverse:
        pedaco_da_seq = generate_reverse_complement(pedaco_da_seq,'DNA')

    return id_sequencia, pedaco_da_seq

def gerar_sequencia_aleatoria(bases, tam_seq):
    sequencia = ''.join(random.choice(bases) for _ in range(tam_seq))
    return sequencia

#Loop para gerar fastq com as amostras:
cont = 1000
while cont != 0:
    if cont >= 901:
        id_aleatorio, read_aleatoria = gerar_read_aleatoria(tamanho_min_read,'banco_de_dados_cp.fasta')
        id_aleatorio = id_aleatorio + f'.type.{tamanho_min_read}.cp.{cont}'
        fasta_final[id_aleatorio] = read_aleatoria
    elif cont <= 900 and cont >= 801:
        id_aleatorio, read_aleatoria = gerar_read_aleatoria(tamanho_max_read, 'banco_de_dados_cp.fasta')
        id_aleatorio = id_aleatorio + f'.type.{tamanho_max_read}.cp.{cont}'
        fasta_final[id_aleatorio] = read_aleatoria
    elif cont <= 800 and cont >= 701:
        id_aleatorio, read_aleatoria = gerar_read_aleatoria(tamanho_min_read, 'banco_de_dados_cp.fasta',True)
        id_aleatorio = id_aleatorio + f'.type.{tamanho_min_read}_rev.cp.{cont}'
        fasta_final[id_aleatorio] = read_aleatoria[::-1]
    elif cont <= 700 and cont >= 601:
        id_aleatorio, read_aleatoria = gerar_read_aleatoria(tamanho_max_read, 'banco_de_dados_cp.fasta', True)
        id_aleatorio = id_aleatorio + f'.type.{tamanho_max_read}_rev.cp.{cont}'
        fasta_final[id_aleatorio] = read_aleatoria[::-1]
    elif cont <= 600 and cont >= 501:
        id_aleatorio, read_aleatoria = gerar_read_aleatoria(tamanho_min_read,'banco_de_dados_cn.fasta')
        id_aleatorio = id_aleatorio + f'.type.{tamanho_min_read}.cn.{cont}'
        fasta_final[id_aleatorio] = read_aleatoria
    elif cont <= 500 and cont >= 401:
        id_aleatorio, read_aleatoria = gerar_read_aleatoria(tamanho_max_read, 'banco_de_dados_cn.fasta')
        id_aleatorio = id_aleatorio + f'.type.{tamanho_max_read}.cn.{cont}'
        fasta_final[id_aleatorio] = read_aleatoria
    elif cont <= 400 and cont >= 301:
        id_aleatorio, read_aleatoria = gerar_read_aleatoria(tamanho_min_read, 'banco_de_dados_cn.fasta',True)
        id_aleatorio = id_aleatorio + f'.type.{tamanho_min_read}_rev.cn.{cont}'
        fasta_final[id_aleatorio] = read_aleatoria[::-1]
    elif cont <= 300 and cont >= 201:
        id_aleatorio, read_aleatoria = gerar_read_aleatoria(tamanho_max_read, 'banco_de_dados_cn.fasta', True)
        id_aleatorio = id_aleatorio + f'.type.{tamanho_max_read}_rev.cn.{cont}'
        fasta_final[id_aleatorio] = read_aleatoria[::-1]
    elif cont <= 200 and cont >= 101:
        read_aleatoria = gerar_sequencia_aleatoria(bases, tamanho_min_read)
        id_aleatorio = f'random.{cont}'
        fasta_final[id_aleatorio] = read_aleatoria
    elif cont <= 100 and cont >= 1:
        read_aleatoria = gerar_sequencia_aleatoria(bases, tamanho_max_read)
        id_aleatorio = f'random.{cont}'
        fasta_final[id_aleatorio] = read_aleatoria
    cont-=1

resultado_final = [SeqRecord(seq, id=id, description="") for id, seq in fasta_final.items()]

with open('random_sequences.fasta', 'w') as output_file:
    SeqIO.write(resultado_final, output_file, 'fasta')

print("FASTA file successfully created!")
