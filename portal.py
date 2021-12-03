import os
import argparse
import time

from core.resources import UserDomain
from core.parser import ColorPrint
from core import process_request as ProcessRequest


def banner():
    """
    banner function is showing ascii art for project name. It contains Domain Trails and tag line for project
    :return: strings for project banner.
    :rtype: basestring
    """

    banner_text = """
  -------------------------------------------------------------------------------
      ____                            _           ______              _  __     
     / __ \ ____   ____ ___   ____ _ (_)____     /_  __/_____ ____ _ (_)/ /_____
    / / / // __ \ / __ `__ \ / __ `// // __ \     / /  / ___// __ `// // // ___/
   / /_/ // /_/ // / / / / // /_/ // // / / /    / /  / /   / /_/ // // /(__  ) 
  /_____/ \____//_/ /_/ /_/ \__,_//_//_/ /_/    /_/  /_/    \__,_//_//_//____/  
  -------------------------------------------------------------------------------
    Domain Trails - domains footprints, reconnaissance & information gathering 
  -------------------------------------------------------------------------------                                                                              
    """
    return banner_text


if __name__ == '__main__':
    os.system("")
    ColorPrint.print_warn(banner())
    # Just giving small amount of sleep before printing content on screen
    time.sleep(.5)
    parser = argparse.ArgumentParser(description="Domain Trails, a project for domain information gathering from online"
                                                 "sources.")
    parser.add_argument("-d", dest="domain", required=True, type=str, help="Domain address for recon operation.")
    # parser.add_argument("-p", dest="enable_proxy", type=bool, default=False,
    #                     help="Enable free ssl proxies while performing analysis.")
    args = parser.parse_args()

    if args.domain:
        UserDomain.domain = args.domain
    ProcessRequest()
