# Building an RSA implementation

> **note:** you should never use your own implementation of a cryptographic scheme in your code, unless you are a specialist in that algorithm. use a standard library instead.

The RSA scheme is probably the easiest to understand public key cryptography protocol. we ask you to implement it almost completely. check these references for guidance:

- [Examples](http://doctrina.org/How-RSA-Works-With-Examples.html)
- [Q & A](http://doctrina.org/Why-RSA-Works-Three-Fundamental-Questions-Answered.html)

## Requirements

*Naming*
    class ``rsapkc``, methods ``generate_keys``, ``encrypt`` and ``decrypt``.

*Input*
    Any sequence of bytes, or a string (in the case of ``encrypt``).

*Output*
    The encrypted or decrypted sequence of bytes, or a string (in the case of
    ``decrypt``).

*Prime number generation*
    You should generate the numbers yourself usign a cryptographically secure way, but you may copy and paste the     [Miller-Rabin test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)   for primality.

### Bonuses


1. Implement your own version of the Miller-Rabin primality test. (make sure
   you understand it, don't just adapt it from the internet).

2. Use the [chinese remainder theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem) instead of the
   [extended euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) (easier to
   understand but slower. make sure you understand it, don't just adapt it from the internet).

1. Optimize your implementation: how large the keys can get before before your
   class gets too slow to use? how far is that from the usual key length (1024 
   or 2048 bits)?
