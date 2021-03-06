'''Utilities related to fault domain information from cloud providers.

************************************************************************
FOR THE TIME BEING WHATEVER MODIFICATIONS ARE APPLIED TO THIS FILE
SHOULD ALSO BE APPLIED TO ANY OTHER PARTNER REPOS
************************************************************************
'''
import logging


log = logging.getLogger(__name__)

# TODO: use cloud provider library APIs to get list of regions.
AWS_REGIONS = [
    'ap-northeast-1',
    'ap-northeast-2',
    'ap-south-1',
    'ap-southeast-1',
    'ap-southeast-2',
    'ca-central-1',
    'eu-central-1',
    'eu-west-1',
    'eu-west-2',
    'sa-east-1',
    'us-east-1',
    'us-east-2',
    'us-west-1',
    'us-west-2'
]

# TODO: use cloud provider library APIs to get list of zones.
AWS_ZONE_SUFFIXES = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']


def is_valid_aws_region(region: str):
    return region in AWS_REGIONS


def is_valid_aws_zone(zone: str):
    region = zone[:-1]
    zone_suffix = zone.lstrip(region)
    return is_valid_region(region) and zone_suffix in AWS_ZONE_SUFFIXES


# TODO: handle multiple cloud providers.
def is_valid_region(region: str):
    return is_valid_aws_region(region)


# TODO: handle multiple cloud providers.
def is_valid_zone(zone: str):
    return is_valid_aws_zone(zone)
