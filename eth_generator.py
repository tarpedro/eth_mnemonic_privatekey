from mnemonic_utils import mnemonic_to_private_key


def private_key_generator(passphrase):
    private_key = mnemonic_to_private_key(f"{passphrase}")
    print(private_key.hex())


if __name__ == "__main__":
    mnemonic_key = input("Enter passphrase:")
    private_key_generator(f"{mnemonic_key}")