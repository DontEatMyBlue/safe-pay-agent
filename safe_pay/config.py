"""설정 읽기와 RPC 연결.

.env에서 RPC 주소와 개인키를 읽는다. 개인키는 이 모듈 밖으로 문자열로 내보내지 않는다.
"""

import os

from dotenv import load_dotenv
from eth_account import Account
from web3 import Web3

load_dotenv()

# Base Sepolia (테스트넷). 메인넷 값은 넣지 않는다.
BASE_SEPOLIA_CHAIN_ID = 84532
DEFAULT_RPC_URL = "https://sepolia.base.org"
EXPLORER_URL = "https://sepolia.basescan.org"
USDC_ADDRESS = "0x036CbD53842c5426634e7929541eC2318f3dCF7e"

RPC_URL = os.getenv("RPC_URL", DEFAULT_RPC_URL)


def get_web3() -> Web3:
    """RPC에 연결된 Web3 객체를 돌려준다. 테스트넷이 아니면 에러를 낸다."""
    w3 = Web3(Web3.HTTPProvider(RPC_URL, request_kwargs={"timeout": 10}))
    if not w3.is_connected():
        raise ConnectionError(f"RPC에 연결할 수 없습니다: {RPC_URL}")
    if w3.eth.chain_id != BASE_SEPOLIA_CHAIN_ID:
        raise RuntimeError(
            f"chain_id가 {w3.eth.chain_id}입니다. Base Sepolia({BASE_SEPOLIA_CHAIN_ID})만 허용합니다."
        )
    return w3


def _private_key(name: str) -> str:
    key = os.getenv(f"PRIVATE_KEY_{name}")
    if not key:
        raise KeyError(f".env에 PRIVATE_KEY_{name}가 없습니다. scripts/create_wallets.py를 먼저 실행하세요.")
    return key


def get_address(name: str) -> str:
    """지갑 이름('A' 또는 'B')의 주소를 개인키에서 계산해 돌려준다."""
    return Account.from_key(_private_key(name)).address


if __name__ == "__main__":
    w3 = get_web3()
    print(f"RPC:          {RPC_URL}")
    print(f"is_connected: {w3.is_connected()}")
    print(f"chain_id:     {w3.eth.chain_id}")
    print(f"최신 블록:    {w3.eth.block_number}")
    for name in ("A", "B"):
        print(f"지갑 {name}:       {get_address(name)}  {EXPLORER_URL}/address/{get_address(name)}")
