"""테스트넷 전용 지갑 A(내 지갑)와 B(받는 사람 지갑)를 만들어 .env에 저장한다.

- 개인키는 .env에만 쓰고, 터미널에는 주소만 출력한다.
- .env가 이미 있으면 덮어쓰지 않고 멈춘다. (기존 지갑의 키를 잃지 않기 위해)

실행: python scripts/create_wallets.py
"""

from pathlib import Path

from eth_account import Account

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"


def main() -> None:
    if ENV_PATH.exists():
        raise SystemExit(f"{ENV_PATH} 가 이미 있습니다. 기존 키를 지키기 위해 중단합니다.")

    wallet_a = Account.create()
    wallet_b = Account.create()

    lines = [
        "# 테스트넷 전용. 절대 커밋하지 말 것.",
        "RPC_URL=https://sepolia.base.org",
        f"PRIVATE_KEY_A=0x{bytes(wallet_a.key).hex()}",
        f"PRIVATE_KEY_B=0x{bytes(wallet_b.key).hex()}",
    ]
    # "x" 모드: 파일이 생기는 사이에 다른 곳에서 만들어졌다면 덮어쓰지 않고 실패한다
    with ENV_PATH.open("x", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"지갑 A (내 지갑):      {wallet_a.address}")
    print(f"지갑 B (받는 사람):    {wallet_b.address}")
    print(f"개인키는 {ENV_PATH.name} 에 저장했습니다.")


if __name__ == "__main__":
    main()
