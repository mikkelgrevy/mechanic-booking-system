# Flask secret key (generate with: import secrets; secrets.token_hex(16))
app_pass = "your-secret-key-here-change-this"

# Admin password for first authentication step
admin_pass = "your-admin-password-here"

# TOTP secret for 2FA (generate with: import pyotp; pyotp.random_base32())
totp_pass = "your-totp-secret-here"