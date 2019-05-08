import requests
import ujson
# from b2b_app.config import CONFIG

class Hubspot:
    def __init__(self, hub_id, refresh_token):
        self.hub_id = hub_id
        self.refresh_token = refresh_token
        self.access_token = self.get_access_token(refresh_token)
        self._lists_url = 'https://api.hubapi.com/contacts/v1/lists'
        pass
    
    def get_access_token(self, refresh_token):
        pass

    def update_access_token():
        pass

    ##### ACCOUNT APIS #####
    def get_account_by_id():
        pass

    # read all companies
    def get_all_accounts():
        pass

    # create company in hubspot
    def create_account():
        pass

    # update company
    def update_account():
        # 
        pass

    def add_contact_to_account():
        pass

    def get_associated_deals_for_account():
        pass

    ##### CONTACT APIS #####
    def get_contact_by_id():
        pass

    # read all companies
    def get_all_contacts():
        url = self._lists_url + 'all/contacts/all'
        querystring = {
            'vid-offset': '0',
            'count': '10',
            'hapikey': '5fb77dd9-1804-4bdb-b21b-8de6c7a2900a',
        }
        response = requests.request(
            'GET',
            url,
            params=querystring
        )
        print(response.text)

    # create contact
    def create_contact():
        pass

    # update contact
    def update_contact():
        pass

    # deleting contact
    def delete_contact():
        pass

    def get_associated_deals_for_contact():
        pass
    
    ##### LISTS APIS #####
    def get_all_static_lists():
        url = self._lists_url
        querystring = {
            'offset': '0',
            'count': '10',
            'hapikey': '5fb77dd9-1804-4bdb-b21b-8de6c7a2900a',
        }
        response = requests.request(
            'GET',
            url,
            params=querystring
        )
        print(response.text)
    
    def get_all_dynamic_lists():
        url = self._lists_url + '/dynamic'
        querystring = {
            'offset': '0',
            'count': '10',
            'hapikey': '5fb77dd9-1804-4bdb-b21b-8de6c7a2900a',
        }
        response = requests.request(
            'GET',
            url,
            params=querystring
        )
        print(response.text)
    
    def get_list_by_id(self, list_id):
        url = self._lists_url + '/' + list_id
        querystring = {
            'hapikey': '5fb77dd9-1804-4bdb-b21b-8de6c7a2900a',
        }
        response = requests.request(
            'GET',
            url,
            params=querystring
        )
        print(response.text)
    
    def create_static_list(self, list_name):
        url = self._lists_url
        querystring = {
            'hapikey': '5fb77dd9-1804-4bdb-b21b-8de6c7a2900a',
        }
        payload = ujson.dumps({
            'name': list_name,
            'dynamic': False,
            'portalId': 5225356,
            'filters': [],
        })
        response = requests.request(
            'POST',
            url,
            data=payload,
            params=querystring
        )
        print(response.text)
    
    def create_dynamic_list():
        url = self._lists_url
        querystring = {
            'hapikey': '5fb77dd9-1804-4bdb-b21b-8de6c7a2900a',
        }
        payload = ujson.dumps({
            'name': list_name,
            'dynamic': True,
            'portalId': 5225356,
            'filters': [],
        })
        response = requests.request(
            'POST',
            url,
            data=payload,
            params=querystring
        )
        print(response.text)
        pass
    
    def delete_list():
        pass
    
    def get_all_contacts_from_a_list(self, list_id):
        url = self._lists_url + '/' + list_id + '/contacts/all'
        querystring = {
            'vidOffset': '0',
            'count': '100',
            'hapikey': '5fb77dd9-1804-4bdb-b21b-8de6c7a2900a',
        }
        response = requests.request(
            'GET',
            url,
            params=querystring
        )
        print(response.text)
    
    def add_contacts_in_a_static_list(self, list_id, array_of_ids):
        url = self._lists_url + '/' + list_id + '/add'
        querystring = {
            'hapikey': '5fb77dd9-1804-4bdb-b21b-8de6c7a2900a',
        }
        payload = ujson.dumps({
            vids: array_of_ids
        })
        response = requests.request(
            'POST',
            url,
            data=payload,
            params=querystring
        )
        print(response.text)

    ##### DEAL APIS #####
    # create deal
    def get_deal_owner_by_id():
        # check deal id or owner id
        pass

    def create_deal():
        pass

    def associate_contact_to_deal():
        pass

    def associate_account_to_deal():
        pass

    def dissociate_contact_from_deal():
        pass

    def find_deal_owner():
        # yes
        pass

    def test():
        pass
