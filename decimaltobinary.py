# This is a tool I am going to use to convert a decimal IP address to binary

def decimaltobinary(ipaddress):
    # First, I am going to split each part of the decimal IP address
    number_list = ipaddress.split(".")

    # Next I am going to format each item in the list as a binary number
    for number in number_list:
        bin_number = format(int(number), '08b')

        # Convert the binary number back to a string
        str_number = str(bin_number)

        # Return the binary number to the user as a string
        print(str(str_number), end=".")

if __name__ == '__main__':
    decimsltobinary()


        
