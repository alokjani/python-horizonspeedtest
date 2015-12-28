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

""" Exception definitions """

class LoginFailureException(Exception):
    """ The user is unable to login using username/password """
    pass

class PageSourceException(Exception):
    """ Page elements missing due to invalid URL or Page source """
    pass

class MissingConfigurationParameter(Exception):
    """ Required parameter was missing from configuration file """
    pass
