def find_contact(contact_list,sreach_name):
    for contact in contact_list:
        if contact['name']==sreach_name:
            return contact['phone']
        else:
            return"not found"