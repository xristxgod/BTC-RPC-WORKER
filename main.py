import json
import logging

import requests

from config import Config


class BTCHost:
    """BTCHost - connect to BTC node"""
    __slots__ = (
        "session", "url", "headers", "__instance",
        "DEFAULT_TIMEOUT", "SATOSHI_IN_BTC"
    )

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.DEFAULT_TIMEOUT, cls.SATOSHI_IN_BTC = 10, 10 ** 8
            cls.__instance = super(BTCHost, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.session = requests.Session()
        self.url = Config.BTC_NODE_HOST + "/wallet/" + Config.WALLET_ADDRESS
        self.headers = {"content-type": "application/json"}
        self.session.verify = False

    def __getattr__(self, method):
        return RPCMethod(method, self)


class RPCMethod:
    """RPCMethod - work to rpc methods"""
    __slots__ = ("_method", "_host")

    def __init__(self, method: str, host: BTCHost):
        self._method = method
        self._host = host

    def __getattr__(self, method: str):
        return RPCMethod('{}.{}'.format(self._method, method), self._host)

    def __call__(self, *params):
        __payload = json.dumps({"method": self._rpc_method, "params": params, "jsonrpc": "2.0"})
        try:
            response = self.host.session.post(
                self._host.url,
                headers=self._host.headers,
                data=json.dumps({
                    "method": self._rpc_method,
                    "params": params,
                    "jsonrpc": "2.0"
                })
            )
        except requests.exceptions.ConnectionError:
            raise ConnectionError
        if response.status_code not in (200, 500):
            raise Exception("RPC CONNECTION FAILURE: " + str(response.status_code) + " " + response.reason)
        response_json = response.json()
        if "error" in response_json and response_json["error"] is not None:
            raise Exception("ERROR IN RPC CALL: " + str(response_json["error"]))
        return response_json["result"]


if __name__ == '__main__':
    btc_host = BTCHost()
    try:
        # Get wallet balance
        balance = sum([x[0] for x in btc_host.get_unspent(Config.WALLET_ADDRESS)])
        logging.info(f"YOUR WALLETS BALANCE: {balance}")
    except Exception as error:
        logging.error(f"ERROR: {error}")
    finally:
        del btc_host
