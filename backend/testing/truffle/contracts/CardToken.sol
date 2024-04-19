// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
// import "@openzeppelin/contracts/utils/Counters.sol";
import "openzeppelin-solidity/contracts/utils/Counters.sol";

// This is the code for the token, based on the ERC721 base.

contract CardToken is ERC721, ERC721URIStorage, ERC721Burnable, Ownable {
    using Counters for Counters.Counter; 
    Counters.Counter private tokenIDs;
    constructor(address initialOwner)
        ERC721("CardToken", "PW")
        Ownable(initialOwner)
    {}

    function safeMint(address to, string memory uri)
        public
        onlyOwner
        returns (uint256)
    {
        uint256 walkerID = tokenIDs.current();
        _safeMint(to, walkerID);
        _setTokenURI(walkerID, uri);

        tokenIDs.increment();
        return walkerID;
    }

    function transfer(
        address from,
        address to,
        uint256 tokenID
    ) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenID),
            "ERC721: transfer caller is not owner nor approved"
        );
        _transfer(from, to, tokenID);
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