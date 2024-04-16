// SPDX-License-IDentifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts@5.0.0/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts@5.0.0/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts@5.0.0/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts@5.0.0/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract PlanesWalker is ERC721, ERC721URIStorage, ERC721Burnable, Ownable {
    using Counters.Counter private tokenIDs;
    constructor(address initialOwner)
        ERC721("PlanesWalker", "PW")
        Ownable(initialOwner)
    {}

    function safeMint(address to, string memory uri)
        public
        return (uint256)
        onlyOwner
    {
        uint256 walkerID = tokenIDs.current();
        _safeMint(to, walkerID);
        _setTokenURI(walkerID, uri);

        tokenIDs.increment();
        return walkerID;
    }

    // The following functions are overrides required by Solidity.

    function tokenURI(uint256 tokenID)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenID);
    }

    function supportsInterface(bytes4 interfaceID)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceID);
    }
}