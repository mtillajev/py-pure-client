# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.pure1.Pure1_1_1 import models

class BucketReplicaLink(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'as_of': 'int',
        'id': 'str',
        'lag': 'int',
        'paused': 'bool',
        'recovery_point': 'int',
        'status': 'str',
        'status_details': 'str',
        'members': 'list[ResourceWithLocation]',
        'sources': 'list[ResourceWithLocation]',
        'targets': 'list[ResourceWithLocation]'
    }

    attribute_map = {
        'as_of': '_as_of',
        'id': 'id',
        'lag': 'lag',
        'paused': 'paused',
        'recovery_point': 'recovery_point',
        'status': 'status',
        'status_details': 'status_details',
        'members': 'members',
        'sources': 'sources',
        'targets': 'targets'
    }

    required_args = {
    }

    def __init__(
        self,
        as_of=None,  # type: int
        id=None,  # type: str
        lag=None,  # type: int
        paused=None,  # type: bool
        recovery_point=None,  # type: int
        status=None,  # type: str
        status_details=None,  # type: str
        members=None,  # type: List[models.ResourceWithLocation]
        sources=None,  # type: List[models.ResourceWithLocation]
        targets=None,  # type: List[models.ResourceWithLocation]
    ):
        """
        Keyword args:
            as_of (int): The freshness of the data (timestamp in millis since epoch).
            id (str): A non-modifiable, globally unique ID chosen by the system.
            lag (int): Duration, in milliseconds, which represents how far behind the replication `target` is from the `source`.
            paused (bool): Returns `true` if the replica link is paused.
            recovery_point (int): Time when the last piece of data was replicated, in milliseconds since the UNIX epoch, and the recovery point of the bucket.
            status (str): Status of the replica link. Values include `replicating`, `idle`, and `unhealthy`.
            status_details (str): Detailed information about the status of the replica link when it is `unhealthy`.
            members (list[ResourceWithLocation]): The union of source and target buckets in the replica link.
            sources (list[ResourceWithLocation]): The source buckets in the replica link.
            targets (list[ResourceWithLocation]): The target buckets in the replica link.
        """
        if as_of is not None:
            self.as_of = as_of
        if id is not None:
            self.id = id
        if lag is not None:
            self.lag = lag
        if paused is not None:
            self.paused = paused
        if recovery_point is not None:
            self.recovery_point = recovery_point
        if status is not None:
            self.status = status
        if status_details is not None:
            self.status_details = status_details
        if members is not None:
            self.members = members
        if sources is not None:
            self.sources = sources
        if targets is not None:
            self.targets = targets

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `BucketReplicaLink`".format(key))
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
            raise KeyError("Invalid key `{}` for `BucketReplicaLink`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `BucketReplicaLink`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `BucketReplicaLink`".format(key))
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
        if issubclass(BucketReplicaLink, dict):
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
        if not isinstance(other, BucketReplicaLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
