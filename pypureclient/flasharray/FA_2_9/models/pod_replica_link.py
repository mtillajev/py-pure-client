# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_9 import models

class PodReplicaLink(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'direction': 'str',
        'lag': 'int',
        'local_pod': 'FixedReference',
        'paused': 'bool',
        'recovery_point': 'int',
        'remote_pod': 'FixedReference',
        'remotes': 'list[FixedReference]',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'direction': 'direction',
        'lag': 'lag',
        'local_pod': 'local_pod',
        'paused': 'paused',
        'recovery_point': 'recovery_point',
        'remote_pod': 'remote_pod',
        'remotes': 'remotes',
        'status': 'status'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        direction=None,  # type: str
        lag=None,  # type: int
        local_pod=None,  # type: models.FixedReference
        paused=None,  # type: bool
        recovery_point=None,  # type: int
        remote_pod=None,  # type: models.FixedReference
        remotes=None,  # type: List[models.FixedReference]
        status=None,  # type: str
    ):
        """
        Keyword args:
            id (str): A non-modifiable, globally unique ID chosen by the system.
            direction (str): The direction of replication. Valid values include `inbound` and `outbound`.
            lag (int): Duration in milliseconds that represents how far behind the replication target is from the source. This is the time difference between current time and `recovery_point`.
            local_pod (FixedReference): Reference to a local pod.
            paused (bool): Returns a value of `true` if the replica link is in a `paused` state. Returns a value of `false` if the replica link is not in a `paused` state.
            recovery_point (int): Time when the last piece of data was replicated, in milliseconds since the UNIX epoch, and the recovery point if the target pod is promoted. If the pod is currently baselining, then the value is `null`.
            remote_pod (FixedReference): Reference to a remote pod.
            remotes (list[FixedReference]): A list of remote arrays that share this pod.
            status (str): Status of the replica-link. Valid values include `replicating`, `baselining`, `paused`, `quiescing`, `quiesced`, `idle`, and `unhealthy`.
        """
        if id is not None:
            self.id = id
        if direction is not None:
            self.direction = direction
        if lag is not None:
            self.lag = lag
        if local_pod is not None:
            self.local_pod = local_pod
        if paused is not None:
            self.paused = paused
        if recovery_point is not None:
            self.recovery_point = recovery_point
        if remote_pod is not None:
            self.remote_pod = remote_pod
        if remotes is not None:
            self.remotes = remotes
        if status is not None:
            self.status = status

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodReplicaLink`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodReplicaLink`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodReplicaLink`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodReplicaLink`".format(key))
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
        if issubclass(PodReplicaLink, dict):
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
        if not isinstance(other, PodReplicaLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
