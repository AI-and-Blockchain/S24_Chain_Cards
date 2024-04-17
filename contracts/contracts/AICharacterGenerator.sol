pragma solidity ^0.8.25;

import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

contract AICharacterGenerator is ChainlinkClient {
    using Chainlink for Chainlink.Request;

    // Chainlink Node address
    address private oracle;
    bytes32 private jobId;
    uint256 private fee;

    // store data from API
    string public characters;

    // event for API result
    event RequestCharactersFulfilled(bytes32 indexed requestId, string indexed data);

    constructor() {
        setPublicChainlinkToken();
        oracle = 0x<Oracle_Address>;
        jobId = "<Job_ID>";
        fee = 0.1 * 10 ** 18; // 0.1 LINK
    }

    function requestCharacterData(string memory apiUrl) public returns (bytes32 requestId) {
        Chainlink.Request memory request = buildChainlinkRequest(jobId, address(this), this.fulfill.selector);
        request.add("get", apiUrl);
        request.add("path", "data.path.to.characters"); // adjest to match the structure
        return sendChainlinkRequestTo(oracle, request, fee);
    }

    function fulfill(bytes32 _requestId, string memory _characters) public recordChainlinkFulfillment(_requestId) {
        characters = _characters;
        emit RequestCharactersFulfilled(_requestId, _characters);
    }
}