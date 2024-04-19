const Contract = artifacts.require('./planeswalker.sol');
module.exports = function(deployer) {
    deployer.deploy(Contract);
}