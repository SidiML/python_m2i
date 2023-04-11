def verification_adn(seq) :
    ret = any(seq)
    for c in seq :
        ret = ret and c in "atgc"
    return ret

seq1 = "atgagtgaacgtctgagcattaccccgctggggccgtatatcggcgca"

# verification_adn(seq1)
def saisie_adn(ch) :
    s = input('{} :'.format(ch))
      
    while not verification_adn(s):
        print("{} ne peut contenir que les chainons 'a','t','g', 'c' et ne doit pas etre vide ".format(ch))
        s = input("{ :s} :".format(ch))
    return s

def proportion(s,a):
    return 100*a.count(s)/len(a)

#################################################
adn = saisie_adn(seq1)
seq = saisie_adn("sequence")

print('Il y a {:.1f}% de "{}" dans "{}".'.format(proportion(adn,seq),seq, adn))
    
    