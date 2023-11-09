# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_4 import models

class RemoteProtectionGroupSnapshotTransfer(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'destroyed': 'bool',
        'started': 'int',
        'progress': 'float',
        'completed': 'int',
        'data_transferred': 'int',
        'physical_bytes_written': 'int'
    }

    attribute_map = {
        'name': 'name',
        'destroyed': 'destroyed',
        'started': 'started',
        'progress': 'progress',
        'completed': 'completed',
        'data_transferred': 'data_transferred',
        'physical_bytes_written': 'physical_bytes_written'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        destroyed=None,  # type: bool
        started=None,  # type: int
        progress=None,  # type: float
        completed=None,  # type: int
        data_transferred=None,  # type: int
        physical_bytes_written=None,  # type: int
    ):
        """
        Keyword args:
            name (str): A user-specified name. The name must be locally unique and can be changed.
            destroyed (bool): Returns a value of `true` if the snapshot has been destroyed and is pending eradication. The destroyed snapshot can be recovered by setting `destroyed=false`. Once the eradication pending period has elapsed, the snapshot is permanently eradicated and can no longer be recovered.
            started (int): The timestamp of when the snapshot replication process started. Measured in milliseconds since the UNIX epoch.
            progress (float): The percentage progress of the snapshot transfer from the source array to the target. Displayed in decimal format.
            completed (int): The timestamp of when the snapshot replication process completed. Measured in milliseconds since the UNIX epoch.
            data_transferred (int): The number of bytes transferred from the source to the target as part of the replication process. Measured in bytes.
            physical_bytes_written (int): The amount of physical/logical data written to the target due to replication. Measured in bytes.
        """
        if name is not None:
            self.name = name
        if destroyed is not None:
            self.destroyed = destroyed
        if started is not None:
            self.started = started
        if progress is not None:
            self.progress = progress
        if completed is not None:
            self.completed = completed
        if data_transferred is not None:
            self.data_transferred = data_transferred
        if physical_bytes_written is not None:
            self.physical_bytes_written = physical_bytes_written

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `RemoteProtectionGroupSnapshotTransfer`".format(key))
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
        else:
            return value

    def __getitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `RemoteProtectionGroupSnapshotTransfer`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `RemoteProtectionGroupSnapshotTransfer`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `RemoteProtectionGroupSnapshotTransfer`".format(key))
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
        if issubclass(RemoteProtectionGroupSnapshotTransfer, dict):
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
        if not isinstance(other, RemoteProtectionGroupSnapshotTransfer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
