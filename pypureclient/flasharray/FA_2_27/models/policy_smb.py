# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.27
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_27 import models

class PolicySmb(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'destroyed': 'bool',
        'enabled': 'bool',
        'pod': 'Reference',
        'policy_type': 'str',
        'time_remaining': 'int',
        'access_based_enumeration_enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'destroyed': 'destroyed',
        'enabled': 'enabled',
        'pod': 'pod',
        'policy_type': 'policy_type',
        'time_remaining': 'time_remaining',
        'access_based_enumeration_enabled': 'access_based_enumeration_enabled'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        destroyed=None,  # type: bool
        enabled=None,  # type: bool
        pod=None,  # type: models.Reference
        policy_type=None,  # type: str
        time_remaining=None,  # type: int
        access_based_enumeration_enabled=None,  # type: bool
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A user-specified name. The name must be locally unique and can be changed.
            destroyed (bool): Returns a value of `true` if the policy has been destroyed and is pending eradication. The `time_remaining` value displays the amount of time left until the destroyed policy is permanently eradicated. Once the `time_remaining` period has elapsed, the policy is permanently eradicated and can no longer be recovered.
            enabled (bool): Returns a value of `true` if the policy is enabled.
            pod (Reference): A reference to the pod.
            policy_type (str): The type of policy. Valid values include `autodir`, `nfs`, `smb`, `snapshot`, and `quota`.
            time_remaining (int): The amount of time left, measured in milliseconds, until the destroyed policy is permanently eradicated.
            access_based_enumeration_enabled (bool): Returns a value of `true` if access based enumeration is enabled on the policy. When access based enumeration is enabled on a policy, files and folders within exports that are attached to the policy will be hidden from users who do not have permission to view them.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if destroyed is not None:
            self.destroyed = destroyed
        if enabled is not None:
            self.enabled = enabled
        if pod is not None:
            self.pod = pod
        if policy_type is not None:
            self.policy_type = policy_type
        if time_remaining is not None:
            self.time_remaining = time_remaining
        if access_based_enumeration_enabled is not None:
            self.access_based_enumeration_enabled = access_based_enumeration_enabled

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicySmb`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicySmb`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicySmb`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PolicySmb`".format(key))
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
        if issubclass(PolicySmb, dict):
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
        if not isinstance(other, PolicySmb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
