# coding: utf-8

"""
    FlashBlade REST API

    A lightweight client for FlashBlade REST API 2.2, developed by Pure Storage, Inc. (http://www.purestorage.com/).

    OpenAPI spec version: 2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flashblade.FB_2_2 import models

class ContinuousReplicationPerformance(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'transmitted_bytes_per_sec': 'float',
        'received_bytes_per_sec': 'float',
        'object_backlog': 'ObjectBacklog'
    }

    attribute_map = {
        'transmitted_bytes_per_sec': 'transmitted_bytes_per_sec',
        'received_bytes_per_sec': 'received_bytes_per_sec',
        'object_backlog': 'object_backlog'
    }

    required_args = {
    }

    def __init__(
        self,
        transmitted_bytes_per_sec=None,  # type: float
        received_bytes_per_sec=None,  # type: float
        object_backlog=None,  # type: models.ObjectBacklog
    ):
        """
        Keyword args:
            transmitted_bytes_per_sec (float): Total bytes transmitted per second.
            received_bytes_per_sec (float): Total bytes received per second.
            object_backlog (ObjectBacklog): The total number of pending object operations and their size that are currently in the backlog.
        """
        if transmitted_bytes_per_sec is not None:
            self.transmitted_bytes_per_sec = transmitted_bytes_per_sec
        if received_bytes_per_sec is not None:
            self.received_bytes_per_sec = received_bytes_per_sec
        if object_backlog is not None:
            self.object_backlog = object_backlog

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `ContinuousReplicationPerformance`".format(key))
        if key == "transmitted_bytes_per_sec" and value is not None:
            if value < 0.0:
                raise ValueError("Invalid value for `transmitted_bytes_per_sec`, must be a value greater than or equal to `0.0`")
        if key == "received_bytes_per_sec" and value is not None:
            if value < 0.0:
                raise ValueError("Invalid value for `received_bytes_per_sec`, must be a value greater than or equal to `0.0`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            return None
        else:
            return value

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
        if issubclass(ContinuousReplicationPerformance, dict):
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
        if not isinstance(other, ContinuousReplicationPerformance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
