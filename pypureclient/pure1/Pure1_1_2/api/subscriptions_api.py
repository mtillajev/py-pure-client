# coding: utf-8

"""
    Pure1 Public REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re

# python 2 and python 3 compatibility library
import six
import uuid
from typing import List, Optional

from .. import models

class SubscriptionsApi(object):

    def __init__(self, api_client):
        self.api_client = api_client

    def api12_subscription_assets_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        filter=None,  # type: str
        ids=None,  # type: List[str]
        limit=None,  # type: int
        names=None,  # type: List[str]
        offset=None,  # type: int
        sort=None,  # type: List[str]
        advanced_space=None,  # type: bool
        subscription_ids=None,  # type: List[str]
        subscription_names=None,  # type: List[str]
        license_ids=None,  # type: List[str]
        license_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.SubscriptionAssetGetResponse
        """Get subscription assets

        Retrieves information about Pure1 subscription assets.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api12_subscription_assets_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param list[str] ids: A comma-separated list of resource IDs. If there is not at least one resource that matches each `id` element, an error is returned. Single quotes are required around all strings.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each `name` element, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :param bool advanced_space: If `true`, returns the `advanced_space` field containing physical and effective space information.
        :param list[str] subscription_ids: A comma-separated list of subscription IDs. If there is not at least one resource that matches each `subscription.id` element, an error is returned. Single quotes are required around all strings.
        :param list[str] subscription_names: A comma-separated list of subscription names. If there is not at least one resource that matches each `subscription.name` element, an error is returned. Single quotes are required around all strings.
        :param list[str] license_ids: A comma-separated list of subscriptionLicense IDs. If there is not at least one resource that matches each `license.id` element, an error is returned. Single quotes are required around all strings.
        :param list[str] license_names: A comma-separated list of subscriptionLicense names. If there is not at least one resource that matches each `license.name` element, an error is returned. Single quotes are required around all strings.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: SubscriptionAssetGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        continuation_token = models.quoteString(continuation_token)
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        ids = models.quoteStrings(ids)
        if names is not None:
            if not isinstance(names, list):
                names = [names]
        names = models.quoteStrings(names)
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
        if subscription_ids is not None:
            if not isinstance(subscription_ids, list):
                subscription_ids = [subscription_ids]
        subscription_ids = models.quoteStrings(subscription_ids)
        if subscription_names is not None:
            if not isinstance(subscription_names, list):
                subscription_names = [subscription_names]
        subscription_names = models.quoteStrings(subscription_names)
        if license_ids is not None:
            if not isinstance(license_ids, list):
                license_ids = [license_ids]
        license_ids = models.quoteStrings(license_ids)
        if license_names is not None:
            if not isinstance(license_names, list):
                license_names = [license_names]
        license_names = models.quoteStrings(license_names)
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api12_subscription_assets_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'advanced_space' in params:
            query_params.append(('advanced_space', params['advanced_space']))
        if 'subscription_ids' in params:
            query_params.append(('subscription_ids', params['subscription_ids']))
            collection_formats['subscription_ids'] = 'csv'
        if 'subscription_names' in params:
            query_params.append(('subscription_names', params['subscription_names']))
            collection_formats['subscription_names'] = 'csv'
        if 'license_ids' in params:
            query_params.append(('license_ids', params['license_ids']))
            collection_formats['license_ids'] = 'csv'
        if 'license_names' in params:
            query_params.append(('license_names', params['license_names']))
            collection_formats['license_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/1.2/subscription-assets', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubscriptionAssetGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api12_subscription_licenses_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        filter=None,  # type: str
        ids=None,  # type: List[str]
        limit=None,  # type: int
        marketplace_partner_reference_ids=None,  # type: List[str]
        names=None,  # type: List[str]
        offset=None,  # type: int
        sort=None,  # type: List[str]
        subscription_ids=None,  # type: List[str]
        subscription_names=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.SubscriptionLicenseGetResponse
        """Get subscription licenses

        Retrieves information about Pure1 subscription licenses.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api12_subscription_licenses_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param list[str] ids: A comma-separated list of resource IDs. If there is not at least one resource that matches each `id` element, an error is returned. Single quotes are required around all strings.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] marketplace_partner_reference_ids: A comma-separated list of marketplace partner reference IDs. If there is not at least one resource that matches each `marketplace_partner.reference_id` element, an error is returned. Single quotes are required around all strings.
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each `name` element, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :param list[str] subscription_ids: A comma-separated list of subscription IDs. If there is not at least one resource that matches each `subscription.id` element, an error is returned. Single quotes are required around all strings.
        :param list[str] subscription_names: A comma-separated list of subscription names. If there is not at least one resource that matches each `subscription.name` element, an error is returned. Single quotes are required around all strings.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: SubscriptionLicenseGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        continuation_token = models.quoteString(continuation_token)
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        ids = models.quoteStrings(ids)
        if marketplace_partner_reference_ids is not None:
            if not isinstance(marketplace_partner_reference_ids, list):
                marketplace_partner_reference_ids = [marketplace_partner_reference_ids]
        marketplace_partner_reference_ids = models.quoteStrings(marketplace_partner_reference_ids)
        if names is not None:
            if not isinstance(names, list):
                names = [names]
        names = models.quoteStrings(names)
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
        if subscription_ids is not None:
            if not isinstance(subscription_ids, list):
                subscription_ids = [subscription_ids]
        subscription_ids = models.quoteStrings(subscription_ids)
        if subscription_names is not None:
            if not isinstance(subscription_names, list):
                subscription_names = [subscription_names]
        subscription_names = models.quoteStrings(subscription_names)
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api12_subscription_licenses_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'marketplace_partner_reference_ids' in params:
            query_params.append(('marketplace_partner_reference_ids', params['marketplace_partner_reference_ids']))
            collection_formats['marketplace_partner_reference_ids'] = 'csv'
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'
        if 'subscription_ids' in params:
            query_params.append(('subscription_ids', params['subscription_ids']))
            collection_formats['subscription_ids'] = 'csv'
        if 'subscription_names' in params:
            query_params.append(('subscription_names', params['subscription_names']))
            collection_formats['subscription_names'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/1.2/subscription-licenses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubscriptionLicenseGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )

    def api12_subscriptions_get_with_http_info(
        self,
        authorization=None,  # type: str
        x_request_id=None,  # type: str
        continuation_token=None,  # type: str
        filter=None,  # type: str
        ids=None,  # type: List[str]
        limit=None,  # type: int
        names=None,  # type: List[str]
        offset=None,  # type: int
        sort=None,  # type: List[str]
        async_req=False,  # type: bool
        _return_http_data_only=False,  # type: bool
        _preload_content=True,  # type: bool
        _request_timeout=None,  # type: Optional[int]
    ):
        # type: (...) -> models.SubscriptionGetResponse
        """Get subscriptions

        Retrieves information about Pure1 subscriptions.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api12_subscriptions_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param str authorization: Access token (in JWT format) required to use any API endpoint (except `/oauth2`)
        :param str x_request_id: Supplied by client during request or generated by server.
        :param str continuation_token: An opaque token used to iterate over a collection. The token to use on the next request is returned in the `continuation_token` field of the result. Single quotes are required around all strings.
        :param str filter: Exclude resources that don't match the specified criteria. Single quotes are required around all strings inside the filters.
        :param list[str] ids: A comma-separated list of resource IDs. If there is not at least one resource that matches each `id` element, an error is returned. Single quotes are required around all strings.
        :param int limit: Limit the size of the response to the specified number of resources. A limit of 0 can be used to get the number of resources without getting all of the resources. It will be returned in the total_item_count field. If a client asks for a page size larger than the maximum number, the request is still valid. In that case the server just returns the maximum number of items, disregarding the client's page size request. If not specified, defaults to 1000.
        :param list[str] names: A comma-separated list of resource names. If there is not at least one resource that matches each `name` element, an error is returned. Single quotes are required around all strings.
        :param int offset: The offset of the first resource to return from a collection.
        :param list[str] sort: Sort the response by the specified fields (in descending order if '-' is appended to the field name). If you provide a sort you will not get a continuation token in the response.
        :param bool async_req: Request runs in separate thread and method returns multiprocessing.pool.ApplyResult.
        :param bool _return_http_data_only: Returns only data field.
        :param bool _preload_content: Response is converted into objects.
        :param int _request_timeout: Total request timeout in seconds.
                 It can also be a tuple of (connection time, read time) timeouts.
        :return: SubscriptionGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        continuation_token = models.quoteString(continuation_token)
        if ids is not None:
            if not isinstance(ids, list):
                ids = [ids]
        ids = models.quoteStrings(ids)
        if names is not None:
            if not isinstance(names, list):
                names = [names]
        names = models.quoteStrings(names)
        if sort is not None:
            if not isinstance(sort, list):
                sort = [sort]
        params = {k: v for k, v in six.iteritems(locals()) if v is not None}

        # Convert the filter into a string
        if params.get('filter'):
            params['filter'] = str(params['filter'])
        if params.get('sort'):
            params['sort'] = [str(_x) for _x in params['sort']]
        # Assign a value to X-Request-Id if it is not specified
        if params.get('x_request_id') is None:
            params['x_request_id'] = str(uuid.uuid4())

        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `api12_subscriptions_get`, must be a value greater than or equal to `0`")
        collection_formats = {}
        path_params = {}

        query_params = []
        if 'continuation_token' in params:
            query_params.append(('continuation_token', params['continuation_token']))
        if 'filter' in params:
            query_params.append(('filter', params['filter']))
        if 'ids' in params:
            query_params.append(('ids', params['ids']))
            collection_formats['ids'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'names' in params:
            query_params.append(('names', params['names']))
            collection_formats['names'] = 'csv'
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['AuthorizationHeader']

        return self.api_client.call_api(
            '/api/1.2/subscriptions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubscriptionGetResponse',
            auth_settings=auth_settings,
            async_req=async_req,
            _return_http_data_only=_return_http_data_only,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            collection_formats=collection_formats,
        )