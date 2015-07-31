import keystoneclient.v2_0.client as ksclient
import novaclient.v2.client as nvclient
import glanceclient.v2.client as glclient
import cinderclient.v2.client as ciclient
import json

class Admin:
    """
    Course class can be used to access services as an Admin.
    This is required for some actions (e.g. creating a tenant).
    """
    def __init__(self):
        self.auth_url = 'http://192.168.35.129:35357/v2.0'
        self.username = 'opnstadm'
        self.password = '@@@adminpw@@@'
        self.ks = self.keystone()

    def getServiceEndpoints(self):
        endpoints = self.ks.service_catalog.get_endpoints()
        print json.dumps(endpoints, sort_keys=True, indent=4, separators=(',', ': '))
        return endpoints

    def keystone(self, tenant="service"):
        creds = {}
        creds['auth_url'] = self.auth_url
        creds['username'] = self.username
        creds['password'] = self.password
        creds['tenant_name'] = tenant
        keystone = ksclient.Client(**creds)
        return keystone

    def nova(self, tenant="service"):
        creds = {}
        creds['auth_url'] = self.auth_url
        creds['username'] = self.username
        creds['api_key'] = self.password
        creds['project_id'] = tenant
        nova = nvclient.Client(**creds)
        return nova

    def glance(self):
        endpoint = self.ks.service_catalog.url_for(service_type='image', endpoint_type='publicURL')
        client = glclient.Client(endpoint, token=self.ks.auth_token)
        return client

    def cinder(self, tenant="service"):
        #endpoint = self.ks.service_catalog.url_for(service_type='volume', endpoint_type='publicURL')
        #client = ciclient.Client(endpoint, token=self.ks.auth_token)
        creds = {}
        creds['auth_url'] = self.auth_url
        creds['username'] = self.username
        creds['api_key'] = self.password
        creds['project_id'] = tenant
        client = ciclient.Client(**creds)        
        return client




