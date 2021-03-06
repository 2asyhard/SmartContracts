from brownie import StoreData, accounts


def test_deploy():
    # arrange
    account = accounts[0]  # get account ready for deploying contract

    # act
    store_data = StoreData.deploy({"from": account})  # deploy
    initial_value = store_data.retrieve()  # get initial value
    expected = 0

    # assert
    assert expected == initial_value


def test_updating_store_data():
    # arrange
    account = accounts[0]
    store_data = StoreData.deploy({"from": account})

    # act
    expected = 15
    store_data.store(expected, {"from": account})

    # assert
    assert expected == store_data.retrieve()


"""         Testing
You can code testing functions in smart contract
But it is more efficient to test in smart contract development framework languages(python, javascript, ...)
Use tests folder for testing
"""

"""
    Test sequence
        1. Arrange
        2. Act
        3. Assert

    Execute `brownie test` in terminal
    
    Tips
        For testing only one function
            Execute `brownie test -k <function name>`
        
        Use python shell when test failed
            Execute `brownie test --pdb`

        To show detail test results
            Execute `brownie test -s`
"""

