Script developed for testing SortMeRNA algorithm. In the future, it could be adjusted for testing others alignment algorithms that use window-based alignment (seed, k-mer, etc). This testing is specially useful for short sequences, like miRNA. 

The script does the following steps:

1) From some database specified by user, take random sequences and create a shorter reference (it is useful for huge databases. If you'd like to use the complete database, just input a a number higher than the total database sequences). The script will create 2 databases, one that we previously know that should align (cp, positive control) and another that we don't want to align (cn, negative control)
2) Create a .fasta that follows the following formula:

	 a) 100 positive control samples, coming from the positive db created. Size 19.
    b) 100 positive control samples, originating from the positive db created. Size 33.
    c) 100 complementary reverse positive control samples, originating from the positive db created. Size 19.
    d) 100 complementary reverse positive control samples, originating from the positive db created. Size 33.
    e) 100 negative control samples, coming from the negative db created. Size 19.
    f) 100 negative control samples, coming from the negative db created. Size 33.
    g) 100 complementary reverse negative control samples, originating from the negative db created. Size 19.
    h) 100 complementary reverse negative control samples, originating from the negative db created. Size 33.
    i) 100 random samples (negative control). Size 19
    j) 100 random samples (negative control). Size 33

3) Use alignment program (sortmerna) with seeds 8, 10, 12, 14, 16 and 18.
4) Generate a report with percentages of alignments.
