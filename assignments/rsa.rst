building an RSA implementation
##############################

**note:** you should never use your own implementation of a cryptographic scheme 
in your code, unless you are a specialist in that algorithm. use a standard 
library instead.

the RSA scheme is probably the easiest to understand public key cryptography 
protocol. we ask you to implement it almost completely. check these references 
for guidance: `1 <http://doctrina.org/How-RSA-Works-With-Examples.html>`__
`2 
<http://doctrina.org/Why-RSA-Works-Three-Fundamental-Questions-Answered.html>`__

requirements
============

naming
    class ``rsapkc``, methods ``generate_keys``, ``encrypt`` and ``decrypt``.

input
    any sequence of bytes, or a string (in the case of ``encrypt``).

output
    the encrypted or decrypted sequence of bytes, or a string (in the case of 
    ``decrypt``).

prime number generation
    you should generate the numbers yourself usign a cryptographically secure 
    way, but you may copy and paste the 
    `Miller-Rabin test 
    <https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test>`__ 
    for primality.

bonuses
-------

#. implement your own version of the Miller-Rabin primality test. (make sure 
   you understand it, don't just adapt it from the internet).

#. use the `chinese remainder theorem 
   <https://en.wikipedia.org/wiki/Chinese_remainder_theorem>`__ instead of the 
   `extended euclidean algorithm 
   <https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm>`__ (easier to 
   understand but slower. make sure 
   you understand it, don't just adapt it from the internet).

#. optimize your implementation: how large keys can you handle before your 
   class gets too slow to use? how far is that from the usual key length (1024 
   or 2048 bits)?