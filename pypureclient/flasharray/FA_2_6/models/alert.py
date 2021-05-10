# coding: utf-8

"""
    FlashArray REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re

import six
import typing

from ....properties import Property
if typing.TYPE_CHECKING:
    from pypureclient.flasharray.FA_2_6 import models

class Alert(object):
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
        'actual': 'str',
        'category': 'str',
        'closed': 'int',
        'code': 'int',
        'component_name': 'str',
        'component_type': 'str',
        'created': 'int',
        'description': 'str',
        'expected': 'str',
        'flagged': 'bool',
        'issue': 'str',
        'knowledge_base_url': 'str',
        'notified': 'int',
        'severity': 'str',
        'state': 'str',
        'summary': 'str',
        'updated': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'actual': 'actual',
        'category': 'category',
        'closed': 'closed',
        'code': 'code',
        'component_name': 'component_name',
        'component_type': 'component_type',
        'created': 'created',
        'description': 'description',
        'expected': 'expected',
        'flagged': 'flagged',
        'issue': 'issue',
        'knowledge_base_url': 'knowledge_base_url',
        'notified': 'notified',
        'severity': 'severity',
        'state': 'state',
        'summary': 'summary',
        'updated': 'updated'
    }

    required_args = {
    }

    def __init__(
        self,
        id=None,  # type: str
        name=None,  # type: str
        actual=None,  # type: str
        category=None,  # type: str
        closed=None,  # type: int
        code=None,  # type: int
        component_name=None,  # type: str
        component_type=None,  # type: str
        created=None,  # type: int
        description=None,  # type: str
        expected=None,  # type: str
        flagged=None,  # type: bool
        issue=None,  # type: str
        knowledge_base_url=None,  # type: str
        notified=None,  # type: int
        severity=None,  # type: str
        state=None,  # type: str
        summary=None,  # type: str
        updated=None,  # type: int
    ):
        """
        Keyword args:
            id (str): A globally unique, system-generated ID. The ID cannot be modified and cannot refer to another resource.
            name (str): A locally unique, system-generated name. The name cannot be modified.
            actual (str): Actual condition at the time the alert is created.
            category (str): The category of the alert. Valid values include `array`, `hardware` and `software`.
            closed (int): The time the alert was closed in milliseconds since the UNIX epoch.
            code (int): The code number of the alert.
            component_name (str): The name of the component that generated the alert.
            component_type (str): The type of component that generated the alert.
            created (int): The time the alert was created in milliseconds since the UNIX epoch.
            description (str): A short description of the alert.
            expected (str): Expected state or threshold under normal conditions.
            flagged (bool): If set to `true`, the message is flagged. Important messages can can be flagged and listed separately.
            issue (str): Information about the alert cause.
            knowledge_base_url (str): The URL of the relevant knowledge base page.
            notified (int): The time the most recent alert notification was sent in milliseconds since the UNIX epoch.
            severity (str): The severity level of the alert. Valid values include `info`, `warning`, `critical`, and `hidden`.
            state (str): The current state of the alert. Valid values include `open`, `closing`, and `closed`.
            summary (str): A summary of the alert.
            updated (int): The time the alert was last updated in milliseconds since the UNIX epoch.
        """
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if actual is not None:
            self.actual = actual
        if category is not None:
            self.category = category
        if closed is not None:
            self.closed = closed
        if code is not None:
            self.code = code
        if component_name is not None:
            self.component_name = component_name
        if component_type is not None:
            self.component_type = component_type
        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        if expected is not None:
            self.expected = expected
        if flagged is not None:
            self.flagged = flagged
        if issue is not None:
            self.issue = issue
        if knowledge_base_url is not None:
            self.knowledge_base_url = knowledge_base_url
        if notified is not None:
            self.notified = notified
        if severity is not None:
            self.severity = severity
        if state is not None:
            self.state = state
        if summary is not None:
            self.summary = summary
        if updated is not None:
            self.updated = updated

    def __setattr__(self, key, value):
        if key not in self.attribute_map:
            raise KeyError("Invalid key `{}` for `Alert`".format(key))
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
        if issubclass(Alert, dict):
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
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
