# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_19 import models

class OverrideCheck(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'args': 'str',
        'persistent': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'args': 'args',
        'persistent': 'persistent'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        args=None,  # type: str
        persistent=None,  # type: bool
    ):
        """
        Keyword args:
            name (str): The name of the upgrade check to be overridden so the software upgrade can continue if the check failed or is anticipated to fail during the upgrade process. Overriding the check forces the system to ignore the check failure and continue with the upgrade. If the check includes more specific checks that failed or are anticipated to fail, set them using the `args` parameter. For example, the HostIOCheck check may include a list of hosts that have failed or are anticipated to fail the upgrade check.
            args (str): The name of the specific check within the override check to ignore so that the system can continue with the software upgrade. The `name` parameter of the override check must be specified with the `args` parameter. For example, if the HostIOCheck check fails on hosts host01 and host02, the system displays a list of these host names in the failed check. To override the HostIOCheck checks for host01 and host02, set `name=HostIOCheck`, and set `args=host01,host02`. Enter multiple `args` in comma-separated format. Note that not all checks have `args` values.
            persistent (bool): If set to `true`, the system always ignores the failure of the specified upgrade check and continues with the upgrade process. If set to `false`, the system ignores the failure of the specified upgrade check until the upgrade check finishes and the upgrade process is continued. For example, the `continue` command is successfully issued in an `interactive` mode, or the first upgrade check step successfully finishes in a `one-click` mode.
        """
        if name is not None:
            self.name = name
        if args is not None:
            self.args = args
        if persistent is not None:
            self.persistent = persistent

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `OverrideCheck`".format(key))
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
            raise KeyError("Invalid key `{}` for `OverrideCheck`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `OverrideCheck`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `OverrideCheck`".format(key))
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
        if issubclass(OverrideCheck, dict):
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
        if not isinstance(other, OverrideCheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
