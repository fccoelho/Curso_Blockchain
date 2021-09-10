# Brownie - Python tools for Ethereum
[Brownie](https://github.com/eth-brownie/brownie) is a Python-based development and testing framework for smart contracts targeting the Ethereum Virtual Machine.

## installation
### via `pipx`

The recommended way to install Brownie is via [`pipx`](https://github.com/pipxproject/pipx). pipx installs Brownie into a virtual environment and makes it available directly from the commandline. Once installed, you will never have to activate a virtual environment prior to using Brownie.

To install `pipx`:

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

To install Brownie using `pipx`:

```bash
pipx install eth-brownie
```

To upgrade to the latest version:

```bash
pipx upgrade eth-brownie
```

To use lastest master or another branch as version:
```bash
pipx install git+https://github.com/eth-brownie/brownie.git@master
```

## Quick Usage

To initialize a new Brownie project, start by creating a new folder. From within that folder, type:

```bash
brownie init
```

Next, type `brownie --help` for basic usage information.

## Creating a Project from a Template
You can initialize [“Brownie mixes”](https://github.com/brownie-mix), simple templates to build your project upon. For many examples within the Brownie documentation we will use the [token mix](https://github.com/brownie-mix/token-mix), which is a very basic ERC-20 implementation.

Mixes are automatically created within a subfolder of their name. To initialize the token mix:

```bash
$ brownie bake token
```
## Basic Project Structure
If we look at the project folder created by the last command, above, that what we'll see:

```bash
$ ls
brownie-config.yaml  contracts/   LICENSE    reports/          scripts/
build/               interfaces/  README.md  requirements.txt  tests/
```
We notice that there are 6 sub-directories created: `contracts/`, `reports/`, `scripts/`, `build/`, `interfaces/` and `tests/`.

The `contracts` directory holds all contract source files for the project. Each time Brownie is run, it checks for new or modified files within this folder. If any are found, they are compiled and included within the project.

Contracts may be written in Solidity (with a .sol extension) or Vyper (with a .vy extension).

The `interfaces` directory holds interface source files that may be referenced by contract sources, but which are not considered to be primary components of the project. Adding or modifying an interface source onlys triggers a recompile if the interface is required by a contract.

Interfaces may be written in Solidity (.sol) or Vyper (.vy), or supplied as a JSON encoded ABI (.json).

The `scripts` directory holds Python scripts used for deploying contracts, or to automate common tasks and interactions. These scripts are executed via the brownie run command.

See the [Brownie Scripts](https://eth-brownie.readthedocs.io/en/latest/interaction.html#scripts) documentation for more information on Brownie scripts.

The `tests` directory holds Python scripts used for testing a project. Brownie uses the [pytest](https://docs.pytest.org/en/latest/) framework for unit testing.

See [Brownie Pytest](https://eth-brownie.readthedocs.io/en/latest/tests-pytest-intro.html#pytest) documentation for more information on testing a project.

## Documentation and Support

Brownie documentation is hosted at [Read the Docs](https://eth-brownie.readthedocs.io/en/latest/).

If you have any questions about how to use Brownie, feel free to ask on [Ethereum StackExchange](https://ethereum.stackexchange.com/) or join us on [Gitter](https://gitter.im/eth-brownie/community).



