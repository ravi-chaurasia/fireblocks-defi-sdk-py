from enum import Enum


class Chain(Enum):
    MAINNET = "mainnet"
    ROPSTEN = "ropsten"
    KOVAN = "kovan"
    GOERLI = "goerli"
    RINKEBY = "rinkeby"
    BSC = "bsc"
    BSC_TEST = "bsc_test"
    POLYGON = "polygon"
    POLYGON_TEST = "polygon_mumbai"
    AVALANCHE = "avalanche"
    AVALANCHE_TEST = "avalanche_fuji"
    MOONRIVER = "moonriver"  # Moonbeam testnet
    MOONBEAM = "moonbeam"
    SONGBIRD = "songbird"
    ARBITRUM = "arbitrum"
    ARBITRUM_RIN = "arbitrum_rin"
    FANTOM = "fantom"
    RSK = "rsk_smart_bitcoin"
    RSK_TEST = "rsk smart bitcoin testnet"
    CELO = "celo"
    CELO_BAK = "celo_baklava"
    OPTIMISM = "optimistic_ethereum"
    OPTIMISM_KOVAN = "optimistic ethereum kovan"
    RONIN = "ronin"
    RONIN_TEST = "ronin_test"
    ARBITRUM = "arbitrum"
    ARBITRUM_GOERLI = "arbitrum_goerli"
