# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_0 import models

class PodArrayStatus(object):
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
        'resource_type': 'str',
        'frozen_at': 'int',
        'mediator_status': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'resource_type': 'resource_type',
        'frozen_at': 'frozen_at',
        'mediator_status': 'mediator_status',
        'status': 'status'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        resource_type=None,  # type: str
        frozen_at=None,  # type: int
        mediator_status=None,  # type: str
        status=None,  # type: str
    ):
        """
        Keyword args:
            id (str): The opaque and unique id of this resource.
            name (str): The name of this resource.
            resource_type (str): The type of this resource represented by the name of its REST endpoint. For example, \"arrays\", \"network-interfaces\", and \"metrics\". The value may be `null` if the resource is not represented.
            frozen_at (int): The Unix timestamp of when the array was last in sync with the pod (or null if the array is currently in sync).
            mediator_status (str): The status of the mediator as assessed by this array. Valid values are `flummoxed`, `online`, `unknown`, and `unreachable`. `flummoxed` - The array has the wrong UUID for the mediator. This means that the array can reach a mediator, but is talking to the wrong one. Typically, this would be due to a misconfiguration in the customer environment (e.g. DNS misconfiguration). UUIDs also have a TTL. If a pod goes offline on one array, and stays like that for weeks (such that the TTL expires), it may also show this status until the peer array is reachable again. `online` - The array is successfully communicating with the mediator. `unreachable` - The array cannot reach the mediator. This could be due to a network issue or the mediator is down.
            status (str): Status of an array in the pod. Valid values are `offline`, `online`, `resyncing`, and `unknown`. `offline` - There is a problem. This array cannot confirm it has the latest data for this pod. This array can not handle IO to the pod nor could it take over during an HA event. `online` - Everything is fine. This array has the latest data for this pod. This array can handle IO to the pod and can take over during an HA event. `resyncing` - There was a problem. This array is actively catching up to get the latest data for this pod. This array can handle IO to this pod's volumes, however it could not take over during an HA event. `unknown` - The state of the pod on this array cannot be determined. This state is only seen on disconnected arrays. The disconnected array cannot determine if the pod on another array is online or offline.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if resource_type is not None:
            self.resource_type = resource_type
        if frozen_at is not None:
            self.frozen_at = frozen_at
        if mediator_status is not None:
            self.mediator_status = mediator_status
        if status is not None:
            self.status = status

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodArrayStatus`".format(key))
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
            raise KeyError("Invalid key `{}` for `PodArrayStatus`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodArrayStatus`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodArrayStatus`".format(key))
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
        if issubclass(PodArrayStatus, dict):
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
        if not isinstance(other, PodArrayStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
