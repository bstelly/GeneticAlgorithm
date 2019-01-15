from random import randint
def mutate(gene, rate):
    gene = list(gene)
    itr = 0
    for x in gene:
        if randint(0, 100) >= rate:
            if x is '0':
                gene[itr] = '1'
            else:
                gene[itr] = '0'
        itr += 1
    return gene

gene = '000000'
newgene = mutate(gene, 50)
newgene