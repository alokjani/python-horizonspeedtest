#    Copyright 2015 Reliance Jio Infocomm, Ltd.
#    Author: Alok Jani <Alok.Jani@ril.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
# -----------------------------------------------------------

import logging

from horizonspeedtest import base
from horizonspeedtest import exceptions

def perform_on_cloud(cloud,cfg,show_browser):
    """ returns list of load times for each of the cloud URLs """
    logging.info("Starting tests for {}.".format(cloud))
    try:
        c = base.HorizonSpeedTest(
            cfg['username'],
            cfg['password'],
            cfg['horizon_login_url'],
            cfg['horizon_switch_tenant_url'],
            cfg['horizon_volumes_url'],
            cfg['horizon_instances_url'],
            cfg['horizon_images_url'],
            cfg['horizon_logout_url'],
            show_browser)

    except KeyError:
        raise exceptions.MissingConfigurationParameterException("Parameter not found")

    # Login first, then load individual pages serially
    t_login =  c.login_into_horizon()
    c.switch_horizon_tenant()
    t_instances = c.load_instances_page()
    t_images = c.load_images_page()
    t_volumes = c.load_volumes_page()

    # Logout once done
    c.logout_from_horizon()
#    import json
#    print "%s, %s, %s, %s" % (json.dumps(t_login), json.dumps(t_instances), json.dumps(t_images), json.dumps(t_volumes))
    d = {}
    d['cloud_name'] = cloud
    d['time_login'] = t_login['Login Page']
    d['time_instances'] = t_instances['Instances Page']
    d['time_volumes'] = t_volumes['Volumes Page']
    d['time_images'] = t_images['Images Page']

    l = []
    l.append(d['cloud_name'])
    l.append(d['time_login'])
    l.append(d['time_instances'])
    l.append(d['time_volumes'])
    l.append(d['time_images'])

    return l

def pretty_print(result_list):
    """ Prints the resultset as a table, one row per object """
    from tabulate import tabulate
    table = tabulate(result_list, tablefmt='psql',stralign='right',
                     headers=[ 'cloud_name', 'time_login', 'time_instances', 'time_volumes', 'time_images'] )
    return table
