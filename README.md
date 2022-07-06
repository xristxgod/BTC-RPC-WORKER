# BTC - RPC worker

>Implementation of work with BTC RPC API node via python code.

-----
### Setup:
## Setup:
>```shell
> # SSH
> git clone https://github.com/xristxgod/BTC-RPC-WORKER.git
> # HTTPS
> git@github.com:xristxgod/BTC-RPC-WORKER.git
>```

-----
### Settings in .env file:
> `BTC_NODE_HOST` - The url from your bitcoin node. Example: `http://xrist_main_node:0000@localhost:5555`
> 
> `WALLET_ADDRESS` - Your main wallet. Example: `bc1q5wt0zra0n8l5gr0hqg569ssu8dlqvf3yt9nlyn`

-----
### Notice:
> For correct operation, you need to download and install/synchronize the BTC Node (CORE). 
> And work with her directly. [Bitcoin CORE](https://bitcoincore.org/en/download/)

-----
### How to run:
> [Bitcoin API methods](https://developer.bitcoin.org/reference/rpc/)

> ```python
> from typing import List, Dict
> 
> from btc import BTCHost
> 
> 
> btc_node = BTCHost()
> 
> 
> def get_all_transactions(address: str) -> List[Dict]:
>   """
>   Get all transactions for wallet
>   :param address: Wallet address
>   """
>   # We turn to the methods of the RPC API. Just enter its name, as
>   # indicated by the link, and pass the parameters separated by commas.
>   result = btc_node.getreceivedbyaddress(address, 0) 
>   if len(result) > 0:
>       return result[0]["txids"]
>   return []
> 
>   
> if __name__ == '__main__':
>   transactions = get_all_transactions(...)
>   print(transactions)
> 
> ```

-----
### Example:
> Method URL: https://developer.bitcoin.org/reference/rpc/importaddress.html
> 
> Method name: `importaddress` 
> 
> Arguments: 
>> `address` | Type: string, required | The Bitcoin address (or hex-encoded script)
>>
>> `label` | Type: string, optional, default=”” | An optional label
>>
>> `rescan` | Type: boolean, optional, default=true | Rescan the wallet for transactions
>>
>> `p2sh` | Type: boolean, optional, default=false | Add the P2SH version of the script as well
> 
> Curl:
> ```shell
> curl --user xrist_main_node --data-binary '{"jsonrpc": "1.0", "id": "curltest", "method": "importaddress", "params": ["myaddress", "testing", false]}' -H 'content-type: text/plain;' http://xrist_main_node:0000@localhost:5555
> ```
>
> Python code:
> ```python
> from btc import BTCHost
>  
>
> btc_node = BTCHost()
> result = btc_node.importaddress(bc1q4ezgpx74wezpf55w967dvy8rpsrncptgw0u8a7, "", True, False)
> print(result)             # None (json null)
> ```