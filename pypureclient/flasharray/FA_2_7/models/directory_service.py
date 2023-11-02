# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_7 import models

class DirectoryService(object):
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'base_dn': 'str',
        'bind_password': 'str',
        'bind_user': 'str',
        'ca_certificate': 'str',
        'check_peer': 'bool',
        'enabled': 'bool',
        'services': 'list[str]',
        'uris': 'list[str]',
        'management': 'DirectoryServiceManagement'
    }

    attribute_map = {
        'name': 'name',
        'base_dn': 'base_dn',
        'bind_password': 'bind_password',
        'bind_user': 'bind_user',
        'ca_certificate': 'ca_certificate',
        'check_peer': 'check_peer',
        'enabled': 'enabled',
        'services': 'services',
        'uris': 'uris',
        'management': 'management'
    }

    required_args = {
    }

    def __init__(
        self,
        name=None,  # type: str
        base_dn=None,  # type: str
        bind_password=None,  # type: str
        bind_user=None,  # type: str
        ca_certificate=None,  # type: str
        check_peer=None,  # type: bool
        enabled=None,  # type: bool
        services=None,  # type: List[str]
        uris=None,  # type: List[str]
        management=None,  # type: models.DirectoryServiceManagement
    ):
        """
        Keyword args:
            name (str): A locally unique, system-generated name. The name cannot be modified.
            base_dn (str): Base of the Distinguished Name (DN) of the directory service groups.
            bind_password (str): Masked password used to query the directory.
            bind_user (str): Username used to query the directory.
            ca_certificate (str): The certificate of the Certificate Authority (CA) that signed the certificates of the directory servers, which is used to validate the authenticity of the configured servers.
            check_peer (bool): Whether or not server authenticity is enforced when a certificate is provided.
            enabled (bool): Whether or not the directory service is enabled.
            services (list[str]): Services for which the directory service configuration is used.
            uris (list[str]): List of URIs for the configured directory servers.
            management (DirectoryServiceManagement)
        """
        if name is not None:
            self.name = name
        if base_dn is not None:
            self.base_dn = base_dn
        if bind_password is not None:
            self.bind_password = bind_password
        if bind_user is not None:
            self.bind_user = bind_user
        if ca_certificate is not None:
            self.ca_certificate = ca_certificate
        if check_peer is not None:
            self.check_peer = check_peer
        if enabled is not None:
            self.enabled = enabled
        if services is not None:
            self.services = services
        if uris is not None:
            self.uris = uris
        if management is not None:
            self.management = management

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryService`".format(key))
        if key == "ca_certificate" and value is not None:
            if len(value) > 3000:
                raise ValueError("Invalid value for `ca_certificate`, length must be less than or equal to `3000`")
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
            raise KeyError("Invalid key `{}` for `DirectoryService`".format(key))
        return object.__getattribute__(self, key)

    def __setitem__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryService`".format(key))
        object.__setattr__(self, key, value)

    def __delitem__(self, key):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `DirectoryService`".format(key))
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
        if issubclass(DirectoryService, dict):
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
        if not isinstance(other, DirectoryService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
