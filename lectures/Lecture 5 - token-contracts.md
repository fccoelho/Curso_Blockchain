# Token Contracts

One of the most widely used type of smart-contract on the Ethereum blockchain is some variation of a token contract. A **token** is a currency issued and managed by a smart contract. Over the years many uses for tokens have been proposed and applied:

- **Utility tokens**: tokens that are issued by a company and have some pre-defined utility, such as being used to "buy" services from that company.
- **Security tokens**: Equivalent to traditional securities. Used to represent participation in physical assets, or companies, or some sort of dividend earning.
- **Payment tokens**: Equivalent to primary cryptocurrencies, i.e., they have no other purposed than to serve as a currency.

Tokens can be created by anyone with the ability to write and publish a contract. Due to the wide applicability of *Tokens*, it did not take long for templates to emerge, embodying the best practices for token security, these templates are also know as standards and in this lecture we will explore the most used token standards. There are [many tokens in existence](https://ethplorer.io/top?from=etop), i. e., token contracts published on the Ethereum blockchain.

## ERC20 Token

the [ERC20 standard](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md), is the most basic of token standards and serve as the basis for many tokens. The goal of a standard is to suggest a minimal common API for tokens to facilitate their use by *wallets* and *exchanges*. Naturally Token developers are free to deviate from this API, however doing so, will only reduce the reach of their token. Ideally developers should extend the standard API with new functionality to tackle their application.

### ERC20 minimal API
Full specification of ERC20 is linked above, here we will go through the  minimal API elements the contranct must implement to be compliant with the standard.
1. *totalSupply*: returns the total token supply
    ```solidity
    function totalSupply() view returns (uint256 totalSupply);
    ```
1. *balanceOf*: Returns the account balance of another account with address `_owner`.
    ```solidity
    function balanceOf(address _owner) view returns (uint256 balance)
    ```
1. *transfer*: Transfers `_value` amount of tokens to address `_to`, and MUST fire the `Transfer` event. The function SHOULD `throw` if the `_from` account balance does not have enough tokens to spend.
    ```solidity
    function transfer(address _to, uint256 _value) returns (bool success)
    ```
1. *transferFrom*: Transfers `_value` amount of tokens from address `_from` to address `_to`, and MUST fire the `Transfer` event.
The `transferFrom` method is used for a withdraw workflow, allowing contracts to transfer tokens on your behalf. This can be used for example to allow a contract to transfer tokens on your behalf and/or to charge fees in sub-currencies. The function SHOULD `throw` unless the `_from` account has deliberately authorized the sender of the message via some mechanism.
    ```solidity
    function transferFrom(address _from, address _to, uint256 _value) returns (bool success)
    ```
1. *approve*: Allows `_spender` to withdraw from your account multiple times, up to the `_value` amount. If this function is called again it overwrites the current allowance with `_value`.
    ```solidity
    function approve(address _spender, uint256 _value) returns (bool success)
    ```
1. *allowance*: Returns the amount which `_spender` is still allowed to withdraw from `_owner`.
    ```solidity
    function allowance(address _owner, address _spender) view returns (uint256 remaining)
    ```
1. *Transfer* (event): MUST trigger when tokens are transferred, including zero value transfers.
A token contract which creates new tokens SHOULD trigger a Transfer event with the `_from` address set to `0x0` when tokens are created.
    ```solidity
    event Transfer(address indexed _from, address indexed _to, uint256 _value)
    ```
1. *Approval* (event): MUST trigger on any successful call to `approve(address _spender, uint256 _value)`.
    ```solidity
    event Approval(address indexed _owner, address indexed _spender, uint256 _value)
    ```

A [good implementation](https://github.com/OpenZeppelin/openzeppelin-solidity/blob/master/contracts/token/ERC20/ERC20.sol) to extend is the one published by the [Open zeppelin](https://openzeppelin.org/) group. Open Zeppelin

## ERC-721 Non-fungible token
Most currencies have the property of [fungibility](https://en.wikipedia.org/wiki/Fungibility), meaning the coins are exchangeable, e. g., a specific 10 dollar bill holds the same value as any other 10 dollar bill, being therefore indistiguishable from the point of view of it being a conveyor of value. 

ERC-721 based tokens are non-fungible, meaning they resemble more a [deed](https://en.wikipedia.org/wiki/Deed) document than a currency bill. Therfore the main uses of ERC-712 tokens is to represent ownership o Assets which can be of various kinds, such as physical, virtual, or [Negative equity](https://en.wikipedia.org/wiki/Negative_equity) like loans, burdens etc.

Below we can see the basic API of an ERC-721 contract:

```solidity
pragma solidity ^0.4.20;

/// @title ERC-721 Non-Fungible Token Standard
/// @dev See https://github.com/ethereum/EIPs/blob/master/EIPS/eip-721.md
///  Note: the ERC-165 identifier for this interface is 0x80ac58cd.
interface ERC721 /* is ERC165 */ {
    /// @dev This emits when ownership of any NFT changes by any mechanism.
    ///  This event emits when NFTs are created (`from` == 0) and destroyed
    ///  (`to` == 0). Exception: during contract creation, any number of NFTs
    ///  may be created and assigned without emitting Transfer. At the time of
    ///  any transfer, the approved address for that NFT (if any) is reset to none.
    event Transfer(address indexed _from, address indexed _to, uint256 indexed _tokenId);

    /// @dev This emits when the approved address for an NFT is changed or
    ///  reaffirmed. The zero address indicates there is no approved address.
    ///  When a Transfer event emits, this also indicates that the approved
    ///  address for that NFT (if any) is reset to none.
    event Approval(address indexed _owner, address indexed _approved, uint256 indexed _tokenId);

    /// @dev This emits when an operator is enabled or disabled for an owner.
    ///  The operator can manage all NFTs of the owner.
    event ApprovalForAll(address indexed _owner, address indexed _operator, bool _approved);

    /// @notice Count all NFTs assigned to an owner
    /// @dev NFTs assigned to the zero address are considered invalid, and this
    ///  function throws for queries about the zero address.
    /// @param _owner An address for whom to query the balance
    /// @return The number of NFTs owned by `_owner`, possibly zero
    function balanceOf(address _owner) external view returns (uint256);

    /// @notice Find the owner of an NFT
    /// @dev NFTs assigned to zero address are considered invalid, and queries
    ///  about them do throw.
    /// @param _tokenId The identifier for an NFT
    /// @return The address of the owner of the NFT
    function ownerOf(uint256 _tokenId) external view returns (address);

    /// @notice Transfers the ownership of an NFT from one address to another address
    /// @dev Throws unless `msg.sender` is the current owner, an authorized
    ///  operator, or the approved address for this NFT. Throws if `_from` is
    ///  not the current owner. Throws if `_to` is the zero address. Throws if
    ///  `_tokenId` is not a valid NFT. When transfer is complete, this function
    ///  checks if `_to` is a smart contract (code size > 0). If so, it calls
    ///  `onERC721Received` on `_to` and throws if the return value is not
    ///  `bytes4(keccak256("onERC721Received(address,address,uint256,bytes)"))`.
    /// @param _from The current owner of the NFT
    /// @param _to The new owner
    /// @param _tokenId The NFT to transfer
    /// @param data Additional data with no specified format, sent in call to `_to`
    function safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes data) external payable;

    /// @notice Transfers the ownership of an NFT from one address to another address
    /// @dev This works identically to the other function with an extra data parameter,
    ///  except this function just sets data to "".
    /// @param _from The current owner of the NFT
    /// @param _to The new owner
    /// @param _tokenId The NFT to transfer
    function safeTransferFrom(address _from, address _to, uint256 _tokenId) external payable;

    /// @notice Transfer ownership of an NFT -- THE CALLER IS RESPONSIBLE
    ///  TO CONFIRM THAT `_to` IS CAPABLE OF RECEIVING NFTS OR ELSE
    ///  THEY MAY BE PERMANENTLY LOST
    /// @dev Throws unless `msg.sender` is the current owner, an authorized
    ///  operator, or the approved address for this NFT. Throws if `_from` is
    ///  not the current owner. Throws if `_to` is the zero address. Throws if
    ///  `_tokenId` is not a valid NFT.
    /// @param _from The current owner of the NFT
    /// @param _to The new owner
    /// @param _tokenId The NFT to transfer
    function transferFrom(address _from, address _to, uint256 _tokenId) external payable;

    /// @notice Change or reaffirm the approved address for an NFT
    /// @dev The zero address indicates there is no approved address.
    ///  Throws unless `msg.sender` is the current NFT owner, or an authorized
    ///  operator of the current owner.
    /// @param _approved The new approved NFT controller
    /// @param _tokenId The NFT to approve
    function approve(address _approved, uint256 _tokenId) external payable;

    /// @notice Enable or disable approval for a third party ("operator") to manage
    ///  all of `msg.sender`'s assets
    /// @dev Emits the ApprovalForAll event. The contract MUST allow
    ///  multiple operators per owner.
    /// @param _operator Address to add to the set of authorized operators
    /// @param _approved True if the operator is approved, false to revoke approval
    function setApprovalForAll(address _operator, bool _approved) external;

    /// @notice Get the approved address for a single NFT
    /// @dev Throws if `_tokenId` is not a valid NFT.
    /// @param _tokenId The NFT to find the approved address for
    /// @return The approved address for this NFT, or the zero address if there is none
    function getApproved(uint256 _tokenId) external view returns (address);

    /// @notice Query if an address is an authorized operator for another address
    /// @param _owner The address that owns the NFTs
    /// @param _operator The address that acts on behalf of the owner
    /// @return True if `_operator` is an approved operator for `_owner`, false otherwise
    function isApprovedForAll(address _owner, address _operator) external view returns (bool);
}

interface ERC165 {
    /// @notice Query if a contract implements an interface
    /// @param interfaceID The interface identifier, as specified in ERC-165
    /// @dev Interface identification is specified in ERC-165. This function
    ///  uses less than 30,000 gas.
    /// @return `true` if the contract implements `interfaceID` and
    ///  `interfaceID` is not 0xffffffff, `false` otherwise
    function supportsInterface(bytes4 interfaceID) external view returns (bool);
}
```

Again, just like ERC-20 a number the ERC-721 can be extended in a variety of ways. Some interesting examples can be found at the [OpenZeppelin repositiry](https://github.com/OpenZeppelin/openzeppelin-solidity/tree/master/contracts/token/ERC721).
