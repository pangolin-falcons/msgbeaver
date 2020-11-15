def writeVendorPrompt(vendor_name, address, message):
    return ("Hi {},\n" +
            "We have a new job for you at {}. Here is the message:\n\n" +
            "{}\n\n" + 
            "To take the job reply \"accept\" or to deny reply \"decline\"").format(
            vendor_name, address, message)

def writeRequestConfirmation(user_name, vendor_name):
    return ("Hi {},\n" +
            "We have hired {} to take care of your request! They will come " +
            "by soon to help you. Have a great day and thanks for using message " +
            "beaver!").format(
            user_name, vendor_name)

