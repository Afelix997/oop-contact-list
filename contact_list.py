class ContactList:


    def __init__(self,group_title,contacts_list):
        self.group_title=group_title
        self.contacts_list=contacts_list
    
    def __str__(self):
        return f'{self.contacts_list}'
    
    def add_contact(self,name,number):
        self.contacts_list.append({"name": name, "number": number})
        self.contacts_list = sorted(self.contacts_list, key=lambda x: list(x['name']))
        return f"{name} added to Contact List!"

    def remove_contact(self, contact_to_remove):
           for i in range(len(self.contacts_list)):
            if self.contacts_list[i]['name'] == contact_to_remove:
                del self.contacts_list[i]
                break
    def find_shared_contacts(self,input_list):
        result=[]
        for i in self.contacts_list:
            for k in input_list.contacts_list:
                if i['name']==k['name']:
                    result.append(i)
        result = sorted(result, key=lambda x: list(x['name']))            
        return result
    
