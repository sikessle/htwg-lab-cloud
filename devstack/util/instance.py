print "OPENSTACK"

# keystone
print "Keystone"
import keystoneclient.v2_0.client as ksclient
import novaclient.v2.client as nvclient
import glanceclient.v2.client as glclient
# general imports
import os
import time



def keystone():
    creds = {}
    creds['auth_url'] = "http://192.168.35.129:35357/v2.0"
    creds['username'] = "opnstadm"
    creds['password'] = "@@@adminpw@@@"
    creds['tenant_name'] = "professor"
    keystone = ksclient.Client(**creds)
    return keystone

def nova():
    creds = {}
    creds['auth_url'] = "http://192.168.35.129:35357/v2.0"
    creds['username'] = "opnstadm"
    creds['api_key'] = "@@@adminpw@@@"
    creds['project_id'] = "professor"
    nova = nvclient.Client(**creds)
    return nova

keystone = keystone()
print "keystone auth token " + keystone.auth_token


print "Glance"
# keystone provide a service catalog, where we can lookup available services.
glanceEndpoint = keystone.service_catalog.url_for(service_type='image', endpoint_type='publicURL')
glance = glclient.Client(glanceEndpoint, token=keystone.auth_token)
images = glance.images.list()
print "Glance endpoint " + glanceEndpoint
print "Glance images:"
for i in images:
    print i.name



print "Nova"
nova = nova()
print nova.servers.list()


def stopInstances():
    print "stop instances"
    servers = nova.servers.list()
    for server in servers:
        server.delete()

def startInstances():
    startInstance()

def startInstance(instanceName="test", imageName="cirros-0.3.2-x86_64-uec", flavorName="m1.tiny"):
    print "start instance"
    #if not nova.keypairs.findall(name="mykey"):
    #    with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
    #        nova.keypairs.create(name="mykey", public_key=fpubkey.read())

    image = nova.images.find(name=imageName)
    #image = nova.images.list()[0]
    flavor = nova.flavors.find(name=flavorName)
    instance = nova.servers.create(name=instanceName, image=image, flavor=flavor)

    # Poll at 5 second intervals, until the status is no longer 'BUILD'
    status = instance.status
    while status == 'BUILD':
        time.sleep(5)
        # Retrieve the instance again so the status field updates
        instance = nova.servers.get(instance.id)
        status = instance.status
        print "status: %s" % status


stopInstances()

#startInstance()
#startInstance()
#startInstances()
