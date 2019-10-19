var FalconsToken = artifacts.require("./FalconsToken.sol");
var FalconsTokenSale = artifacts.require("./FalconsTokenSale.sol");

module.exports = function (deployer) {
  deployer.deploy(FalconsToken, 1000000).then(function () {
    // Token price is 0.001 Ether
    var tokenPrice = 1000000000000000;
    return deployer.deploy(FalconsTokenSale, FalconsToken.address, tokenPrice);
  });
};
