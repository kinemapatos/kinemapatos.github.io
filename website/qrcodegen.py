import qrcode
import random
import string

def generate_qr_codes(num_codes):
    qr_codes = []
    ticket_codes = []
    
    for _ in range(num_codes):
        ticket_code = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(ticket_code)
        qr.make(fit=True)
        qr_code = qr.make_image(fill_color="black", back_color="white")
        qr_codes.append(qr_code)
        ticket_codes.append(ticket_code)

    return qr_codes, ticket_codes

# Generate 40 QR codes and ticket codes
qr_codes, ticket_codes = generate_qr_codes(40)

# Save QR codes as images
for i, qr_code in enumerate(qr_codes, start=1):
    qr_code_file = f'qr_code_{i}.png'
    qr_code.save(qr_code_file)
    print(f"QR code {i} with ticket code '{ticket_codes[i-1]}' has been generated and saved as '{qr_code_file}'.")

# Print ticket codes list
print(f"Ticket codes: {ticket_codes}")