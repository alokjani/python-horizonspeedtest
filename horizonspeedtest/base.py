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
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pyvirtualdisplay import Display

from horizonspeedtest import exceptions

class HorizonSpeedTest(object):
    def __init__(self, username, password, horizon_login_url,
            horizon_switch_tenant_url, horizon_volumes_url, horizon_instances_url,
            horizon_images_url,horizon_logout_url,show_browser=False):
        """ Initialize parameters for the target cloud """
        self.username = username
        self.password = password
        self.horizon_login_url = horizon_login_url
        self.horizon_switch_tenant_url = horizon_switch_tenant_url
        self.horizon_volumes_url = horizon_volumes_url
        self.horizon_instances_url = horizon_instances_url
        self.horizon_images_url = horizon_images_url
        self.horizon_logout_url = horizon_logout_url
        self.show_browser = show_browser
        self.driver = None
        self.display = None

        if self.show_browser is False:
           self.display = Display(visible=0, size=(800, 600))
           self.display.start()

        self.driver = webdriver.Firefox()


    def login_into_horizon(self):
        """ first login into Horizon Dashboard """
        logging.info("logging into {}".format(self.horizon_login_url))
        try:
            self.driver.get(self.horizon_login_url)
            pageElement = self.driver.find_element_by_name("username")
            pageElement.send_keys(self.username)
            pageElement = self.driver.find_element_by_name("password")
            pageElement.send_keys(self.password)
            pageElement.submit()

        except NoSuchElementException:
            raise exceptions.PageSourceException("Element not found")

        navigationStart = self.driver.execute_script(
                "return window.performance.timing.navigationStart")
        responseStart   = self.driver.execute_script(
                "return window.performance.timing.responseStart")
        domComplete     = self.driver.execute_script(
                "return window.performance.timing.domComplete")

        if "Invalid" in self.driver.page_source:
            raise exceptions.LoginFailureException('Invalid Username/Password')

        backendPerformance = responseStart - navigationStart
        frontendPerformance = domComplete - responseStart
        totalTime = (backendPerformance + frontendPerformance) 

        logging.info("load time [Login Page] is {} ms".format(totalTime))
        return { 'Login Page': str(totalTime) + " ms" }


    def switch_horizon_tenant(self):
        """ Switch to the tenant underwhich we want test browser calls """
        logging.info("switching tenant {}".format(self.horizon_switch_tenant_url))
        self.driver.get(self.horizon_switch_tenant_url)


    def logout_from_horizon(self):
        """ Ensure that we logout from the browser before we exit """
        self.driver.get(self.horizon_logout_url)
        logging.info("logging out of horizon {}".format(self.horizon_logout_url))
        self._driverQuit()


    def _load_page_measure_time(self, driver, source, tag):
        """ program core that GETs the URL, computes browser load time """
        self.driver.get(source)
        navigationStart = driver.execute_script(
                "return window.performance.timing.navigationStart")
        responseStart   = driver.execute_script(
                "return window.performance.timing.responseStart")
        domComplete     = driver.execute_script(
                "return window.performance.timing.domComplete")

        backendPerformance = responseStart - navigationStart
        frontendPerformance = domComplete - responseStart
        totalTime = (backendPerformance + frontendPerformance) 

        logging.info("load time [%s] is %s ms" % (tag,totalTime))
        return { tag: str(totalTime) + " ms" }


    def load_images_page(self):
        """ Navigate to Images Page """
        logging.info("loading images page {}".format(self.horizon_instances_url))
        return self._load_page_measure_time(self.driver,self.horizon_images_url,
                tag = "Images Page")


    def load_instances_page(self):
        """ Navigate to Instances Page """
        logging.info("loading instances page {}".format(self.horizon_instances_url))
        return self._load_page_measure_time(self.driver, self.horizon_instances_url,
                tag = "Instances Page")


    def load_volumes_page(self):
        """ Navigate to the Volumes Page """
        logging.info("loading volumes page {}".format(self.horizon_volumes_url))
        return self._load_page_measure_time(self.driver, self.horizon_volumes_url,
                tag = "Volumes Page")


    def _driverQuit(self):
        self.driver.close()

