#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  krita_fedora.py
#  
#  Copyright 2018 youcef sourani <youssef.m.sourani@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
from software_center import utils
from software_center.classesplugin import BasePlugin
from software_center.utils import get_uniq_name,write_to_tmp
import subprocess



if_true_skip         = False
type_                = "installer"
arch                 = ("all",)
distro_name          = ("fedora",)
distro_version       = ("all",)
category             = "Graphics"
category_icon_theme  = "applications-graphics-symbolic"
desktop_env          = ("all",)
display_type         = ("all",)
title                = "Krita"
subtitle             = "Digital Painting, Creative Freedom"
keywords             = "krita"
licenses             = (("License\nGPL-3.0-only","https://www.gnu.org/licenses/gpl-3.0.en.html"),)
website              = ("WebSite","https://krita.org/")


all_package = ["krita","krita-libs"]

class Plugin(BasePlugin):
    __gtype_name__ = get_uniq_name(__file__) #uniq name and no space
    def __init__(self,parent,threads):
        BasePlugin.__init__(self,parent=parent,
                            threads=threads,
                            button_image="krita.png",
                            button_install_label="Install",
                            button_remove_label="Remove",
                            button_frame=False,
                            blockparent=False,
                            daemon=True,
                            waitmsg="Wait...",
                            runningmsg="Running...",
                            loadingmsg="Loading...",
                            ifinstallfailmsg="Install Krita Failed",
                            ifremovefailmsg="Remove Krita Failed",
                            parallel_install=False)


    def check(self):
        check_package = all([utils.check_rpm_package_exists(pack) for pack in all_package])
        return not check_package     
         
    def install(self):
        to_install = [pack for pack in all_package if not utils.check_rpm_package_exists(pack)]
        to_install = " ".join(to_install)
        if subprocess.call("pkexec dnf install {} -y --best".format(to_install),shell=True)==0:
            return True
        return False
        
    def remove(self):
        to_remove = " ".join([pack for pack in all_package if utils.check_rpm_package_exists(pack)])
        if subprocess.call("pkexec rpm -v --nodeps -e {}".format(to_remove),shell=True)==0:
            return True
        return False


        
