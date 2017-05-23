building a cryptographic hash function
######################################

**note:** you should never use your own implementation of a cryptographic scheme 
in your code, unless you are a specialist in that algorithm. use a standard 
library instead.

in this exercise we ask you to implement a cryptographic hash function. the 
easiest to understand candidates seem to be 
`VSH <http://eprint.iacr.org/2005/193.pdf>`__ and
`CubeHash <http://cubehash.cr.yp.to/index.html>`__.

bonus
-----

these are not the best cryptographic hash functions, but they seem easier to 
implement. if you want a bigger challenge, go for SHA2 or SHA3.