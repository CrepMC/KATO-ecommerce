import bcrypt  

password = "nhan0202"  # Đổi thành mật khẩu bạn muốn
hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())  

print("Hashed password:", hashed_password.decode())  
