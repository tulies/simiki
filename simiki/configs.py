#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from os import path as osp
from pprint import pprint

import yaml

from simiki import utils

def parse_configs(config_file):
    #base_dir = osp.dirname(osp.dirname(osp.realpath(__file__)))
    try:
        with open(config_file, "rb") as fd:
            configs = yaml.load(fd)
    except yaml.YAMLError, e:
        msg = "Yaml format error in {}:\n{}".format(
                config_file,
                unicode(str(e), "utf-8")
                )
        sys.exit(utils.color_msg("error", msg))

    if configs["base_dir"] is None:
        configs["base_dir"] = osp.dirname(osp.realpath(config_file))

    configs.update(
        # The directory to store markdown files
        source = osp.join(configs["base_dir"], configs["source"]),
        # The directory to store the generated html files
        destination = osp.join(configs["base_dir"],  configs["destination"]),
        # The path of html template file
        tpl_path = osp.join(configs["base_dir"], "simiki/themes", configs["theme"]),
    )
    if configs.get("url", "") is None:
        configs["url"] = ""
    if configs.get("keywords", "") is None:
        configs["keywords"] = ""
    if configs.get("description", "") is None:
        configs["description"] = ""

    return configs

if __name__ == "__main__":
    BASE_DIR = osp.dirname(osp.dirname(osp.realpath(__file__)))
    config_file = osp.join(BASE_DIR, "_config.yml")
    pprint(parse_configs(config_file))
