# S24_Chain_Cards
# Project Idea
Chain Cards is a digital collectible card game on the blockchain developed by Michael Annor, Yufei Song, Dante Luis, and Chris for S24 AI and Blockchain. Chain cards allows players to create random characters cards in the form of NFTs (and if possible a physical card linked to it) to safely trade and engage in combat over the blockchain. 

## Character creation: 
An AI fills out 10 D&D character sheets with stats (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma), skills, and equipment. The AI also generates a short backstory, this is fed to another AI to create an image for the character. The information from the character sheet and the image are used to create a card similar to Magic the Gathering. This card will serve as a representation for the ERC-721 for each character.

## Trade:
The Chain Cards trade mechanism is designed around a user-friendly website that leverages smart contracts for secure and transparent trading of character cards as NFTs. It offers features for listing cards for trade, setting prices via auctions or fixed rates, and facilitating direct trades between players. Smart contracts ensure atomicity in trades, guaranteeing simultaneous asset swaps to prevent fraud. Users can manage their NFTs and transactions through digital wallet integration with platforms like MetaMask and WalletConnect. An optional feature links each NFT to a physical card or card in NFTs via a unique identifier, adding a tangible aspect to the collectibles. The platform prioritizes high security standards and compliance with regulations to protect user data and ensure lawful operations.

## Architecture / High-level component diagram
![image](https://github.com/AI-and-Blockchain/S24_Chain_Cards/assets/90219263/44ee2d8a-3d27-440f-b58a-ce013b342da6)

## Sequence diagram
![Check_In2](https://github.com/AI-and-Blockchain/S24_Chain_Cards/assets/89411564/6fba9533-f627-49cf-84b7-e6cd5b061ffa)

## Expected Features for the Demo:
AI Card Creation: A feature for players to interact with the AI, requesting new cards or modifications to existing ones.
Sample Deck and Combat: A selection of AI generated decks that players can use to understand basic and advanced game mechanics through AI simulated combat scenarios.
Trading Interface: A user-friendly interface (expected to be a website) for trading cards, integrated with blockchain technology for secure transactions.

## User Stories
As an NFT collector and a gamer, I want a fun and interactive way to collect NFTs and use them to engage others with them.  

As a player, I wish to receive both a digital and a physical version of my character card, enabling me to collect tangible items and trade them in the real world while keeping the benefits of blockchain verification.

As a new player, I need clear instructions on how to create my character and understand the stats, so that I can easily get started with the game.

As an NFT collector, I want ways to trade and gain new cards that seem more suitable to me.

As a player, I want different there to be a variety of combat forms with different stakes and rewards.

As a player, I want my characters to be secure with no chance of them being manipulated.




