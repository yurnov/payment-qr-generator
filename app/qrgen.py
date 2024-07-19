import base64
import qrcode
import argparse


def create_qr(account, edrpo, recipient, amount, purpose, output_file):
    # Construct the data string for version 002 of QR code, reference https://bank.gov.ua/ua/legislation/Resolution_01022021_11
    # Elements of string are separated by LF (line feed) character:
    # 1. Empty element without any separator
    # 2. Service tag (always 'BCB') with end of line separator (LF)
    # 3. Version of the QR code (always '002')
    # 4. Encoding, 1 for UTF-8 or 2 for CP1251 (always '1')
    # 5. Function, olny 'UCT' allowed (Ukrainian Credit Transfer)
    # 6. Element BIC (Bank Identifier Code), reserved for future use
    # 7. Recipient, string up to 70 characters long
    # 8. Account number of the recipient (IBAN)
    # 9. Amount with currency, i.e. UAH999999999.99
    # 10. Code of recepient (EDRPOU)
    # 11. Code of Payment purpose, reserved for future use
    # 12. Payment reference, reserved for future use
    # 13. Payment purpose, string up to 140 characters long
    # 14. Displayed message, reserved for future use
    # All reserved for future use fields are empty (only LF character)

    data_str = f"BCB\n002\n1\nUCT\n\n{recipient}\n{account}\n{amount}\n{edrpo}\n\n\n{purpose}\n"

    # Encode the data string in Base64Url
    encoded_data = base64.urlsafe_b64encode(data_str.encode()).decode()

    # Construct the full URL
    qr_url = f"https://bank.gov.ua/qr/{encoded_data}"

    # Generate the QR code
    qr = qrcode.make(qr_url)
    qr.save(output_file)

    # return the URL, it's used for testing
    return qr_url


def main():

    parser = argparse.ArgumentParser(description="Generate a QR code for a Ukrainian payment")
    parser.add_argument("-a", "--account", help="Recipient's account number")
    parser.add_argument("-e", "--edrpo", help="Recipient's EDRPOU code")
    parser.add_argument("-r", "--recipient", help="Recipient's name")
    parser.add_argument("-m", "--amount", help="Amount to transfer with currency in format UAH999999999.99")
    parser.add_argument("-p", "--purpose", help="Purpose of the payment")

    # ensure that arguments are provided
    args = parser.parse_args()
    if not args.account or not args.edrpo or not args.recipient or not args.amount or not args.purpose:
        parser.print_help()

    if args.account:
        account = args.account
    else:
        account = input("Enter the recipient's account number: ")

    if args.edrpo:
        edrpo = args.edrpo
    else:
        edrpo = input("Enter the recipient's EDRPOU code: ")

    if args.recipient:
        recipient = args.recipient
    else:
        recipient = input("Enter the recipient's name: ")

    if args.amount:
        amount = args.amount
    else:
        amount = input("Enter the amount to transfer: ")

    if args.purpose:
        purpose = args.purpose
    else:
        purpose = input("Enter the purpose of the payment: ")

    # Create QR code
    output_file = "/output/qr_code.png"
    create_qr(account, edrpo, recipient, amount, purpose, output_file)


if __name__ == "__main__":
    main()
