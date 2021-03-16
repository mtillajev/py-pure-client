# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_5 import models

class PodPerformanceReplication(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'continuous_bytes_per_sec': 'ReplicationPerformanceWithTotal',
        'periodic_bytes_per_sec': 'ReplicationPerformanceWithTotal',
        'pod': 'FixedReference',
        'resync_bytes_per_sec': 'ReplicationPerformanceWithTotal',
        'sync_bytes_per_sec': 'ReplicationPerformanceWithTotal',
        'time': 'int',
        'total_bytes_per_sec': 'int'
    }

    attribute_map = {
        'continuous_bytes_per_sec': 'continuous_bytes_per_sec',
        'periodic_bytes_per_sec': 'periodic_bytes_per_sec',
        'pod': 'pod',
        'resync_bytes_per_sec': 'resync_bytes_per_sec',
        'sync_bytes_per_sec': 'sync_bytes_per_sec',
        'time': 'time',
        'total_bytes_per_sec': 'total_bytes_per_sec'
    }

    required_args = {
    }

    def __init__(
        self,
        continuous_bytes_per_sec=None,  # type: models.ReplicationPerformanceWithTotal
        periodic_bytes_per_sec=None,  # type: models.ReplicationPerformanceWithTotal
        pod=None,  # type: models.FixedReference
        resync_bytes_per_sec=None,  # type: models.ReplicationPerformanceWithTotal
        sync_bytes_per_sec=None,  # type: models.ReplicationPerformanceWithTotal
        time=None,  # type: int
        total_bytes_per_sec=None,  # type: int
    ):
        """
        Keyword args:
            continuous_bytes_per_sec (ReplicationPerformanceWithTotal): Total bytes transmitted or received per second for continuous replication. The continuous replication feature is used for disaster recovery on FlashArray and provides a recovery point objective (RPO) of significantly less than 30s.
            periodic_bytes_per_sec (ReplicationPerformanceWithTotal): Total bytes transmitted or received per second for periodic replication.
            pod (FixedReference): Reference to the pod that the performance data is associated with.
            resync_bytes_per_sec (ReplicationPerformanceWithTotal): Total bytes transmitted or received per second during resync replication. Resync replication is the mechanism to bring two arrays into sync. This may occur during an initial pod stretch, or, in case of outage, when two arrays reestablish connection. After the connection is restored, the array that was online starts replicating pod data to its peer array until the pod is once again in sync.
            sync_bytes_per_sec (ReplicationPerformanceWithTotal): Total bytes transmitted or received per second for synchronous replication.
            time (int): Sample time in milliseconds since the UNIX epoch.
            total_bytes_per_sec (int): Total bytes transmitted and received per second for all types of replication.
        """
        if continuous_bytes_per_sec is not None:
            self.continuous_bytes_per_sec = continuous_bytes_per_sec
        if periodic_bytes_per_sec is not None:
            self.periodic_bytes_per_sec = periodic_bytes_per_sec
        if pod is not None:
            self.pod = pod
        if resync_bytes_per_sec is not None:
            self.resync_bytes_per_sec = resync_bytes_per_sec
        if sync_bytes_per_sec is not None:
            self.sync_bytes_per_sec = sync_bytes_per_sec
        if time is not None:
            self.time = time
        if total_bytes_per_sec is not None:
            self.total_bytes_per_sec = total_bytes_per_sec

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `PodPerformanceReplication`".format(key))
        if key == "total_bytes_per_sec" and value is not None:
            if value < 0:
                raise ValueError("Invalid value for `total_bytes_per_sec`, must be a value greater than or equal to `0`")
        self.__dict__[key] = value

    def __getattribute__(self, item):
        value = object.__getattribute__(self, item)
        if isinstance(value, Property):
            raise AttributeError
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
        if issubclass(PodPerformanceReplication, dict):
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
        if not isinstance(other, PodPerformanceReplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
