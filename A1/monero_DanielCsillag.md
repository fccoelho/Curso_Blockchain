# [Monero](https://www.getmonero.org/)

Monero é uma criptomoeda com um foco em privacidade. Foi lançada em 2014, mas desde então já passou por mudanças relativamente fundamentais, sempre com o objetivo de melhor atingir seus objetivos:

- **Segurança**

  Não há espaço para operações na blockchain do Monero serem falsificadas;

- **Privacidade**

  Diferente da vasta maioria de criptomoedas, a blockchain do Monero não é transparente: é obfuscada de tal maneira que é verificável mas não identificável;

- **Decentralização**

  Na maioria das criptomoedas mineráveis, tem-se uma vantagem absurda em adquirir hardwares especializados e de mais difícil acesso. Monero usa um algoritmo de Proof of Work que previne tais hardwares, tendo melhor performance em CPU mesmo; e assim, aumenta a decentralização da rede;

## Proof of Work

Até recentemente, a blockchain do Monero utilizava um algoritmo de Proof of Work chamado _CryptoNightR_. Atualmente, ela utiliza um outro algoritmo de PoW, desenvolvido do zero especialmente para o Monero, chamado _RandomX_.

Um dos principais objetivos do _RandomX_ é resistir a ASICs. A maneira com que optaram em atingir isso foi elaborando um algoritmo que se aproveita fundamentalmente da utilidade genérica de CPUs.

Segue o esboço do algoritmo. Por questões de apresentação, simplifiquei um pouco, em particular em relação à manter os estados dos geradores de números aleatórios; para uma especificação totalmente precisa, veja [RandomX/doc/specs.md](https://github.com/tevador/RandomX/blob/master/doc/specs.md#2-algorithm-description):

```
function RandomX(key, to_hash)
  // Initialize the execution VM:
  vm = RandomX_VirtualMachine()
  vm.initialize_dataset(key)
  vm.fill_with_random_bytes(l3_size)

  // Build the blocks:
  seed = ... // (um valor não estático, que dependende da inicialização da VM)
  for i in 1..n_blocks
    // Generate random program:
    program_instructions = fill_with_random_bytes(128 + 8*program_size, seed)
    vm.execute(program_instructions)

    // Update seed
    seed = hash_512(vm.register_file)

  // Finalize:
  fingerprint = hash_aes1r(vm.scratchpad)
  vm.register_file[192..255] = fingerprint
  return hash_256(vm.register_file)
```

Vale destacar algumas coisas nesse algoritmo:

- O bloco `n+1` depende do resultado da execução do bloco `n`;
- Conseguir prever o que vai acontecer com um programa gerado aleatoriamente, de forma geral, se reduz ao _Halting Problem_;
- Alguns programas levam mais tempo de executar do que outros. Ao adicionar um novo bloco, há sempre um risco de você gastar tempo demais para pouco adicional;
- A utilização de funções hash impede ataques via geração de programas fáceis de rodar;

## Privacidade

Como mencionado acima, a blockchain do Monero foi elaborada com o intuito de manter a privacidade o máximo possível.

Para isso, ela se utiliza de várias tecnologias:

- _RingCT_

  Uma variação de ring signatures. É utilizada para ocultar, em uma transação, a quantidade transacionada, origem e destino.

- _Stealth Addresses_

  Na blockchain do Monero, cada carteira tem seu endereço correspondente. Ao usar este endereço para um pagamento, você está essencialmente se identificando (por mais que esta identificação seja relativamente separada da sua identidade pessoal); o conceito de stealth addresses é você poder gerar um outro endereço na blockchain que se refere a você, mas que não pode ser traçado ao endereço principal.

- Integração com tecnologias focadas em privacidade

  - _Tor_ e _I2P_

    Ambos se tratam de protocolos para anonimização de requests, e ambos podem ser facilmente utilizados para realizar transações com Monero.

  - _Dandelion++_

    Se trata de um protocolo para anonimização em criptomoedas, de uma forma bem geral. É compatível com Monero.

## Emissão da Criptomoeda

<!-- Descever regras para emissão da criptomoeda e se é inflacionária ou não. -->

## Interoperabilidade com Bitcoin

*Hot news!* Esse mecanismo está no ar faz poucas semanas: [veja o blog post](https://www.getmonero.org/2021/08/20/atomic-swaps.html).

Uma coisa bem bacana que está sendo trabalhada e deve chegar logo ao Monero é interoperabilidade com Bitcoin. Mais precisamente, swaps atômicos -- isto é, ao fazer a operação, ela pode ou acontecer por completo (i.e., resultando na troca desejada entre Monero e Bitcoin) ou não acontece nada.

Isto é parecido com o que algumas exchanges de criptomoedas fazem, mas estes swaps atômicos são feitos de maneira decentralizada; isto é, sem uma terceira entidade, e de uma maneira _trustless_.
