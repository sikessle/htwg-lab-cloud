import keystoneclient.v2_0.client as ksclient
import novaclient.v2.client as nvclient
import glanceclient.v2.client as glclient
import cinderclient.v2.client as ciclient
import json

class Client:
    def __init__(self):
        self.ks = self.keystone()

    def getServiceEndpoints(self):
        endpoints = self.ks.service_catalog.get_endpoints()
        print json.dumps(endpoints, sort_keys=True, indent=4, separators=(',', ': '))
        return endpoints

    def keystone(self):
        creds = {}
        creds['auth_url'] = "http://192.168.35.129:35357/v2.0"
        creds['username'] = "admin"
        creds['password'] = "adminpw"
        creds['tenant_name'] = "demo"
        keystone = ksclient.Client(**creds)
        return keystone

    def nova(self):
        creds = {}
        creds['auth_url'] = "http://192.168.35.129:35357/v2.0"
        creds['username'] = "admin"
        creds['api_key'] = "adminpw"
        creds['project_id'] = "demo"
        nova = nvclient.Client(**creds)
        return nova

    def glance(self):
        endpoint = self.ks.service_catalog.url_for(service_type='image', endpoint_type='publicURL')
        client = glclient.Client(endpoint, token=self.ks.auth_token)
        return client

    def cinder(self):
	print self.ks.auth_token
        endpoint = self.ks.service_catalog.url_for(service_type='volume', endpoint_type='publicURL')
        client = ciclient.Client(endpoint, token=self.ks.auth_token)
        return client




