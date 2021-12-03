import os
import argparse

from core.resources import UserDomain
from core.parser import ColorPrint
from core import ProcessRequest


def banner():
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
    parser = argparse.ArgumentParser(description="Domain Trails, a project for domain information gathering from online"
                                                 "sources.")
    parser.add_argument("-d", dest="domain", required=True, type=str, help="Domain address for recon operation.")
    # parser.add_argument("-p", dest="enable_proxy", type=bool, default=False,
    #                     help="Enable free ssl proxies while performing analysis.")
    args = parser.parse_args()

    if args.domain:
        UserDomain.DOMAIN = args.domain
    ProcessRequest()
