#-*-coding:utf-8-*-

import os
import sys
import string
import traceback
import importlib
from inflector import Inflector
from .package_map import PackageMap

class Loader(object):

    @staticmethod
    @PackageMap.ensure_setup_packages()
    def load_all_tasks():
        result     = {"success": list(), "failure": list()}

        for task_clsname_1 in PackageMap.task_clsname_to_package.keys():
            is_success = False
            task_cls   = None
            err        = None

            try:
                task_cls    = Loader.load_a_task_by_name(task_clsname_1)
                is_success  = True
            except Exception as e:
                err = list(sys.exc_info())
                err[2] = "".join(traceback.format_tb(err[2]))
                err = str(err[0]) + ": " + str(err[1]) + "\n" + err[2]

            if is_success:
                result['success'].append({"task_cls": task_cls})
            else:
                result['failure'].append({"err": err,           "task_clsname": task_clsname_1})

        return result

    @staticmethod
    @PackageMap.ensure_setup_packages()
    def load_a_task_by_name(task_clsname_1):
        assert task_clsname_1[0] in string.uppercase, \
                                "Task name should begin with UpperCase !"

        package_path = PackageMap.task_clsname_to_package[task_clsname_1].__name__ + \
                       ".luiti_tasks." + \
                       Inflector().underscore(task_clsname_1)
        task_lib     = Loader.import2(package_path)
        return getattr(task_lib, task_clsname_1)


    @staticmethod
    def import2(a_package):
        return __import__(a_package, None, None, 'non_empty')

PackageMap.Loader = Loader
