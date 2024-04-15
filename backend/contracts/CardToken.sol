// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract CardToken is ERC721URIStorage, Ownable {
    uint256 private _currentTokenId = 0;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) Ownable(msg.sender) {}

    function mintTo(address recipient, string memory metadataURI) public onlyOwner returns (uint256) {
        uint256 newTokenId = _currentTokenId + 1;
        _mint(recipient, newTokenId);
        _setTokenURI(newTokenId, metadataURI);
        _currentTokenId = newTokenId;
        return newTokenId;
    }
}

