# coding: utf-8

"""
    Accounting API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 2.1.6
    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class Contacts(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"contacts": "list[Contact]"}

    attribute_map = {"contacts": "Contacts"}

    def __init__(self, contacts=None):  # noqa: E501
        """Contacts - a model defined in OpenAPI"""  # noqa: E501

        self._contacts = None
        self.discriminator = None

        if contacts is not None:
            self.contacts = contacts

    @property
    def contacts(self):
        """Gets the contacts of this Contacts.  # noqa: E501


        :return: The contacts of this Contacts.  # noqa: E501
        :rtype: list[Contact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this Contacts.


        :param contacts: The contacts of this Contacts.  # noqa: E501
        :type: list[Contact]
        """

        self._contacts = contacts
