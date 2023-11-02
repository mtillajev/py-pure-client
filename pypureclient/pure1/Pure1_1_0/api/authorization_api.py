# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
import uuid
from typing import List, Optional

from .. import models

class AuthorizationApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def oauth210_token_post_with_http_info(
        self,
        grant_type=None,  # type: str
        subject_token=None,  # type: str
        subject_token_type=None,  # type: str
        x_request_id=None,  # type: str
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.OauthTokenResponse
        """Get access token

        Exchanges an ID Token for an OAuth 2.0 access token. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.oauth210_token_post_with_http_info(grant_type, subject_token, subject_token_type, async_req=True)
        >>> result = thread.get()

        :param str grant_type: The method by which the access token will be obtained. The Pure Storage REST API supports the OAuth 2.0 \"token exchange\" grant type, which indicates that a token exchange is being performed. Set `grant_type` to `urn:ietf:params:oauth:grant-type:token-exchange`. (required)
        :param str subject_token: An encoded security ID Token representing the identity of the party on behalf of whom the request is being made. The token must be issued by a trusted identity provider which must be either a registered application in Pure1 or an enabled API client on the array. The token must be a JSON Web Token and must contain the following claims: > | JWT claim | Location | API Client Field | Description | Required By | > |-|-|-|-|-| > | kid | Header | key_id | Key ID of the API client that issues the identity token. | FlashArray and FlashBlade only. | > | aud | Payload | id | Client ID of the API client that issues the identity token. | FlashArray and FlashBlade only. | > | sub | Payload | | Login name of the array user for whom the token should be issued. This must be a valid user in the system. | FlashArray and FlashBlade only. | > | iss | Payload | issuer | Application ID for the Pure1 or API client's trusted identity issuer on the array. | All products. | > | iat | Payload | | Timestamp of when the identity token was issued. Measured in milliseconds since the UNIX epoch. | All products. | > | exp | Payload | | Timestamp of when the identity token will expire. Measured in milliseconds since the UNIX epoch. | All products. |  Each token must also be signed with the private key that is paired with the API client's public key. (required)
        :param str subject_token_type: An identifier that indicates the type of security token specifed in the `subject_token` parameter. The Pure Storage REST API supports the JSON Web Token (JWT) as the means for requesting the access token. Set `subject_token_type` to `urn:ietf:params:oauth:token-type:jwt`. (required)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: OauthTokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())
        # verify the required parameter 'grant_type' is set
        if grant_type is None:
            raise TypeError("Missing the required parameter `grant_type` when calling `oauth210_token_post`")
        # verify the required parameter 'subject_token' is set
        if subject_token is None:
            raise TypeError("Missing the required parameter `subject_token` when calling `oauth210_token_post`")
        # verify the required parameter 'subject_token_type' is set
        if subject_token_type is None:
            raise TypeError("Missing the required parameter `subject_token_type` when calling `oauth210_token_post`")

        collection_formats = {}
        path_params = {}

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}
        if 'grant_type' in params:
            form_params.append(('grant_type', params['grant_type']))
        if 'subject_token' in params:
            form_params.append(('subject_token', params['subject_token']))
        if 'subject_token_type' in params:
            form_params.append(('subject_token_type', params['subject_token_type']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/oauth2/1.0/token', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OauthTokenResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )
