def telephone():
    phone_number = int(input())
    area_code = "(" + str(int(phone_number / 10000000)) + ") "
    body = str(int((phone_number % 10000000) / 10000)) + "-" + str(phone_number % 10000)
    print(area_code + body)
    
if __name__ == "__main__":
    telephone()