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

import argparse
import logging
import sys

import yaml

from horizonspeedtest import utils
from horizonspeedtest import constants
from horizonspeedtest import exceptions

def parse_args():
    desc = "Measure the page load times for OpenStack's Horizon Dashboard."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("--verbose", action="store_true",
                        help="Makes output verbose")
    parser.add_argument("--show-browser", action='store_true',
                        help="Run Firefox in the foreground where visible")
    parser.add_argument("--config-file", required=True,
                        help="Horizon URLs in YAML to test")
    args = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_usage()
        sys.exit(1)

    return args

def main():
    cli_opts = parse_args()

    if cli_opts.verbose:
        logging.basicConfig(level=logging.INFO,format=constants.LOGGING_FORMAT)
    else:
        logging.basicConfig(level=logging.WARNING)

    try:
        with open(cli_opts.config_file, 'r') as yamlfile:
            cfg = yaml.load(yamlfile)
    except (OSError, IOError) as exc:
        print("Configuration file not found.")
        sys.exit(1)

    try:
        result_list = []
        for cloud in cfg:
            result_list.append(
                utils.perform_on_cloud(cloud, cfg[cloud], cli_opts.show_browser))

        print utils.pretty_print(result_list)

    except exceptions.LoginFailureException as exc:
        print ("Login Failure: {}.".format(str(exc)))
        sys.exit(constants.INVALID_LOGIN)
    except exceptions.PageSourceException as exc:
        print ("Invalid Page Source or URL: {}.".format(str(exc)))
        sys.exit(constants.INVALID_URL_OR_PAGE)


if __name__ == "__main__":
    main()
