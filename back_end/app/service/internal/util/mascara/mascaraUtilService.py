def mascarar_email(email):
    return email[0] + '*****' + email[email.find('@')-1:] 
    