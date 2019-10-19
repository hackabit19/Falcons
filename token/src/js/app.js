App = {
  web3Provider: null,
  contracts: {},
  account: '0x0',
  loading: false,
  tokenPrice: 1000000000000000,
  tokensSold: 0,
  tokensAvailable: 750000,

  init: function () {
    console.log("App initialized...")
    return App.initWeb3();
  },

  initWeb3: function () {
    if (typeof web3 !== 'undefined') {
      // If a web3 instance is already provided by Meta Mask.
      App.web3Provider = web3.currentProvider;
      web3 = new Web3(web3.currentProvider);
    } else {
      // Specify default instance if no web3 instance provided
      App.web3Provider = new Web3.providers.HttpProvider('http://127.0.0.1:7545');
      web3 = new Web3(App.web3Provider);
    }
    return App.initContracts();
  },

  initContracts: function () {
    $.getJSON("FalconsTokenSale.json", function (falconsTokenSale) {
      App.contracts.FalconsTokenSale = TruffleContract(falconsTokenSale);
      App.contracts.FalconsTokenSale.setProvider(App.web3Provider);
      App.contracts.FalconsTokenSale.deployed().then(function (falconsTokenSale) {
        console.log("Falcons Token Sale Address:", falconsTokenSale.address);
      });
    }).done(function () {
      $.getJSON("FalconsToken.json", function (falconsToken) {
        App.contracts.FalconsToken = TruffleContract(falconsToken);
        App.contracts.FalconsToken.setProvider(App.web3Provider);
        App.contracts.FalconsToken.deployed().then(function (falconsToken) {
          console.log("Falcons Token Address:", falconsToken.address);
        });

        App.listenForEvents();
        return App.render();
      });
    })
  },

  // Listen for events emitted from the contract
  listenForEvents: function () {
    App.contracts.FalconsTokenSale.deployed().then(function (instance) {
      instance.Sell({}, {
        fromBlock: 0,
        toBlock: 'latest',
      }).watch(function (error, event) {
        console.log("event triggered", event);
        App.render();
      })
    })
  },

  render: function () {
    if (App.loading) {
      return;
    }
    App.loading = true;

    var loader = $('#loader');
    var content = $('#content');

    loader.hide();
    content.show();
    window.ethereum.enable();
    // Load account data
    web3.eth.getCoinbase(function (err, account) {
      if (err === null) {
        console.log("account",account);
        App.account = account;
        $('#accountAddress').html("Your Account: " + account);
      }
    })

    // Load token sale contract
    App.contracts.FalconsTokenSale.deployed().then(function (instance) {
      falconsTokenSaleInstance = instance;
      return falconsTokenSaleInstance.tokenPrice();
    }).then(function (tokenPrice) {
      App.tokenPrice = tokenPrice;
      $('.token-price').html(web3.fromWei(App.tokenPrice, "ether").toNumber());
      return falconsTokenSaleInstance.tokensSold();
    }).then(function (tokensSold) {
      App.tokensSold = tokensSold.toNumber();
      $('.tokens-sold').html(App.tokensSold);
      $('.tokens-available').html(App.tokensAvailable);

      var progressPercent = (Math.ceil(App.tokensSold) / App.tokensAvailable) * 100;
      $('#progress').css('width', progressPercent + '%');

      // Load token contract
      App.contracts.FalconsToken.deployed().then(function (instance) {
        falconsTokenInstance = instance;
        return falconsTokenInstance.balanceOf(App.account);
      }).then(function (balance) {
        $('.falcons-balance').html(balance.toNumber());
        App.loading = false;
        loader.hide();
        content.show();
      })
    });
  },

  xhr: function () {
    var phone = $('#phone').val();
    console.log(phone);
    var o;
    function reqListener() {
      o = JSON.parse(this.responseText);
      console.log(o.a);
      console.log('gy');
      document.getElementById("balance_amount").innerHTML = o.a;
    }

    var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", reqListener);
    oReq.open("GET", `http://192.168.43.247:8080/getAmountp/${phone}`);


    oReq.send()
    $('form3').trigger('reset')
  },

  buyTokens: function () {
    $('#content').hide();
    $('#loader').show();
    var numberOfTokens = $('#numberOfTokens').val();
    App.contracts.FalconsTokenSale.deployed().then(function (instance) {
      return instance.buyTokens(numberOfTokens, {
        from: App.account,
        value: numberOfTokens * App.tokenPrice,
        gas: 500000 // Gas limit
      });
    }).then(function (result) {
      console.log("Tokens bought...")
      $('form').trigger('reset') // reset number of tokens in form
      // Wait for Sell event
    });
  },
  // delegatedTransfers: function () {
  //   $('#content').hide();
  //   $('#loader').show();
  //   var numberOfTokens = $('#numberOfTokens').val();
  //   App.contracts.FalconsToken.deployed().then(function (instance) {
  //     return instance.buyTokens(numberOfTokens, {
  //       from: App.account,
  //       value: numberOfTokens * App.tokenPrice,
  //       gas: 500000 // Gas limit
  //     });
  //   }).then(function (result) {
  //     console.log("Tokens bought...")
  //     $('form').trigger('reset') // reset number of tokens in form
  //     // Wait for Sell event
  //   });
  // },
  approve: function () {
    $('#content').hide();
    $('#loader').show();
    var valueOfTokens = $('#valueOfTokens').val();
    var spender = "0x10EEA7e4620c32D94151eab8C66a4cA8380aD84e";
    App.contracts.FalconsToken.deployed().then(function (instance) {
      return instance.approve(spender, valueOfTokens, {
        from: App.account,
        // value: numberOfTokens * App.tokenPrice,
        // gas: 500000 // Gas limit
      });
    }).then(function (result) {
      console.log("Allowance given")
      $('form1').trigger('reset') // reset number of tokens in form
      // Wait for Approve event
    });
  },
  transferFrom: function () {
    $('#content').hide();
    $('#loader').show();
    var spender = "0x10EEA7e4620c32D94151eab8C66a4cA8380aD84e";
    var numberOfTokensToSlave = 1;
    console.log(spender);

    var slave = $('#slave').val();
    console.log(slave);

    App.contracts.FalconsToken.deployed().then(function (instance) {
      // var numberOfTokensToSlave = instance.allowance[slave][spender];
      return instance.transferFrom(spender, slave, numberOfTokensToSlave, {
        from: App.account,
      });
    }).then(function (result) {
      console.log("Tokens passed to slaves...")
      $('form2').trigger('reset') // reset number of tokens in form
      // Wait for Sell event
    });
  },
}

$(function () {
  $(window).load(function () {
    App.init();
  })
});
