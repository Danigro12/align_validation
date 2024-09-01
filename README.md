## Alignment Validation of SORTMERNA

Script developed for testing SortMeRNA alignment algorithm. This testing is specially useful for short sequences, like miRNA. In the future, it could be adjusted for testing others alignment algorithms.
<br/>
<br/>
What you need to run it?
<br/>
- SortMeRNA installed (https://github.com/sortmerna)
- Python v.3+
- Biopython (https://biopython.org)
<br/>
Run the .sh file on the terminal with the following inputs:
<br/>
<br/>
batch_align.sh -- path_to_sortme_rna_bin -- min_len_of_read -- max_len_of_read -- cp_database -- cn_database

- path_to_sortme_rna_bin = path to sortmerna binary file
- min_len_of_read = the minimum length of the sequence to be tested
- max_len_of_read = the minimum length of the sequence to be tested
- cp_database = database used as positive control
- cn_database = database used as negative control

<br/>
The script does the following steps:

1) From some database specified by user, take random sequences and create a shorter reference (it is useful for huge databases. If you'd like to use the complete database, just input a a number higher than the total database sequences). The script will create 2 databases, one that we previously know that should align (cp, positive control) and another that we don't want to align (cn, negative control)

2) Create a .fasta that follows the following formula:

- 100 positive control samples, coming from the positive db created. Length of the sequences: User specified minimum length.
- 100 positive control samples, originating from the positive db created. Length of the sequences: User specified maximum length.
- 100 complementary reverse positive control samples, originating from the positive db created. Length of the sequences: User specified minimum length.
- 100 complementary reverse positive control samples, originating from the positive db created. Length of the sequences: User specified maximum length.
- 100 negative control samples, coming from the negative db created. Length of the sequences: User specified minimum length.
- 100 negative control samples, coming from the negative db created. Length of the sequences: User specified maximum length.
- 100 complementary reverse negative control samples, originating from the negative db created. Length of the sequences: User specified minimum length.
- 100 complementary reverse negative control samples, originating from the negative db created. Length of the sequences: User specified maximum length.
- 100 random samples (negative control). Length of the sequences: User specified minimum length.
- 100 random samples (negative control). Length of the sequences: User specified maximum length.

3) Use alignment program (sortmerna) with seeds 8, 10, 12, 14, 16 and 18.

4) Generate a report with percentages of alignments.
