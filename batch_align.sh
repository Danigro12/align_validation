#!/bin/bash

if [ $# -ne 5 ]; then
  echo "Uso: $0 <path_to_sortme_rna_bin> <min_len_of_read> <max_len_of_read> <cp_database> <cn_database>"
  exit 1
fi

tam_min="$2"
tam_max="$3"
cp_ref="$4"
cn_ref="$5"

python3 "./build_file.py" $tam_min $tam_max $cp_ref $cn_ref

rm -rf OUTPUT_*

sortmerna_bin="$1"
seeds=(8 10 12 14 16 18)

for seed in "${seeds[@]}"; do
  command="$sortmerna_bin --ref ./banco_de_dados_cp.fasta --reads "./random_sequences.fasta" --workdir OUTPUT_$seed --num_alignments 1 --fastx --other --blast 1 --threads 8 -L $seed"

  # Executa o comando
  echo "Running: $command"
  $command
  
done

python3 "./build_results.py" $tam_min $tam_max
