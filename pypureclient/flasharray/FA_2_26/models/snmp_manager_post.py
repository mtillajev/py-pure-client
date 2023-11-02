# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_26 import models

class SnmpManagerPost(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'host': 'str',
        'notification': 'str',
        'v2c': 'SnmpV2c',
        'v3': 'SnmpV3Post',
        'version': 'str'
    }

    attribute_map = {
        'host': 'host',
        'notification': 'notification',
        'v2c': 'v2c',
        'v3': 'v3',
        'version': 'version'
    }

    required_args = {
    }

    def __init__(
        self,
        host=None,  # type: str
        notification=None,  # type: str
        v2c=None,  # type: models.SnmpV2c
        v3=None,  # type: models.SnmpV3Post
        version=None,  # type: str
    ):
        """
        Keyword args:
            host (str): DNS hostname or IP address of a computer that hosts an SNMP manager to which Purity//FA is to send trap messages when it generates alerts.
            notification (str): The type of notification the agent will send. Valid values are `inform` and `trap`.
            v2c (SnmpV2c)
            v3 (SnmpV3Post)
            version (str): Version of the SNMP protocol to be used by Purity//FA to communicate with the specified manager. Valid values are `v2c` and `v3`.
        """
        if host is not None:
            self.host = host
        if notification is not None:
            self.notification = notification
        if v2c is not None:
            self.v2c = v2c
        if v3 is not None:
            self.v3 = v3
        if version is not None:
            self.version = version

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SnmpManagerPost`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            if item in self.attribute_map:
                return None
            else:
                raise AttributeError(f"{self} object has no attribute '{name}'")
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SnmpManagerPost`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SnmpManagerPost`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `SnmpManagerPost`".format(key))
        object.__delattr__(self, key)

    def keys(self):
        return self.attribute_map.keys()

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, list):
                    result[attr] = list(map(
                        lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                        value
                    ))
                elif hasattr(value, "to_dict"):
                    result[attr] = value.to_dict()
                elif isinstance(value, dict):
                    result[attr] = dict(map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict") else item,
                        value.items()
                    ))
                else:
                    result[attr] = value
        if issubclass(SnmpManagerPost, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SnmpManagerPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
