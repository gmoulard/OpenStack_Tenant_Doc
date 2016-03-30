# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:20:01 2016

@author: guillaume.moulard@orange.com

0750177459_Common_Services_Sandbox-openrc.sh

#!/bin/bash

# To use an OpenStack cloud you need to authenticate against the Identity
# service named keystone, which returns a **Token** and **Service Catalog**.
# The catalog contains the endpoints for all services the user/tenant has
# access to - such as Compute, Image Service, Identity, Object Storage, Block
# Storage, and Networking (code-named nova, glance, keystone, swift,
# cinder, and neutron).
#
# *NOTE*: Using the 2.0 *Identity API* does not necessarily mean any other
# OpenStack API is version 2.0. For example, your cloud provider may implement
# Image API v1.1, Block Storage API v2, and Compute API v2.0. OS_AUTH_URL is
# only for the Identity API served through keystone.
export OS_AUTH_URL=https://identity.fr1.cloudwatt.com/v2.0

# With the addition of Keystone we have standardized on the term **tenant**
# as the entity that owns the resources.
export OS_TENANT_ID=c7260422075a48aba0e569de9d8a2d77
export OS_TENANT_NAME="0750177459_Common_Services_Sandbox"
export OS_PROJECT_NAME="0750177459_Common_Services_Sandbox"

# In addition to the owning entity (tenant), OpenStack stores the entity
# performing the action as the **user**.
export OS_USERNAME="guillaume.moulard@orange.com"

# With Keystone you pass the keystone password.
echo "Please enter your OpenStack Password: "
read -sr OS_PASSWORD_INPUT
export OS_PASSWORD=$OS_PASSWORD_INPUT

# If your configuration has multiple regions, we set that information here.
# OS_REGION_NAME is optional and only valid in certain environments.
export OS_REGION_NAME="fr1"
# Don't leave a blank variable, unset it if it was empty
if [ -z "$OS_REGION_NAME" ]; then unset OS_REGION_NAME; fi

"""

from novaclient import client

nova = client.Client(VERSION, 
                     USERNAME, 
                     PASSWORD, 
                     PROJECT_ID, 
                     AUTH_URL,
                     connection_pool=True)

nova.servers.list()
nova.flavors.list()





