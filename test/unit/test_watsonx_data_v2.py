# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Unit Tests for WatsonxDataV2
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import io
import json
import os
import pytest
import re
import requests
import responses
import tempfile
import urllib
from ibm_watsonxdata.watsonx_data_v2 import *


_service = WatsonxDataV2(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://ibmcloud/lakehouse/api/v2'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: Buckets
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = WatsonxDataV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, WatsonxDataV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = WatsonxDataV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListBucketRegistrations:
    """
    Test Class for list_bucket_registrations
    """

    @responses.activate
    def test_list_bucket_registrations_all_params(self):
        """
        list_bucket_registrations()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations')
        mock_response = '{"bucket_registrations": [{"access_key": "<access_key>", "actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "bucket_display_name": "sample-bucket-displayname", "bucket_id": "samplebucket123", "bucket_name": "sample-bucket", "bucket_type": "ibm_cos", "created_by": "<username>@<domain>.com", "created_on": "1686120645", "description": "COS bucket for customer data", "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud/", "managed_by": "ibm", "region": "us-south", "secret_key": "secret_key", "state": "active", "tags": ["tags"]}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_bucket_registrations(
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_bucket_registrations_all_params_with_retries(self):
        # Enable retries and run test_list_bucket_registrations_all_params.
        _service.enable_retries()
        self.test_list_bucket_registrations_all_params()

        # Disable retries and run test_list_bucket_registrations_all_params.
        _service.disable_retries()
        self.test_list_bucket_registrations_all_params()

    @responses.activate
    def test_list_bucket_registrations_required_params(self):
        """
        test_list_bucket_registrations_required_params()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations')
        mock_response = '{"bucket_registrations": [{"access_key": "<access_key>", "actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "bucket_display_name": "sample-bucket-displayname", "bucket_id": "samplebucket123", "bucket_name": "sample-bucket", "bucket_type": "ibm_cos", "created_by": "<username>@<domain>.com", "created_on": "1686120645", "description": "COS bucket for customer data", "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud/", "managed_by": "ibm", "region": "us-south", "secret_key": "secret_key", "state": "active", "tags": ["tags"]}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_bucket_registrations()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_bucket_registrations_required_params_with_retries(self):
        # Enable retries and run test_list_bucket_registrations_required_params.
        _service.enable_retries()
        self.test_list_bucket_registrations_required_params()

        # Disable retries and run test_list_bucket_registrations_required_params.
        _service.disable_retries()
        self.test_list_bucket_registrations_required_params()


class TestCreateBucketRegistration:
    """
    Test Class for create_bucket_registration
    """

    @responses.activate
    def test_create_bucket_registration_all_params(self):
        """
        create_bucket_registration()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations')
        mock_response = '{"bucket_registration": {"access_key": "<access_key>", "actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "bucket_display_name": "sample-bucket-displayname", "bucket_id": "samplebucket123", "bucket_name": "sample-bucket", "bucket_type": "ibm_cos", "created_by": "<username>@<domain>.com", "created_on": "1686120645", "description": "COS bucket for customer data", "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud/", "managed_by": "ibm", "region": "us-south", "secret_key": "secret_key", "state": "active", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a BucketDetails model
        bucket_details_model = {}
        bucket_details_model['access_key'] = '<access_key>'
        bucket_details_model['bucket_name'] = 'sample-bucket'
        bucket_details_model['endpoint'] = 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        bucket_details_model['secret_key'] = 'secret_key'

        # Set up parameter values
        bucket_details = bucket_details_model
        bucket_type = 'ibm_cos'
        catalog_name = 'sampleCatalog'
        description = 'COS bucket for customer data'
        managed_by = 'ibm'
        table_type = 'iceberg'
        bucket_display_name = 'sample-bucket-displayname'
        bucket_tags = ['read customer data', 'write customer data\'']
        catalog_tags = ['catalog_tag_1', 'catalog_tag_2']
        region = 'us-south'
        state = 'active'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_bucket_registration(
            bucket_details,
            bucket_type,
            catalog_name,
            description,
            managed_by,
            table_type,
            bucket_display_name=bucket_display_name,
            bucket_tags=bucket_tags,
            catalog_tags=catalog_tags,
            region=region,
            state=state,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['bucket_details'] == bucket_details_model
        assert req_body['bucket_type'] == 'ibm_cos'
        assert req_body['catalog_name'] == 'sampleCatalog'
        assert req_body['description'] == 'COS bucket for customer data'
        assert req_body['managed_by'] == 'ibm'
        assert req_body['table_type'] == 'iceberg'
        assert req_body['bucket_display_name'] == 'sample-bucket-displayname'
        assert req_body['bucket_tags'] == ['read customer data', 'write customer data\'']
        assert req_body['catalog_tags'] == ['catalog_tag_1', 'catalog_tag_2']
        assert req_body['region'] == 'us-south'
        assert req_body['state'] == 'active'

    def test_create_bucket_registration_all_params_with_retries(self):
        # Enable retries and run test_create_bucket_registration_all_params.
        _service.enable_retries()
        self.test_create_bucket_registration_all_params()

        # Disable retries and run test_create_bucket_registration_all_params.
        _service.disable_retries()
        self.test_create_bucket_registration_all_params()

    @responses.activate
    def test_create_bucket_registration_required_params(self):
        """
        test_create_bucket_registration_required_params()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations')
        mock_response = '{"bucket_registration": {"access_key": "<access_key>", "actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "bucket_display_name": "sample-bucket-displayname", "bucket_id": "samplebucket123", "bucket_name": "sample-bucket", "bucket_type": "ibm_cos", "created_by": "<username>@<domain>.com", "created_on": "1686120645", "description": "COS bucket for customer data", "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud/", "managed_by": "ibm", "region": "us-south", "secret_key": "secret_key", "state": "active", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a BucketDetails model
        bucket_details_model = {}
        bucket_details_model['access_key'] = '<access_key>'
        bucket_details_model['bucket_name'] = 'sample-bucket'
        bucket_details_model['endpoint'] = 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        bucket_details_model['secret_key'] = 'secret_key'

        # Set up parameter values
        bucket_details = bucket_details_model
        bucket_type = 'ibm_cos'
        catalog_name = 'sampleCatalog'
        description = 'COS bucket for customer data'
        managed_by = 'ibm'
        table_type = 'iceberg'
        bucket_display_name = 'sample-bucket-displayname'
        bucket_tags = ['read customer data', 'write customer data\'']
        catalog_tags = ['catalog_tag_1', 'catalog_tag_2']
        region = 'us-south'
        state = 'active'

        # Invoke method
        response = _service.create_bucket_registration(
            bucket_details,
            bucket_type,
            catalog_name,
            description,
            managed_by,
            table_type,
            bucket_display_name=bucket_display_name,
            bucket_tags=bucket_tags,
            catalog_tags=catalog_tags,
            region=region,
            state=state,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['bucket_details'] == bucket_details_model
        assert req_body['bucket_type'] == 'ibm_cos'
        assert req_body['catalog_name'] == 'sampleCatalog'
        assert req_body['description'] == 'COS bucket for customer data'
        assert req_body['managed_by'] == 'ibm'
        assert req_body['table_type'] == 'iceberg'
        assert req_body['bucket_display_name'] == 'sample-bucket-displayname'
        assert req_body['bucket_tags'] == ['read customer data', 'write customer data\'']
        assert req_body['catalog_tags'] == ['catalog_tag_1', 'catalog_tag_2']
        assert req_body['region'] == 'us-south'
        assert req_body['state'] == 'active'

    def test_create_bucket_registration_required_params_with_retries(self):
        # Enable retries and run test_create_bucket_registration_required_params.
        _service.enable_retries()
        self.test_create_bucket_registration_required_params()

        # Disable retries and run test_create_bucket_registration_required_params.
        _service.disable_retries()
        self.test_create_bucket_registration_required_params()

    @responses.activate
    def test_create_bucket_registration_value_error(self):
        """
        test_create_bucket_registration_value_error()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations')
        mock_response = '{"bucket_registration": {"access_key": "<access_key>", "actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "bucket_display_name": "sample-bucket-displayname", "bucket_id": "samplebucket123", "bucket_name": "sample-bucket", "bucket_type": "ibm_cos", "created_by": "<username>@<domain>.com", "created_on": "1686120645", "description": "COS bucket for customer data", "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud/", "managed_by": "ibm", "region": "us-south", "secret_key": "secret_key", "state": "active", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a BucketDetails model
        bucket_details_model = {}
        bucket_details_model['access_key'] = '<access_key>'
        bucket_details_model['bucket_name'] = 'sample-bucket'
        bucket_details_model['endpoint'] = 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        bucket_details_model['secret_key'] = 'secret_key'

        # Set up parameter values
        bucket_details = bucket_details_model
        bucket_type = 'ibm_cos'
        catalog_name = 'sampleCatalog'
        description = 'COS bucket for customer data'
        managed_by = 'ibm'
        table_type = 'iceberg'
        bucket_display_name = 'sample-bucket-displayname'
        bucket_tags = ['read customer data', 'write customer data\'']
        catalog_tags = ['catalog_tag_1', 'catalog_tag_2']
        region = 'us-south'
        state = 'active'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "bucket_details": bucket_details,
            "bucket_type": bucket_type,
            "catalog_name": catalog_name,
            "description": description,
            "managed_by": managed_by,
            "table_type": table_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_bucket_registration(**req_copy)

    def test_create_bucket_registration_value_error_with_retries(self):
        # Enable retries and run test_create_bucket_registration_value_error.
        _service.enable_retries()
        self.test_create_bucket_registration_value_error()

        # Disable retries and run test_create_bucket_registration_value_error.
        _service.disable_retries()
        self.test_create_bucket_registration_value_error()


class TestGetBucketRegistration:
    """
    Test Class for get_bucket_registration
    """

    @responses.activate
    def test_get_bucket_registration_all_params(self):
        """
        get_bucket_registration()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString')
        mock_response = '{"bucket_registration": {"access_key": "<access_key>", "actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "bucket_display_name": "sample-bucket-displayname", "bucket_id": "samplebucket123", "bucket_name": "sample-bucket", "bucket_type": "ibm_cos", "created_by": "<username>@<domain>.com", "created_on": "1686120645", "description": "COS bucket for customer data", "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud/", "managed_by": "ibm", "region": "us-south", "secret_key": "secret_key", "state": "active", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        bucket_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.get_bucket_registration(
            bucket_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_bucket_registration_all_params_with_retries(self):
        # Enable retries and run test_get_bucket_registration_all_params.
        _service.enable_retries()
        self.test_get_bucket_registration_all_params()

        # Disable retries and run test_get_bucket_registration_all_params.
        _service.disable_retries()
        self.test_get_bucket_registration_all_params()

    @responses.activate
    def test_get_bucket_registration_required_params(self):
        """
        test_get_bucket_registration_required_params()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString')
        mock_response = '{"bucket_registration": {"access_key": "<access_key>", "actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "bucket_display_name": "sample-bucket-displayname", "bucket_id": "samplebucket123", "bucket_name": "sample-bucket", "bucket_type": "ibm_cos", "created_by": "<username>@<domain>.com", "created_on": "1686120645", "description": "COS bucket for customer data", "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud/", "managed_by": "ibm", "region": "us-south", "secret_key": "secret_key", "state": "active", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        bucket_id = 'testString'

        # Invoke method
        response = _service.get_bucket_registration(
            bucket_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_bucket_registration_required_params_with_retries(self):
        # Enable retries and run test_get_bucket_registration_required_params.
        _service.enable_retries()
        self.test_get_bucket_registration_required_params()

        # Disable retries and run test_get_bucket_registration_required_params.
        _service.disable_retries()
        self.test_get_bucket_registration_required_params()

    @responses.activate
    def test_get_bucket_registration_value_error(self):
        """
        test_get_bucket_registration_value_error()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString')
        mock_response = '{"bucket_registration": {"access_key": "<access_key>", "actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "bucket_display_name": "sample-bucket-displayname", "bucket_id": "samplebucket123", "bucket_name": "sample-bucket", "bucket_type": "ibm_cos", "created_by": "<username>@<domain>.com", "created_on": "1686120645", "description": "COS bucket for customer data", "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud/", "managed_by": "ibm", "region": "us-south", "secret_key": "secret_key", "state": "active", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        bucket_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "bucket_id": bucket_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_bucket_registration(**req_copy)

    def test_get_bucket_registration_value_error_with_retries(self):
        # Enable retries and run test_get_bucket_registration_value_error.
        _service.enable_retries()
        self.test_get_bucket_registration_value_error()

        # Disable retries and run test_get_bucket_registration_value_error.
        _service.disable_retries()
        self.test_get_bucket_registration_value_error()


class TestDeleteBucketRegistration:
    """
    Test Class for delete_bucket_registration
    """

    @responses.activate
    def test_delete_bucket_registration_all_params(self):
        """
        delete_bucket_registration()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        bucket_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_bucket_registration(
            bucket_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_bucket_registration_all_params_with_retries(self):
        # Enable retries and run test_delete_bucket_registration_all_params.
        _service.enable_retries()
        self.test_delete_bucket_registration_all_params()

        # Disable retries and run test_delete_bucket_registration_all_params.
        _service.disable_retries()
        self.test_delete_bucket_registration_all_params()

    @responses.activate
    def test_delete_bucket_registration_required_params(self):
        """
        test_delete_bucket_registration_required_params()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        bucket_id = 'testString'

        # Invoke method
        response = _service.delete_bucket_registration(
            bucket_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_bucket_registration_required_params_with_retries(self):
        # Enable retries and run test_delete_bucket_registration_required_params.
        _service.enable_retries()
        self.test_delete_bucket_registration_required_params()

        # Disable retries and run test_delete_bucket_registration_required_params.
        _service.disable_retries()
        self.test_delete_bucket_registration_required_params()

    @responses.activate
    def test_delete_bucket_registration_value_error(self):
        """
        test_delete_bucket_registration_value_error()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        bucket_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "bucket_id": bucket_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_bucket_registration(**req_copy)

    def test_delete_bucket_registration_value_error_with_retries(self):
        # Enable retries and run test_delete_bucket_registration_value_error.
        _service.enable_retries()
        self.test_delete_bucket_registration_value_error()

        # Disable retries and run test_delete_bucket_registration_value_error.
        _service.disable_retries()
        self.test_delete_bucket_registration_value_error()


class TestUpdateBucketRegistration:
    """
    Test Class for update_bucket_registration
    """

    @responses.activate
    def test_update_bucket_registration_all_params(self):
        """
        update_bucket_registration()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString')
        mock_response = '{"bucket_registration": {"access_key": "<access_key>", "actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "bucket_display_name": "sample-bucket-displayname", "bucket_id": "samplebucket123", "bucket_name": "sample-bucket", "bucket_type": "ibm_cos", "created_by": "<username>@<domain>.com", "created_on": "1686120645", "description": "COS bucket for customer data", "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud/", "managed_by": "ibm", "region": "us-south", "secret_key": "secret_key", "state": "active", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        bucket_id = 'testString'
        body = [json_patch_operation_model]
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.update_bucket_registration(
            bucket_id,
            body,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_bucket_registration_all_params_with_retries(self):
        # Enable retries and run test_update_bucket_registration_all_params.
        _service.enable_retries()
        self.test_update_bucket_registration_all_params()

        # Disable retries and run test_update_bucket_registration_all_params.
        _service.disable_retries()
        self.test_update_bucket_registration_all_params()

    @responses.activate
    def test_update_bucket_registration_required_params(self):
        """
        test_update_bucket_registration_required_params()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString')
        mock_response = '{"bucket_registration": {"access_key": "<access_key>", "actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "bucket_display_name": "sample-bucket-displayname", "bucket_id": "samplebucket123", "bucket_name": "sample-bucket", "bucket_type": "ibm_cos", "created_by": "<username>@<domain>.com", "created_on": "1686120645", "description": "COS bucket for customer data", "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud/", "managed_by": "ibm", "region": "us-south", "secret_key": "secret_key", "state": "active", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        bucket_id = 'testString'
        body = [json_patch_operation_model]

        # Invoke method
        response = _service.update_bucket_registration(
            bucket_id,
            body,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_bucket_registration_required_params_with_retries(self):
        # Enable retries and run test_update_bucket_registration_required_params.
        _service.enable_retries()
        self.test_update_bucket_registration_required_params()

        # Disable retries and run test_update_bucket_registration_required_params.
        _service.disable_retries()
        self.test_update_bucket_registration_required_params()

    @responses.activate
    def test_update_bucket_registration_value_error(self):
        """
        test_update_bucket_registration_value_error()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString')
        mock_response = '{"bucket_registration": {"access_key": "<access_key>", "actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "bucket_display_name": "sample-bucket-displayname", "bucket_id": "samplebucket123", "bucket_name": "sample-bucket", "bucket_type": "ibm_cos", "created_by": "<username>@<domain>.com", "created_on": "1686120645", "description": "COS bucket for customer data", "endpoint": "https://s3.<region>.cloud-object-storage.appdomain.cloud/", "managed_by": "ibm", "region": "us-south", "secret_key": "secret_key", "state": "active", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        bucket_id = 'testString'
        body = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "bucket_id": bucket_id,
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_bucket_registration(**req_copy)

    def test_update_bucket_registration_value_error_with_retries(self):
        # Enable retries and run test_update_bucket_registration_value_error.
        _service.enable_retries()
        self.test_update_bucket_registration_value_error()

        # Disable retries and run test_update_bucket_registration_value_error.
        _service.disable_retries()
        self.test_update_bucket_registration_value_error()


class TestCreateActivateBucket:
    """
    Test Class for create_activate_bucket
    """

    @responses.activate
    def test_create_activate_bucket_all_params(self):
        """
        create_activate_bucket()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString/activate')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        bucket_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_activate_bucket(
            bucket_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_activate_bucket_all_params_with_retries(self):
        # Enable retries and run test_create_activate_bucket_all_params.
        _service.enable_retries()
        self.test_create_activate_bucket_all_params()

        # Disable retries and run test_create_activate_bucket_all_params.
        _service.disable_retries()
        self.test_create_activate_bucket_all_params()

    @responses.activate
    def test_create_activate_bucket_required_params(self):
        """
        test_create_activate_bucket_required_params()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString/activate')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        bucket_id = 'testString'

        # Invoke method
        response = _service.create_activate_bucket(
            bucket_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_activate_bucket_required_params_with_retries(self):
        # Enable retries and run test_create_activate_bucket_required_params.
        _service.enable_retries()
        self.test_create_activate_bucket_required_params()

        # Disable retries and run test_create_activate_bucket_required_params.
        _service.disable_retries()
        self.test_create_activate_bucket_required_params()

    @responses.activate
    def test_create_activate_bucket_value_error(self):
        """
        test_create_activate_bucket_value_error()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString/activate')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        bucket_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "bucket_id": bucket_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_activate_bucket(**req_copy)

    def test_create_activate_bucket_value_error_with_retries(self):
        # Enable retries and run test_create_activate_bucket_value_error.
        _service.enable_retries()
        self.test_create_activate_bucket_value_error()

        # Disable retries and run test_create_activate_bucket_value_error.
        _service.disable_retries()
        self.test_create_activate_bucket_value_error()


class TestDeleteDeactivateBucket:
    """
    Test Class for delete_deactivate_bucket
    """

    @responses.activate
    def test_delete_deactivate_bucket_all_params(self):
        """
        delete_deactivate_bucket()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString/deactivate')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        bucket_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_deactivate_bucket(
            bucket_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_deactivate_bucket_all_params_with_retries(self):
        # Enable retries and run test_delete_deactivate_bucket_all_params.
        _service.enable_retries()
        self.test_delete_deactivate_bucket_all_params()

        # Disable retries and run test_delete_deactivate_bucket_all_params.
        _service.disable_retries()
        self.test_delete_deactivate_bucket_all_params()

    @responses.activate
    def test_delete_deactivate_bucket_required_params(self):
        """
        test_delete_deactivate_bucket_required_params()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString/deactivate')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        bucket_id = 'testString'

        # Invoke method
        response = _service.delete_deactivate_bucket(
            bucket_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_deactivate_bucket_required_params_with_retries(self):
        # Enable retries and run test_delete_deactivate_bucket_required_params.
        _service.enable_retries()
        self.test_delete_deactivate_bucket_required_params()

        # Disable retries and run test_delete_deactivate_bucket_required_params.
        _service.disable_retries()
        self.test_delete_deactivate_bucket_required_params()

    @responses.activate
    def test_delete_deactivate_bucket_value_error(self):
        """
        test_delete_deactivate_bucket_value_error()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString/deactivate')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        bucket_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "bucket_id": bucket_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_deactivate_bucket(**req_copy)

    def test_delete_deactivate_bucket_value_error_with_retries(self):
        # Enable retries and run test_delete_deactivate_bucket_value_error.
        _service.enable_retries()
        self.test_delete_deactivate_bucket_value_error()

        # Disable retries and run test_delete_deactivate_bucket_value_error.
        _service.disable_retries()
        self.test_delete_deactivate_bucket_value_error()


class TestListBucketObjects:
    """
    Test Class for list_bucket_objects
    """

    @responses.activate
    def test_list_bucket_objects_all_params(self):
        """
        list_bucket_objects()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString/objects')
        mock_response = '{"objects": ["object_1"], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        bucket_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_bucket_objects(
            bucket_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_bucket_objects_all_params_with_retries(self):
        # Enable retries and run test_list_bucket_objects_all_params.
        _service.enable_retries()
        self.test_list_bucket_objects_all_params()

        # Disable retries and run test_list_bucket_objects_all_params.
        _service.disable_retries()
        self.test_list_bucket_objects_all_params()

    @responses.activate
    def test_list_bucket_objects_required_params(self):
        """
        test_list_bucket_objects_required_params()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString/objects')
        mock_response = '{"objects": ["object_1"], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        bucket_id = 'testString'

        # Invoke method
        response = _service.list_bucket_objects(
            bucket_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_bucket_objects_required_params_with_retries(self):
        # Enable retries and run test_list_bucket_objects_required_params.
        _service.enable_retries()
        self.test_list_bucket_objects_required_params()

        # Disable retries and run test_list_bucket_objects_required_params.
        _service.disable_retries()
        self.test_list_bucket_objects_required_params()

    @responses.activate
    def test_list_bucket_objects_value_error(self):
        """
        test_list_bucket_objects_value_error()
        """
        # Set up mock
        url = preprocess_url('/bucket_registrations/testString/objects')
        mock_response = '{"objects": ["object_1"], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        bucket_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "bucket_id": bucket_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_bucket_objects(**req_copy)

    def test_list_bucket_objects_value_error_with_retries(self):
        # Enable retries and run test_list_bucket_objects_value_error.
        _service.enable_retries()
        self.test_list_bucket_objects_value_error()

        # Disable retries and run test_list_bucket_objects_value_error.
        _service.disable_retries()
        self.test_list_bucket_objects_value_error()


class TestTestBucketConnection:
    """
    Test Class for test_bucket_connection
    """

    @responses.activate
    def test_test_bucket_connection_all_params(self):
        """
        test_bucket_connection()
        """
        # Set up mock
        url = preprocess_url('/test_bucket_connection')
        mock_response = '{"bucket_status": {"state": true, "state_message": "bucket does not exist or the credentials provided are not valid."}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_key = '<access_key>'
        bucket_name = 'sample-bucket'
        bucket_type = 'ibm_cos'
        endpoint = 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        region = 'us-south'
        secret_key = 'secret_key'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.test_bucket_connection(
            access_key,
            bucket_name,
            bucket_type,
            endpoint,
            region,
            secret_key,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['access_key'] == '<access_key>'
        assert req_body['bucket_name'] == 'sample-bucket'
        assert req_body['bucket_type'] == 'ibm_cos'
        assert req_body['endpoint'] == 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        assert req_body['region'] == 'us-south'
        assert req_body['secret_key'] == 'secret_key'

    def test_test_bucket_connection_all_params_with_retries(self):
        # Enable retries and run test_test_bucket_connection_all_params.
        _service.enable_retries()
        self.test_test_bucket_connection_all_params()

        # Disable retries and run test_test_bucket_connection_all_params.
        _service.disable_retries()
        self.test_test_bucket_connection_all_params()

    @responses.activate
    def test_test_bucket_connection_required_params(self):
        """
        test_test_bucket_connection_required_params()
        """
        # Set up mock
        url = preprocess_url('/test_bucket_connection')
        mock_response = '{"bucket_status": {"state": true, "state_message": "bucket does not exist or the credentials provided are not valid."}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_key = '<access_key>'
        bucket_name = 'sample-bucket'
        bucket_type = 'ibm_cos'
        endpoint = 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        region = 'us-south'
        secret_key = 'secret_key'

        # Invoke method
        response = _service.test_bucket_connection(
            access_key,
            bucket_name,
            bucket_type,
            endpoint,
            region,
            secret_key,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['access_key'] == '<access_key>'
        assert req_body['bucket_name'] == 'sample-bucket'
        assert req_body['bucket_type'] == 'ibm_cos'
        assert req_body['endpoint'] == 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        assert req_body['region'] == 'us-south'
        assert req_body['secret_key'] == 'secret_key'

    def test_test_bucket_connection_required_params_with_retries(self):
        # Enable retries and run test_test_bucket_connection_required_params.
        _service.enable_retries()
        self.test_test_bucket_connection_required_params()

        # Disable retries and run test_test_bucket_connection_required_params.
        _service.disable_retries()
        self.test_test_bucket_connection_required_params()

    @responses.activate
    def test_test_bucket_connection_value_error(self):
        """
        test_test_bucket_connection_value_error()
        """
        # Set up mock
        url = preprocess_url('/test_bucket_connection')
        mock_response = '{"bucket_status": {"state": true, "state_message": "bucket does not exist or the credentials provided are not valid."}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        access_key = '<access_key>'
        bucket_name = 'sample-bucket'
        bucket_type = 'ibm_cos'
        endpoint = 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        region = 'us-south'
        secret_key = 'secret_key'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "access_key": access_key,
            "bucket_name": bucket_name,
            "bucket_type": bucket_type,
            "endpoint": endpoint,
            "region": region,
            "secret_key": secret_key,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.test_bucket_connection(**req_copy)

    def test_test_bucket_connection_value_error_with_retries(self):
        # Enable retries and run test_test_bucket_connection_value_error.
        _service.enable_retries()
        self.test_test_bucket_connection_value_error()

        # Disable retries and run test_test_bucket_connection_value_error.
        _service.disable_retries()
        self.test_test_bucket_connection_value_error()


# endregion
##############################################################################
# End of Service: Buckets
##############################################################################

##############################################################################
# Start of Service: Databases
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = WatsonxDataV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, WatsonxDataV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = WatsonxDataV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestCreateDriverDatabaseCatalog:
    """
    Test Class for create_driver_database_catalog
    """

    @responses.activate
    def test_create_driver_database_catalog_all_params(self):
        """
        create_driver_database_catalog()
        """
        # Set up mock
        url = preprocess_url('/database_driver_registrations')
        mock_response = '{"database": {"database_display_name": "database_display_name", "database_id": "database_id"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        database_display_name = 'testString'
        database_type = 'testString'
        catalog_name = 'testString'
        hostname = 'testString'
        port = 'testString'
        driver = io.BytesIO(b'This is a mock file.').getvalue()
        driver_content_type = 'testString'
        driver_file_name = 'testString'
        certificate = 'testString'
        certificate_extension = 'testString'
        ssl = 'testString'
        username = 'testString'
        password = 'testString'
        database_name = 'testString'
        description = 'testString'
        created_on = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_driver_database_catalog(
            database_display_name,
            database_type,
            catalog_name,
            hostname,
            port,
            driver=driver,
            driver_content_type=driver_content_type,
            driver_file_name=driver_file_name,
            certificate=certificate,
            certificate_extension=certificate_extension,
            ssl=ssl,
            username=username,
            password=password,
            database_name=database_name,
            description=description,
            created_on=created_on,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_driver_database_catalog_all_params_with_retries(self):
        # Enable retries and run test_create_driver_database_catalog_all_params.
        _service.enable_retries()
        self.test_create_driver_database_catalog_all_params()

        # Disable retries and run test_create_driver_database_catalog_all_params.
        _service.disable_retries()
        self.test_create_driver_database_catalog_all_params()

    @responses.activate
    def test_create_driver_database_catalog_required_params(self):
        """
        test_create_driver_database_catalog_required_params()
        """
        # Set up mock
        url = preprocess_url('/database_driver_registrations')
        mock_response = '{"database": {"database_display_name": "database_display_name", "database_id": "database_id"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        database_display_name = 'testString'
        database_type = 'testString'
        catalog_name = 'testString'
        hostname = 'testString'
        port = 'testString'

        # Invoke method
        response = _service.create_driver_database_catalog(
            database_display_name,
            database_type,
            catalog_name,
            hostname,
            port,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_driver_database_catalog_required_params_with_retries(self):
        # Enable retries and run test_create_driver_database_catalog_required_params.
        _service.enable_retries()
        self.test_create_driver_database_catalog_required_params()

        # Disable retries and run test_create_driver_database_catalog_required_params.
        _service.disable_retries()
        self.test_create_driver_database_catalog_required_params()

    @responses.activate
    def test_create_driver_database_catalog_value_error(self):
        """
        test_create_driver_database_catalog_value_error()
        """
        # Set up mock
        url = preprocess_url('/database_driver_registrations')
        mock_response = '{"database": {"database_display_name": "database_display_name", "database_id": "database_id"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        database_display_name = 'testString'
        database_type = 'testString'
        catalog_name = 'testString'
        hostname = 'testString'
        port = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "database_display_name": database_display_name,
            "database_type": database_type,
            "catalog_name": catalog_name,
            "hostname": hostname,
            "port": port,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_driver_database_catalog(**req_copy)

    def test_create_driver_database_catalog_value_error_with_retries(self):
        # Enable retries and run test_create_driver_database_catalog_value_error.
        _service.enable_retries()
        self.test_create_driver_database_catalog_value_error()

        # Disable retries and run test_create_driver_database_catalog_value_error.
        _service.disable_retries()
        self.test_create_driver_database_catalog_value_error()


class TestListDatabaseRegistrations:
    """
    Test Class for list_database_registrations
    """

    @responses.activate
    def test_list_database_registrations_all_params(self):
        """
        list_database_registrations()
        """
        # Set up mock
        url = preprocess_url('/database_registrations')
        mock_response = '{"database_registrations": [{"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "created_by": "user1@bim.com", "created_on": "1686792721", "database_details": {"database_name": "new_database", "hostname": "netezza://ps.fyre.com", "password": "samplepassword", "port": 4543, "sasl": true, "ssl": true, "tables": "kafka_table_name", "username": "sampleuser"}, "database_display_name": "new_database", "database_id": "new_database_id", "database_properties": ["database_properties"], "database_type": "netezza", "description": "Description of the external Database", "tags": ["tags"]}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_database_registrations(
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_database_registrations_all_params_with_retries(self):
        # Enable retries and run test_list_database_registrations_all_params.
        _service.enable_retries()
        self.test_list_database_registrations_all_params()

        # Disable retries and run test_list_database_registrations_all_params.
        _service.disable_retries()
        self.test_list_database_registrations_all_params()

    @responses.activate
    def test_list_database_registrations_required_params(self):
        """
        test_list_database_registrations_required_params()
        """
        # Set up mock
        url = preprocess_url('/database_registrations')
        mock_response = '{"database_registrations": [{"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "created_by": "user1@bim.com", "created_on": "1686792721", "database_details": {"database_name": "new_database", "hostname": "netezza://ps.fyre.com", "password": "samplepassword", "port": 4543, "sasl": true, "ssl": true, "tables": "kafka_table_name", "username": "sampleuser"}, "database_display_name": "new_database", "database_id": "new_database_id", "database_properties": ["database_properties"], "database_type": "netezza", "description": "Description of the external Database", "tags": ["tags"]}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_database_registrations()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_database_registrations_required_params_with_retries(self):
        # Enable retries and run test_list_database_registrations_required_params.
        _service.enable_retries()
        self.test_list_database_registrations_required_params()

        # Disable retries and run test_list_database_registrations_required_params.
        _service.disable_retries()
        self.test_list_database_registrations_required_params()


class TestCreateDatabaseRegistration:
    """
    Test Class for create_database_registration
    """

    @responses.activate
    def test_create_database_registration_all_params(self):
        """
        create_database_registration()
        """
        # Set up mock
        url = preprocess_url('/database_registrations')
        mock_response = '{"database_registration": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "created_by": "user1@bim.com", "created_on": "1686792721", "database_details": {"database_name": "new_database", "hostname": "netezza://ps.fyre.com", "password": "samplepassword", "port": 4543, "sasl": true, "ssl": true, "tables": "kafka_table_name", "username": "sampleuser"}, "database_display_name": "new_database", "database_id": "new_database_id", "database_properties": ["database_properties"], "database_type": "netezza", "description": "Description of the external Database", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a RegisterDatabaseCatalogBodyDatabaseDetails model
        register_database_catalog_body_database_details_model = {}
        register_database_catalog_body_database_details_model['certificate'] = 'contents of a pem/crt file'
        register_database_catalog_body_database_details_model['certificate_extension'] = 'pem/crt'
        register_database_catalog_body_database_details_model['database_name'] = 'new_database'
        register_database_catalog_body_database_details_model['hostname'] = 'db2@<hostname>.com'
        register_database_catalog_body_database_details_model['hosts'] = 'abc.com:1234,xyz.com:4321'
        register_database_catalog_body_database_details_model['password'] = 'samplepassword'
        register_database_catalog_body_database_details_model['port'] = 4553
        register_database_catalog_body_database_details_model['sasl'] = True
        register_database_catalog_body_database_details_model['ssl'] = True
        register_database_catalog_body_database_details_model['tables'] = 'kafka_table_name'
        register_database_catalog_body_database_details_model['username'] = 'sampleuser'

        # Construct a dict representation of a RegisterDatabaseCatalogBodyDatabasePropertiesItems model
        register_database_catalog_body_database_properties_items_model = {}
        register_database_catalog_body_database_properties_items_model['encrypt'] = True
        register_database_catalog_body_database_properties_items_model['key'] = 'abc'
        register_database_catalog_body_database_properties_items_model['value'] = 'xyz'

        # Set up parameter values
        catalog_name = 'sampleCatalog'
        database_display_name = 'new_database'
        database_type = 'db2'
        created_on = 38
        database_details = register_database_catalog_body_database_details_model
        database_properties = [register_database_catalog_body_database_properties_items_model]
        description = 'db2 extenal database description'
        tags = ['tag_1', 'tag_2']
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_database_registration(
            catalog_name,
            database_display_name,
            database_type,
            created_on=created_on,
            database_details=database_details,
            database_properties=database_properties,
            description=description,
            tags=tags,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['catalog_name'] == 'sampleCatalog'
        assert req_body['database_display_name'] == 'new_database'
        assert req_body['database_type'] == 'db2'
        assert req_body['created_on'] == 38
        assert req_body['database_details'] == register_database_catalog_body_database_details_model
        assert req_body['database_properties'] == [register_database_catalog_body_database_properties_items_model]
        assert req_body['description'] == 'db2 extenal database description'
        assert req_body['tags'] == ['tag_1', 'tag_2']

    def test_create_database_registration_all_params_with_retries(self):
        # Enable retries and run test_create_database_registration_all_params.
        _service.enable_retries()
        self.test_create_database_registration_all_params()

        # Disable retries and run test_create_database_registration_all_params.
        _service.disable_retries()
        self.test_create_database_registration_all_params()

    @responses.activate
    def test_create_database_registration_required_params(self):
        """
        test_create_database_registration_required_params()
        """
        # Set up mock
        url = preprocess_url('/database_registrations')
        mock_response = '{"database_registration": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "created_by": "user1@bim.com", "created_on": "1686792721", "database_details": {"database_name": "new_database", "hostname": "netezza://ps.fyre.com", "password": "samplepassword", "port": 4543, "sasl": true, "ssl": true, "tables": "kafka_table_name", "username": "sampleuser"}, "database_display_name": "new_database", "database_id": "new_database_id", "database_properties": ["database_properties"], "database_type": "netezza", "description": "Description of the external Database", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a RegisterDatabaseCatalogBodyDatabaseDetails model
        register_database_catalog_body_database_details_model = {}
        register_database_catalog_body_database_details_model['certificate'] = 'contents of a pem/crt file'
        register_database_catalog_body_database_details_model['certificate_extension'] = 'pem/crt'
        register_database_catalog_body_database_details_model['database_name'] = 'new_database'
        register_database_catalog_body_database_details_model['hostname'] = 'db2@<hostname>.com'
        register_database_catalog_body_database_details_model['hosts'] = 'abc.com:1234,xyz.com:4321'
        register_database_catalog_body_database_details_model['password'] = 'samplepassword'
        register_database_catalog_body_database_details_model['port'] = 4553
        register_database_catalog_body_database_details_model['sasl'] = True
        register_database_catalog_body_database_details_model['ssl'] = True
        register_database_catalog_body_database_details_model['tables'] = 'kafka_table_name'
        register_database_catalog_body_database_details_model['username'] = 'sampleuser'

        # Construct a dict representation of a RegisterDatabaseCatalogBodyDatabasePropertiesItems model
        register_database_catalog_body_database_properties_items_model = {}
        register_database_catalog_body_database_properties_items_model['encrypt'] = True
        register_database_catalog_body_database_properties_items_model['key'] = 'abc'
        register_database_catalog_body_database_properties_items_model['value'] = 'xyz'

        # Set up parameter values
        catalog_name = 'sampleCatalog'
        database_display_name = 'new_database'
        database_type = 'db2'
        created_on = 38
        database_details = register_database_catalog_body_database_details_model
        database_properties = [register_database_catalog_body_database_properties_items_model]
        description = 'db2 extenal database description'
        tags = ['tag_1', 'tag_2']

        # Invoke method
        response = _service.create_database_registration(
            catalog_name,
            database_display_name,
            database_type,
            created_on=created_on,
            database_details=database_details,
            database_properties=database_properties,
            description=description,
            tags=tags,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['catalog_name'] == 'sampleCatalog'
        assert req_body['database_display_name'] == 'new_database'
        assert req_body['database_type'] == 'db2'
        assert req_body['created_on'] == 38
        assert req_body['database_details'] == register_database_catalog_body_database_details_model
        assert req_body['database_properties'] == [register_database_catalog_body_database_properties_items_model]
        assert req_body['description'] == 'db2 extenal database description'
        assert req_body['tags'] == ['tag_1', 'tag_2']

    def test_create_database_registration_required_params_with_retries(self):
        # Enable retries and run test_create_database_registration_required_params.
        _service.enable_retries()
        self.test_create_database_registration_required_params()

        # Disable retries and run test_create_database_registration_required_params.
        _service.disable_retries()
        self.test_create_database_registration_required_params()

    @responses.activate
    def test_create_database_registration_value_error(self):
        """
        test_create_database_registration_value_error()
        """
        # Set up mock
        url = preprocess_url('/database_registrations')
        mock_response = '{"database_registration": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "created_by": "user1@bim.com", "created_on": "1686792721", "database_details": {"database_name": "new_database", "hostname": "netezza://ps.fyre.com", "password": "samplepassword", "port": 4543, "sasl": true, "ssl": true, "tables": "kafka_table_name", "username": "sampleuser"}, "database_display_name": "new_database", "database_id": "new_database_id", "database_properties": ["database_properties"], "database_type": "netezza", "description": "Description of the external Database", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a RegisterDatabaseCatalogBodyDatabaseDetails model
        register_database_catalog_body_database_details_model = {}
        register_database_catalog_body_database_details_model['certificate'] = 'contents of a pem/crt file'
        register_database_catalog_body_database_details_model['certificate_extension'] = 'pem/crt'
        register_database_catalog_body_database_details_model['database_name'] = 'new_database'
        register_database_catalog_body_database_details_model['hostname'] = 'db2@<hostname>.com'
        register_database_catalog_body_database_details_model['hosts'] = 'abc.com:1234,xyz.com:4321'
        register_database_catalog_body_database_details_model['password'] = 'samplepassword'
        register_database_catalog_body_database_details_model['port'] = 4553
        register_database_catalog_body_database_details_model['sasl'] = True
        register_database_catalog_body_database_details_model['ssl'] = True
        register_database_catalog_body_database_details_model['tables'] = 'kafka_table_name'
        register_database_catalog_body_database_details_model['username'] = 'sampleuser'

        # Construct a dict representation of a RegisterDatabaseCatalogBodyDatabasePropertiesItems model
        register_database_catalog_body_database_properties_items_model = {}
        register_database_catalog_body_database_properties_items_model['encrypt'] = True
        register_database_catalog_body_database_properties_items_model['key'] = 'abc'
        register_database_catalog_body_database_properties_items_model['value'] = 'xyz'

        # Set up parameter values
        catalog_name = 'sampleCatalog'
        database_display_name = 'new_database'
        database_type = 'db2'
        created_on = 38
        database_details = register_database_catalog_body_database_details_model
        database_properties = [register_database_catalog_body_database_properties_items_model]
        description = 'db2 extenal database description'
        tags = ['tag_1', 'tag_2']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_name": catalog_name,
            "database_display_name": database_display_name,
            "database_type": database_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_database_registration(**req_copy)

    def test_create_database_registration_value_error_with_retries(self):
        # Enable retries and run test_create_database_registration_value_error.
        _service.enable_retries()
        self.test_create_database_registration_value_error()

        # Disable retries and run test_create_database_registration_value_error.
        _service.disable_retries()
        self.test_create_database_registration_value_error()


class TestGetDatabase:
    """
    Test Class for get_database
    """

    @responses.activate
    def test_get_database_all_params(self):
        """
        get_database()
        """
        # Set up mock
        url = preprocess_url('/database_registrations/testString')
        mock_response = '{"database": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "created_by": "user1@bim.com", "created_on": "1686792721", "database_details": {"database_name": "new_database", "hostname": "netezza://ps.fyre.com", "password": "samplepassword", "port": 4543, "sasl": true, "ssl": true, "tables": "kafka_table_name", "username": "sampleuser"}, "database_display_name": "new_database", "database_id": "new_database_id", "database_properties": ["database_properties"], "database_type": "netezza", "description": "Description of the external Database", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        database_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.get_database(
            database_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_database_all_params_with_retries(self):
        # Enable retries and run test_get_database_all_params.
        _service.enable_retries()
        self.test_get_database_all_params()

        # Disable retries and run test_get_database_all_params.
        _service.disable_retries()
        self.test_get_database_all_params()

    @responses.activate
    def test_get_database_required_params(self):
        """
        test_get_database_required_params()
        """
        # Set up mock
        url = preprocess_url('/database_registrations/testString')
        mock_response = '{"database": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "created_by": "user1@bim.com", "created_on": "1686792721", "database_details": {"database_name": "new_database", "hostname": "netezza://ps.fyre.com", "password": "samplepassword", "port": 4543, "sasl": true, "ssl": true, "tables": "kafka_table_name", "username": "sampleuser"}, "database_display_name": "new_database", "database_id": "new_database_id", "database_properties": ["database_properties"], "database_type": "netezza", "description": "Description of the external Database", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        database_id = 'testString'

        # Invoke method
        response = _service.get_database(
            database_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_database_required_params_with_retries(self):
        # Enable retries and run test_get_database_required_params.
        _service.enable_retries()
        self.test_get_database_required_params()

        # Disable retries and run test_get_database_required_params.
        _service.disable_retries()
        self.test_get_database_required_params()

    @responses.activate
    def test_get_database_value_error(self):
        """
        test_get_database_value_error()
        """
        # Set up mock
        url = preprocess_url('/database_registrations/testString')
        mock_response = '{"database": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "created_by": "user1@bim.com", "created_on": "1686792721", "database_details": {"database_name": "new_database", "hostname": "netezza://ps.fyre.com", "password": "samplepassword", "port": 4543, "sasl": true, "ssl": true, "tables": "kafka_table_name", "username": "sampleuser"}, "database_display_name": "new_database", "database_id": "new_database_id", "database_properties": ["database_properties"], "database_type": "netezza", "description": "Description of the external Database", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        database_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "database_id": database_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_database(**req_copy)

    def test_get_database_value_error_with_retries(self):
        # Enable retries and run test_get_database_value_error.
        _service.enable_retries()
        self.test_get_database_value_error()

        # Disable retries and run test_get_database_value_error.
        _service.disable_retries()
        self.test_get_database_value_error()


class TestDeleteDatabaseCatalog:
    """
    Test Class for delete_database_catalog
    """

    @responses.activate
    def test_delete_database_catalog_all_params(self):
        """
        delete_database_catalog()
        """
        # Set up mock
        url = preprocess_url('/database_registrations/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        database_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_database_catalog(
            database_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_database_catalog_all_params_with_retries(self):
        # Enable retries and run test_delete_database_catalog_all_params.
        _service.enable_retries()
        self.test_delete_database_catalog_all_params()

        # Disable retries and run test_delete_database_catalog_all_params.
        _service.disable_retries()
        self.test_delete_database_catalog_all_params()

    @responses.activate
    def test_delete_database_catalog_required_params(self):
        """
        test_delete_database_catalog_required_params()
        """
        # Set up mock
        url = preprocess_url('/database_registrations/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        database_id = 'testString'

        # Invoke method
        response = _service.delete_database_catalog(
            database_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_database_catalog_required_params_with_retries(self):
        # Enable retries and run test_delete_database_catalog_required_params.
        _service.enable_retries()
        self.test_delete_database_catalog_required_params()

        # Disable retries and run test_delete_database_catalog_required_params.
        _service.disable_retries()
        self.test_delete_database_catalog_required_params()

    @responses.activate
    def test_delete_database_catalog_value_error(self):
        """
        test_delete_database_catalog_value_error()
        """
        # Set up mock
        url = preprocess_url('/database_registrations/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        database_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "database_id": database_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_database_catalog(**req_copy)

    def test_delete_database_catalog_value_error_with_retries(self):
        # Enable retries and run test_delete_database_catalog_value_error.
        _service.enable_retries()
        self.test_delete_database_catalog_value_error()

        # Disable retries and run test_delete_database_catalog_value_error.
        _service.disable_retries()
        self.test_delete_database_catalog_value_error()


class TestUpdateDatabase:
    """
    Test Class for update_database
    """

    @responses.activate
    def test_update_database_all_params(self):
        """
        update_database()
        """
        # Set up mock
        url = preprocess_url('/database_registrations/testString')
        mock_response = '{"database": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "created_by": "user1@bim.com", "created_on": "1686792721", "database_details": {"database_name": "new_database", "hostname": "netezza://ps.fyre.com", "password": "samplepassword", "port": 4543, "sasl": true, "ssl": true, "tables": "kafka_table_name", "username": "sampleuser"}, "database_display_name": "new_database", "database_id": "new_database_id", "database_properties": ["database_properties"], "database_type": "netezza", "description": "Description of the external Database", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        database_id = 'testString'
        body = [json_patch_operation_model]
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.update_database(
            database_id,
            body,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_database_all_params_with_retries(self):
        # Enable retries and run test_update_database_all_params.
        _service.enable_retries()
        self.test_update_database_all_params()

        # Disable retries and run test_update_database_all_params.
        _service.disable_retries()
        self.test_update_database_all_params()

    @responses.activate
    def test_update_database_required_params(self):
        """
        test_update_database_required_params()
        """
        # Set up mock
        url = preprocess_url('/database_registrations/testString')
        mock_response = '{"database": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "created_by": "user1@bim.com", "created_on": "1686792721", "database_details": {"database_name": "new_database", "hostname": "netezza://ps.fyre.com", "password": "samplepassword", "port": 4543, "sasl": true, "ssl": true, "tables": "kafka_table_name", "username": "sampleuser"}, "database_display_name": "new_database", "database_id": "new_database_id", "database_properties": ["database_properties"], "database_type": "netezza", "description": "Description of the external Database", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        database_id = 'testString'
        body = [json_patch_operation_model]

        # Invoke method
        response = _service.update_database(
            database_id,
            body,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_database_required_params_with_retries(self):
        # Enable retries and run test_update_database_required_params.
        _service.enable_retries()
        self.test_update_database_required_params()

        # Disable retries and run test_update_database_required_params.
        _service.disable_retries()
        self.test_update_database_required_params()

    @responses.activate
    def test_update_database_value_error(self):
        """
        test_update_database_value_error()
        """
        # Set up mock
        url = preprocess_url('/database_registrations/testString')
        mock_response = '{"database": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "created_by": "user1@bim.com", "created_on": "1686792721", "database_details": {"database_name": "new_database", "hostname": "netezza://ps.fyre.com", "password": "samplepassword", "port": 4543, "sasl": true, "ssl": true, "tables": "kafka_table_name", "username": "sampleuser"}, "database_display_name": "new_database", "database_id": "new_database_id", "database_properties": ["database_properties"], "database_type": "netezza", "description": "Description of the external Database", "tags": ["tags"]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        database_id = 'testString'
        body = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "database_id": database_id,
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_database(**req_copy)

    def test_update_database_value_error_with_retries(self):
        # Enable retries and run test_update_database_value_error.
        _service.enable_retries()
        self.test_update_database_value_error()

        # Disable retries and run test_update_database_value_error.
        _service.disable_retries()
        self.test_update_database_value_error()


class TestValidateDatabaseConnection:
    """
    Test Class for validate_database_connection
    """

    @responses.activate
    def test_validate_database_connection_all_params(self):
        """
        validate_database_connection()
        """
        # Set up mock
        url = preprocess_url('/test_database_connection')
        mock_response = '{"connection_response": {"state": false, "state_message": "state_message"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ValidateDatabaseBodyDatabaseDetails model
        validate_database_body_database_details_model = {}
        validate_database_body_database_details_model['database_name'] = 'sampledatabase'
        validate_database_body_database_details_model['hostname'] = 'db2@hostname.com'
        validate_database_body_database_details_model['password'] = 'samplepassword'
        validate_database_body_database_details_model['port'] = 4553
        validate_database_body_database_details_model['sasl'] = True
        validate_database_body_database_details_model['ssl'] = True
        validate_database_body_database_details_model['tables'] = 'kafka_table_name'
        validate_database_body_database_details_model['username'] = 'sampleuser'

        # Set up parameter values
        database_details = validate_database_body_database_details_model
        database_type = 'netezza'
        certificate = 'contents of a pem/crt file'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.validate_database_connection(
            database_details,
            database_type,
            certificate=certificate,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['database_details'] == validate_database_body_database_details_model
        assert req_body['database_type'] == 'netezza'
        assert req_body['certificate'] == 'contents of a pem/crt file'

    def test_validate_database_connection_all_params_with_retries(self):
        # Enable retries and run test_validate_database_connection_all_params.
        _service.enable_retries()
        self.test_validate_database_connection_all_params()

        # Disable retries and run test_validate_database_connection_all_params.
        _service.disable_retries()
        self.test_validate_database_connection_all_params()

    @responses.activate
    def test_validate_database_connection_required_params(self):
        """
        test_validate_database_connection_required_params()
        """
        # Set up mock
        url = preprocess_url('/test_database_connection')
        mock_response = '{"connection_response": {"state": false, "state_message": "state_message"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ValidateDatabaseBodyDatabaseDetails model
        validate_database_body_database_details_model = {}
        validate_database_body_database_details_model['database_name'] = 'sampledatabase'
        validate_database_body_database_details_model['hostname'] = 'db2@hostname.com'
        validate_database_body_database_details_model['password'] = 'samplepassword'
        validate_database_body_database_details_model['port'] = 4553
        validate_database_body_database_details_model['sasl'] = True
        validate_database_body_database_details_model['ssl'] = True
        validate_database_body_database_details_model['tables'] = 'kafka_table_name'
        validate_database_body_database_details_model['username'] = 'sampleuser'

        # Set up parameter values
        database_details = validate_database_body_database_details_model
        database_type = 'netezza'
        certificate = 'contents of a pem/crt file'

        # Invoke method
        response = _service.validate_database_connection(
            database_details,
            database_type,
            certificate=certificate,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['database_details'] == validate_database_body_database_details_model
        assert req_body['database_type'] == 'netezza'
        assert req_body['certificate'] == 'contents of a pem/crt file'

    def test_validate_database_connection_required_params_with_retries(self):
        # Enable retries and run test_validate_database_connection_required_params.
        _service.enable_retries()
        self.test_validate_database_connection_required_params()

        # Disable retries and run test_validate_database_connection_required_params.
        _service.disable_retries()
        self.test_validate_database_connection_required_params()

    @responses.activate
    def test_validate_database_connection_value_error(self):
        """
        test_validate_database_connection_value_error()
        """
        # Set up mock
        url = preprocess_url('/test_database_connection')
        mock_response = '{"connection_response": {"state": false, "state_message": "state_message"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ValidateDatabaseBodyDatabaseDetails model
        validate_database_body_database_details_model = {}
        validate_database_body_database_details_model['database_name'] = 'sampledatabase'
        validate_database_body_database_details_model['hostname'] = 'db2@hostname.com'
        validate_database_body_database_details_model['password'] = 'samplepassword'
        validate_database_body_database_details_model['port'] = 4553
        validate_database_body_database_details_model['sasl'] = True
        validate_database_body_database_details_model['ssl'] = True
        validate_database_body_database_details_model['tables'] = 'kafka_table_name'
        validate_database_body_database_details_model['username'] = 'sampleuser'

        # Set up parameter values
        database_details = validate_database_body_database_details_model
        database_type = 'netezza'
        certificate = 'contents of a pem/crt file'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "database_details": database_details,
            "database_type": database_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.validate_database_connection(**req_copy)

    def test_validate_database_connection_value_error_with_retries(self):
        # Enable retries and run test_validate_database_connection_value_error.
        _service.enable_retries()
        self.test_validate_database_connection_value_error()

        # Disable retries and run test_validate_database_connection_value_error.
        _service.disable_retries()
        self.test_validate_database_connection_value_error()


# endregion
##############################################################################
# End of Service: Databases
##############################################################################

##############################################################################
# Start of Service: Engines
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = WatsonxDataV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, WatsonxDataV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = WatsonxDataV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListDb2Engines:
    """
    Test Class for list_db2_engines
    """

    @responses.activate
    def test_list_db2_engines_all_params(self):
        """
        list_db2_engines()
        """
        # Set up mock
        url = preprocess_url('/db2_engines')
        mock_response = '{"db2_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "db2 engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-db2-01-db2-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "db2"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_db2_engines(
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_db2_engines_all_params_with_retries(self):
        # Enable retries and run test_list_db2_engines_all_params.
        _service.enable_retries()
        self.test_list_db2_engines_all_params()

        # Disable retries and run test_list_db2_engines_all_params.
        _service.disable_retries()
        self.test_list_db2_engines_all_params()

    @responses.activate
    def test_list_db2_engines_required_params(self):
        """
        test_list_db2_engines_required_params()
        """
        # Set up mock
        url = preprocess_url('/db2_engines')
        mock_response = '{"db2_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "db2 engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-db2-01-db2-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "db2"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_db2_engines()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_db2_engines_required_params_with_retries(self):
        # Enable retries and run test_list_db2_engines_required_params.
        _service.enable_retries()
        self.test_list_db2_engines_required_params()

        # Disable retries and run test_list_db2_engines_required_params.
        _service.disable_retries()
        self.test_list_db2_engines_required_params()


class TestCreateDb2Engine:
    """
    Test Class for create_db2_engine
    """

    @responses.activate
    def test_create_db2_engine_all_params(self):
        """
        create_db2_engine()
        """
        # Set up mock
        url = preprocess_url('/db2_engines')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "db2 engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-db2-01-db2-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "db2"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a CreateDb2EngineDetails model
        create_db2_engine_details_model = {}
        create_db2_engine_details_model['connection_string'] = '1.2.3.4'

        # Set up parameter values
        origin = 'external'
        type = 'db2'
        description = 'db2 engine description'
        engine_details = create_db2_engine_details_model
        engine_display_name = 'sampleEngine'
        tags = ['tag1', 'tag2']
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_db2_engine(
            origin,
            type,
            description=description,
            engine_details=engine_details,
            engine_display_name=engine_display_name,
            tags=tags,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['origin'] == 'external'
        assert req_body['type'] == 'db2'
        assert req_body['description'] == 'db2 engine description'
        assert req_body['engine_details'] == create_db2_engine_details_model
        assert req_body['engine_display_name'] == 'sampleEngine'
        assert req_body['tags'] == ['tag1', 'tag2']

    def test_create_db2_engine_all_params_with_retries(self):
        # Enable retries and run test_create_db2_engine_all_params.
        _service.enable_retries()
        self.test_create_db2_engine_all_params()

        # Disable retries and run test_create_db2_engine_all_params.
        _service.disable_retries()
        self.test_create_db2_engine_all_params()

    @responses.activate
    def test_create_db2_engine_required_params(self):
        """
        test_create_db2_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/db2_engines')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "db2 engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-db2-01-db2-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "db2"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a CreateDb2EngineDetails model
        create_db2_engine_details_model = {}
        create_db2_engine_details_model['connection_string'] = '1.2.3.4'

        # Set up parameter values
        origin = 'external'
        type = 'db2'
        description = 'db2 engine description'
        engine_details = create_db2_engine_details_model
        engine_display_name = 'sampleEngine'
        tags = ['tag1', 'tag2']

        # Invoke method
        response = _service.create_db2_engine(
            origin,
            type,
            description=description,
            engine_details=engine_details,
            engine_display_name=engine_display_name,
            tags=tags,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['origin'] == 'external'
        assert req_body['type'] == 'db2'
        assert req_body['description'] == 'db2 engine description'
        assert req_body['engine_details'] == create_db2_engine_details_model
        assert req_body['engine_display_name'] == 'sampleEngine'
        assert req_body['tags'] == ['tag1', 'tag2']

    def test_create_db2_engine_required_params_with_retries(self):
        # Enable retries and run test_create_db2_engine_required_params.
        _service.enable_retries()
        self.test_create_db2_engine_required_params()

        # Disable retries and run test_create_db2_engine_required_params.
        _service.disable_retries()
        self.test_create_db2_engine_required_params()

    @responses.activate
    def test_create_db2_engine_value_error(self):
        """
        test_create_db2_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/db2_engines')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "db2 engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-db2-01-db2-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "db2"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a CreateDb2EngineDetails model
        create_db2_engine_details_model = {}
        create_db2_engine_details_model['connection_string'] = '1.2.3.4'

        # Set up parameter values
        origin = 'external'
        type = 'db2'
        description = 'db2 engine description'
        engine_details = create_db2_engine_details_model
        engine_display_name = 'sampleEngine'
        tags = ['tag1', 'tag2']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "origin": origin,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_db2_engine(**req_copy)

    def test_create_db2_engine_value_error_with_retries(self):
        # Enable retries and run test_create_db2_engine_value_error.
        _service.enable_retries()
        self.test_create_db2_engine_value_error()

        # Disable retries and run test_create_db2_engine_value_error.
        _service.disable_retries()
        self.test_create_db2_engine_value_error()


class TestDeleteDb2Engine:
    """
    Test Class for delete_db2_engine
    """

    @responses.activate
    def test_delete_db2_engine_all_params(self):
        """
        delete_db2_engine()
        """
        # Set up mock
        url = preprocess_url('/db2_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_db2_engine(
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_db2_engine_all_params_with_retries(self):
        # Enable retries and run test_delete_db2_engine_all_params.
        _service.enable_retries()
        self.test_delete_db2_engine_all_params()

        # Disable retries and run test_delete_db2_engine_all_params.
        _service.disable_retries()
        self.test_delete_db2_engine_all_params()

    @responses.activate
    def test_delete_db2_engine_required_params(self):
        """
        test_delete_db2_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/db2_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Invoke method
        response = _service.delete_db2_engine(
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_db2_engine_required_params_with_retries(self):
        # Enable retries and run test_delete_db2_engine_required_params.
        _service.enable_retries()
        self.test_delete_db2_engine_required_params()

        # Disable retries and run test_delete_db2_engine_required_params.
        _service.disable_retries()
        self.test_delete_db2_engine_required_params()

    @responses.activate
    def test_delete_db2_engine_value_error(self):
        """
        test_delete_db2_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/db2_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_db2_engine(**req_copy)

    def test_delete_db2_engine_value_error_with_retries(self):
        # Enable retries and run test_delete_db2_engine_value_error.
        _service.enable_retries()
        self.test_delete_db2_engine_value_error()

        # Disable retries and run test_delete_db2_engine_value_error.
        _service.disable_retries()
        self.test_delete_db2_engine_value_error()


class TestUpdateDb2Engine:
    """
    Test Class for update_db2_engine
    """

    @responses.activate
    def test_update_db2_engine_all_params(self):
        """
        update_db2_engine()
        """
        # Set up mock
        url = preprocess_url('/db2_engines/testString')
        mock_response = '{"db2_engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "db2 engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-db2-01-db2-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "db2"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.update_db2_engine(
            engine_id,
            body,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_db2_engine_all_params_with_retries(self):
        # Enable retries and run test_update_db2_engine_all_params.
        _service.enable_retries()
        self.test_update_db2_engine_all_params()

        # Disable retries and run test_update_db2_engine_all_params.
        _service.disable_retries()
        self.test_update_db2_engine_all_params()

    @responses.activate
    def test_update_db2_engine_required_params(self):
        """
        test_update_db2_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/db2_engines/testString')
        mock_response = '{"db2_engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "db2 engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-db2-01-db2-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "db2"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]

        # Invoke method
        response = _service.update_db2_engine(
            engine_id,
            body,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_db2_engine_required_params_with_retries(self):
        # Enable retries and run test_update_db2_engine_required_params.
        _service.enable_retries()
        self.test_update_db2_engine_required_params()

        # Disable retries and run test_update_db2_engine_required_params.
        _service.disable_retries()
        self.test_update_db2_engine_required_params()

    @responses.activate
    def test_update_db2_engine_value_error(self):
        """
        test_update_db2_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/db2_engines/testString')
        mock_response = '{"db2_engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "db2 engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-db2-01-db2-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "db2"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_db2_engine(**req_copy)

    def test_update_db2_engine_value_error_with_retries(self):
        # Enable retries and run test_update_db2_engine_value_error.
        _service.enable_retries()
        self.test_update_db2_engine_value_error()

        # Disable retries and run test_update_db2_engine_value_error.
        _service.disable_retries()
        self.test_update_db2_engine_value_error()


class TestListEngines:
    """
    Test Class for list_engines
    """

    @responses.activate
    def test_list_engines_all_params(self):
        """
        list_engines()
        """
        # Set up mock
        url = preprocess_url('/engines')
        mock_response = '{"engines": {"db2_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "db2 engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-db2-01-db2-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "db2"}], "milvus_services": [{"actions": ["actions"], "created_by": "<username>@<domain>.com", "created_on": 10, "description": "milvus service for running sql queries", "grpc_port": 9, "host_name": "sampleMilvus", "https_port": 10, "origin": "native", "service_display_name": "sampleService", "service_id": "sampleService123", "status": "running", "status_code": 11, "tags": ["tags"], "type": "milvus"}], "netezza_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "netezza engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-netezza-01-netezza-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "netezza"}], "prestissimo_engines": [{"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "prestissimo engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "ibm-lh-lakehouse-prestissimo-01-prestissimo-svc-cpd-instance.apps.wkclhconnectortest.cp.fyre.ibm.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-prestissimo-01-prestissimo-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "prestissimo", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}], "presto_engines": [{"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}], "spark_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "spark engine for running sql queries", "engine_details": {"connection_string": "https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "Registered", "tags": ["tags"], "type": "spark"}]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_engines(
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_engines_all_params_with_retries(self):
        # Enable retries and run test_list_engines_all_params.
        _service.enable_retries()
        self.test_list_engines_all_params()

        # Disable retries and run test_list_engines_all_params.
        _service.disable_retries()
        self.test_list_engines_all_params()

    @responses.activate
    def test_list_engines_required_params(self):
        """
        test_list_engines_required_params()
        """
        # Set up mock
        url = preprocess_url('/engines')
        mock_response = '{"engines": {"db2_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "db2 engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-db2-01-db2-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "db2"}], "milvus_services": [{"actions": ["actions"], "created_by": "<username>@<domain>.com", "created_on": 10, "description": "milvus service for running sql queries", "grpc_port": 9, "host_name": "sampleMilvus", "https_port": 10, "origin": "native", "service_display_name": "sampleService", "service_id": "sampleService123", "status": "running", "status_code": 11, "tags": ["tags"], "type": "milvus"}], "netezza_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "netezza engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-netezza-01-netezza-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "netezza"}], "prestissimo_engines": [{"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "prestissimo engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "ibm-lh-lakehouse-prestissimo-01-prestissimo-svc-cpd-instance.apps.wkclhconnectortest.cp.fyre.ibm.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-prestissimo-01-prestissimo-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "prestissimo", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}], "presto_engines": [{"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}], "spark_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "spark engine for running sql queries", "engine_details": {"connection_string": "https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "Registered", "tags": ["tags"], "type": "spark"}]}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_engines()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_engines_required_params_with_retries(self):
        # Enable retries and run test_list_engines_required_params.
        _service.enable_retries()
        self.test_list_engines_required_params()

        # Disable retries and run test_list_engines_required_params.
        _service.disable_retries()
        self.test_list_engines_required_params()


class TestGetDeployments:
    """
    Test Class for get_deployments
    """

    @responses.activate
    def test_get_deployments_all_params(self):
        """
        get_deployments()
        """
        # Set up mock
        url = preprocess_url('/instance')
        mock_response = '{"deploymentresponse": {"deployment": {"cloud_type": "awq", "enable_private_endpoints": true, "enable_public_endpoints": true, "first_time_use": false, "formation_id": "new_form_id", "id": "dep_id", "plan_id": "new_plan_id", "platform_options": {"backup_encryption_key_crn": "<backup_encryption_key_crn>", "disk_encryption_key_crn": "<disk_encryption_key_crn>", "key_protect_key_id": "<key_protect_key_id>"}, "region": "us-south", "resource_group_crn": "crn:v1:staging:public:resource-controller::a/hddrtnjjj27dh38xbw::resource-group:c02a6a94f16e4ca", "type": "deployment_type", "version": "1.0.2"}}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.get_deployments(
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_deployments_all_params_with_retries(self):
        # Enable retries and run test_get_deployments_all_params.
        _service.enable_retries()
        self.test_get_deployments_all_params()

        # Disable retries and run test_get_deployments_all_params.
        _service.disable_retries()
        self.test_get_deployments_all_params()

    @responses.activate
    def test_get_deployments_required_params(self):
        """
        test_get_deployments_required_params()
        """
        # Set up mock
        url = preprocess_url('/instance')
        mock_response = '{"deploymentresponse": {"deployment": {"cloud_type": "awq", "enable_private_endpoints": true, "enable_public_endpoints": true, "first_time_use": false, "formation_id": "new_form_id", "id": "dep_id", "plan_id": "new_plan_id", "platform_options": {"backup_encryption_key_crn": "<backup_encryption_key_crn>", "disk_encryption_key_crn": "<disk_encryption_key_crn>", "key_protect_key_id": "<key_protect_key_id>"}, "region": "us-south", "resource_group_crn": "crn:v1:staging:public:resource-controller::a/hddrtnjjj27dh38xbw::resource-group:c02a6a94f16e4ca", "type": "deployment_type", "version": "1.0.2"}}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_deployments()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_deployments_required_params_with_retries(self):
        # Enable retries and run test_get_deployments_required_params.
        _service.enable_retries()
        self.test_get_deployments_required_params()

        # Disable retries and run test_get_deployments_required_params.
        _service.disable_retries()
        self.test_get_deployments_required_params()


class TestListNetezzaEngines:
    """
    Test Class for list_netezza_engines
    """

    @responses.activate
    def test_list_netezza_engines_all_params(self):
        """
        list_netezza_engines()
        """
        # Set up mock
        url = preprocess_url('/netezza_engines')
        mock_response = '{"netezza_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "netezza engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-netezza-01-netezza-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "netezza"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_netezza_engines(
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_netezza_engines_all_params_with_retries(self):
        # Enable retries and run test_list_netezza_engines_all_params.
        _service.enable_retries()
        self.test_list_netezza_engines_all_params()

        # Disable retries and run test_list_netezza_engines_all_params.
        _service.disable_retries()
        self.test_list_netezza_engines_all_params()

    @responses.activate
    def test_list_netezza_engines_required_params(self):
        """
        test_list_netezza_engines_required_params()
        """
        # Set up mock
        url = preprocess_url('/netezza_engines')
        mock_response = '{"netezza_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "netezza engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-netezza-01-netezza-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "netezza"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_netezza_engines()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_netezza_engines_required_params_with_retries(self):
        # Enable retries and run test_list_netezza_engines_required_params.
        _service.enable_retries()
        self.test_list_netezza_engines_required_params()

        # Disable retries and run test_list_netezza_engines_required_params.
        _service.disable_retries()
        self.test_list_netezza_engines_required_params()


class TestCreateNetezzaEngine:
    """
    Test Class for create_netezza_engine
    """

    @responses.activate
    def test_create_netezza_engine_all_params(self):
        """
        create_netezza_engine()
        """
        # Set up mock
        url = preprocess_url('/netezza_engines')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "netezza engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-netezza-01-netezza-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "netezza"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a CreateNetezzaEngineDetails model
        create_netezza_engine_details_model = {}
        create_netezza_engine_details_model['connection_string'] = '1.2.3.4'

        # Set up parameter values
        origin = 'external'
        type = 'netezza'
        description = 'netezza engine description'
        engine_details = create_netezza_engine_details_model
        engine_display_name = 'sampleEngine'
        tags = ['tag1', 'tag2']
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_netezza_engine(
            origin,
            type,
            description=description,
            engine_details=engine_details,
            engine_display_name=engine_display_name,
            tags=tags,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['origin'] == 'external'
        assert req_body['type'] == 'netezza'
        assert req_body['description'] == 'netezza engine description'
        assert req_body['engine_details'] == create_netezza_engine_details_model
        assert req_body['engine_display_name'] == 'sampleEngine'
        assert req_body['tags'] == ['tag1', 'tag2']

    def test_create_netezza_engine_all_params_with_retries(self):
        # Enable retries and run test_create_netezza_engine_all_params.
        _service.enable_retries()
        self.test_create_netezza_engine_all_params()

        # Disable retries and run test_create_netezza_engine_all_params.
        _service.disable_retries()
        self.test_create_netezza_engine_all_params()

    @responses.activate
    def test_create_netezza_engine_required_params(self):
        """
        test_create_netezza_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/netezza_engines')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "netezza engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-netezza-01-netezza-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "netezza"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a CreateNetezzaEngineDetails model
        create_netezza_engine_details_model = {}
        create_netezza_engine_details_model['connection_string'] = '1.2.3.4'

        # Set up parameter values
        origin = 'external'
        type = 'netezza'
        description = 'netezza engine description'
        engine_details = create_netezza_engine_details_model
        engine_display_name = 'sampleEngine'
        tags = ['tag1', 'tag2']

        # Invoke method
        response = _service.create_netezza_engine(
            origin,
            type,
            description=description,
            engine_details=engine_details,
            engine_display_name=engine_display_name,
            tags=tags,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['origin'] == 'external'
        assert req_body['type'] == 'netezza'
        assert req_body['description'] == 'netezza engine description'
        assert req_body['engine_details'] == create_netezza_engine_details_model
        assert req_body['engine_display_name'] == 'sampleEngine'
        assert req_body['tags'] == ['tag1', 'tag2']

    def test_create_netezza_engine_required_params_with_retries(self):
        # Enable retries and run test_create_netezza_engine_required_params.
        _service.enable_retries()
        self.test_create_netezza_engine_required_params()

        # Disable retries and run test_create_netezza_engine_required_params.
        _service.disable_retries()
        self.test_create_netezza_engine_required_params()

    @responses.activate
    def test_create_netezza_engine_value_error(self):
        """
        test_create_netezza_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/netezza_engines')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "netezza engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-netezza-01-netezza-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "netezza"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a CreateNetezzaEngineDetails model
        create_netezza_engine_details_model = {}
        create_netezza_engine_details_model['connection_string'] = '1.2.3.4'

        # Set up parameter values
        origin = 'external'
        type = 'netezza'
        description = 'netezza engine description'
        engine_details = create_netezza_engine_details_model
        engine_display_name = 'sampleEngine'
        tags = ['tag1', 'tag2']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "origin": origin,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_netezza_engine(**req_copy)

    def test_create_netezza_engine_value_error_with_retries(self):
        # Enable retries and run test_create_netezza_engine_value_error.
        _service.enable_retries()
        self.test_create_netezza_engine_value_error()

        # Disable retries and run test_create_netezza_engine_value_error.
        _service.disable_retries()
        self.test_create_netezza_engine_value_error()


class TestDeleteNetezzaEngine:
    """
    Test Class for delete_netezza_engine
    """

    @responses.activate
    def test_delete_netezza_engine_all_params(self):
        """
        delete_netezza_engine()
        """
        # Set up mock
        url = preprocess_url('/netezza_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_netezza_engine(
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_netezza_engine_all_params_with_retries(self):
        # Enable retries and run test_delete_netezza_engine_all_params.
        _service.enable_retries()
        self.test_delete_netezza_engine_all_params()

        # Disable retries and run test_delete_netezza_engine_all_params.
        _service.disable_retries()
        self.test_delete_netezza_engine_all_params()

    @responses.activate
    def test_delete_netezza_engine_required_params(self):
        """
        test_delete_netezza_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/netezza_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Invoke method
        response = _service.delete_netezza_engine(
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_netezza_engine_required_params_with_retries(self):
        # Enable retries and run test_delete_netezza_engine_required_params.
        _service.enable_retries()
        self.test_delete_netezza_engine_required_params()

        # Disable retries and run test_delete_netezza_engine_required_params.
        _service.disable_retries()
        self.test_delete_netezza_engine_required_params()

    @responses.activate
    def test_delete_netezza_engine_value_error(self):
        """
        test_delete_netezza_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/netezza_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_netezza_engine(**req_copy)

    def test_delete_netezza_engine_value_error_with_retries(self):
        # Enable retries and run test_delete_netezza_engine_value_error.
        _service.enable_retries()
        self.test_delete_netezza_engine_value_error()

        # Disable retries and run test_delete_netezza_engine_value_error.
        _service.disable_retries()
        self.test_delete_netezza_engine_value_error()


class TestUpdateNetezzaEngine:
    """
    Test Class for update_netezza_engine
    """

    @responses.activate
    def test_update_netezza_engine_all_params(self):
        """
        update_netezza_engine()
        """
        # Set up mock
        url = preprocess_url('/netezza_engines/testString')
        mock_response = '{"netezza_engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "netezza engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-netezza-01-netezza-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "netezza"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.update_netezza_engine(
            engine_id,
            body,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_netezza_engine_all_params_with_retries(self):
        # Enable retries and run test_update_netezza_engine_all_params.
        _service.enable_retries()
        self.test_update_netezza_engine_all_params()

        # Disable retries and run test_update_netezza_engine_all_params.
        _service.disable_retries()
        self.test_update_netezza_engine_all_params()

    @responses.activate
    def test_update_netezza_engine_required_params(self):
        """
        test_update_netezza_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/netezza_engines/testString')
        mock_response = '{"netezza_engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "netezza engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-netezza-01-netezza-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "netezza"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]

        # Invoke method
        response = _service.update_netezza_engine(
            engine_id,
            body,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_netezza_engine_required_params_with_retries(self):
        # Enable retries and run test_update_netezza_engine_required_params.
        _service.enable_retries()
        self.test_update_netezza_engine_required_params()

        # Disable retries and run test_update_netezza_engine_required_params.
        _service.disable_retries()
        self.test_update_netezza_engine_required_params()

    @responses.activate
    def test_update_netezza_engine_value_error(self):
        """
        test_update_netezza_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/netezza_engines/testString')
        mock_response = '{"netezza_engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "netezza engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "host_name": "xyz-netezza-01-netezza-svc", "origin": "ibm", "port": 4, "status": "REGISTERED", "tags": ["tags"], "type": "netezza"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_netezza_engine(**req_copy)

    def test_update_netezza_engine_value_error_with_retries(self):
        # Enable retries and run test_update_netezza_engine_value_error.
        _service.enable_retries()
        self.test_update_netezza_engine_value_error()

        # Disable retries and run test_update_netezza_engine_value_error.
        _service.disable_retries()
        self.test_update_netezza_engine_value_error()


class TestListOtherEngines:
    """
    Test Class for list_other_engines
    """

    @responses.activate
    def test_list_other_engines_all_params(self):
        """
        list_other_engines()
        """
        # Set up mock
        url = preprocess_url('/other_engines')
        mock_response = '{"other_engines": [{"created_by": "<username>@<domain>.com", "created_on": 10, "description": "engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "engine_type": "netezza", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "registered", "status_code": 11, "tags": ["tags"], "type": "external"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_other_engines(
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_other_engines_all_params_with_retries(self):
        # Enable retries and run test_list_other_engines_all_params.
        _service.enable_retries()
        self.test_list_other_engines_all_params()

        # Disable retries and run test_list_other_engines_all_params.
        _service.disable_retries()
        self.test_list_other_engines_all_params()

    @responses.activate
    def test_list_other_engines_required_params(self):
        """
        test_list_other_engines_required_params()
        """
        # Set up mock
        url = preprocess_url('/other_engines')
        mock_response = '{"other_engines": [{"created_by": "<username>@<domain>.com", "created_on": 10, "description": "engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "engine_type": "netezza", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "registered", "status_code": 11, "tags": ["tags"], "type": "external"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_other_engines()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_other_engines_required_params_with_retries(self):
        # Enable retries and run test_list_other_engines_required_params.
        _service.enable_retries()
        self.test_list_other_engines_required_params()

        # Disable retries and run test_list_other_engines_required_params.
        _service.disable_retries()
        self.test_list_other_engines_required_params()


class TestCreateOtherEngine:
    """
    Test Class for create_other_engine
    """

    @responses.activate
    def test_create_other_engine_all_params(self):
        """
        create_other_engine()
        """
        # Set up mock
        url = preprocess_url('/other_engines')
        mock_response = '{"engine": {"created_by": "<username>@<domain>.com", "created_on": 10, "description": "engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "engine_type": "netezza", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "registered", "status_code": 11, "tags": ["tags"], "type": "external"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a OtherEngineDetails model
        other_engine_details_model = {}
        other_engine_details_model['connection_string'] = '1.2.3.4'
        other_engine_details_model['engine_type'] = 'netezza'
        other_engine_details_model['metastore_host'] = '1.2.3.4'

        # Set up parameter values
        description = 'external engine description'
        engine_details = other_engine_details_model
        engine_display_name = 'sampleEngine01'
        tags = ['tag1', 'tag2']
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_other_engine(
            description=description,
            engine_details=engine_details,
            engine_display_name=engine_display_name,
            tags=tags,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'external engine description'
        assert req_body['engine_details'] == other_engine_details_model
        assert req_body['engine_display_name'] == 'sampleEngine01'
        assert req_body['tags'] == ['tag1', 'tag2']

    def test_create_other_engine_all_params_with_retries(self):
        # Enable retries and run test_create_other_engine_all_params.
        _service.enable_retries()
        self.test_create_other_engine_all_params()

        # Disable retries and run test_create_other_engine_all_params.
        _service.disable_retries()
        self.test_create_other_engine_all_params()

    @responses.activate
    def test_create_other_engine_required_params(self):
        """
        test_create_other_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/other_engines')
        mock_response = '{"engine": {"created_by": "<username>@<domain>.com", "created_on": 10, "description": "engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "engine_type": "netezza", "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "registered", "status_code": 11, "tags": ["tags"], "type": "external"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a OtherEngineDetails model
        other_engine_details_model = {}
        other_engine_details_model['connection_string'] = '1.2.3.4'
        other_engine_details_model['engine_type'] = 'netezza'
        other_engine_details_model['metastore_host'] = '1.2.3.4'

        # Set up parameter values
        description = 'external engine description'
        engine_details = other_engine_details_model
        engine_display_name = 'sampleEngine01'
        tags = ['tag1', 'tag2']

        # Invoke method
        response = _service.create_other_engine(
            description=description,
            engine_details=engine_details,
            engine_display_name=engine_display_name,
            tags=tags,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'external engine description'
        assert req_body['engine_details'] == other_engine_details_model
        assert req_body['engine_display_name'] == 'sampleEngine01'
        assert req_body['tags'] == ['tag1', 'tag2']

    def test_create_other_engine_required_params_with_retries(self):
        # Enable retries and run test_create_other_engine_required_params.
        _service.enable_retries()
        self.test_create_other_engine_required_params()

        # Disable retries and run test_create_other_engine_required_params.
        _service.disable_retries()
        self.test_create_other_engine_required_params()


class TestDeleteOtherEngine:
    """
    Test Class for delete_other_engine
    """

    @responses.activate
    def test_delete_other_engine_all_params(self):
        """
        delete_other_engine()
        """
        # Set up mock
        url = preprocess_url('/other_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_other_engine(
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_other_engine_all_params_with_retries(self):
        # Enable retries and run test_delete_other_engine_all_params.
        _service.enable_retries()
        self.test_delete_other_engine_all_params()

        # Disable retries and run test_delete_other_engine_all_params.
        _service.disable_retries()
        self.test_delete_other_engine_all_params()

    @responses.activate
    def test_delete_other_engine_required_params(self):
        """
        test_delete_other_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/other_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Invoke method
        response = _service.delete_other_engine(
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_other_engine_required_params_with_retries(self):
        # Enable retries and run test_delete_other_engine_required_params.
        _service.enable_retries()
        self.test_delete_other_engine_required_params()

        # Disable retries and run test_delete_other_engine_required_params.
        _service.disable_retries()
        self.test_delete_other_engine_required_params()

    @responses.activate
    def test_delete_other_engine_value_error(self):
        """
        test_delete_other_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/other_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_other_engine(**req_copy)

    def test_delete_other_engine_value_error_with_retries(self):
        # Enable retries and run test_delete_other_engine_value_error.
        _service.enable_retries()
        self.test_delete_other_engine_value_error()

        # Disable retries and run test_delete_other_engine_value_error.
        _service.disable_retries()
        self.test_delete_other_engine_value_error()


class TestListPrestoEngines:
    """
    Test Class for list_presto_engines
    """

    @responses.activate
    def test_list_presto_engines_all_params(self):
        """
        list_presto_engines()
        """
        # Set up mock
        url = preprocess_url('/presto_engines')
        mock_response = '{"presto_engines": [{"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_presto_engines(
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_presto_engines_all_params_with_retries(self):
        # Enable retries and run test_list_presto_engines_all_params.
        _service.enable_retries()
        self.test_list_presto_engines_all_params()

        # Disable retries and run test_list_presto_engines_all_params.
        _service.disable_retries()
        self.test_list_presto_engines_all_params()

    @responses.activate
    def test_list_presto_engines_required_params(self):
        """
        test_list_presto_engines_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines')
        mock_response = '{"presto_engines": [{"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_presto_engines()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_presto_engines_required_params_with_retries(self):
        # Enable retries and run test_list_presto_engines_required_params.
        _service.enable_retries()
        self.test_list_presto_engines_required_params()

        # Disable retries and run test_list_presto_engines_required_params.
        _service.disable_retries()
        self.test_list_presto_engines_required_params()


class TestCreateEngine:
    """
    Test Class for create_engine
    """

    @responses.activate
    def test_create_engine_all_params(self):
        """
        create_engine()
        """
        # Set up mock
        url = preprocess_url('/presto_engines')
        mock_response = '{"engine": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a NodeDescriptionBody model
        node_description_body_model = {}
        node_description_body_model['node_type'] = 'worker'
        node_description_body_model['quantity'] = 38

        # Construct a dict representation of a EngineDetailsBody model
        engine_details_body_model = {}
        engine_details_body_model['api_key'] = '<api_key>'
        engine_details_body_model['connection_string'] = '1.2.3.4'
        engine_details_body_model['coordinator'] = node_description_body_model
        engine_details_body_model['instance_id'] = 'instance_id'
        engine_details_body_model['managed_by'] = 'fully/self'
        engine_details_body_model['size_config'] = 'starter'
        engine_details_body_model['worker'] = node_description_body_model

        # Set up parameter values
        origin = 'native'
        type = 'presto'
        associated_catalogs = ['iceberg_data', 'hive_data']
        description = 'presto engine description'
        engine_details = engine_details_body_model
        engine_display_name = 'sampleEngine'
        first_time_use = True
        region = 'us-south'
        tags = ['tag1', 'tag2']
        version = '1.2.3'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_engine(
            origin,
            type,
            associated_catalogs=associated_catalogs,
            description=description,
            engine_details=engine_details,
            engine_display_name=engine_display_name,
            first_time_use=first_time_use,
            region=region,
            tags=tags,
            version=version,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['origin'] == 'native'
        assert req_body['type'] == 'presto'
        assert req_body['associated_catalogs'] == ['iceberg_data', 'hive_data']
        assert req_body['description'] == 'presto engine description'
        assert req_body['engine_details'] == engine_details_body_model
        assert req_body['engine_display_name'] == 'sampleEngine'
        assert req_body['first_time_use'] == True
        assert req_body['region'] == 'us-south'
        assert req_body['tags'] == ['tag1', 'tag2']
        assert req_body['version'] == '1.2.3'

    def test_create_engine_all_params_with_retries(self):
        # Enable retries and run test_create_engine_all_params.
        _service.enable_retries()
        self.test_create_engine_all_params()

        # Disable retries and run test_create_engine_all_params.
        _service.disable_retries()
        self.test_create_engine_all_params()

    @responses.activate
    def test_create_engine_required_params(self):
        """
        test_create_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines')
        mock_response = '{"engine": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a NodeDescriptionBody model
        node_description_body_model = {}
        node_description_body_model['node_type'] = 'worker'
        node_description_body_model['quantity'] = 38

        # Construct a dict representation of a EngineDetailsBody model
        engine_details_body_model = {}
        engine_details_body_model['api_key'] = '<api_key>'
        engine_details_body_model['connection_string'] = '1.2.3.4'
        engine_details_body_model['coordinator'] = node_description_body_model
        engine_details_body_model['instance_id'] = 'instance_id'
        engine_details_body_model['managed_by'] = 'fully/self'
        engine_details_body_model['size_config'] = 'starter'
        engine_details_body_model['worker'] = node_description_body_model

        # Set up parameter values
        origin = 'native'
        type = 'presto'
        associated_catalogs = ['iceberg_data', 'hive_data']
        description = 'presto engine description'
        engine_details = engine_details_body_model
        engine_display_name = 'sampleEngine'
        first_time_use = True
        region = 'us-south'
        tags = ['tag1', 'tag2']
        version = '1.2.3'

        # Invoke method
        response = _service.create_engine(
            origin,
            type,
            associated_catalogs=associated_catalogs,
            description=description,
            engine_details=engine_details,
            engine_display_name=engine_display_name,
            first_time_use=first_time_use,
            region=region,
            tags=tags,
            version=version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['origin'] == 'native'
        assert req_body['type'] == 'presto'
        assert req_body['associated_catalogs'] == ['iceberg_data', 'hive_data']
        assert req_body['description'] == 'presto engine description'
        assert req_body['engine_details'] == engine_details_body_model
        assert req_body['engine_display_name'] == 'sampleEngine'
        assert req_body['first_time_use'] == True
        assert req_body['region'] == 'us-south'
        assert req_body['tags'] == ['tag1', 'tag2']
        assert req_body['version'] == '1.2.3'

    def test_create_engine_required_params_with_retries(self):
        # Enable retries and run test_create_engine_required_params.
        _service.enable_retries()
        self.test_create_engine_required_params()

        # Disable retries and run test_create_engine_required_params.
        _service.disable_retries()
        self.test_create_engine_required_params()

    @responses.activate
    def test_create_engine_value_error(self):
        """
        test_create_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines')
        mock_response = '{"engine": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a NodeDescriptionBody model
        node_description_body_model = {}
        node_description_body_model['node_type'] = 'worker'
        node_description_body_model['quantity'] = 38

        # Construct a dict representation of a EngineDetailsBody model
        engine_details_body_model = {}
        engine_details_body_model['api_key'] = '<api_key>'
        engine_details_body_model['connection_string'] = '1.2.3.4'
        engine_details_body_model['coordinator'] = node_description_body_model
        engine_details_body_model['instance_id'] = 'instance_id'
        engine_details_body_model['managed_by'] = 'fully/self'
        engine_details_body_model['size_config'] = 'starter'
        engine_details_body_model['worker'] = node_description_body_model

        # Set up parameter values
        origin = 'native'
        type = 'presto'
        associated_catalogs = ['iceberg_data', 'hive_data']
        description = 'presto engine description'
        engine_details = engine_details_body_model
        engine_display_name = 'sampleEngine'
        first_time_use = True
        region = 'us-south'
        tags = ['tag1', 'tag2']
        version = '1.2.3'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "origin": origin,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_engine(**req_copy)

    def test_create_engine_value_error_with_retries(self):
        # Enable retries and run test_create_engine_value_error.
        _service.enable_retries()
        self.test_create_engine_value_error()

        # Disable retries and run test_create_engine_value_error.
        _service.disable_retries()
        self.test_create_engine_value_error()


class TestGetPrestoEngine:
    """
    Test Class for get_presto_engine
    """

    @responses.activate
    def test_get_presto_engine_all_params(self):
        """
        get_presto_engine()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString')
        mock_response = '{"engine": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.get_presto_engine(
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_presto_engine_all_params_with_retries(self):
        # Enable retries and run test_get_presto_engine_all_params.
        _service.enable_retries()
        self.test_get_presto_engine_all_params()

        # Disable retries and run test_get_presto_engine_all_params.
        _service.disable_retries()
        self.test_get_presto_engine_all_params()

    @responses.activate
    def test_get_presto_engine_required_params(self):
        """
        test_get_presto_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString')
        mock_response = '{"engine": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Invoke method
        response = _service.get_presto_engine(
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_presto_engine_required_params_with_retries(self):
        # Enable retries and run test_get_presto_engine_required_params.
        _service.enable_retries()
        self.test_get_presto_engine_required_params()

        # Disable retries and run test_get_presto_engine_required_params.
        _service.disable_retries()
        self.test_get_presto_engine_required_params()

    @responses.activate
    def test_get_presto_engine_value_error(self):
        """
        test_get_presto_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString')
        mock_response = '{"engine": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_presto_engine(**req_copy)

    def test_get_presto_engine_value_error_with_retries(self):
        # Enable retries and run test_get_presto_engine_value_error.
        _service.enable_retries()
        self.test_get_presto_engine_value_error()

        # Disable retries and run test_get_presto_engine_value_error.
        _service.disable_retries()
        self.test_get_presto_engine_value_error()


class TestDeleteEngine:
    """
    Test Class for delete_engine
    """

    @responses.activate
    def test_delete_engine_all_params(self):
        """
        delete_engine()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_engine(
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_engine_all_params_with_retries(self):
        # Enable retries and run test_delete_engine_all_params.
        _service.enable_retries()
        self.test_delete_engine_all_params()

        # Disable retries and run test_delete_engine_all_params.
        _service.disable_retries()
        self.test_delete_engine_all_params()

    @responses.activate
    def test_delete_engine_required_params(self):
        """
        test_delete_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Invoke method
        response = _service.delete_engine(
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_engine_required_params_with_retries(self):
        # Enable retries and run test_delete_engine_required_params.
        _service.enable_retries()
        self.test_delete_engine_required_params()

        # Disable retries and run test_delete_engine_required_params.
        _service.disable_retries()
        self.test_delete_engine_required_params()

    @responses.activate
    def test_delete_engine_value_error(self):
        """
        test_delete_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_engine(**req_copy)

    def test_delete_engine_value_error_with_retries(self):
        # Enable retries and run test_delete_engine_value_error.
        _service.enable_retries()
        self.test_delete_engine_value_error()

        # Disable retries and run test_delete_engine_value_error.
        _service.disable_retries()
        self.test_delete_engine_value_error()


class TestUpdateEngine:
    """
    Test Class for update_engine
    """

    @responses.activate
    def test_update_engine_all_params(self):
        """
        update_engine()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString')
        mock_response = '{"engine": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.update_engine(
            engine_id,
            body,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_engine_all_params_with_retries(self):
        # Enable retries and run test_update_engine_all_params.
        _service.enable_retries()
        self.test_update_engine_all_params()

        # Disable retries and run test_update_engine_all_params.
        _service.disable_retries()
        self.test_update_engine_all_params()

    @responses.activate
    def test_update_engine_required_params(self):
        """
        test_update_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString')
        mock_response = '{"engine": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]

        # Invoke method
        response = _service.update_engine(
            engine_id,
            body,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_engine_required_params_with_retries(self):
        # Enable retries and run test_update_engine_required_params.
        _service.enable_retries()
        self.test_update_engine_required_params()

        # Disable retries and run test_update_engine_required_params.
        _service.disable_retries()
        self.test_update_engine_required_params()

    @responses.activate
    def test_update_engine_value_error(self):
        """
        test_update_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString')
        mock_response = '{"engine": {"actions": ["actions"], "associated_catalogs": ["associated_catalogs"], "build_version": "1.0.3.0.0", "coordinator": {"node_type": "worker", "quantity": 8}, "created_by": "<username>@<domain>.com", "created_on": 10, "description": "presto engine for running sql queries", "engine_details": {"connection_string": "1.2.3.4", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}, "metastore_host": "1.2.3.4"}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "external_host_name": "your-hostname.apps.your-domain.com", "group_id": "new_group_id", "host_name": "ibm-lh-lakehouse-presto-01-presto-svc", "origin": "ibm", "port": 4, "region": "us-south", "size_config": "starter", "status": "running", "status_code": 11, "tags": ["tags"], "type": "presto", "version": "1.2.0", "worker": {"node_type": "worker", "quantity": 8}}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_engine(**req_copy)

    def test_update_engine_value_error_with_retries(self):
        # Enable retries and run test_update_engine_value_error.
        _service.enable_retries()
        self.test_update_engine_value_error()

        # Disable retries and run test_update_engine_value_error.
        _service.disable_retries()
        self.test_update_engine_value_error()


class TestListPrestoEngineCatalogs:
    """
    Test Class for list_presto_engine_catalogs
    """

    @responses.activate
    def test_list_presto_engine_catalogs_all_params(self):
        """
        list_presto_engine_catalogs()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs')
        mock_response = '{"catalogs": [{"catalog_name": "sampleCatalog", "creation_date": "16073847388"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_presto_engine_catalogs(
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_presto_engine_catalogs_all_params_with_retries(self):
        # Enable retries and run test_list_presto_engine_catalogs_all_params.
        _service.enable_retries()
        self.test_list_presto_engine_catalogs_all_params()

        # Disable retries and run test_list_presto_engine_catalogs_all_params.
        _service.disable_retries()
        self.test_list_presto_engine_catalogs_all_params()

    @responses.activate
    def test_list_presto_engine_catalogs_required_params(self):
        """
        test_list_presto_engine_catalogs_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs')
        mock_response = '{"catalogs": [{"catalog_name": "sampleCatalog", "creation_date": "16073847388"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Invoke method
        response = _service.list_presto_engine_catalogs(
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_presto_engine_catalogs_required_params_with_retries(self):
        # Enable retries and run test_list_presto_engine_catalogs_required_params.
        _service.enable_retries()
        self.test_list_presto_engine_catalogs_required_params()

        # Disable retries and run test_list_presto_engine_catalogs_required_params.
        _service.disable_retries()
        self.test_list_presto_engine_catalogs_required_params()

    @responses.activate
    def test_list_presto_engine_catalogs_value_error(self):
        """
        test_list_presto_engine_catalogs_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs')
        mock_response = '{"catalogs": [{"catalog_name": "sampleCatalog", "creation_date": "16073847388"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_presto_engine_catalogs(**req_copy)

    def test_list_presto_engine_catalogs_value_error_with_retries(self):
        # Enable retries and run test_list_presto_engine_catalogs_value_error.
        _service.enable_retries()
        self.test_list_presto_engine_catalogs_value_error()

        # Disable retries and run test_list_presto_engine_catalogs_value_error.
        _service.disable_retries()
        self.test_list_presto_engine_catalogs_value_error()


class TestReplacePrestoEngineCatalogs:
    """
    Test Class for replace_presto_engine_catalogs
    """

    @responses.activate
    def test_replace_presto_engine_catalogs_all_params(self):
        """
        replace_presto_engine_catalogs()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs')
        mock_response = '{"catalogs": [{"catalog_name": "sampleCatalog", "creation_date": "16073847388"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_names = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.replace_presto_engine_catalogs(
            engine_id,
            catalog_names,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_names={}'.format(catalog_names) in query_string

    def test_replace_presto_engine_catalogs_all_params_with_retries(self):
        # Enable retries and run test_replace_presto_engine_catalogs_all_params.
        _service.enable_retries()
        self.test_replace_presto_engine_catalogs_all_params()

        # Disable retries and run test_replace_presto_engine_catalogs_all_params.
        _service.disable_retries()
        self.test_replace_presto_engine_catalogs_all_params()

    @responses.activate
    def test_replace_presto_engine_catalogs_required_params(self):
        """
        test_replace_presto_engine_catalogs_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs')
        mock_response = '{"catalogs": [{"catalog_name": "sampleCatalog", "creation_date": "16073847388"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_names = 'testString'

        # Invoke method
        response = _service.replace_presto_engine_catalogs(
            engine_id,
            catalog_names,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_names={}'.format(catalog_names) in query_string

    def test_replace_presto_engine_catalogs_required_params_with_retries(self):
        # Enable retries and run test_replace_presto_engine_catalogs_required_params.
        _service.enable_retries()
        self.test_replace_presto_engine_catalogs_required_params()

        # Disable retries and run test_replace_presto_engine_catalogs_required_params.
        _service.disable_retries()
        self.test_replace_presto_engine_catalogs_required_params()

    @responses.activate
    def test_replace_presto_engine_catalogs_value_error(self):
        """
        test_replace_presto_engine_catalogs_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs')
        mock_response = '{"catalogs": [{"catalog_name": "sampleCatalog", "creation_date": "16073847388"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_names = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "catalog_names": catalog_names,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_presto_engine_catalogs(**req_copy)

    def test_replace_presto_engine_catalogs_value_error_with_retries(self):
        # Enable retries and run test_replace_presto_engine_catalogs_value_error.
        _service.enable_retries()
        self.test_replace_presto_engine_catalogs_value_error()

        # Disable retries and run test_replace_presto_engine_catalogs_value_error.
        _service.disable_retries()
        self.test_replace_presto_engine_catalogs_value_error()


class TestDeletePrestoEngineCatalogs:
    """
    Test Class for delete_presto_engine_catalogs
    """

    @responses.activate
    def test_delete_presto_engine_catalogs_all_params(self):
        """
        delete_presto_engine_catalogs()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_names = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_presto_engine_catalogs(
            engine_id,
            catalog_names,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_names={}'.format(catalog_names) in query_string

    def test_delete_presto_engine_catalogs_all_params_with_retries(self):
        # Enable retries and run test_delete_presto_engine_catalogs_all_params.
        _service.enable_retries()
        self.test_delete_presto_engine_catalogs_all_params()

        # Disable retries and run test_delete_presto_engine_catalogs_all_params.
        _service.disable_retries()
        self.test_delete_presto_engine_catalogs_all_params()

    @responses.activate
    def test_delete_presto_engine_catalogs_required_params(self):
        """
        test_delete_presto_engine_catalogs_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_names = 'testString'

        # Invoke method
        response = _service.delete_presto_engine_catalogs(
            engine_id,
            catalog_names,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'catalog_names={}'.format(catalog_names) in query_string

    def test_delete_presto_engine_catalogs_required_params_with_retries(self):
        # Enable retries and run test_delete_presto_engine_catalogs_required_params.
        _service.enable_retries()
        self.test_delete_presto_engine_catalogs_required_params()

        # Disable retries and run test_delete_presto_engine_catalogs_required_params.
        _service.disable_retries()
        self.test_delete_presto_engine_catalogs_required_params()

    @responses.activate
    def test_delete_presto_engine_catalogs_value_error(self):
        """
        test_delete_presto_engine_catalogs_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_names = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "catalog_names": catalog_names,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_presto_engine_catalogs(**req_copy)

    def test_delete_presto_engine_catalogs_value_error_with_retries(self):
        # Enable retries and run test_delete_presto_engine_catalogs_value_error.
        _service.enable_retries()
        self.test_delete_presto_engine_catalogs_value_error()

        # Disable retries and run test_delete_presto_engine_catalogs_value_error.
        _service.disable_retries()
        self.test_delete_presto_engine_catalogs_value_error()


class TestGetPrestoEngineCatalog:
    """
    Test Class for get_presto_engine_catalog
    """

    @responses.activate
    def test_get_presto_engine_catalog_all_params(self):
        """
        get_presto_engine_catalog()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs/testString')
        mock_response = '{"catalog": {"actions": ["actions"], "associated_buckets": ["associated_buckets"], "associated_databases": ["associated_databases"], "associated_engines": ["associated_engines"], "catalog_name": "sampleCatalog", "catalog_type": "iceberg", "created_by": "<username>@<domain>.com", "created_on": "1602839833", "description": "Iceberg catalog description", "hostname": "s3a://samplehost.com", "last_sync_at": "1602839833", "managed_by": "ibm", "metastore": "glue", "port": "3232", "status": "running", "sync_description": "Table registration was successful", "sync_exception": ["sync_exception"], "sync_status": "SUCCESS", "tags": ["tags"], "thrift_uri": "thrift://samplehost-catalog:4354"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.get_presto_engine_catalog(
            engine_id,
            catalog_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_presto_engine_catalog_all_params_with_retries(self):
        # Enable retries and run test_get_presto_engine_catalog_all_params.
        _service.enable_retries()
        self.test_get_presto_engine_catalog_all_params()

        # Disable retries and run test_get_presto_engine_catalog_all_params.
        _service.disable_retries()
        self.test_get_presto_engine_catalog_all_params()

    @responses.activate
    def test_get_presto_engine_catalog_required_params(self):
        """
        test_get_presto_engine_catalog_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs/testString')
        mock_response = '{"catalog": {"actions": ["actions"], "associated_buckets": ["associated_buckets"], "associated_databases": ["associated_databases"], "associated_engines": ["associated_engines"], "catalog_name": "sampleCatalog", "catalog_type": "iceberg", "created_by": "<username>@<domain>.com", "created_on": "1602839833", "description": "Iceberg catalog description", "hostname": "s3a://samplehost.com", "last_sync_at": "1602839833", "managed_by": "ibm", "metastore": "glue", "port": "3232", "status": "running", "sync_description": "Table registration was successful", "sync_exception": ["sync_exception"], "sync_status": "SUCCESS", "tags": ["tags"], "thrift_uri": "thrift://samplehost-catalog:4354"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'

        # Invoke method
        response = _service.get_presto_engine_catalog(
            engine_id,
            catalog_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_presto_engine_catalog_required_params_with_retries(self):
        # Enable retries and run test_get_presto_engine_catalog_required_params.
        _service.enable_retries()
        self.test_get_presto_engine_catalog_required_params()

        # Disable retries and run test_get_presto_engine_catalog_required_params.
        _service.disable_retries()
        self.test_get_presto_engine_catalog_required_params()

    @responses.activate
    def test_get_presto_engine_catalog_value_error(self):
        """
        test_get_presto_engine_catalog_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/catalogs/testString')
        mock_response = '{"catalog": {"actions": ["actions"], "associated_buckets": ["associated_buckets"], "associated_databases": ["associated_databases"], "associated_engines": ["associated_engines"], "catalog_name": "sampleCatalog", "catalog_type": "iceberg", "created_by": "<username>@<domain>.com", "created_on": "1602839833", "description": "Iceberg catalog description", "hostname": "s3a://samplehost.com", "last_sync_at": "1602839833", "managed_by": "ibm", "metastore": "glue", "port": "3232", "status": "running", "sync_description": "Table registration was successful", "sync_exception": ["sync_exception"], "sync_status": "SUCCESS", "tags": ["tags"], "thrift_uri": "thrift://samplehost-catalog:4354"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "catalog_id": catalog_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_presto_engine_catalog(**req_copy)

    def test_get_presto_engine_catalog_value_error_with_retries(self):
        # Enable retries and run test_get_presto_engine_catalog_value_error.
        _service.enable_retries()
        self.test_get_presto_engine_catalog_value_error()

        # Disable retries and run test_get_presto_engine_catalog_value_error.
        _service.disable_retries()
        self.test_get_presto_engine_catalog_value_error()


class TestCreateEnginePause:
    """
    Test Class for create_engine_pause
    """

    @responses.activate
    def test_create_engine_pause_all_params(self):
        """
        create_engine_pause()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/pause')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_engine_pause(
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_engine_pause_all_params_with_retries(self):
        # Enable retries and run test_create_engine_pause_all_params.
        _service.enable_retries()
        self.test_create_engine_pause_all_params()

        # Disable retries and run test_create_engine_pause_all_params.
        _service.disable_retries()
        self.test_create_engine_pause_all_params()

    @responses.activate
    def test_create_engine_pause_required_params(self):
        """
        test_create_engine_pause_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/pause')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Invoke method
        response = _service.create_engine_pause(
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_engine_pause_required_params_with_retries(self):
        # Enable retries and run test_create_engine_pause_required_params.
        _service.enable_retries()
        self.test_create_engine_pause_required_params()

        # Disable retries and run test_create_engine_pause_required_params.
        _service.disable_retries()
        self.test_create_engine_pause_required_params()

    @responses.activate
    def test_create_engine_pause_value_error(self):
        """
        test_create_engine_pause_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/pause')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_engine_pause(**req_copy)

    def test_create_engine_pause_value_error_with_retries(self):
        # Enable retries and run test_create_engine_pause_value_error.
        _service.enable_retries()
        self.test_create_engine_pause_value_error()

        # Disable retries and run test_create_engine_pause_value_error.
        _service.disable_retries()
        self.test_create_engine_pause_value_error()


class TestRunExplainStatement:
    """
    Test Class for run_explain_statement
    """

    @responses.activate
    def test_run_explain_statement_all_params(self):
        """
        run_explain_statement()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/query_explain')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "result": "result"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        statement = 'show schemas in catalog_name'
        format = 'json'
        type = 'io'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.run_explain_statement(
            engine_id,
            statement,
            format=format,
            type=type,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['statement'] == 'show schemas in catalog_name'
        assert req_body['format'] == 'json'
        assert req_body['type'] == 'io'

    def test_run_explain_statement_all_params_with_retries(self):
        # Enable retries and run test_run_explain_statement_all_params.
        _service.enable_retries()
        self.test_run_explain_statement_all_params()

        # Disable retries and run test_run_explain_statement_all_params.
        _service.disable_retries()
        self.test_run_explain_statement_all_params()

    @responses.activate
    def test_run_explain_statement_required_params(self):
        """
        test_run_explain_statement_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/query_explain')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "result": "result"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        statement = 'show schemas in catalog_name'
        format = 'json'
        type = 'io'

        # Invoke method
        response = _service.run_explain_statement(
            engine_id,
            statement,
            format=format,
            type=type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['statement'] == 'show schemas in catalog_name'
        assert req_body['format'] == 'json'
        assert req_body['type'] == 'io'

    def test_run_explain_statement_required_params_with_retries(self):
        # Enable retries and run test_run_explain_statement_required_params.
        _service.enable_retries()
        self.test_run_explain_statement_required_params()

        # Disable retries and run test_run_explain_statement_required_params.
        _service.disable_retries()
        self.test_run_explain_statement_required_params()

    @responses.activate
    def test_run_explain_statement_value_error(self):
        """
        test_run_explain_statement_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/query_explain')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "result": "result"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        statement = 'show schemas in catalog_name'
        format = 'json'
        type = 'io'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "statement": statement,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.run_explain_statement(**req_copy)

    def test_run_explain_statement_value_error_with_retries(self):
        # Enable retries and run test_run_explain_statement_value_error.
        _service.enable_retries()
        self.test_run_explain_statement_value_error()

        # Disable retries and run test_run_explain_statement_value_error.
        _service.disable_retries()
        self.test_run_explain_statement_value_error()


class TestRunExplainAnalyzeStatement:
    """
    Test Class for run_explain_analyze_statement
    """

    @responses.activate
    def test_run_explain_analyze_statement_all_params(self):
        """
        run_explain_analyze_statement()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/query_explain_analyze')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "result": "result"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        statement = 'show schemas in catalog_name'
        verbose = True
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.run_explain_analyze_statement(
            engine_id,
            statement,
            verbose=verbose,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['statement'] == 'show schemas in catalog_name'
        assert req_body['verbose'] == True

    def test_run_explain_analyze_statement_all_params_with_retries(self):
        # Enable retries and run test_run_explain_analyze_statement_all_params.
        _service.enable_retries()
        self.test_run_explain_analyze_statement_all_params()

        # Disable retries and run test_run_explain_analyze_statement_all_params.
        _service.disable_retries()
        self.test_run_explain_analyze_statement_all_params()

    @responses.activate
    def test_run_explain_analyze_statement_required_params(self):
        """
        test_run_explain_analyze_statement_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/query_explain_analyze')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "result": "result"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        statement = 'show schemas in catalog_name'
        verbose = True

        # Invoke method
        response = _service.run_explain_analyze_statement(
            engine_id,
            statement,
            verbose=verbose,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['statement'] == 'show schemas in catalog_name'
        assert req_body['verbose'] == True

    def test_run_explain_analyze_statement_required_params_with_retries(self):
        # Enable retries and run test_run_explain_analyze_statement_required_params.
        _service.enable_retries()
        self.test_run_explain_analyze_statement_required_params()

        # Disable retries and run test_run_explain_analyze_statement_required_params.
        _service.disable_retries()
        self.test_run_explain_analyze_statement_required_params()

    @responses.activate
    def test_run_explain_analyze_statement_value_error(self):
        """
        test_run_explain_analyze_statement_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/query_explain_analyze')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "result": "result"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        statement = 'show schemas in catalog_name'
        verbose = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "statement": statement,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.run_explain_analyze_statement(**req_copy)

    def test_run_explain_analyze_statement_value_error_with_retries(self):
        # Enable retries and run test_run_explain_analyze_statement_value_error.
        _service.enable_retries()
        self.test_run_explain_analyze_statement_value_error()

        # Disable retries and run test_run_explain_analyze_statement_value_error.
        _service.disable_retries()
        self.test_run_explain_analyze_statement_value_error()


class TestCreateEngineRestart:
    """
    Test Class for create_engine_restart
    """

    @responses.activate
    def test_create_engine_restart_all_params(self):
        """
        create_engine_restart()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/restart')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_engine_restart(
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_engine_restart_all_params_with_retries(self):
        # Enable retries and run test_create_engine_restart_all_params.
        _service.enable_retries()
        self.test_create_engine_restart_all_params()

        # Disable retries and run test_create_engine_restart_all_params.
        _service.disable_retries()
        self.test_create_engine_restart_all_params()

    @responses.activate
    def test_create_engine_restart_required_params(self):
        """
        test_create_engine_restart_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/restart')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Invoke method
        response = _service.create_engine_restart(
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_engine_restart_required_params_with_retries(self):
        # Enable retries and run test_create_engine_restart_required_params.
        _service.enable_retries()
        self.test_create_engine_restart_required_params()

        # Disable retries and run test_create_engine_restart_required_params.
        _service.disable_retries()
        self.test_create_engine_restart_required_params()

    @responses.activate
    def test_create_engine_restart_value_error(self):
        """
        test_create_engine_restart_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/restart')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_engine_restart(**req_copy)

    def test_create_engine_restart_value_error_with_retries(self):
        # Enable retries and run test_create_engine_restart_value_error.
        _service.enable_retries()
        self.test_create_engine_restart_value_error()

        # Disable retries and run test_create_engine_restart_value_error.
        _service.disable_retries()
        self.test_create_engine_restart_value_error()


class TestCreateEngineResume:
    """
    Test Class for create_engine_resume
    """

    @responses.activate
    def test_create_engine_resume_all_params(self):
        """
        create_engine_resume()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/resume')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_engine_resume(
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_engine_resume_all_params_with_retries(self):
        # Enable retries and run test_create_engine_resume_all_params.
        _service.enable_retries()
        self.test_create_engine_resume_all_params()

        # Disable retries and run test_create_engine_resume_all_params.
        _service.disable_retries()
        self.test_create_engine_resume_all_params()

    @responses.activate
    def test_create_engine_resume_required_params(self):
        """
        test_create_engine_resume_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/resume')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Invoke method
        response = _service.create_engine_resume(
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_engine_resume_required_params_with_retries(self):
        # Enable retries and run test_create_engine_resume_required_params.
        _service.enable_retries()
        self.test_create_engine_resume_required_params()

        # Disable retries and run test_create_engine_resume_required_params.
        _service.disable_retries()
        self.test_create_engine_resume_required_params()

    @responses.activate
    def test_create_engine_resume_value_error(self):
        """
        test_create_engine_resume_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/resume')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_engine_resume(**req_copy)

    def test_create_engine_resume_value_error_with_retries(self):
        # Enable retries and run test_create_engine_resume_value_error.
        _service.enable_retries()
        self.test_create_engine_resume_value_error()

        # Disable retries and run test_create_engine_resume_value_error.
        _service.disable_retries()
        self.test_create_engine_resume_value_error()


class TestCreateEngineScale:
    """
    Test Class for create_engine_scale
    """

    @responses.activate
    def test_create_engine_scale_all_params(self):
        """
        create_engine_scale()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/scale')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a NodeDescription model
        node_description_model = {}
        node_description_model['node_type'] = 'worker'
        node_description_model['quantity'] = 38

        # Set up parameter values
        engine_id = 'testString'
        coordinator = node_description_model
        worker = node_description_model
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_engine_scale(
            engine_id,
            coordinator=coordinator,
            worker=worker,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['coordinator'] == node_description_model
        assert req_body['worker'] == node_description_model

    def test_create_engine_scale_all_params_with_retries(self):
        # Enable retries and run test_create_engine_scale_all_params.
        _service.enable_retries()
        self.test_create_engine_scale_all_params()

        # Disable retries and run test_create_engine_scale_all_params.
        _service.disable_retries()
        self.test_create_engine_scale_all_params()

    @responses.activate
    def test_create_engine_scale_required_params(self):
        """
        test_create_engine_scale_required_params()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/scale')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a NodeDescription model
        node_description_model = {}
        node_description_model['node_type'] = 'worker'
        node_description_model['quantity'] = 38

        # Set up parameter values
        engine_id = 'testString'
        coordinator = node_description_model
        worker = node_description_model

        # Invoke method
        response = _service.create_engine_scale(
            engine_id,
            coordinator=coordinator,
            worker=worker,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['coordinator'] == node_description_model
        assert req_body['worker'] == node_description_model

    def test_create_engine_scale_required_params_with_retries(self):
        # Enable retries and run test_create_engine_scale_required_params.
        _service.enable_retries()
        self.test_create_engine_scale_required_params()

        # Disable retries and run test_create_engine_scale_required_params.
        _service.disable_retries()
        self.test_create_engine_scale_required_params()

    @responses.activate
    def test_create_engine_scale_value_error(self):
        """
        test_create_engine_scale_value_error()
        """
        # Set up mock
        url = preprocess_url('/presto_engines/testString/scale')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a NodeDescription model
        node_description_model = {}
        node_description_model['node_type'] = 'worker'
        node_description_model['quantity'] = 38

        # Set up parameter values
        engine_id = 'testString'
        coordinator = node_description_model
        worker = node_description_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_engine_scale(**req_copy)

    def test_create_engine_scale_value_error_with_retries(self):
        # Enable retries and run test_create_engine_scale_value_error.
        _service.enable_retries()
        self.test_create_engine_scale_value_error()

        # Disable retries and run test_create_engine_scale_value_error.
        _service.disable_retries()
        self.test_create_engine_scale_value_error()


class TestListSparkEngines:
    """
    Test Class for list_spark_engines
    """

    @responses.activate
    def test_list_spark_engines_all_params(self):
        """
        list_spark_engines()
        """
        # Set up mock
        url = preprocess_url('/spark_engines')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "spark_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "spark engine for running sql queries", "engine_details": {"connection_string": "https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "Registered", "tags": ["tags"], "type": "spark"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_spark_engines(
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_spark_engines_all_params_with_retries(self):
        # Enable retries and run test_list_spark_engines_all_params.
        _service.enable_retries()
        self.test_list_spark_engines_all_params()

        # Disable retries and run test_list_spark_engines_all_params.
        _service.disable_retries()
        self.test_list_spark_engines_all_params()

    @responses.activate
    def test_list_spark_engines_required_params(self):
        """
        test_list_spark_engines_required_params()
        """
        # Set up mock
        url = preprocess_url('/spark_engines')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "spark_engines": [{"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "spark engine for running sql queries", "engine_details": {"connection_string": "https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "Registered", "tags": ["tags"], "type": "spark"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_spark_engines()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_spark_engines_required_params_with_retries(self):
        # Enable retries and run test_list_spark_engines_required_params.
        _service.enable_retries()
        self.test_list_spark_engines_required_params()

        # Disable retries and run test_list_spark_engines_required_params.
        _service.disable_retries()
        self.test_list_spark_engines_required_params()


class TestCreateSparkEngine:
    """
    Test Class for create_spark_engine
    """

    @responses.activate
    def test_create_spark_engine_all_params(self):
        """
        create_spark_engine()
        """
        # Set up mock
        url = preprocess_url('/spark_engines')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "spark engine for running sql queries", "engine_details": {"connection_string": "https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "Registered", "tags": ["tags"], "type": "spark"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a SparkEngineDetailsPrototype model
        spark_engine_details_prototype_model = {}
        spark_engine_details_prototype_model['api_key'] = 'apikey'
        spark_engine_details_prototype_model['connection_string'] = '1.2.3.4'
        spark_engine_details_prototype_model['instance_id'] = 'spark-id'
        spark_engine_details_prototype_model['managed_by'] = 'fully/self'

        # Set up parameter values
        origin = 'native'
        type = 'spark'
        description = 'spark engine description'
        engine_details = spark_engine_details_prototype_model
        engine_display_name = 'sampleEngine'
        tags = ['tag1', 'tag2']
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_spark_engine(
            origin,
            type,
            description=description,
            engine_details=engine_details,
            engine_display_name=engine_display_name,
            tags=tags,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['origin'] == 'native'
        assert req_body['type'] == 'spark'
        assert req_body['description'] == 'spark engine description'
        assert req_body['engine_details'] == spark_engine_details_prototype_model
        assert req_body['engine_display_name'] == 'sampleEngine'
        assert req_body['tags'] == ['tag1', 'tag2']

    def test_create_spark_engine_all_params_with_retries(self):
        # Enable retries and run test_create_spark_engine_all_params.
        _service.enable_retries()
        self.test_create_spark_engine_all_params()

        # Disable retries and run test_create_spark_engine_all_params.
        _service.disable_retries()
        self.test_create_spark_engine_all_params()

    @responses.activate
    def test_create_spark_engine_required_params(self):
        """
        test_create_spark_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/spark_engines')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "spark engine for running sql queries", "engine_details": {"connection_string": "https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "Registered", "tags": ["tags"], "type": "spark"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a SparkEngineDetailsPrototype model
        spark_engine_details_prototype_model = {}
        spark_engine_details_prototype_model['api_key'] = 'apikey'
        spark_engine_details_prototype_model['connection_string'] = '1.2.3.4'
        spark_engine_details_prototype_model['instance_id'] = 'spark-id'
        spark_engine_details_prototype_model['managed_by'] = 'fully/self'

        # Set up parameter values
        origin = 'native'
        type = 'spark'
        description = 'spark engine description'
        engine_details = spark_engine_details_prototype_model
        engine_display_name = 'sampleEngine'
        tags = ['tag1', 'tag2']

        # Invoke method
        response = _service.create_spark_engine(
            origin,
            type,
            description=description,
            engine_details=engine_details,
            engine_display_name=engine_display_name,
            tags=tags,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['origin'] == 'native'
        assert req_body['type'] == 'spark'
        assert req_body['description'] == 'spark engine description'
        assert req_body['engine_details'] == spark_engine_details_prototype_model
        assert req_body['engine_display_name'] == 'sampleEngine'
        assert req_body['tags'] == ['tag1', 'tag2']

    def test_create_spark_engine_required_params_with_retries(self):
        # Enable retries and run test_create_spark_engine_required_params.
        _service.enable_retries()
        self.test_create_spark_engine_required_params()

        # Disable retries and run test_create_spark_engine_required_params.
        _service.disable_retries()
        self.test_create_spark_engine_required_params()

    @responses.activate
    def test_create_spark_engine_value_error(self):
        """
        test_create_spark_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/spark_engines')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "spark engine for running sql queries", "engine_details": {"connection_string": "https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "Registered", "tags": ["tags"], "type": "spark"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a SparkEngineDetailsPrototype model
        spark_engine_details_prototype_model = {}
        spark_engine_details_prototype_model['api_key'] = 'apikey'
        spark_engine_details_prototype_model['connection_string'] = '1.2.3.4'
        spark_engine_details_prototype_model['instance_id'] = 'spark-id'
        spark_engine_details_prototype_model['managed_by'] = 'fully/self'

        # Set up parameter values
        origin = 'native'
        type = 'spark'
        description = 'spark engine description'
        engine_details = spark_engine_details_prototype_model
        engine_display_name = 'sampleEngine'
        tags = ['tag1', 'tag2']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "origin": origin,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_spark_engine(**req_copy)

    def test_create_spark_engine_value_error_with_retries(self):
        # Enable retries and run test_create_spark_engine_value_error.
        _service.enable_retries()
        self.test_create_spark_engine_value_error()

        # Disable retries and run test_create_spark_engine_value_error.
        _service.disable_retries()
        self.test_create_spark_engine_value_error()


class TestDeleteSparkEngine:
    """
    Test Class for delete_spark_engine
    """

    @responses.activate
    def test_delete_spark_engine_all_params(self):
        """
        delete_spark_engine()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_spark_engine(
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_spark_engine_all_params_with_retries(self):
        # Enable retries and run test_delete_spark_engine_all_params.
        _service.enable_retries()
        self.test_delete_spark_engine_all_params()

        # Disable retries and run test_delete_spark_engine_all_params.
        _service.disable_retries()
        self.test_delete_spark_engine_all_params()

    @responses.activate
    def test_delete_spark_engine_required_params(self):
        """
        test_delete_spark_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Invoke method
        response = _service.delete_spark_engine(
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_spark_engine_required_params_with_retries(self):
        # Enable retries and run test_delete_spark_engine_required_params.
        _service.enable_retries()
        self.test_delete_spark_engine_required_params()

        # Disable retries and run test_delete_spark_engine_required_params.
        _service.disable_retries()
        self.test_delete_spark_engine_required_params()

    @responses.activate
    def test_delete_spark_engine_value_error(self):
        """
        test_delete_spark_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_spark_engine(**req_copy)

    def test_delete_spark_engine_value_error_with_retries(self):
        # Enable retries and run test_delete_spark_engine_value_error.
        _service.enable_retries()
        self.test_delete_spark_engine_value_error()

        # Disable retries and run test_delete_spark_engine_value_error.
        _service.disable_retries()
        self.test_delete_spark_engine_value_error()


class TestUpdateSparkEngine:
    """
    Test Class for update_spark_engine
    """

    @responses.activate
    def test_update_spark_engine_all_params(self):
        """
        update_spark_engine()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "spark engine for running sql queries", "engine_details": {"connection_string": "https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "Registered", "tags": ["tags"], "type": "spark"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.update_spark_engine(
            engine_id,
            body,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_spark_engine_all_params_with_retries(self):
        # Enable retries and run test_update_spark_engine_all_params.
        _service.enable_retries()
        self.test_update_spark_engine_all_params()

        # Disable retries and run test_update_spark_engine_all_params.
        _service.disable_retries()
        self.test_update_spark_engine_all_params()

    @responses.activate
    def test_update_spark_engine_required_params(self):
        """
        test_update_spark_engine_required_params()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "spark engine for running sql queries", "engine_details": {"connection_string": "https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "Registered", "tags": ["tags"], "type": "spark"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]

        # Invoke method
        response = _service.update_spark_engine(
            engine_id,
            body,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_spark_engine_required_params_with_retries(self):
        # Enable retries and run test_update_spark_engine_required_params.
        _service.enable_retries()
        self.test_update_spark_engine_required_params()

        # Disable retries and run test_update_spark_engine_required_params.
        _service.disable_retries()
        self.test_update_spark_engine_required_params()

    @responses.activate
    def test_update_spark_engine_value_error(self):
        """
        test_update_spark_engine_value_error()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString')
        mock_response = '{"engine": {"actions": ["actions"], "build_version": "1.0.3.0.0", "created_by": "<username>@<domain>.com", "created_on": 10, "description": "spark engine for running sql queries", "engine_details": {"connection_string": "https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>", "endpoints": {"applications_api": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>", "history_server_endpoint": "$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server", "spark_access_endpoint": "$HOST/analytics-engine/details/spark-<instance_id>", "spark_jobs_v4_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications", "spark_kernel_endpoint": "$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels", "view_history_server": "view_history_server", "wxd_application_endpoint": "$HOST/v1/1698311655308796/engines/spark817/applications"}}, "engine_display_name": "sampleEngine", "engine_id": "sampleEngine123", "origin": "ibm", "status": "Registered", "tags": ["tags"], "type": "spark"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        engine_id = 'testString'
        body = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_spark_engine(**req_copy)

    def test_update_spark_engine_value_error_with_retries(self):
        # Enable retries and run test_update_spark_engine_value_error.
        _service.enable_retries()
        self.test_update_spark_engine_value_error()

        # Disable retries and run test_update_spark_engine_value_error.
        _service.disable_retries()
        self.test_update_spark_engine_value_error()


class TestListSparkEngineApplications:
    """
    Test Class for list_spark_engine_applications
    """

    @responses.activate
    def test_list_spark_engine_applications_all_params(self):
        """
        list_spark_engine_applications()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications')
        mock_response = '{"applications": [{"application_id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "auto_termination_time": "2020-12-08T10:00:00.000Z", "creation_time": "2020-12-08T10:00:00.000Z", "end_time": "2020-12-08T10:00:00.000Z", "failed_time": "2020-12-08T10:00:00.000Z", "finish_time": "2020-12-08T10:00:00.000Z", "id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "runtime": {"spark_version": "3.3"}, "spark_application_id": "application_16073847388_0001", "spark_application_name": "spark_application_name", "start_time": "2020-12-08T10:00:00.000Z", "state": "RUNNING", "submission_time": "2023-11-01T11:18:49.758Z", "template_id": "spark-3.3-jaas-v2-cp4d-template"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_spark_engine_applications(
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_spark_engine_applications_all_params_with_retries(self):
        # Enable retries and run test_list_spark_engine_applications_all_params.
        _service.enable_retries()
        self.test_list_spark_engine_applications_all_params()

        # Disable retries and run test_list_spark_engine_applications_all_params.
        _service.disable_retries()
        self.test_list_spark_engine_applications_all_params()

    @responses.activate
    def test_list_spark_engine_applications_required_params(self):
        """
        test_list_spark_engine_applications_required_params()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications')
        mock_response = '{"applications": [{"application_id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "auto_termination_time": "2020-12-08T10:00:00.000Z", "creation_time": "2020-12-08T10:00:00.000Z", "end_time": "2020-12-08T10:00:00.000Z", "failed_time": "2020-12-08T10:00:00.000Z", "finish_time": "2020-12-08T10:00:00.000Z", "id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "runtime": {"spark_version": "3.3"}, "spark_application_id": "application_16073847388_0001", "spark_application_name": "spark_application_name", "start_time": "2020-12-08T10:00:00.000Z", "state": "RUNNING", "submission_time": "2023-11-01T11:18:49.758Z", "template_id": "spark-3.3-jaas-v2-cp4d-template"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Invoke method
        response = _service.list_spark_engine_applications(
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_spark_engine_applications_required_params_with_retries(self):
        # Enable retries and run test_list_spark_engine_applications_required_params.
        _service.enable_retries()
        self.test_list_spark_engine_applications_required_params()

        # Disable retries and run test_list_spark_engine_applications_required_params.
        _service.disable_retries()
        self.test_list_spark_engine_applications_required_params()

    @responses.activate
    def test_list_spark_engine_applications_value_error(self):
        """
        test_list_spark_engine_applications_value_error()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications')
        mock_response = '{"applications": [{"application_id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "auto_termination_time": "2020-12-08T10:00:00.000Z", "creation_time": "2020-12-08T10:00:00.000Z", "end_time": "2020-12-08T10:00:00.000Z", "failed_time": "2020-12-08T10:00:00.000Z", "finish_time": "2020-12-08T10:00:00.000Z", "id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "runtime": {"spark_version": "3.3"}, "spark_application_id": "application_16073847388_0001", "spark_application_name": "spark_application_name", "start_time": "2020-12-08T10:00:00.000Z", "state": "RUNNING", "submission_time": "2023-11-01T11:18:49.758Z", "template_id": "spark-3.3-jaas-v2-cp4d-template"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_spark_engine_applications(**req_copy)

    def test_list_spark_engine_applications_value_error_with_retries(self):
        # Enable retries and run test_list_spark_engine_applications_value_error.
        _service.enable_retries()
        self.test_list_spark_engine_applications_value_error()

        # Disable retries and run test_list_spark_engine_applications_value_error.
        _service.disable_retries()
        self.test_list_spark_engine_applications_value_error()


class TestCreateSparkEngineApplication:
    """
    Test Class for create_spark_engine_application
    """

    @responses.activate
    def test_create_spark_engine_application_all_params(self):
        """
        create_spark_engine_application()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "spark_engine_application": {"application_id": "23c99c14-3af8-467d-9703-cc8163c60d35", "id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "state": "ACCEPTED"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a SparkApplicationDetails model
        spark_application_details_model = {}
        spark_application_details_model['application'] = 's3://mybucket/wordcount.py'
        spark_application_details_model['arguments'] = ['people.txt']
        spark_application_details_model['conf'] = {'key1': 'key:value'}
        spark_application_details_model['env'] = {'key1': 'key:value'}
        spark_application_details_model['name'] = 'SparkApplicaton1'

        # Set up parameter values
        engine_id = 'testString'
        application_details = spark_application_details_model
        job_endpoint = '<host>/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/engine_applications'
        service_instance_id = 'testString'
        type = 'iae'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_spark_engine_application(
            engine_id,
            application_details,
            job_endpoint=job_endpoint,
            service_instance_id=service_instance_id,
            type=type,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['application_details'] == spark_application_details_model
        assert req_body['job_endpoint'] == '<host>/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/engine_applications'
        assert req_body['service_instance_id'] == 'testString'
        assert req_body['type'] == 'iae'

    def test_create_spark_engine_application_all_params_with_retries(self):
        # Enable retries and run test_create_spark_engine_application_all_params.
        _service.enable_retries()
        self.test_create_spark_engine_application_all_params()

        # Disable retries and run test_create_spark_engine_application_all_params.
        _service.disable_retries()
        self.test_create_spark_engine_application_all_params()

    @responses.activate
    def test_create_spark_engine_application_required_params(self):
        """
        test_create_spark_engine_application_required_params()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "spark_engine_application": {"application_id": "23c99c14-3af8-467d-9703-cc8163c60d35", "id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "state": "ACCEPTED"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a SparkApplicationDetails model
        spark_application_details_model = {}
        spark_application_details_model['application'] = 's3://mybucket/wordcount.py'
        spark_application_details_model['arguments'] = ['people.txt']
        spark_application_details_model['conf'] = {'key1': 'key:value'}
        spark_application_details_model['env'] = {'key1': 'key:value'}
        spark_application_details_model['name'] = 'SparkApplicaton1'

        # Set up parameter values
        engine_id = 'testString'
        application_details = spark_application_details_model
        job_endpoint = '<host>/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/engine_applications'
        service_instance_id = 'testString'
        type = 'iae'

        # Invoke method
        response = _service.create_spark_engine_application(
            engine_id,
            application_details,
            job_endpoint=job_endpoint,
            service_instance_id=service_instance_id,
            type=type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['application_details'] == spark_application_details_model
        assert req_body['job_endpoint'] == '<host>/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/engine_applications'
        assert req_body['service_instance_id'] == 'testString'
        assert req_body['type'] == 'iae'

    def test_create_spark_engine_application_required_params_with_retries(self):
        # Enable retries and run test_create_spark_engine_application_required_params.
        _service.enable_retries()
        self.test_create_spark_engine_application_required_params()

        # Disable retries and run test_create_spark_engine_application_required_params.
        _service.disable_retries()
        self.test_create_spark_engine_application_required_params()

    @responses.activate
    def test_create_spark_engine_application_value_error(self):
        """
        test_create_spark_engine_application_value_error()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "spark_engine_application": {"application_id": "23c99c14-3af8-467d-9703-cc8163c60d35", "id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "state": "ACCEPTED"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a SparkApplicationDetails model
        spark_application_details_model = {}
        spark_application_details_model['application'] = 's3://mybucket/wordcount.py'
        spark_application_details_model['arguments'] = ['people.txt']
        spark_application_details_model['conf'] = {'key1': 'key:value'}
        spark_application_details_model['env'] = {'key1': 'key:value'}
        spark_application_details_model['name'] = 'SparkApplicaton1'

        # Set up parameter values
        engine_id = 'testString'
        application_details = spark_application_details_model
        job_endpoint = '<host>/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/engine_applications'
        service_instance_id = 'testString'
        type = 'iae'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "application_details": application_details,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_spark_engine_application(**req_copy)

    def test_create_spark_engine_application_value_error_with_retries(self):
        # Enable retries and run test_create_spark_engine_application_value_error.
        _service.enable_retries()
        self.test_create_spark_engine_application_value_error()

        # Disable retries and run test_create_spark_engine_application_value_error.
        _service.disable_retries()
        self.test_create_spark_engine_application_value_error()


class TestDeleteSparkEngineApplications:
    """
    Test Class for delete_spark_engine_applications
    """

    @responses.activate
    def test_delete_spark_engine_applications_all_params(self):
        """
        delete_spark_engine_applications()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        application_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_spark_engine_applications(
            engine_id,
            application_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'application_id={}'.format(application_id) in query_string

    def test_delete_spark_engine_applications_all_params_with_retries(self):
        # Enable retries and run test_delete_spark_engine_applications_all_params.
        _service.enable_retries()
        self.test_delete_spark_engine_applications_all_params()

        # Disable retries and run test_delete_spark_engine_applications_all_params.
        _service.disable_retries()
        self.test_delete_spark_engine_applications_all_params()

    @responses.activate
    def test_delete_spark_engine_applications_required_params(self):
        """
        test_delete_spark_engine_applications_required_params()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        application_id = 'testString'

        # Invoke method
        response = _service.delete_spark_engine_applications(
            engine_id,
            application_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'application_id={}'.format(application_id) in query_string

    def test_delete_spark_engine_applications_required_params_with_retries(self):
        # Enable retries and run test_delete_spark_engine_applications_required_params.
        _service.enable_retries()
        self.test_delete_spark_engine_applications_required_params()

        # Disable retries and run test_delete_spark_engine_applications_required_params.
        _service.disable_retries()
        self.test_delete_spark_engine_applications_required_params()

    @responses.activate
    def test_delete_spark_engine_applications_value_error(self):
        """
        test_delete_spark_engine_applications_value_error()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        application_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "application_id": application_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_spark_engine_applications(**req_copy)

    def test_delete_spark_engine_applications_value_error_with_retries(self):
        # Enable retries and run test_delete_spark_engine_applications_value_error.
        _service.enable_retries()
        self.test_delete_spark_engine_applications_value_error()

        # Disable retries and run test_delete_spark_engine_applications_value_error.
        _service.disable_retries()
        self.test_delete_spark_engine_applications_value_error()


class TestGetSparkEngineApplicationStatus:
    """
    Test Class for get_spark_engine_application_status
    """

    @responses.activate
    def test_get_spark_engine_application_status_all_params(self):
        """
        get_spark_engine_application_status()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications/testString')
        mock_response = '{"application": {"application_details": {"application": "/opt/ibm/spark/examples/src/main/python/wordcount.py", "arguments": ["arguments"], "conf": {"spark_app_name": "MyJob", "spark_hive_metastore_client_auth_mode": "PLAIN", "spark_hive_metastore_client_plain_password": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...", "spark_hive_metastore_client_plain_username": "ibm_lh_token_admin", "spark_hive_metastore_truststore_password": "changeit", "spark_hive_metastore_truststore_path": "file:///opt/ibm/jdk/lib/security/cacerts", "spark_hive_metastore_truststore_type": "JKS", "spark_hive_metastore_use_ssl": "true", "spark_sql_catalog_implementation": "hive", "spark_sql_catalog_lakehouse": "org.apache.iceberg.spark.SparkCatalog", "spark_sql_catalog_lakehouse_type": "hive", "spark_sql_catalog_lakehouse_uri": "spark_sql_catalog_lakehouse_uri", "spark_sql_extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions", "spark_sql_iceberg_vectorization_enabled": "false"}, "env": {"anyKey": "anyValue"}, "name": "SparkApplication1"}, "application_id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "auto_termination_time": "2020-12-08T10:00:00.000Z", "creation_time": "Saturday 28 October 2023 07:17:06.856+0000", "deploy_mode": "stand-alone", "end_time": "2020-12-08T10:00:00.000Z", "failed_time": "failed_time", "finish_time": "Saturday 28 October 2023 07:17:38.966+0000", "id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "return_code": "0", "spark_application_id": "app-20231028071726-0000", "spark_application_name": "PythonWordCount", "start_time": "Saturday 28 October 2023 07:17:26.649+0000", "state": "FINISHED", "state_details": [{"code": "code", "message": "message", "type": "type"}], "submission_time": "2023-11-01T11:18:49.758Z", "template_id": "spark-3.3-jaas-v2-cp4d-template"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        application_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.get_spark_engine_application_status(
            engine_id,
            application_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_spark_engine_application_status_all_params_with_retries(self):
        # Enable retries and run test_get_spark_engine_application_status_all_params.
        _service.enable_retries()
        self.test_get_spark_engine_application_status_all_params()

        # Disable retries and run test_get_spark_engine_application_status_all_params.
        _service.disable_retries()
        self.test_get_spark_engine_application_status_all_params()

    @responses.activate
    def test_get_spark_engine_application_status_required_params(self):
        """
        test_get_spark_engine_application_status_required_params()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications/testString')
        mock_response = '{"application": {"application_details": {"application": "/opt/ibm/spark/examples/src/main/python/wordcount.py", "arguments": ["arguments"], "conf": {"spark_app_name": "MyJob", "spark_hive_metastore_client_auth_mode": "PLAIN", "spark_hive_metastore_client_plain_password": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...", "spark_hive_metastore_client_plain_username": "ibm_lh_token_admin", "spark_hive_metastore_truststore_password": "changeit", "spark_hive_metastore_truststore_path": "file:///opt/ibm/jdk/lib/security/cacerts", "spark_hive_metastore_truststore_type": "JKS", "spark_hive_metastore_use_ssl": "true", "spark_sql_catalog_implementation": "hive", "spark_sql_catalog_lakehouse": "org.apache.iceberg.spark.SparkCatalog", "spark_sql_catalog_lakehouse_type": "hive", "spark_sql_catalog_lakehouse_uri": "spark_sql_catalog_lakehouse_uri", "spark_sql_extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions", "spark_sql_iceberg_vectorization_enabled": "false"}, "env": {"anyKey": "anyValue"}, "name": "SparkApplication1"}, "application_id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "auto_termination_time": "2020-12-08T10:00:00.000Z", "creation_time": "Saturday 28 October 2023 07:17:06.856+0000", "deploy_mode": "stand-alone", "end_time": "2020-12-08T10:00:00.000Z", "failed_time": "failed_time", "finish_time": "Saturday 28 October 2023 07:17:38.966+0000", "id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "return_code": "0", "spark_application_id": "app-20231028071726-0000", "spark_application_name": "PythonWordCount", "start_time": "Saturday 28 October 2023 07:17:26.649+0000", "state": "FINISHED", "state_details": [{"code": "code", "message": "message", "type": "type"}], "submission_time": "2023-11-01T11:18:49.758Z", "template_id": "spark-3.3-jaas-v2-cp4d-template"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        application_id = 'testString'

        # Invoke method
        response = _service.get_spark_engine_application_status(
            engine_id,
            application_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_spark_engine_application_status_required_params_with_retries(self):
        # Enable retries and run test_get_spark_engine_application_status_required_params.
        _service.enable_retries()
        self.test_get_spark_engine_application_status_required_params()

        # Disable retries and run test_get_spark_engine_application_status_required_params.
        _service.disable_retries()
        self.test_get_spark_engine_application_status_required_params()

    @responses.activate
    def test_get_spark_engine_application_status_value_error(self):
        """
        test_get_spark_engine_application_status_value_error()
        """
        # Set up mock
        url = preprocess_url('/spark_engines/testString/applications/testString')
        mock_response = '{"application": {"application_details": {"application": "/opt/ibm/spark/examples/src/main/python/wordcount.py", "arguments": ["arguments"], "conf": {"spark_app_name": "MyJob", "spark_hive_metastore_client_auth_mode": "PLAIN", "spark_hive_metastore_client_plain_password": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...", "spark_hive_metastore_client_plain_username": "ibm_lh_token_admin", "spark_hive_metastore_truststore_password": "changeit", "spark_hive_metastore_truststore_path": "file:///opt/ibm/jdk/lib/security/cacerts", "spark_hive_metastore_truststore_type": "JKS", "spark_hive_metastore_use_ssl": "true", "spark_sql_catalog_implementation": "hive", "spark_sql_catalog_lakehouse": "org.apache.iceberg.spark.SparkCatalog", "spark_sql_catalog_lakehouse_type": "hive", "spark_sql_catalog_lakehouse_uri": "spark_sql_catalog_lakehouse_uri", "spark_sql_extensions": "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions", "spark_sql_iceberg_vectorization_enabled": "false"}, "env": {"anyKey": "anyValue"}, "name": "SparkApplication1"}, "application_id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "auto_termination_time": "2020-12-08T10:00:00.000Z", "creation_time": "Saturday 28 October 2023 07:17:06.856+0000", "deploy_mode": "stand-alone", "end_time": "2020-12-08T10:00:00.000Z", "failed_time": "failed_time", "finish_time": "Saturday 28 October 2023 07:17:38.966+0000", "id": "cd7cbf1f-8893-4c51-aa3d-d92729f05e99", "return_code": "0", "spark_application_id": "app-20231028071726-0000", "spark_application_name": "PythonWordCount", "start_time": "Saturday 28 October 2023 07:17:26.649+0000", "state": "FINISHED", "state_details": [{"code": "code", "message": "message", "type": "type"}], "submission_time": "2023-11-01T11:18:49.758Z", "template_id": "spark-3.3-jaas-v2-cp4d-template"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        application_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "application_id": application_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_spark_engine_application_status(**req_copy)

    def test_get_spark_engine_application_status_value_error_with_retries(self):
        # Enable retries and run test_get_spark_engine_application_status_value_error.
        _service.enable_retries()
        self.test_get_spark_engine_application_status_value_error()

        # Disable retries and run test_get_spark_engine_application_status_value_error.
        _service.disable_retries()
        self.test_get_spark_engine_application_status_value_error()


# endregion
##############################################################################
# End of Service: Engines
##############################################################################

##############################################################################
# Start of Service: Lhconsole
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = WatsonxDataV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, WatsonxDataV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = WatsonxDataV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestTestLhConsole:
    """
    Test Class for test_lh_console
    """

    @responses.activate
    def test_test_lh_console_all_params(self):
        """
        test_lh_console()
        """
        # Set up mock
        url = preprocess_url('/ready')
        mock_response = '{"message": "Successful message", "message_code": "successfulCode"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.test_lh_console()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_test_lh_console_all_params_with_retries(self):
        # Enable retries and run test_test_lh_console_all_params.
        _service.enable_retries()
        self.test_test_lh_console_all_params()

        # Disable retries and run test_test_lh_console_all_params.
        _service.disable_retries()
        self.test_test_lh_console_all_params()


# endregion
##############################################################################
# End of Service: Lhconsole
##############################################################################

##############################################################################
# Start of Service: Catalogs
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = WatsonxDataV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, WatsonxDataV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = WatsonxDataV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )


class TestListCatalogs:
    """
    Test Class for list_catalogs
    """

    @responses.activate
    def test_list_catalogs_all_params(self):
        """
        list_catalogs()
        """
        # Set up mock
        url = preprocess_url('/catalogs')
        mock_response = '{"catalogs": [{"actions": ["actions"], "associated_buckets": ["associated_buckets"], "associated_databases": ["associated_databases"], "associated_engines": ["associated_engines"], "catalog_name": "sampleCatalog", "catalog_type": "iceberg", "created_by": "<username>@<domain>.com", "created_on": "1602839833", "description": "Iceberg catalog description", "hostname": "s3a://samplehost.com", "last_sync_at": "1602839833", "managed_by": "ibm", "metastore": "glue", "port": "3232", "status": "running", "sync_description": "Table registration was successful", "sync_exception": ["sync_exception"], "sync_status": "SUCCESS", "tags": ["tags"], "thrift_uri": "thrift://samplehost-catalog:4354"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_catalogs(
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_catalogs_all_params_with_retries(self):
        # Enable retries and run test_list_catalogs_all_params.
        _service.enable_retries()
        self.test_list_catalogs_all_params()

        # Disable retries and run test_list_catalogs_all_params.
        _service.disable_retries()
        self.test_list_catalogs_all_params()

    @responses.activate
    def test_list_catalogs_required_params(self):
        """
        test_list_catalogs_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs')
        mock_response = '{"catalogs": [{"actions": ["actions"], "associated_buckets": ["associated_buckets"], "associated_databases": ["associated_databases"], "associated_engines": ["associated_engines"], "catalog_name": "sampleCatalog", "catalog_type": "iceberg", "created_by": "<username>@<domain>.com", "created_on": "1602839833", "description": "Iceberg catalog description", "hostname": "s3a://samplehost.com", "last_sync_at": "1602839833", "managed_by": "ibm", "metastore": "glue", "port": "3232", "status": "running", "sync_description": "Table registration was successful", "sync_exception": ["sync_exception"], "sync_status": "SUCCESS", "tags": ["tags"], "thrift_uri": "thrift://samplehost-catalog:4354"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_catalogs()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_catalogs_required_params_with_retries(self):
        # Enable retries and run test_list_catalogs_required_params.
        _service.enable_retries()
        self.test_list_catalogs_required_params()

        # Disable retries and run test_list_catalogs_required_params.
        _service.disable_retries()
        self.test_list_catalogs_required_params()


class TestGetCatalog:
    """
    Test Class for get_catalog
    """

    @responses.activate
    def test_get_catalog_all_params(self):
        """
        get_catalog()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString')
        mock_response = '{"catalog": {"actions": ["actions"], "associated_buckets": ["associated_buckets"], "associated_databases": ["associated_databases"], "associated_engines": ["associated_engines"], "catalog_name": "sampleCatalog", "catalog_type": "iceberg", "created_by": "<username>@<domain>.com", "created_on": "1602839833", "description": "Iceberg catalog description", "hostname": "s3a://samplehost.com", "last_sync_at": "1602839833", "managed_by": "ibm", "metastore": "glue", "port": "3232", "status": "running", "sync_description": "Table registration was successful", "sync_exception": ["sync_exception"], "sync_status": "SUCCESS", "tags": ["tags"], "thrift_uri": "thrift://samplehost-catalog:4354"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        catalog_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.get_catalog(
            catalog_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_catalog_all_params_with_retries(self):
        # Enable retries and run test_get_catalog_all_params.
        _service.enable_retries()
        self.test_get_catalog_all_params()

        # Disable retries and run test_get_catalog_all_params.
        _service.disable_retries()
        self.test_get_catalog_all_params()

    @responses.activate
    def test_get_catalog_required_params(self):
        """
        test_get_catalog_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString')
        mock_response = '{"catalog": {"actions": ["actions"], "associated_buckets": ["associated_buckets"], "associated_databases": ["associated_databases"], "associated_engines": ["associated_engines"], "catalog_name": "sampleCatalog", "catalog_type": "iceberg", "created_by": "<username>@<domain>.com", "created_on": "1602839833", "description": "Iceberg catalog description", "hostname": "s3a://samplehost.com", "last_sync_at": "1602839833", "managed_by": "ibm", "metastore": "glue", "port": "3232", "status": "running", "sync_description": "Table registration was successful", "sync_exception": ["sync_exception"], "sync_status": "SUCCESS", "tags": ["tags"], "thrift_uri": "thrift://samplehost-catalog:4354"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        catalog_id = 'testString'

        # Invoke method
        response = _service.get_catalog(
            catalog_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_catalog_required_params_with_retries(self):
        # Enable retries and run test_get_catalog_required_params.
        _service.enable_retries()
        self.test_get_catalog_required_params()

        # Disable retries and run test_get_catalog_required_params.
        _service.disable_retries()
        self.test_get_catalog_required_params()

    @responses.activate
    def test_get_catalog_value_error(self):
        """
        test_get_catalog_value_error()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString')
        mock_response = '{"catalog": {"actions": ["actions"], "associated_buckets": ["associated_buckets"], "associated_databases": ["associated_databases"], "associated_engines": ["associated_engines"], "catalog_name": "sampleCatalog", "catalog_type": "iceberg", "created_by": "<username>@<domain>.com", "created_on": "1602839833", "description": "Iceberg catalog description", "hostname": "s3a://samplehost.com", "last_sync_at": "1602839833", "managed_by": "ibm", "metastore": "glue", "port": "3232", "status": "running", "sync_description": "Table registration was successful", "sync_exception": ["sync_exception"], "sync_status": "SUCCESS", "tags": ["tags"], "thrift_uri": "thrift://samplehost-catalog:4354"}, "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        catalog_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_id": catalog_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_catalog(**req_copy)

    def test_get_catalog_value_error_with_retries(self):
        # Enable retries and run test_get_catalog_value_error.
        _service.enable_retries()
        self.test_get_catalog_value_error()

        # Disable retries and run test_get_catalog_value_error.
        _service.disable_retries()
        self.test_get_catalog_value_error()


class TestListSchemas:
    """
    Test Class for list_schemas
    """

    @responses.activate
    def test_list_schemas_all_params(self):
        """
        list_schemas()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "schemas": ["schemas"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_schemas(
            engine_id,
            catalog_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_list_schemas_all_params_with_retries(self):
        # Enable retries and run test_list_schemas_all_params.
        _service.enable_retries()
        self.test_list_schemas_all_params()

        # Disable retries and run test_list_schemas_all_params.
        _service.disable_retries()
        self.test_list_schemas_all_params()

    @responses.activate
    def test_list_schemas_required_params(self):
        """
        test_list_schemas_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "schemas": ["schemas"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'

        # Invoke method
        response = _service.list_schemas(
            engine_id,
            catalog_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_list_schemas_required_params_with_retries(self):
        # Enable retries and run test_list_schemas_required_params.
        _service.enable_retries()
        self.test_list_schemas_required_params()

        # Disable retries and run test_list_schemas_required_params.
        _service.disable_retries()
        self.test_list_schemas_required_params()

    @responses.activate
    def test_list_schemas_value_error(self):
        """
        test_list_schemas_value_error()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "schemas": ["schemas"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "catalog_id": catalog_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_schemas(**req_copy)

    def test_list_schemas_value_error_with_retries(self):
        # Enable retries and run test_list_schemas_value_error.
        _service.enable_retries()
        self.test_list_schemas_value_error()

        # Disable retries and run test_list_schemas_value_error.
        _service.disable_retries()
        self.test_list_schemas_value_error()


class TestCreateSchema:
    """
    Test Class for create_schema
    """

    @responses.activate
    def test_create_schema_all_params(self):
        """
        create_schema()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        custom_path = 'sample-path'
        schema_name = 'SampleSchema1'
        bucket_name = 'sample-bucket'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.create_schema(
            engine_id,
            catalog_id,
            custom_path,
            schema_name,
            bucket_name=bucket_name,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['custom_path'] == 'sample-path'
        assert req_body['schema_name'] == 'SampleSchema1'
        assert req_body['bucket_name'] == 'sample-bucket'

    def test_create_schema_all_params_with_retries(self):
        # Enable retries and run test_create_schema_all_params.
        _service.enable_retries()
        self.test_create_schema_all_params()

        # Disable retries and run test_create_schema_all_params.
        _service.disable_retries()
        self.test_create_schema_all_params()

    @responses.activate
    def test_create_schema_required_params(self):
        """
        test_create_schema_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        custom_path = 'sample-path'
        schema_name = 'SampleSchema1'
        bucket_name = 'sample-bucket'

        # Invoke method
        response = _service.create_schema(
            engine_id,
            catalog_id,
            custom_path,
            schema_name,
            bucket_name=bucket_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['custom_path'] == 'sample-path'
        assert req_body['schema_name'] == 'SampleSchema1'
        assert req_body['bucket_name'] == 'sample-bucket'

    def test_create_schema_required_params_with_retries(self):
        # Enable retries and run test_create_schema_required_params.
        _service.enable_retries()
        self.test_create_schema_required_params()

        # Disable retries and run test_create_schema_required_params.
        _service.disable_retries()
        self.test_create_schema_required_params()

    @responses.activate
    def test_create_schema_value_error(self):
        """
        test_create_schema_value_error()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        custom_path = 'sample-path'
        schema_name = 'SampleSchema1'
        bucket_name = 'sample-bucket'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "catalog_id": catalog_id,
            "custom_path": custom_path,
            "schema_name": schema_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_schema(**req_copy)

    def test_create_schema_value_error_with_retries(self):
        # Enable retries and run test_create_schema_value_error.
        _service.enable_retries()
        self.test_create_schema_value_error()

        # Disable retries and run test_create_schema_value_error.
        _service.disable_retries()
        self.test_create_schema_value_error()


class TestDeleteSchema:
    """
    Test Class for delete_schema
    """

    @responses.activate
    def test_delete_schema_all_params(self):
        """
        delete_schema()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        schema_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_schema(
            engine_id,
            catalog_id,
            schema_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_delete_schema_all_params_with_retries(self):
        # Enable retries and run test_delete_schema_all_params.
        _service.enable_retries()
        self.test_delete_schema_all_params()

        # Disable retries and run test_delete_schema_all_params.
        _service.disable_retries()
        self.test_delete_schema_all_params()

    @responses.activate
    def test_delete_schema_required_params(self):
        """
        test_delete_schema_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        schema_id = 'testString'

        # Invoke method
        response = _service.delete_schema(
            engine_id,
            catalog_id,
            schema_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_delete_schema_required_params_with_retries(self):
        # Enable retries and run test_delete_schema_required_params.
        _service.enable_retries()
        self.test_delete_schema_required_params()

        # Disable retries and run test_delete_schema_required_params.
        _service.disable_retries()
        self.test_delete_schema_required_params()

    @responses.activate
    def test_delete_schema_value_error(self):
        """
        test_delete_schema_value_error()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        schema_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "catalog_id": catalog_id,
            "schema_id": schema_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_schema(**req_copy)

    def test_delete_schema_value_error_with_retries(self):
        # Enable retries and run test_delete_schema_value_error.
        _service.enable_retries()
        self.test_delete_schema_value_error()

        # Disable retries and run test_delete_schema_value_error.
        _service.disable_retries()
        self.test_delete_schema_value_error()


class TestListTables:
    """
    Test Class for list_tables
    """

    @responses.activate
    def test_list_tables_all_params(self):
        """
        list_tables()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "tables": ["tables"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_tables(
            catalog_id,
            schema_id,
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_list_tables_all_params_with_retries(self):
        # Enable retries and run test_list_tables_all_params.
        _service.enable_retries()
        self.test_list_tables_all_params()

        # Disable retries and run test_list_tables_all_params.
        _service.disable_retries()
        self.test_list_tables_all_params()

    @responses.activate
    def test_list_tables_required_params(self):
        """
        test_list_tables_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "tables": ["tables"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        engine_id = 'testString'

        # Invoke method
        response = _service.list_tables(
            catalog_id,
            schema_id,
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_list_tables_required_params_with_retries(self):
        # Enable retries and run test_list_tables_required_params.
        _service.enable_retries()
        self.test_list_tables_required_params()

        # Disable retries and run test_list_tables_required_params.
        _service.disable_retries()
        self.test_list_tables_required_params()

    @responses.activate
    def test_list_tables_value_error(self):
        """
        test_list_tables_value_error()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "tables": ["tables"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_id": catalog_id,
            "schema_id": schema_id,
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_tables(**req_copy)

    def test_list_tables_value_error_with_retries(self):
        # Enable retries and run test_list_tables_value_error.
        _service.enable_retries()
        self.test_list_tables_value_error()

        # Disable retries and run test_list_tables_value_error.
        _service.disable_retries()
        self.test_list_tables_value_error()


class TestGetTable:
    """
    Test Class for get_table
    """

    @responses.activate
    def test_get_table_all_params(self):
        """
        get_table()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString')
        mock_response = '{"columns": [{"column_name": "expenses", "comment": "expenses column", "extra": "varchar", "type": "varchar"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.get_table(
            catalog_id,
            schema_id,
            table_id,
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_get_table_all_params_with_retries(self):
        # Enable retries and run test_get_table_all_params.
        _service.enable_retries()
        self.test_get_table_all_params()

        # Disable retries and run test_get_table_all_params.
        _service.disable_retries()
        self.test_get_table_all_params()

    @responses.activate
    def test_get_table_required_params(self):
        """
        test_get_table_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString')
        mock_response = '{"columns": [{"column_name": "expenses", "comment": "expenses column", "extra": "varchar", "type": "varchar"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        engine_id = 'testString'

        # Invoke method
        response = _service.get_table(
            catalog_id,
            schema_id,
            table_id,
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_get_table_required_params_with_retries(self):
        # Enable retries and run test_get_table_required_params.
        _service.enable_retries()
        self.test_get_table_required_params()

        # Disable retries and run test_get_table_required_params.
        _service.disable_retries()
        self.test_get_table_required_params()

    @responses.activate
    def test_get_table_value_error(self):
        """
        test_get_table_value_error()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString')
        mock_response = '{"columns": [{"column_name": "expenses", "comment": "expenses column", "extra": "varchar", "type": "varchar"}], "response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_id": catalog_id,
            "schema_id": schema_id,
            "table_id": table_id,
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_table(**req_copy)

    def test_get_table_value_error_with_retries(self):
        # Enable retries and run test_get_table_value_error.
        _service.enable_retries()
        self.test_get_table_value_error()

        # Disable retries and run test_get_table_value_error.
        _service.disable_retries()
        self.test_get_table_value_error()


class TestDeleteTable:
    """
    Test Class for delete_table
    """

    @responses.activate
    def test_delete_table_all_params(self):
        """
        delete_table()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        engine_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.delete_table(
            catalog_id,
            schema_id,
            table_id,
            engine_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_delete_table_all_params_with_retries(self):
        # Enable retries and run test_delete_table_all_params.
        _service.enable_retries()
        self.test_delete_table_all_params()

        # Disable retries and run test_delete_table_all_params.
        _service.disable_retries()
        self.test_delete_table_all_params()

    @responses.activate
    def test_delete_table_required_params(self):
        """
        test_delete_table_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        engine_id = 'testString'

        # Invoke method
        response = _service.delete_table(
            catalog_id,
            schema_id,
            table_id,
            engine_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_delete_table_required_params_with_retries(self):
        # Enable retries and run test_delete_table_required_params.
        _service.enable_retries()
        self.test_delete_table_required_params()

        # Disable retries and run test_delete_table_required_params.
        _service.disable_retries()
        self.test_delete_table_required_params()

    @responses.activate
    def test_delete_table_value_error(self):
        """
        test_delete_table_value_error()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        engine_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_id": catalog_id,
            "schema_id": schema_id,
            "table_id": table_id,
            "engine_id": engine_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_table(**req_copy)

    def test_delete_table_value_error_with_retries(self):
        # Enable retries and run test_delete_table_value_error.
        _service.enable_retries()
        self.test_delete_table_value_error()

        # Disable retries and run test_delete_table_value_error.
        _service.disable_retries()
        self.test_delete_table_value_error()


class TestUpdateTable:
    """
    Test Class for update_table
    """

    @responses.activate
    def test_update_table_all_params(self):
        """
        update_table()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        engine_id = 'testString'
        body = [json_patch_operation_model]
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.update_table(
            catalog_id,
            schema_id,
            table_id,
            engine_id,
            body,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_table_all_params_with_retries(self):
        # Enable retries and run test_update_table_all_params.
        _service.enable_retries()
        self.test_update_table_all_params()

        # Disable retries and run test_update_table_all_params.
        _service.disable_retries()
        self.test_update_table_all_params()

    @responses.activate
    def test_update_table_required_params(self):
        """
        test_update_table_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        engine_id = 'testString'
        body = [json_patch_operation_model]

        # Invoke method
        response = _service.update_table(
            catalog_id,
            schema_id,
            table_id,
            engine_id,
            body,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_table_required_params_with_retries(self):
        # Enable retries and run test_update_table_required_params.
        _service.enable_retries()
        self.test_update_table_required_params()

        # Disable retries and run test_update_table_required_params.
        _service.disable_retries()
        self.test_update_table_required_params()

    @responses.activate
    def test_update_table_value_error(self):
        """
        test_update_table_value_error()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        engine_id = 'testString'
        body = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_id": catalog_id,
            "schema_id": schema_id,
            "table_id": table_id,
            "engine_id": engine_id,
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_table(**req_copy)

    def test_update_table_value_error_with_retries(self):
        # Enable retries and run test_update_table_value_error.
        _service.enable_retries()
        self.test_update_table_value_error()

        # Disable retries and run test_update_table_value_error.
        _service.disable_retries()
        self.test_update_table_value_error()


class TestListTableSnapshots:
    """
    Test Class for list_table_snapshots
    """

    @responses.activate
    def test_list_table_snapshots_all_params(self):
        """
        list_table_snapshots()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString/snapshots')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "snapshots": [{"committed_at": "1609379392", "operation": "alter", "snapshot_id": "2332342122211222", "summary": {"anyKey": "anyValue"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.list_table_snapshots(
            engine_id,
            catalog_id,
            schema_id,
            table_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_list_table_snapshots_all_params_with_retries(self):
        # Enable retries and run test_list_table_snapshots_all_params.
        _service.enable_retries()
        self.test_list_table_snapshots_all_params()

        # Disable retries and run test_list_table_snapshots_all_params.
        _service.disable_retries()
        self.test_list_table_snapshots_all_params()

    @responses.activate
    def test_list_table_snapshots_required_params(self):
        """
        test_list_table_snapshots_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString/snapshots')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "snapshots": [{"committed_at": "1609379392", "operation": "alter", "snapshot_id": "2332342122211222", "summary": {"anyKey": "anyValue"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'

        # Invoke method
        response = _service.list_table_snapshots(
            engine_id,
            catalog_id,
            schema_id,
            table_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_list_table_snapshots_required_params_with_retries(self):
        # Enable retries and run test_list_table_snapshots_required_params.
        _service.enable_retries()
        self.test_list_table_snapshots_required_params()

        # Disable retries and run test_list_table_snapshots_required_params.
        _service.disable_retries()
        self.test_list_table_snapshots_required_params()

    @responses.activate
    def test_list_table_snapshots_value_error(self):
        """
        test_list_table_snapshots_value_error()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString/snapshots')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}, "snapshots": [{"committed_at": "1609379392", "operation": "alter", "snapshot_id": "2332342122211222", "summary": {"anyKey": "anyValue"}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "catalog_id": catalog_id,
            "schema_id": schema_id,
            "table_id": table_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_table_snapshots(**req_copy)

    def test_list_table_snapshots_value_error_with_retries(self):
        # Enable retries and run test_list_table_snapshots_value_error.
        _service.enable_retries()
        self.test_list_table_snapshots_value_error()

        # Disable retries and run test_list_table_snapshots_value_error.
        _service.disable_retries()
        self.test_list_table_snapshots_value_error()


class TestReplaceSnapshot:
    """
    Test Class for replace_snapshot
    """

    @responses.activate
    def test_replace_snapshot_all_params(self):
        """
        replace_snapshot()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString/snapshots/testString')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        snapshot_id = 'testString'
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.replace_snapshot(
            engine_id,
            catalog_id,
            schema_id,
            table_id,
            snapshot_id,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_replace_snapshot_all_params_with_retries(self):
        # Enable retries and run test_replace_snapshot_all_params.
        _service.enable_retries()
        self.test_replace_snapshot_all_params()

        # Disable retries and run test_replace_snapshot_all_params.
        _service.disable_retries()
        self.test_replace_snapshot_all_params()

    @responses.activate
    def test_replace_snapshot_required_params(self):
        """
        test_replace_snapshot_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString/snapshots/testString')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        snapshot_id = 'testString'

        # Invoke method
        response = _service.replace_snapshot(
            engine_id,
            catalog_id,
            schema_id,
            table_id,
            snapshot_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'engine_id={}'.format(engine_id) in query_string

    def test_replace_snapshot_required_params_with_retries(self):
        # Enable retries and run test_replace_snapshot_required_params.
        _service.enable_retries()
        self.test_replace_snapshot_required_params()

        # Disable retries and run test_replace_snapshot_required_params.
        _service.disable_retries()
        self.test_replace_snapshot_required_params()

    @responses.activate
    def test_replace_snapshot_value_error(self):
        """
        test_replace_snapshot_value_error()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/schemas/testString/tables/testString/snapshots/testString')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        engine_id = 'testString'
        catalog_id = 'testString'
        schema_id = 'testString'
        table_id = 'testString'
        snapshot_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "engine_id": engine_id,
            "catalog_id": catalog_id,
            "schema_id": schema_id,
            "table_id": table_id,
            "snapshot_id": snapshot_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_snapshot(**req_copy)

    def test_replace_snapshot_value_error_with_retries(self):
        # Enable retries and run test_replace_snapshot_value_error.
        _service.enable_retries()
        self.test_replace_snapshot_value_error()

        # Disable retries and run test_replace_snapshot_value_error.
        _service.disable_retries()
        self.test_replace_snapshot_value_error()


class TestUpdateSyncCatalog:
    """
    Test Class for update_sync_catalog
    """

    @responses.activate
    def test_update_sync_catalog_all_params(self):
        """
        update_sync_catalog()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/sync')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        catalog_id = 'testString'
        body = [json_patch_operation_model]
        auth_instance_id = 'testString'

        # Invoke method
        response = _service.update_sync_catalog(
            catalog_id,
            body,
            auth_instance_id=auth_instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_sync_catalog_all_params_with_retries(self):
        # Enable retries and run test_update_sync_catalog_all_params.
        _service.enable_retries()
        self.test_update_sync_catalog_all_params()

        # Disable retries and run test_update_sync_catalog_all_params.
        _service.disable_retries()
        self.test_update_sync_catalog_all_params()

    @responses.activate
    def test_update_sync_catalog_required_params(self):
        """
        test_update_sync_catalog_required_params()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/sync')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        catalog_id = 'testString'
        body = [json_patch_operation_model]

        # Invoke method
        response = _service.update_sync_catalog(
            catalog_id,
            body,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_update_sync_catalog_required_params_with_retries(self):
        # Enable retries and run test_update_sync_catalog_required_params.
        _service.enable_retries()
        self.test_update_sync_catalog_required_params()

        # Disable retries and run test_update_sync_catalog_required_params.
        _service.disable_retries()
        self.test_update_sync_catalog_required_params()

    @responses.activate
    def test_update_sync_catalog_value_error(self):
        """
        test_update_sync_catalog_value_error()
        """
        # Set up mock
        url = preprocess_url('/catalogs/testString/sync')
        mock_response = '{"response": {"message": "Successful message", "message_code": "successfulCode"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a JsonPatchOperation model
        json_patch_operation_model = {}
        json_patch_operation_model['op'] = 'add'
        json_patch_operation_model['path'] = 'testString'
        json_patch_operation_model['from'] = 'testString'
        json_patch_operation_model['value'] = 'testString'

        # Set up parameter values
        catalog_id = 'testString'
        body = [json_patch_operation_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "catalog_id": catalog_id,
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_sync_catalog(**req_copy)

    def test_update_sync_catalog_value_error_with_retries(self):
        # Enable retries and run test_update_sync_catalog_value_error.
        _service.enable_retries()
        self.test_update_sync_catalog_value_error()

        # Disable retries and run test_update_sync_catalog_value_error.
        _service.disable_retries()
        self.test_update_sync_catalog_value_error()


# endregion
##############################################################################
# End of Service: Catalogs
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_BucketDetails:
    """
    Test Class for BucketDetails
    """

    def test_bucket_details_serialization(self):
        """
        Test serialization/deserialization for BucketDetails
        """

        # Construct a json representation of a BucketDetails model
        bucket_details_model_json = {}
        bucket_details_model_json['access_key'] = '<access_key>'
        bucket_details_model_json['bucket_name'] = 'sample-bucket'
        bucket_details_model_json['endpoint'] = 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        bucket_details_model_json['secret_key'] = 'secret_key'

        # Construct a model instance of BucketDetails by calling from_dict on the json representation
        bucket_details_model = BucketDetails.from_dict(bucket_details_model_json)
        assert bucket_details_model != False

        # Construct a model instance of BucketDetails by calling from_dict on the json representation
        bucket_details_model_dict = BucketDetails.from_dict(bucket_details_model_json).__dict__
        bucket_details_model2 = BucketDetails(**bucket_details_model_dict)

        # Verify the model instances are equivalent
        assert bucket_details_model == bucket_details_model2

        # Convert model instance back to dict and verify no loss of data
        bucket_details_model_json2 = bucket_details_model.to_dict()
        assert bucket_details_model_json2 == bucket_details_model_json


class TestModel_BucketRegistration:
    """
    Test Class for BucketRegistration
    """

    def test_bucket_registration_serialization(self):
        """
        Test serialization/deserialization for BucketRegistration
        """

        # Construct a json representation of a BucketRegistration model
        bucket_registration_model_json = {}
        bucket_registration_model_json['access_key'] = '<access_key>'
        bucket_registration_model_json['actions'] = ['read', 'update']
        bucket_registration_model_json['associated_catalogs'] = ['iceberg_catalog', 'hive_catalog']
        bucket_registration_model_json['bucket_display_name'] = 'sample-bucket-displayname'
        bucket_registration_model_json['bucket_id'] = 'samplebucket123'
        bucket_registration_model_json['bucket_name'] = 'sample-bucket'
        bucket_registration_model_json['bucket_type'] = 'ibm_cos'
        bucket_registration_model_json['created_by'] = '<username>@<domain>.com'
        bucket_registration_model_json['created_on'] = '1686120645'
        bucket_registration_model_json['description'] = 'COS bucket for customer data'
        bucket_registration_model_json['endpoint'] = 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        bucket_registration_model_json['managed_by'] = 'ibm'
        bucket_registration_model_json['region'] = 'us-south'
        bucket_registration_model_json['secret_key'] = 'secret_key'
        bucket_registration_model_json['state'] = 'active'
        bucket_registration_model_json['tags'] = ['testbucket', 'userbucket']

        # Construct a model instance of BucketRegistration by calling from_dict on the json representation
        bucket_registration_model = BucketRegistration.from_dict(bucket_registration_model_json)
        assert bucket_registration_model != False

        # Construct a model instance of BucketRegistration by calling from_dict on the json representation
        bucket_registration_model_dict = BucketRegistration.from_dict(bucket_registration_model_json).__dict__
        bucket_registration_model2 = BucketRegistration(**bucket_registration_model_dict)

        # Verify the model instances are equivalent
        assert bucket_registration_model == bucket_registration_model2

        # Convert model instance back to dict and verify no loss of data
        bucket_registration_model_json2 = bucket_registration_model.to_dict()
        assert bucket_registration_model_json2 == bucket_registration_model_json


class TestModel_BucketStatusResponse:
    """
    Test Class for BucketStatusResponse
    """

    def test_bucket_status_response_serialization(self):
        """
        Test serialization/deserialization for BucketStatusResponse
        """

        # Construct a json representation of a BucketStatusResponse model
        bucket_status_response_model_json = {}
        bucket_status_response_model_json['state'] = True
        bucket_status_response_model_json['state_message'] = 'bucket does not exist or the credentials provided are not valid.'

        # Construct a model instance of BucketStatusResponse by calling from_dict on the json representation
        bucket_status_response_model = BucketStatusResponse.from_dict(bucket_status_response_model_json)
        assert bucket_status_response_model != False

        # Construct a model instance of BucketStatusResponse by calling from_dict on the json representation
        bucket_status_response_model_dict = BucketStatusResponse.from_dict(bucket_status_response_model_json).__dict__
        bucket_status_response_model2 = BucketStatusResponse(**bucket_status_response_model_dict)

        # Verify the model instances are equivalent
        assert bucket_status_response_model == bucket_status_response_model2

        # Convert model instance back to dict and verify no loss of data
        bucket_status_response_model_json2 = bucket_status_response_model.to_dict()
        assert bucket_status_response_model_json2 == bucket_status_response_model_json


class TestModel_Catalog:
    """
    Test Class for Catalog
    """

    def test_catalog_serialization(self):
        """
        Test serialization/deserialization for Catalog
        """

        # Construct a json representation of a Catalog model
        catalog_model_json = {}
        catalog_model_json['catalog_name'] = 'sampleCatalog'
        catalog_model_json['creation_date'] = '16073847388'

        # Construct a model instance of Catalog by calling from_dict on the json representation
        catalog_model = Catalog.from_dict(catalog_model_json)
        assert catalog_model != False

        # Construct a model instance of Catalog by calling from_dict on the json representation
        catalog_model_dict = Catalog.from_dict(catalog_model_json).__dict__
        catalog_model2 = Catalog(**catalog_model_dict)

        # Verify the model instances are equivalent
        assert catalog_model == catalog_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_model_json2 = catalog_model.to_dict()
        assert catalog_model_json2 == catalog_model_json


class TestModel_CatalogDetail:
    """
    Test Class for CatalogDetail
    """

    def test_catalog_detail_serialization(self):
        """
        Test serialization/deserialization for CatalogDetail
        """

        # Construct a json representation of a CatalogDetail model
        catalog_detail_model_json = {}
        catalog_detail_model_json['actions'] = ['update', 'delete']
        catalog_detail_model_json['associated_buckets'] = ['bucket_1', 'bucket_2']
        catalog_detail_model_json['associated_databases'] = ['database_1', 'database_2']
        catalog_detail_model_json['associated_engines'] = ['engine_1', 'engine_2']
        catalog_detail_model_json['catalog_name'] = 'sampleCatalog'
        catalog_detail_model_json['catalog_type'] = 'iceberg'
        catalog_detail_model_json['created_by'] = '<username>@<domain>.com'
        catalog_detail_model_json['created_on'] = '1602839833'
        catalog_detail_model_json['description'] = 'Iceberg catalog description'
        catalog_detail_model_json['hostname'] = 's3a://samplehost.com'
        catalog_detail_model_json['last_sync_at'] = '1602839833'
        catalog_detail_model_json['managed_by'] = 'ibm'
        catalog_detail_model_json['metastore'] = 'glue'
        catalog_detail_model_json['port'] = '3232'
        catalog_detail_model_json['status'] = 'running'
        catalog_detail_model_json['sync_description'] = 'Table registration was successful'
        catalog_detail_model_json['sync_exception'] = ['table is corrupted', 'table metadata not there']
        catalog_detail_model_json['sync_status'] = 'SUCCESS'
        catalog_detail_model_json['tags'] = ['tag1', 'tag2']
        catalog_detail_model_json['thrift_uri'] = 'thrift://samplehost-catalog:4354'

        # Construct a model instance of CatalogDetail by calling from_dict on the json representation
        catalog_detail_model = CatalogDetail.from_dict(catalog_detail_model_json)
        assert catalog_detail_model != False

        # Construct a model instance of CatalogDetail by calling from_dict on the json representation
        catalog_detail_model_dict = CatalogDetail.from_dict(catalog_detail_model_json).__dict__
        catalog_detail_model2 = CatalogDetail(**catalog_detail_model_dict)

        # Verify the model instances are equivalent
        assert catalog_detail_model == catalog_detail_model2

        # Convert model instance back to dict and verify no loss of data
        catalog_detail_model_json2 = catalog_detail_model.to_dict()
        assert catalog_detail_model_json2 == catalog_detail_model_json


class TestModel_Column:
    """
    Test Class for Column
    """

    def test_column_serialization(self):
        """
        Test serialization/deserialization for Column
        """

        # Construct a json representation of a Column model
        column_model_json = {}
        column_model_json['column_name'] = 'expenses'
        column_model_json['comment'] = 'expenses column'
        column_model_json['extra'] = 'varchar'
        column_model_json['type'] = 'varchar'

        # Construct a model instance of Column by calling from_dict on the json representation
        column_model = Column.from_dict(column_model_json)
        assert column_model != False

        # Construct a model instance of Column by calling from_dict on the json representation
        column_model_dict = Column.from_dict(column_model_json).__dict__
        column_model2 = Column(**column_model_dict)

        # Verify the model instances are equivalent
        assert column_model == column_model2

        # Convert model instance back to dict and verify no loss of data
        column_model_json2 = column_model.to_dict()
        assert column_model_json2 == column_model_json


class TestModel_CreateActivateBucketCreatedBody:
    """
    Test Class for CreateActivateBucketCreatedBody
    """

    def test_create_activate_bucket_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateActivateBucketCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Activate bucket'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateActivateBucketCreatedBody model
        create_activate_bucket_created_body_model_json = {}
        create_activate_bucket_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateActivateBucketCreatedBody by calling from_dict on the json representation
        create_activate_bucket_created_body_model = CreateActivateBucketCreatedBody.from_dict(create_activate_bucket_created_body_model_json)
        assert create_activate_bucket_created_body_model != False

        # Construct a model instance of CreateActivateBucketCreatedBody by calling from_dict on the json representation
        create_activate_bucket_created_body_model_dict = CreateActivateBucketCreatedBody.from_dict(create_activate_bucket_created_body_model_json).__dict__
        create_activate_bucket_created_body_model2 = CreateActivateBucketCreatedBody(**create_activate_bucket_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_activate_bucket_created_body_model == create_activate_bucket_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_activate_bucket_created_body_model_json2 = create_activate_bucket_created_body_model.to_dict()
        assert create_activate_bucket_created_body_model_json2 == create_activate_bucket_created_body_model_json


class TestModel_CreateBucketRegistrationCreatedBody:
    """
    Test Class for CreateBucketRegistrationCreatedBody
    """

    def test_create_bucket_registration_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateBucketRegistrationCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bucket_registration_model = {}  # BucketRegistration
        bucket_registration_model['access_key'] = '<access_key>'
        bucket_registration_model['actions'] = ['create', 'update']
        bucket_registration_model['associated_catalogs'] = ['iceberg_catalog', 'hive_catalog']
        bucket_registration_model['bucket_display_name'] = 'samplebucketdisplayname'
        bucket_registration_model['bucket_id'] = 'samplebucketid'
        bucket_registration_model['bucket_name'] = 'samplebucket'
        bucket_registration_model['bucket_type'] = 'minio'
        bucket_registration_model['created_by'] = 'username@domain.com'
        bucket_registration_model['created_on'] = '1699457595'
        bucket_registration_model['description'] = 'default bucket'
        bucket_registration_model['endpoint'] = 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        bucket_registration_model['managed_by'] = 'ibm'
        bucket_registration_model['region'] = 'us-south'
        bucket_registration_model['secret_key'] = 'secret_key'
        bucket_registration_model['state'] = 'active'
        bucket_registration_model['tags'] = ['tag1', 'tag2']

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Register Bucket'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateBucketRegistrationCreatedBody model
        create_bucket_registration_created_body_model_json = {}
        create_bucket_registration_created_body_model_json['bucket_registration'] = bucket_registration_model
        create_bucket_registration_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateBucketRegistrationCreatedBody by calling from_dict on the json representation
        create_bucket_registration_created_body_model = CreateBucketRegistrationCreatedBody.from_dict(create_bucket_registration_created_body_model_json)
        assert create_bucket_registration_created_body_model != False

        # Construct a model instance of CreateBucketRegistrationCreatedBody by calling from_dict on the json representation
        create_bucket_registration_created_body_model_dict = CreateBucketRegistrationCreatedBody.from_dict(create_bucket_registration_created_body_model_json).__dict__
        create_bucket_registration_created_body_model2 = CreateBucketRegistrationCreatedBody(**create_bucket_registration_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_bucket_registration_created_body_model == create_bucket_registration_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_bucket_registration_created_body_model_json2 = create_bucket_registration_created_body_model.to_dict()
        assert create_bucket_registration_created_body_model_json2 == create_bucket_registration_created_body_model_json


class TestModel_CreateDatabaseRegistrationCreatedBody:
    """
    Test Class for CreateDatabaseRegistrationCreatedBody
    """

    def test_create_database_registration_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateDatabaseRegistrationCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        database_registration_database_details_model = {}  # DatabaseRegistrationDatabaseDetails
        database_registration_database_details_model['database_name'] = 'new_database'
        database_registration_database_details_model['hostname'] = 'netezza://abc.efg.com'
        database_registration_database_details_model['password'] = 'samplepassword'
        database_registration_database_details_model['port'] = 4353
        database_registration_database_details_model['sasl'] = True
        database_registration_database_details_model['ssl'] = True
        database_registration_database_details_model['tables'] = 'netezza_table_name'
        database_registration_database_details_model['username'] = 'sampleuser'

        database_registration_model = {}  # DatabaseRegistration
        database_registration_model['actions'] = ['update', 'delete']
        database_registration_model['associated_catalogs'] = ['iceberg_catalog', 'hive_catalog']
        database_registration_model['created_by'] = 'user1@bim.com'
        database_registration_model['created_on'] = '1686792721'
        database_registration_model['database_details'] = database_registration_database_details_model
        database_registration_model['database_display_name'] = 'new_database,'
        database_registration_model['database_id'] = 'new_database_id,'
        database_registration_model['database_properties'] = ['key1', 'key2']
        database_registration_model['database_type'] = 'netezza'
        database_registration_model['description'] = 'Description of the database'
        database_registration_model['tags'] = ['testdatabase', 'userdatabase']

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Create database registration'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateDatabaseRegistrationCreatedBody model
        create_database_registration_created_body_model_json = {}
        create_database_registration_created_body_model_json['database_registration'] = database_registration_model
        create_database_registration_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateDatabaseRegistrationCreatedBody by calling from_dict on the json representation
        create_database_registration_created_body_model = CreateDatabaseRegistrationCreatedBody.from_dict(create_database_registration_created_body_model_json)
        assert create_database_registration_created_body_model != False

        # Construct a model instance of CreateDatabaseRegistrationCreatedBody by calling from_dict on the json representation
        create_database_registration_created_body_model_dict = CreateDatabaseRegistrationCreatedBody.from_dict(create_database_registration_created_body_model_json).__dict__
        create_database_registration_created_body_model2 = CreateDatabaseRegistrationCreatedBody(**create_database_registration_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_database_registration_created_body_model == create_database_registration_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_database_registration_created_body_model_json2 = create_database_registration_created_body_model.to_dict()
        assert create_database_registration_created_body_model_json2 == create_database_registration_created_body_model_json


class TestModel_CreateDb2EngineCreatedBody:
    """
    Test Class for CreateDb2EngineCreatedBody
    """

    def test_create_db2_engine_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateDb2EngineCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        db2_engine_details_model = {}  # Db2EngineDetails
        db2_engine_details_model['connection_string'] = '1.2.3.4'
        db2_engine_details_model['metastore_host'] = '1.2.3.4'

        db2_engine_model = {}  # Db2Engine
        db2_engine_model['actions'] = ['update', 'delete']
        db2_engine_model['build_version'] = '1.0.3.0.0'
        db2_engine_model['created_by'] = '<username>@<domain>.com'
        db2_engine_model['created_on'] = 163788384993
        db2_engine_model['description'] = 'db2 engine for running sql queries'
        db2_engine_model['engine_details'] = db2_engine_details_model
        db2_engine_model['engine_display_name'] = 'sampleEngine'
        db2_engine_model['engine_id'] = 'sampleEngine123'
        db2_engine_model['host_name'] = 'your-hostname.apps.your-domain.com'
        db2_engine_model['origin'] = 'ibm'
        db2_engine_model['port'] = 38
        db2_engine_model['status'] = 'REGISTERED'
        db2_engine_model['tags'] = ['tag1', 'tag2']
        db2_engine_model['type'] = 'db2'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'create engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateDb2EngineCreatedBody model
        create_db2_engine_created_body_model_json = {}
        create_db2_engine_created_body_model_json['engine'] = db2_engine_model
        create_db2_engine_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateDb2EngineCreatedBody by calling from_dict on the json representation
        create_db2_engine_created_body_model = CreateDb2EngineCreatedBody.from_dict(create_db2_engine_created_body_model_json)
        assert create_db2_engine_created_body_model != False

        # Construct a model instance of CreateDb2EngineCreatedBody by calling from_dict on the json representation
        create_db2_engine_created_body_model_dict = CreateDb2EngineCreatedBody.from_dict(create_db2_engine_created_body_model_json).__dict__
        create_db2_engine_created_body_model2 = CreateDb2EngineCreatedBody(**create_db2_engine_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_db2_engine_created_body_model == create_db2_engine_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_db2_engine_created_body_model_json2 = create_db2_engine_created_body_model.to_dict()
        assert create_db2_engine_created_body_model_json2 == create_db2_engine_created_body_model_json


class TestModel_CreateDb2EngineDetails:
    """
    Test Class for CreateDb2EngineDetails
    """

    def test_create_db2_engine_details_serialization(self):
        """
        Test serialization/deserialization for CreateDb2EngineDetails
        """

        # Construct a json representation of a CreateDb2EngineDetails model
        create_db2_engine_details_model_json = {}
        create_db2_engine_details_model_json['connection_string'] = '1.2.3.4'

        # Construct a model instance of CreateDb2EngineDetails by calling from_dict on the json representation
        create_db2_engine_details_model = CreateDb2EngineDetails.from_dict(create_db2_engine_details_model_json)
        assert create_db2_engine_details_model != False

        # Construct a model instance of CreateDb2EngineDetails by calling from_dict on the json representation
        create_db2_engine_details_model_dict = CreateDb2EngineDetails.from_dict(create_db2_engine_details_model_json).__dict__
        create_db2_engine_details_model2 = CreateDb2EngineDetails(**create_db2_engine_details_model_dict)

        # Verify the model instances are equivalent
        assert create_db2_engine_details_model == create_db2_engine_details_model2

        # Convert model instance back to dict and verify no loss of data
        create_db2_engine_details_model_json2 = create_db2_engine_details_model.to_dict()
        assert create_db2_engine_details_model_json2 == create_db2_engine_details_model_json


class TestModel_CreateDriverDatabaseCatalogCreatedBody:
    """
    Test Class for CreateDriverDatabaseCatalogCreatedBody
    """

    def test_create_driver_database_catalog_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateDriverDatabaseCatalogCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        create_driver_database_catalog_created_body_database_model = {}  # CreateDriverDatabaseCatalogCreatedBodyDatabase
        create_driver_database_catalog_created_body_database_model['database_display_name'] = 'sampledb'
        create_driver_database_catalog_created_body_database_model['database_id'] = 'db123'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Register database'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateDriverDatabaseCatalogCreatedBody model
        create_driver_database_catalog_created_body_model_json = {}
        create_driver_database_catalog_created_body_model_json['database'] = create_driver_database_catalog_created_body_database_model
        create_driver_database_catalog_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateDriverDatabaseCatalogCreatedBody by calling from_dict on the json representation
        create_driver_database_catalog_created_body_model = CreateDriverDatabaseCatalogCreatedBody.from_dict(create_driver_database_catalog_created_body_model_json)
        assert create_driver_database_catalog_created_body_model != False

        # Construct a model instance of CreateDriverDatabaseCatalogCreatedBody by calling from_dict on the json representation
        create_driver_database_catalog_created_body_model_dict = CreateDriverDatabaseCatalogCreatedBody.from_dict(create_driver_database_catalog_created_body_model_json).__dict__
        create_driver_database_catalog_created_body_model2 = CreateDriverDatabaseCatalogCreatedBody(**create_driver_database_catalog_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_driver_database_catalog_created_body_model == create_driver_database_catalog_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_driver_database_catalog_created_body_model_json2 = create_driver_database_catalog_created_body_model.to_dict()
        assert create_driver_database_catalog_created_body_model_json2 == create_driver_database_catalog_created_body_model_json


class TestModel_CreateDriverDatabaseCatalogCreatedBodyDatabase:
    """
    Test Class for CreateDriverDatabaseCatalogCreatedBodyDatabase
    """

    def test_create_driver_database_catalog_created_body_database_serialization(self):
        """
        Test serialization/deserialization for CreateDriverDatabaseCatalogCreatedBodyDatabase
        """

        # Construct a json representation of a CreateDriverDatabaseCatalogCreatedBodyDatabase model
        create_driver_database_catalog_created_body_database_model_json = {}
        create_driver_database_catalog_created_body_database_model_json['database_display_name'] = 'testString'
        create_driver_database_catalog_created_body_database_model_json['database_id'] = 'testString'

        # Construct a model instance of CreateDriverDatabaseCatalogCreatedBodyDatabase by calling from_dict on the json representation
        create_driver_database_catalog_created_body_database_model = CreateDriverDatabaseCatalogCreatedBodyDatabase.from_dict(create_driver_database_catalog_created_body_database_model_json)
        assert create_driver_database_catalog_created_body_database_model != False

        # Construct a model instance of CreateDriverDatabaseCatalogCreatedBodyDatabase by calling from_dict on the json representation
        create_driver_database_catalog_created_body_database_model_dict = CreateDriverDatabaseCatalogCreatedBodyDatabase.from_dict(create_driver_database_catalog_created_body_database_model_json).__dict__
        create_driver_database_catalog_created_body_database_model2 = CreateDriverDatabaseCatalogCreatedBodyDatabase(**create_driver_database_catalog_created_body_database_model_dict)

        # Verify the model instances are equivalent
        assert create_driver_database_catalog_created_body_database_model == create_driver_database_catalog_created_body_database_model2

        # Convert model instance back to dict and verify no loss of data
        create_driver_database_catalog_created_body_database_model_json2 = create_driver_database_catalog_created_body_database_model.to_dict()
        assert create_driver_database_catalog_created_body_database_model_json2 == create_driver_database_catalog_created_body_database_model_json


class TestModel_CreateEngineCreatedBody:
    """
    Test Class for CreateEngineCreatedBody
    """

    def test_create_engine_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateEngineCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        node_description_model = {}  # NodeDescription
        node_description_model['node_type'] = 'worker'
        node_description_model['quantity'] = 1

        endpoints_model = {}  # Endpoints
        endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        endpoints_model['view_history_server'] = 'testString'
        endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        engine_details_model = {}  # EngineDetails
        engine_details_model['connection_string'] = '1.2.3.4'
        engine_details_model['endpoints'] = endpoints_model
        engine_details_model['metastore_host'] = '1.2.3.4'

        presto_engine_model = {}  # PrestoEngine
        presto_engine_model['actions'] = ['update', 'delete']
        presto_engine_model['associated_catalogs'] = ['iceberg_data', 'hive_data']
        presto_engine_model['build_version'] = '1.0.3.0.0'
        presto_engine_model['coordinator'] = node_description_model
        presto_engine_model['created_by'] = '<username>@<domain>.com'
        presto_engine_model['created_on'] = 163788384993
        presto_engine_model['description'] = 'presto engine for running sql queries'
        presto_engine_model['engine_details'] = engine_details_model
        presto_engine_model['engine_display_name'] = 'sampleEngine'
        presto_engine_model['engine_id'] = 'sampleEngine123'
        presto_engine_model['external_host_name'] = 'your-hostname.apps.your-domain.com'
        presto_engine_model['group_id'] = 'new_group_id'
        presto_engine_model['host_name'] = 'your-hostname.apps.your-domain.com'
        presto_engine_model['origin'] = 'ibm'
        presto_engine_model['port'] = 38
        presto_engine_model['region'] = 'us-south'
        presto_engine_model['size_config'] = 'starter'
        presto_engine_model['status'] = 'running'
        presto_engine_model['status_code'] = 0
        presto_engine_model['tags'] = ['tag1', 'tag2']
        presto_engine_model['type'] = 'presto'
        presto_engine_model['version'] = '1.2.0'
        presto_engine_model['worker'] = node_description_model

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'create engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateEngineCreatedBody model
        create_engine_created_body_model_json = {}
        create_engine_created_body_model_json['engine'] = presto_engine_model
        create_engine_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateEngineCreatedBody by calling from_dict on the json representation
        create_engine_created_body_model = CreateEngineCreatedBody.from_dict(create_engine_created_body_model_json)
        assert create_engine_created_body_model != False

        # Construct a model instance of CreateEngineCreatedBody by calling from_dict on the json representation
        create_engine_created_body_model_dict = CreateEngineCreatedBody.from_dict(create_engine_created_body_model_json).__dict__
        create_engine_created_body_model2 = CreateEngineCreatedBody(**create_engine_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_engine_created_body_model == create_engine_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_engine_created_body_model_json2 = create_engine_created_body_model.to_dict()
        assert create_engine_created_body_model_json2 == create_engine_created_body_model_json


class TestModel_CreateEnginePauseCreatedBody:
    """
    Test Class for CreateEnginePauseCreatedBody
    """

    def test_create_engine_pause_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateEnginePauseCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'pause presto engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateEnginePauseCreatedBody model
        create_engine_pause_created_body_model_json = {}
        create_engine_pause_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateEnginePauseCreatedBody by calling from_dict on the json representation
        create_engine_pause_created_body_model = CreateEnginePauseCreatedBody.from_dict(create_engine_pause_created_body_model_json)
        assert create_engine_pause_created_body_model != False

        # Construct a model instance of CreateEnginePauseCreatedBody by calling from_dict on the json representation
        create_engine_pause_created_body_model_dict = CreateEnginePauseCreatedBody.from_dict(create_engine_pause_created_body_model_json).__dict__
        create_engine_pause_created_body_model2 = CreateEnginePauseCreatedBody(**create_engine_pause_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_engine_pause_created_body_model == create_engine_pause_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_engine_pause_created_body_model_json2 = create_engine_pause_created_body_model.to_dict()
        assert create_engine_pause_created_body_model_json2 == create_engine_pause_created_body_model_json


class TestModel_CreateEngineRestartCreatedBody:
    """
    Test Class for CreateEngineRestartCreatedBody
    """

    def test_create_engine_restart_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateEngineRestartCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Restart presto engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateEngineRestartCreatedBody model
        create_engine_restart_created_body_model_json = {}
        create_engine_restart_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateEngineRestartCreatedBody by calling from_dict on the json representation
        create_engine_restart_created_body_model = CreateEngineRestartCreatedBody.from_dict(create_engine_restart_created_body_model_json)
        assert create_engine_restart_created_body_model != False

        # Construct a model instance of CreateEngineRestartCreatedBody by calling from_dict on the json representation
        create_engine_restart_created_body_model_dict = CreateEngineRestartCreatedBody.from_dict(create_engine_restart_created_body_model_json).__dict__
        create_engine_restart_created_body_model2 = CreateEngineRestartCreatedBody(**create_engine_restart_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_engine_restart_created_body_model == create_engine_restart_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_engine_restart_created_body_model_json2 = create_engine_restart_created_body_model.to_dict()
        assert create_engine_restart_created_body_model_json2 == create_engine_restart_created_body_model_json


class TestModel_CreateEngineResumeCreatedBody:
    """
    Test Class for CreateEngineResumeCreatedBody
    """

    def test_create_engine_resume_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateEngineResumeCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'resume presto engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateEngineResumeCreatedBody model
        create_engine_resume_created_body_model_json = {}
        create_engine_resume_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateEngineResumeCreatedBody by calling from_dict on the json representation
        create_engine_resume_created_body_model = CreateEngineResumeCreatedBody.from_dict(create_engine_resume_created_body_model_json)
        assert create_engine_resume_created_body_model != False

        # Construct a model instance of CreateEngineResumeCreatedBody by calling from_dict on the json representation
        create_engine_resume_created_body_model_dict = CreateEngineResumeCreatedBody.from_dict(create_engine_resume_created_body_model_json).__dict__
        create_engine_resume_created_body_model2 = CreateEngineResumeCreatedBody(**create_engine_resume_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_engine_resume_created_body_model == create_engine_resume_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_engine_resume_created_body_model_json2 = create_engine_resume_created_body_model.to_dict()
        assert create_engine_resume_created_body_model_json2 == create_engine_resume_created_body_model_json


class TestModel_CreateEngineScaleCreatedBody:
    """
    Test Class for CreateEngineScaleCreatedBody
    """

    def test_create_engine_scale_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateEngineScaleCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'scale presto engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateEngineScaleCreatedBody model
        create_engine_scale_created_body_model_json = {}
        create_engine_scale_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateEngineScaleCreatedBody by calling from_dict on the json representation
        create_engine_scale_created_body_model = CreateEngineScaleCreatedBody.from_dict(create_engine_scale_created_body_model_json)
        assert create_engine_scale_created_body_model != False

        # Construct a model instance of CreateEngineScaleCreatedBody by calling from_dict on the json representation
        create_engine_scale_created_body_model_dict = CreateEngineScaleCreatedBody.from_dict(create_engine_scale_created_body_model_json).__dict__
        create_engine_scale_created_body_model2 = CreateEngineScaleCreatedBody(**create_engine_scale_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_engine_scale_created_body_model == create_engine_scale_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_engine_scale_created_body_model_json2 = create_engine_scale_created_body_model.to_dict()
        assert create_engine_scale_created_body_model_json2 == create_engine_scale_created_body_model_json


class TestModel_CreateNetezzaEngineCreatedBody:
    """
    Test Class for CreateNetezzaEngineCreatedBody
    """

    def test_create_netezza_engine_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateNetezzaEngineCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        netezza_engine_details_model = {}  # NetezzaEngineDetails
        netezza_engine_details_model['connection_string'] = '1.2.3.4'
        netezza_engine_details_model['metastore_host'] = '1.2.3.4'

        netezza_engine_model = {}  # NetezzaEngine
        netezza_engine_model['actions'] = ['update', 'delete']
        netezza_engine_model['build_version'] = '1.0.3.0.0'
        netezza_engine_model['created_by'] = '<username>@<domain>.com'
        netezza_engine_model['created_on'] = 163788384993
        netezza_engine_model['description'] = 'netezza engine for running sql queries'
        netezza_engine_model['engine_details'] = netezza_engine_details_model
        netezza_engine_model['engine_display_name'] = 'sampleEngine'
        netezza_engine_model['engine_id'] = 'sampleEngine123'
        netezza_engine_model['host_name'] = 'your-hostname.apps.your-domain.com'
        netezza_engine_model['origin'] = 'ibm'
        netezza_engine_model['port'] = 38
        netezza_engine_model['status'] = 'REGISTERED'
        netezza_engine_model['tags'] = ['tag1', 'tag2']
        netezza_engine_model['type'] = 'netezza'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'create engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateNetezzaEngineCreatedBody model
        create_netezza_engine_created_body_model_json = {}
        create_netezza_engine_created_body_model_json['engine'] = netezza_engine_model
        create_netezza_engine_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateNetezzaEngineCreatedBody by calling from_dict on the json representation
        create_netezza_engine_created_body_model = CreateNetezzaEngineCreatedBody.from_dict(create_netezza_engine_created_body_model_json)
        assert create_netezza_engine_created_body_model != False

        # Construct a model instance of CreateNetezzaEngineCreatedBody by calling from_dict on the json representation
        create_netezza_engine_created_body_model_dict = CreateNetezzaEngineCreatedBody.from_dict(create_netezza_engine_created_body_model_json).__dict__
        create_netezza_engine_created_body_model2 = CreateNetezzaEngineCreatedBody(**create_netezza_engine_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_netezza_engine_created_body_model == create_netezza_engine_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_netezza_engine_created_body_model_json2 = create_netezza_engine_created_body_model.to_dict()
        assert create_netezza_engine_created_body_model_json2 == create_netezza_engine_created_body_model_json


class TestModel_CreateNetezzaEngineDetails:
    """
    Test Class for CreateNetezzaEngineDetails
    """

    def test_create_netezza_engine_details_serialization(self):
        """
        Test serialization/deserialization for CreateNetezzaEngineDetails
        """

        # Construct a json representation of a CreateNetezzaEngineDetails model
        create_netezza_engine_details_model_json = {}
        create_netezza_engine_details_model_json['connection_string'] = '1.2.3.4'

        # Construct a model instance of CreateNetezzaEngineDetails by calling from_dict on the json representation
        create_netezza_engine_details_model = CreateNetezzaEngineDetails.from_dict(create_netezza_engine_details_model_json)
        assert create_netezza_engine_details_model != False

        # Construct a model instance of CreateNetezzaEngineDetails by calling from_dict on the json representation
        create_netezza_engine_details_model_dict = CreateNetezzaEngineDetails.from_dict(create_netezza_engine_details_model_json).__dict__
        create_netezza_engine_details_model2 = CreateNetezzaEngineDetails(**create_netezza_engine_details_model_dict)

        # Verify the model instances are equivalent
        assert create_netezza_engine_details_model == create_netezza_engine_details_model2

        # Convert model instance back to dict and verify no loss of data
        create_netezza_engine_details_model_json2 = create_netezza_engine_details_model.to_dict()
        assert create_netezza_engine_details_model_json2 == create_netezza_engine_details_model_json


class TestModel_CreateOtherEngineCreatedBody:
    """
    Test Class for CreateOtherEngineCreatedBody
    """

    def test_create_other_engine_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateOtherEngineCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        other_engine_details_model = {}  # OtherEngineDetails
        other_engine_details_model['connection_string'] = '1.2.3.4'
        other_engine_details_model['engine_type'] = 'netezza'
        other_engine_details_model['metastore_host'] = '1.2.3.4'

        other_engine_model = {}  # OtherEngine
        other_engine_model['created_by'] = '<username>@<domain>.com'
        other_engine_model['created_on'] = 163788384993
        other_engine_model['description'] = 'other engine for running sql queries'
        other_engine_model['engine_details'] = other_engine_details_model
        other_engine_model['engine_display_name'] = 'sampleEngine'
        other_engine_model['engine_id'] = 'sampleEngine123'
        other_engine_model['origin'] = 'external'
        other_engine_model['status'] = 'registered'
        other_engine_model['status_code'] = 38
        other_engine_model['tags'] = ['tag1', 'tag2']
        other_engine_model['type'] = 'other'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'create engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateOtherEngineCreatedBody model
        create_other_engine_created_body_model_json = {}
        create_other_engine_created_body_model_json['engine'] = other_engine_model
        create_other_engine_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateOtherEngineCreatedBody by calling from_dict on the json representation
        create_other_engine_created_body_model = CreateOtherEngineCreatedBody.from_dict(create_other_engine_created_body_model_json)
        assert create_other_engine_created_body_model != False

        # Construct a model instance of CreateOtherEngineCreatedBody by calling from_dict on the json representation
        create_other_engine_created_body_model_dict = CreateOtherEngineCreatedBody.from_dict(create_other_engine_created_body_model_json).__dict__
        create_other_engine_created_body_model2 = CreateOtherEngineCreatedBody(**create_other_engine_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_other_engine_created_body_model == create_other_engine_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_other_engine_created_body_model_json2 = create_other_engine_created_body_model.to_dict()
        assert create_other_engine_created_body_model_json2 == create_other_engine_created_body_model_json


class TestModel_CreateSchemaCreatedBody:
    """
    Test Class for CreateSchemaCreatedBody
    """

    def test_create_schema_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateSchemaCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'create schema'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateSchemaCreatedBody model
        create_schema_created_body_model_json = {}
        create_schema_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateSchemaCreatedBody by calling from_dict on the json representation
        create_schema_created_body_model = CreateSchemaCreatedBody.from_dict(create_schema_created_body_model_json)
        assert create_schema_created_body_model != False

        # Construct a model instance of CreateSchemaCreatedBody by calling from_dict on the json representation
        create_schema_created_body_model_dict = CreateSchemaCreatedBody.from_dict(create_schema_created_body_model_json).__dict__
        create_schema_created_body_model2 = CreateSchemaCreatedBody(**create_schema_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_schema_created_body_model == create_schema_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_schema_created_body_model_json2 = create_schema_created_body_model.to_dict()
        assert create_schema_created_body_model_json2 == create_schema_created_body_model_json


class TestModel_CreateSparkEngineApplicationCreatedBody:
    """
    Test Class for CreateSparkEngineApplicationCreatedBody
    """

    def test_create_spark_engine_application_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateSparkEngineApplicationCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Spark application created successfully'
        success_response_model['message_code'] = 'success'

        spark_engine_application_model = {}  # SparkEngineApplication
        spark_engine_application_model['application_id'] = '<application_id>'
        spark_engine_application_model['id'] = 'cd7cbf1f-8893-4c51-aa3d-d92729f05e99'
        spark_engine_application_model['state'] = 'accepted'

        # Construct a json representation of a CreateSparkEngineApplicationCreatedBody model
        create_spark_engine_application_created_body_model_json = {}
        create_spark_engine_application_created_body_model_json['response'] = success_response_model
        create_spark_engine_application_created_body_model_json['spark_engine_application'] = spark_engine_application_model

        # Construct a model instance of CreateSparkEngineApplicationCreatedBody by calling from_dict on the json representation
        create_spark_engine_application_created_body_model = CreateSparkEngineApplicationCreatedBody.from_dict(create_spark_engine_application_created_body_model_json)
        assert create_spark_engine_application_created_body_model != False

        # Construct a model instance of CreateSparkEngineApplicationCreatedBody by calling from_dict on the json representation
        create_spark_engine_application_created_body_model_dict = CreateSparkEngineApplicationCreatedBody.from_dict(create_spark_engine_application_created_body_model_json).__dict__
        create_spark_engine_application_created_body_model2 = CreateSparkEngineApplicationCreatedBody(**create_spark_engine_application_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_spark_engine_application_created_body_model == create_spark_engine_application_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_spark_engine_application_created_body_model_json2 = create_spark_engine_application_created_body_model.to_dict()
        assert create_spark_engine_application_created_body_model_json2 == create_spark_engine_application_created_body_model_json


class TestModel_CreateSparkEngineCreatedBody:
    """
    Test Class for CreateSparkEngineCreatedBody
    """

    def test_create_spark_engine_created_body_serialization(self):
        """
        Test serialization/deserialization for CreateSparkEngineCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        spark_engine_details_endpoints_model = {}  # SparkEngineDetailsEndpoints
        spark_engine_details_endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/<spark_id>/spark_applications/<application_id>'
        spark_engine_details_endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/<spark_id>/spark_history_server'
        spark_engine_details_endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        spark_engine_details_endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/<spark_id>/spark_applications'
        spark_engine_details_endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/<spark_id>/jkg/api/kernels'
        spark_engine_details_endpoints_model['view_history_server'] = 'View history server'
        spark_engine_details_endpoints_model['wxd_application_endpoint'] = '$HOST/v1/<wxd_instance_id>/engines/<engine_id>/applications'

        spark_engine_details_model = {}  # SparkEngineDetails
        spark_engine_details_model['connection_string'] = 'https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>'
        spark_engine_details_model['endpoints'] = spark_engine_details_endpoints_model

        spark_engine_model = {}  # SparkEngine
        spark_engine_model['actions'] = ['update', 'delete']
        spark_engine_model['build_version'] = '1.0.3.0.0'
        spark_engine_model['created_by'] = '<username>@<domain>.com'
        spark_engine_model['created_on'] = 163788384993
        spark_engine_model['description'] = 'Spark engines for running spark applications'
        spark_engine_model['engine_details'] = spark_engine_details_model
        spark_engine_model['engine_display_name'] = 'sampleEngine'
        spark_engine_model['engine_id'] = 'sampleEngine123'
        spark_engine_model['origin'] = 'discover'
        spark_engine_model['status'] = 'REGISTERED'
        spark_engine_model['tags'] = ['tag1', 'tag2']
        spark_engine_model['type'] = 'spark'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Spark engines list'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a CreateSparkEngineCreatedBody model
        create_spark_engine_created_body_model_json = {}
        create_spark_engine_created_body_model_json['engine'] = spark_engine_model
        create_spark_engine_created_body_model_json['response'] = success_response_model

        # Construct a model instance of CreateSparkEngineCreatedBody by calling from_dict on the json representation
        create_spark_engine_created_body_model = CreateSparkEngineCreatedBody.from_dict(create_spark_engine_created_body_model_json)
        assert create_spark_engine_created_body_model != False

        # Construct a model instance of CreateSparkEngineCreatedBody by calling from_dict on the json representation
        create_spark_engine_created_body_model_dict = CreateSparkEngineCreatedBody.from_dict(create_spark_engine_created_body_model_json).__dict__
        create_spark_engine_created_body_model2 = CreateSparkEngineCreatedBody(**create_spark_engine_created_body_model_dict)

        # Verify the model instances are equivalent
        assert create_spark_engine_created_body_model == create_spark_engine_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        create_spark_engine_created_body_model_json2 = create_spark_engine_created_body_model.to_dict()
        assert create_spark_engine_created_body_model_json2 == create_spark_engine_created_body_model_json


class TestModel_DatabaseRegistration:
    """
    Test Class for DatabaseRegistration
    """

    def test_database_registration_serialization(self):
        """
        Test serialization/deserialization for DatabaseRegistration
        """

        # Construct dict forms of any model objects needed in order to build this model.

        database_registration_database_details_model = {}  # DatabaseRegistrationDatabaseDetails
        database_registration_database_details_model['database_name'] = 'new_database'
        database_registration_database_details_model['hostname'] = 'netezza://ps.fyre.com'
        database_registration_database_details_model['password'] = 'samplepassword'
        database_registration_database_details_model['port'] = 4543
        database_registration_database_details_model['sasl'] = True
        database_registration_database_details_model['ssl'] = True
        database_registration_database_details_model['tables'] = 'kafka_table_name'
        database_registration_database_details_model['username'] = 'sampleuser'

        # Construct a json representation of a DatabaseRegistration model
        database_registration_model_json = {}
        database_registration_model_json['actions'] = ['update', 'delete']
        database_registration_model_json['associated_catalogs'] = ['iceberg_catalog', 'hive_catalog']
        database_registration_model_json['created_by'] = 'user1@bim.com'
        database_registration_model_json['created_on'] = '1686792721'
        database_registration_model_json['database_details'] = database_registration_database_details_model
        database_registration_model_json['database_display_name'] = 'new_database'
        database_registration_model_json['database_id'] = 'new_database_id'
        database_registration_model_json['database_properties'] = ['key1', 'key2']
        database_registration_model_json['database_type'] = 'netezza'
        database_registration_model_json['description'] = 'Description of the external Database'
        database_registration_model_json['tags'] = ['testdatabase', 'userdatabase']

        # Construct a model instance of DatabaseRegistration by calling from_dict on the json representation
        database_registration_model = DatabaseRegistration.from_dict(database_registration_model_json)
        assert database_registration_model != False

        # Construct a model instance of DatabaseRegistration by calling from_dict on the json representation
        database_registration_model_dict = DatabaseRegistration.from_dict(database_registration_model_json).__dict__
        database_registration_model2 = DatabaseRegistration(**database_registration_model_dict)

        # Verify the model instances are equivalent
        assert database_registration_model == database_registration_model2

        # Convert model instance back to dict and verify no loss of data
        database_registration_model_json2 = database_registration_model.to_dict()
        assert database_registration_model_json2 == database_registration_model_json


class TestModel_DatabaseRegistrationDatabaseDetails:
    """
    Test Class for DatabaseRegistrationDatabaseDetails
    """

    def test_database_registration_database_details_serialization(self):
        """
        Test serialization/deserialization for DatabaseRegistrationDatabaseDetails
        """

        # Construct a json representation of a DatabaseRegistrationDatabaseDetails model
        database_registration_database_details_model_json = {}
        database_registration_database_details_model_json['database_name'] = 'new_database'
        database_registration_database_details_model_json['hostname'] = 'netezza://ps.fyre.com'
        database_registration_database_details_model_json['password'] = 'samplepassword'
        database_registration_database_details_model_json['port'] = 4543
        database_registration_database_details_model_json['sasl'] = True
        database_registration_database_details_model_json['ssl'] = True
        database_registration_database_details_model_json['tables'] = 'kafka_table_name'
        database_registration_database_details_model_json['username'] = 'sampleuser'

        # Construct a model instance of DatabaseRegistrationDatabaseDetails by calling from_dict on the json representation
        database_registration_database_details_model = DatabaseRegistrationDatabaseDetails.from_dict(database_registration_database_details_model_json)
        assert database_registration_database_details_model != False

        # Construct a model instance of DatabaseRegistrationDatabaseDetails by calling from_dict on the json representation
        database_registration_database_details_model_dict = DatabaseRegistrationDatabaseDetails.from_dict(database_registration_database_details_model_json).__dict__
        database_registration_database_details_model2 = DatabaseRegistrationDatabaseDetails(**database_registration_database_details_model_dict)

        # Verify the model instances are equivalent
        assert database_registration_database_details_model == database_registration_database_details_model2

        # Convert model instance back to dict and verify no loss of data
        database_registration_database_details_model_json2 = database_registration_database_details_model.to_dict()
        assert database_registration_database_details_model_json2 == database_registration_database_details_model_json


class TestModel_Db2Engine:
    """
    Test Class for Db2Engine
    """

    def test_db2_engine_serialization(self):
        """
        Test serialization/deserialization for Db2Engine
        """

        # Construct dict forms of any model objects needed in order to build this model.

        db2_engine_details_model = {}  # Db2EngineDetails
        db2_engine_details_model['connection_string'] = '1.2.3.4'
        db2_engine_details_model['metastore_host'] = '1.2.3.4'

        # Construct a json representation of a Db2Engine model
        db2_engine_model_json = {}
        db2_engine_model_json['actions'] = ['update', 'delete']
        db2_engine_model_json['build_version'] = '1.0.3.0.0'
        db2_engine_model_json['created_by'] = '<username>@<domain>.com'
        db2_engine_model_json['created_on'] = 38
        db2_engine_model_json['description'] = 'db2 engine for running sql queries'
        db2_engine_model_json['engine_details'] = db2_engine_details_model
        db2_engine_model_json['engine_display_name'] = 'sampleEngine'
        db2_engine_model_json['engine_id'] = 'sampleEngine123'
        db2_engine_model_json['host_name'] = 'xyz-db2-01-db2-svc'
        db2_engine_model_json['origin'] = 'ibm'
        db2_engine_model_json['port'] = 38
        db2_engine_model_json['status'] = 'REGISTERED'
        db2_engine_model_json['tags'] = ['tag1', 'tag2']
        db2_engine_model_json['type'] = 'db2'

        # Construct a model instance of Db2Engine by calling from_dict on the json representation
        db2_engine_model = Db2Engine.from_dict(db2_engine_model_json)
        assert db2_engine_model != False

        # Construct a model instance of Db2Engine by calling from_dict on the json representation
        db2_engine_model_dict = Db2Engine.from_dict(db2_engine_model_json).__dict__
        db2_engine_model2 = Db2Engine(**db2_engine_model_dict)

        # Verify the model instances are equivalent
        assert db2_engine_model == db2_engine_model2

        # Convert model instance back to dict and verify no loss of data
        db2_engine_model_json2 = db2_engine_model.to_dict()
        assert db2_engine_model_json2 == db2_engine_model_json


class TestModel_Db2EngineDetails:
    """
    Test Class for Db2EngineDetails
    """

    def test_db2_engine_details_serialization(self):
        """
        Test serialization/deserialization for Db2EngineDetails
        """

        # Construct a json representation of a Db2EngineDetails model
        db2_engine_details_model_json = {}
        db2_engine_details_model_json['connection_string'] = '1.2.3.4'
        db2_engine_details_model_json['metastore_host'] = '1.2.3.4'

        # Construct a model instance of Db2EngineDetails by calling from_dict on the json representation
        db2_engine_details_model = Db2EngineDetails.from_dict(db2_engine_details_model_json)
        assert db2_engine_details_model != False

        # Construct a model instance of Db2EngineDetails by calling from_dict on the json representation
        db2_engine_details_model_dict = Db2EngineDetails.from_dict(db2_engine_details_model_json).__dict__
        db2_engine_details_model2 = Db2EngineDetails(**db2_engine_details_model_dict)

        # Verify the model instances are equivalent
        assert db2_engine_details_model == db2_engine_details_model2

        # Convert model instance back to dict and verify no loss of data
        db2_engine_details_model_json2 = db2_engine_details_model.to_dict()
        assert db2_engine_details_model_json2 == db2_engine_details_model_json


class TestModel_Deployment:
    """
    Test Class for Deployment
    """

    def test_deployment_serialization(self):
        """
        Test serialization/deserialization for Deployment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deployment_platform_options_model = {}  # DeploymentPlatformOptions
        deployment_platform_options_model['backup_encryption_key_crn'] = '<backup_encryption_key_crn>'
        deployment_platform_options_model['disk_encryption_key_crn'] = '<disk_encryption_key_crn>'
        deployment_platform_options_model['key_protect_key_id'] = '<key_protect_key_id>'

        # Construct a json representation of a Deployment model
        deployment_model_json = {}
        deployment_model_json['cloud_type'] = 'awq'
        deployment_model_json['enable_private_endpoints'] = True
        deployment_model_json['enable_public_endpoints'] = True
        deployment_model_json['first_time_use'] = False
        deployment_model_json['formation_id'] = 'new_form_id'
        deployment_model_json['id'] = 'dep_id'
        deployment_model_json['plan_id'] = 'new_plan_id'
        deployment_model_json['platform_options'] = deployment_platform_options_model
        deployment_model_json['region'] = 'us-south'
        deployment_model_json['resource_group_crn'] = 'crn:v1:staging:public:resource-controller::a/hddrtnjjj27dh38xbw::resource-group:c02a6a94f16e4ca'
        deployment_model_json['type'] = 'deployment_type'
        deployment_model_json['version'] = '1.0.2'

        # Construct a model instance of Deployment by calling from_dict on the json representation
        deployment_model = Deployment.from_dict(deployment_model_json)
        assert deployment_model != False

        # Construct a model instance of Deployment by calling from_dict on the json representation
        deployment_model_dict = Deployment.from_dict(deployment_model_json).__dict__
        deployment_model2 = Deployment(**deployment_model_dict)

        # Verify the model instances are equivalent
        assert deployment_model == deployment_model2

        # Convert model instance back to dict and verify no loss of data
        deployment_model_json2 = deployment_model.to_dict()
        assert deployment_model_json2 == deployment_model_json


class TestModel_DeploymentPlatformOptions:
    """
    Test Class for DeploymentPlatformOptions
    """

    def test_deployment_platform_options_serialization(self):
        """
        Test serialization/deserialization for DeploymentPlatformOptions
        """

        # Construct a json representation of a DeploymentPlatformOptions model
        deployment_platform_options_model_json = {}
        deployment_platform_options_model_json['backup_encryption_key_crn'] = '<backup_encryption_key_crn>'
        deployment_platform_options_model_json['disk_encryption_key_crn'] = '<disk_encryption_key_crn>'
        deployment_platform_options_model_json['key_protect_key_id'] = '<key_protect_key_id>'

        # Construct a model instance of DeploymentPlatformOptions by calling from_dict on the json representation
        deployment_platform_options_model = DeploymentPlatformOptions.from_dict(deployment_platform_options_model_json)
        assert deployment_platform_options_model != False

        # Construct a model instance of DeploymentPlatformOptions by calling from_dict on the json representation
        deployment_platform_options_model_dict = DeploymentPlatformOptions.from_dict(deployment_platform_options_model_json).__dict__
        deployment_platform_options_model2 = DeploymentPlatformOptions(**deployment_platform_options_model_dict)

        # Verify the model instances are equivalent
        assert deployment_platform_options_model == deployment_platform_options_model2

        # Convert model instance back to dict and verify no loss of data
        deployment_platform_options_model_json2 = deployment_platform_options_model.to_dict()
        assert deployment_platform_options_model_json2 == deployment_platform_options_model_json


class TestModel_DeploymentsResponse:
    """
    Test Class for DeploymentsResponse
    """

    def test_deployments_response_serialization(self):
        """
        Test serialization/deserialization for DeploymentsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deployment_platform_options_model = {}  # DeploymentPlatformOptions
        deployment_platform_options_model['backup_encryption_key_crn'] = '<backup_encryption_key_crn>'
        deployment_platform_options_model['disk_encryption_key_crn'] = '<disk_encryption_key_crn>'
        deployment_platform_options_model['key_protect_key_id'] = '<key_protect_key_id>'

        deployment_model = {}  # Deployment
        deployment_model['cloud_type'] = 'awq'
        deployment_model['enable_private_endpoints'] = True
        deployment_model['enable_public_endpoints'] = True
        deployment_model['first_time_use'] = False
        deployment_model['formation_id'] = 'new_form_id'
        deployment_model['id'] = 'dep_id'
        deployment_model['plan_id'] = 'new_plan_id'
        deployment_model['platform_options'] = deployment_platform_options_model
        deployment_model['region'] = 'us-south'
        deployment_model['resource_group_crn'] = 'crn:v1:staging:public:resource-controller::a/hddrtnjjj27dh38xbw::resource-group:c02a6a94f16e4ca'
        deployment_model['type'] = 'deployment_type'
        deployment_model['version'] = '1.0.2'

        # Construct a json representation of a DeploymentsResponse model
        deployments_response_model_json = {}
        deployments_response_model_json['deployment'] = deployment_model

        # Construct a model instance of DeploymentsResponse by calling from_dict on the json representation
        deployments_response_model = DeploymentsResponse.from_dict(deployments_response_model_json)
        assert deployments_response_model != False

        # Construct a model instance of DeploymentsResponse by calling from_dict on the json representation
        deployments_response_model_dict = DeploymentsResponse.from_dict(deployments_response_model_json).__dict__
        deployments_response_model2 = DeploymentsResponse(**deployments_response_model_dict)

        # Verify the model instances are equivalent
        assert deployments_response_model == deployments_response_model2

        # Convert model instance back to dict and verify no loss of data
        deployments_response_model_json2 = deployments_response_model.to_dict()
        assert deployments_response_model_json2 == deployments_response_model_json


class TestModel_Endpoints:
    """
    Test Class for Endpoints
    """

    def test_endpoints_serialization(self):
        """
        Test serialization/deserialization for Endpoints
        """

        # Construct a json representation of a Endpoints model
        endpoints_model_json = {}
        endpoints_model_json['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        endpoints_model_json['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        endpoints_model_json['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        endpoints_model_json['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        endpoints_model_json['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        endpoints_model_json['view_history_server'] = 'testString'
        endpoints_model_json['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        # Construct a model instance of Endpoints by calling from_dict on the json representation
        endpoints_model = Endpoints.from_dict(endpoints_model_json)
        assert endpoints_model != False

        # Construct a model instance of Endpoints by calling from_dict on the json representation
        endpoints_model_dict = Endpoints.from_dict(endpoints_model_json).__dict__
        endpoints_model2 = Endpoints(**endpoints_model_dict)

        # Verify the model instances are equivalent
        assert endpoints_model == endpoints_model2

        # Convert model instance back to dict and verify no loss of data
        endpoints_model_json2 = endpoints_model.to_dict()
        assert endpoints_model_json2 == endpoints_model_json


class TestModel_Engine:
    """
    Test Class for Engine
    """

    def test_engine_serialization(self):
        """
        Test serialization/deserialization for Engine
        """

        # Construct dict forms of any model objects needed in order to build this model.

        db2_engine_details_model = {}  # Db2EngineDetails
        db2_engine_details_model['connection_string'] = '1.2.3.4'
        db2_engine_details_model['metastore_host'] = '1.2.3.4'

        db2_engine_model = {}  # Db2Engine
        db2_engine_model['actions'] = ['update', 'delete']
        db2_engine_model['build_version'] = '1.0.3.0.0'
        db2_engine_model['created_by'] = '<username>@<domain>.com'
        db2_engine_model['created_on'] = 38
        db2_engine_model['description'] = 'db2 engine for running sql queries'
        db2_engine_model['engine_details'] = db2_engine_details_model
        db2_engine_model['engine_display_name'] = 'sampleEngine'
        db2_engine_model['engine_id'] = 'sampleEngine123'
        db2_engine_model['host_name'] = 'xyz-db2-01-db2-svc'
        db2_engine_model['origin'] = 'ibm'
        db2_engine_model['port'] = 38
        db2_engine_model['status'] = 'REGISTERED'
        db2_engine_model['tags'] = ['tag1', 'tag2']
        db2_engine_model['type'] = 'db2'

        milvus_service_model = {}  # MilvusService
        milvus_service_model['actions'] = ['update', 'delete']
        milvus_service_model['created_by'] = '<username>@<domain>.com'
        milvus_service_model['created_on'] = 38
        milvus_service_model['description'] = 'milvus service for running sql queries'
        milvus_service_model['grpc_port'] = 26
        milvus_service_model['host_name'] = 'sampleMilvus'
        milvus_service_model['https_port'] = 26
        milvus_service_model['origin'] = 'native'
        milvus_service_model['service_display_name'] = 'sampleService'
        milvus_service_model['service_id'] = 'sampleService123'
        milvus_service_model['status'] = 'running'
        milvus_service_model['status_code'] = 38
        milvus_service_model['tags'] = ['tag1', 'tag2']
        milvus_service_model['type'] = 'milvus'

        netezza_engine_details_model = {}  # NetezzaEngineDetails
        netezza_engine_details_model['connection_string'] = '1.2.3.4'
        netezza_engine_details_model['metastore_host'] = '1.2.3.4'

        netezza_engine_model = {}  # NetezzaEngine
        netezza_engine_model['actions'] = ['update', 'delete']
        netezza_engine_model['build_version'] = '1.0.3.0.0'
        netezza_engine_model['created_by'] = '<username>@<domain>.com'
        netezza_engine_model['created_on'] = 38
        netezza_engine_model['description'] = 'netezza engine for running sql queries'
        netezza_engine_model['engine_details'] = netezza_engine_details_model
        netezza_engine_model['engine_display_name'] = 'sampleEngine'
        netezza_engine_model['engine_id'] = 'sampleEngine123'
        netezza_engine_model['host_name'] = 'xyz-netezza-01-netezza-svc'
        netezza_engine_model['origin'] = 'ibm'
        netezza_engine_model['port'] = 38
        netezza_engine_model['status'] = 'REGISTERED'
        netezza_engine_model['tags'] = ['tag1', 'tag2']
        netezza_engine_model['type'] = 'netezza'

        prestissimo_node_description_body_model = {}  # PrestissimoNodeDescriptionBody
        prestissimo_node_description_body_model['node_type'] = 'worker'
        prestissimo_node_description_body_model['quantity'] = 38

        prestissimo_endpoints_model = {}  # PrestissimoEndpoints
        prestissimo_endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        prestissimo_endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        prestissimo_endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        prestissimo_endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        prestissimo_endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        prestissimo_endpoints_model['view_history_server'] = 'testString'
        prestissimo_endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        prestissimo_engine_details_model = {}  # PrestissimoEngineDetails
        prestissimo_engine_details_model['connection_string'] = '1.2.3.4'
        prestissimo_engine_details_model['endpoints'] = prestissimo_endpoints_model
        prestissimo_engine_details_model['metastore_host'] = '1.2.3.4'

        prestissimo_engine_model = {}  # PrestissimoEngine
        prestissimo_engine_model['actions'] = ['update', 'delete']
        prestissimo_engine_model['associated_catalogs'] = ['new_catalog_1', 'new_catalog_2']
        prestissimo_engine_model['build_version'] = '1.0.3.0.0'
        prestissimo_engine_model['coordinator'] = prestissimo_node_description_body_model
        prestissimo_engine_model['created_by'] = '<username>@<domain>.com'
        prestissimo_engine_model['created_on'] = 38
        prestissimo_engine_model['description'] = 'prestissimo engine for running sql queries'
        prestissimo_engine_model['engine_details'] = prestissimo_engine_details_model
        prestissimo_engine_model['engine_display_name'] = 'sampleEngine'
        prestissimo_engine_model['engine_id'] = 'sampleEngine123'
        prestissimo_engine_model['external_host_name'] = 'ibm-lh-lakehouse-prestissimo-01-prestissimo-svc-cpd-instance.apps.wkclhconnectortest.cp.fyre.ibm.com'
        prestissimo_engine_model['group_id'] = 'new_group_id'
        prestissimo_engine_model['host_name'] = 'ibm-lh-lakehouse-prestissimo-01-prestissimo-svc'
        prestissimo_engine_model['origin'] = 'ibm'
        prestissimo_engine_model['port'] = 38
        prestissimo_engine_model['region'] = 'us-south'
        prestissimo_engine_model['size_config'] = 'starter'
        prestissimo_engine_model['status'] = 'running'
        prestissimo_engine_model['status_code'] = 38
        prestissimo_engine_model['tags'] = ['tag1', 'tag2']
        prestissimo_engine_model['type'] = 'prestissimo'
        prestissimo_engine_model['version'] = '1.2.0'
        prestissimo_engine_model['worker'] = prestissimo_node_description_body_model

        node_description_model = {}  # NodeDescription
        node_description_model['node_type'] = 'worker'
        node_description_model['quantity'] = 38

        endpoints_model = {}  # Endpoints
        endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        endpoints_model['view_history_server'] = 'testString'
        endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        engine_details_model = {}  # EngineDetails
        engine_details_model['connection_string'] = '1.2.3.4'
        engine_details_model['endpoints'] = endpoints_model
        engine_details_model['metastore_host'] = '1.2.3.4'

        presto_engine_model = {}  # PrestoEngine
        presto_engine_model['actions'] = ['update', 'delete']
        presto_engine_model['associated_catalogs'] = ['iceberg_data', 'hive_data']
        presto_engine_model['build_version'] = '1.0.3.0.0'
        presto_engine_model['coordinator'] = node_description_model
        presto_engine_model['created_by'] = '<username>@<domain>.com'
        presto_engine_model['created_on'] = 38
        presto_engine_model['description'] = 'presto engine for running sql queries'
        presto_engine_model['engine_details'] = engine_details_model
        presto_engine_model['engine_display_name'] = 'sampleEngine'
        presto_engine_model['engine_id'] = 'sampleEngine123'
        presto_engine_model['external_host_name'] = 'your-hostname.apps.your-domain.com'
        presto_engine_model['group_id'] = 'new_group_id'
        presto_engine_model['host_name'] = 'ibm-lh-lakehouse-presto-01-presto-svc'
        presto_engine_model['origin'] = 'ibm'
        presto_engine_model['port'] = 38
        presto_engine_model['region'] = 'us-south'
        presto_engine_model['size_config'] = 'starter'
        presto_engine_model['status'] = 'running'
        presto_engine_model['status_code'] = 38
        presto_engine_model['tags'] = ['tag1', 'tag2']
        presto_engine_model['type'] = 'presto'
        presto_engine_model['version'] = '1.2.0'
        presto_engine_model['worker'] = node_description_model

        spark_engine_details_endpoints_model = {}  # SparkEngineDetailsEndpoints
        spark_engine_details_endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        spark_engine_details_endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        spark_engine_details_endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        spark_engine_details_endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        spark_engine_details_endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        spark_engine_details_endpoints_model['view_history_server'] = 'testString'
        spark_engine_details_endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        spark_engine_details_model = {}  # SparkEngineDetails
        spark_engine_details_model['connection_string'] = 'https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>'
        spark_engine_details_model['endpoints'] = spark_engine_details_endpoints_model

        spark_engine_model = {}  # SparkEngine
        spark_engine_model['actions'] = ['update', 'delete']
        spark_engine_model['build_version'] = '1.0.3.0.0'
        spark_engine_model['created_by'] = '<username>@<domain>.com'
        spark_engine_model['created_on'] = 38
        spark_engine_model['description'] = 'spark engine for running sql queries'
        spark_engine_model['engine_details'] = spark_engine_details_model
        spark_engine_model['engine_display_name'] = 'sampleEngine'
        spark_engine_model['engine_id'] = 'sampleEngine123'
        spark_engine_model['origin'] = 'ibm'
        spark_engine_model['status'] = 'Registered'
        spark_engine_model['tags'] = ['tag1', 'tag2']
        spark_engine_model['type'] = 'spark'

        # Construct a json representation of a Engine model
        engine_model_json = {}
        engine_model_json['db2_engines'] = [db2_engine_model]
        engine_model_json['milvus_services'] = [milvus_service_model]
        engine_model_json['netezza_engines'] = [netezza_engine_model]
        engine_model_json['prestissimo_engines'] = [prestissimo_engine_model]
        engine_model_json['presto_engines'] = [presto_engine_model]
        engine_model_json['spark_engines'] = [spark_engine_model]

        # Construct a model instance of Engine by calling from_dict on the json representation
        engine_model = Engine.from_dict(engine_model_json)
        assert engine_model != False

        # Construct a model instance of Engine by calling from_dict on the json representation
        engine_model_dict = Engine.from_dict(engine_model_json).__dict__
        engine_model2 = Engine(**engine_model_dict)

        # Verify the model instances are equivalent
        assert engine_model == engine_model2

        # Convert model instance back to dict and verify no loss of data
        engine_model_json2 = engine_model.to_dict()
        assert engine_model_json2 == engine_model_json


class TestModel_EngineDetails:
    """
    Test Class for EngineDetails
    """

    def test_engine_details_serialization(self):
        """
        Test serialization/deserialization for EngineDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        endpoints_model = {}  # Endpoints
        endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        endpoints_model['view_history_server'] = 'testString'
        endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        # Construct a json representation of a EngineDetails model
        engine_details_model_json = {}
        engine_details_model_json['connection_string'] = '1.2.3.4'
        engine_details_model_json['endpoints'] = endpoints_model
        engine_details_model_json['metastore_host'] = '1.2.3.4'

        # Construct a model instance of EngineDetails by calling from_dict on the json representation
        engine_details_model = EngineDetails.from_dict(engine_details_model_json)
        assert engine_details_model != False

        # Construct a model instance of EngineDetails by calling from_dict on the json representation
        engine_details_model_dict = EngineDetails.from_dict(engine_details_model_json).__dict__
        engine_details_model2 = EngineDetails(**engine_details_model_dict)

        # Verify the model instances are equivalent
        assert engine_details_model == engine_details_model2

        # Convert model instance back to dict and verify no loss of data
        engine_details_model_json2 = engine_details_model.to_dict()
        assert engine_details_model_json2 == engine_details_model_json


class TestModel_EngineDetailsBody:
    """
    Test Class for EngineDetailsBody
    """

    def test_engine_details_body_serialization(self):
        """
        Test serialization/deserialization for EngineDetailsBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        node_description_body_model = {}  # NodeDescriptionBody
        node_description_body_model['node_type'] = 'worker'
        node_description_body_model['quantity'] = 38

        # Construct a json representation of a EngineDetailsBody model
        engine_details_body_model_json = {}
        engine_details_body_model_json['api_key'] = '<api_key>'
        engine_details_body_model_json['connection_string'] = '1.2.3.4'
        engine_details_body_model_json['coordinator'] = node_description_body_model
        engine_details_body_model_json['instance_id'] = 'instance_id'
        engine_details_body_model_json['managed_by'] = 'fully/self'
        engine_details_body_model_json['size_config'] = 'starter'
        engine_details_body_model_json['worker'] = node_description_body_model

        # Construct a model instance of EngineDetailsBody by calling from_dict on the json representation
        engine_details_body_model = EngineDetailsBody.from_dict(engine_details_body_model_json)
        assert engine_details_body_model != False

        # Construct a model instance of EngineDetailsBody by calling from_dict on the json representation
        engine_details_body_model_dict = EngineDetailsBody.from_dict(engine_details_body_model_json).__dict__
        engine_details_body_model2 = EngineDetailsBody(**engine_details_body_model_dict)

        # Verify the model instances are equivalent
        assert engine_details_body_model == engine_details_body_model2

        # Convert model instance back to dict and verify no loss of data
        engine_details_body_model_json2 = engine_details_body_model.to_dict()
        assert engine_details_body_model_json2 == engine_details_body_model_json


class TestModel_GetBucketRegistrationOKBody:
    """
    Test Class for GetBucketRegistrationOKBody
    """

    def test_get_bucket_registration_ok_body_serialization(self):
        """
        Test serialization/deserialization for GetBucketRegistrationOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bucket_registration_model = {}  # BucketRegistration
        bucket_registration_model['access_key'] = '<access_key>'
        bucket_registration_model['actions'] = ['create', 'update']
        bucket_registration_model['associated_catalogs'] = ['iceberg_catalog', 'hive_catalog']
        bucket_registration_model['bucket_display_name'] = 'samplebucketdisplayname'
        bucket_registration_model['bucket_id'] = 'samplebucketid'
        bucket_registration_model['bucket_name'] = 'samplebucket'
        bucket_registration_model['bucket_type'] = 'minio'
        bucket_registration_model['created_by'] = 'username@domain.com'
        bucket_registration_model['created_on'] = '1699457595'
        bucket_registration_model['description'] = 'default bucket'
        bucket_registration_model['endpoint'] = 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        bucket_registration_model['managed_by'] = 'ibm'
        bucket_registration_model['region'] = 'us-south'
        bucket_registration_model['secret_key'] = 'secret_key'
        bucket_registration_model['state'] = 'active'
        bucket_registration_model['tags'] = ['tag1', 'tag2']

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Get registered bucket'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a GetBucketRegistrationOKBody model
        get_bucket_registration_ok_body_model_json = {}
        get_bucket_registration_ok_body_model_json['bucket_registration'] = bucket_registration_model
        get_bucket_registration_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of GetBucketRegistrationOKBody by calling from_dict on the json representation
        get_bucket_registration_ok_body_model = GetBucketRegistrationOKBody.from_dict(get_bucket_registration_ok_body_model_json)
        assert get_bucket_registration_ok_body_model != False

        # Construct a model instance of GetBucketRegistrationOKBody by calling from_dict on the json representation
        get_bucket_registration_ok_body_model_dict = GetBucketRegistrationOKBody.from_dict(get_bucket_registration_ok_body_model_json).__dict__
        get_bucket_registration_ok_body_model2 = GetBucketRegistrationOKBody(**get_bucket_registration_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert get_bucket_registration_ok_body_model == get_bucket_registration_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        get_bucket_registration_ok_body_model_json2 = get_bucket_registration_ok_body_model.to_dict()
        assert get_bucket_registration_ok_body_model_json2 == get_bucket_registration_ok_body_model_json


class TestModel_GetCatalogOKBody:
    """
    Test Class for GetCatalogOKBody
    """

    def test_get_catalog_ok_body_serialization(self):
        """
        Test serialization/deserialization for GetCatalogOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        catalog_detail_model = {}  # CatalogDetail
        catalog_detail_model['actions'] = ['select', 'use', 'show', 'view', 'create', 'drop', 'alter', 'insert', 'grant', 'revoke', 'delete', 'update', 'remove', 'register']
        catalog_detail_model['associated_buckets'] = ['iceberg-bucket']
        catalog_detail_model['associated_databases'] = []
        catalog_detail_model['associated_engines'] = ['presto88']
        catalog_detail_model['catalog_name'] = 'iceberg_data'
        catalog_detail_model['catalog_type'] = 'iceberg'
        catalog_detail_model['created_by'] = 'example@ibm.com'
        catalog_detail_model['created_on'] = '1700549252'
        catalog_detail_model['description'] = 'get one catalog'
        catalog_detail_model['hostname'] = '9c11c623-685a-444b-b3fa-989b2f7a3f8e.cfjag3sf0s5o87astjo0.databases.appdomain.cloud'
        catalog_detail_model['last_sync_at'] = '0'
        catalog_detail_model['managed_by'] = 'ibm'
        catalog_detail_model['metastore'] = 'glue'
        catalog_detail_model['port'] = '32355'
        catalog_detail_model['status'] = 'Running'
        catalog_detail_model['sync_description'] = 'Registration has not started'
        catalog_detail_model['sync_exception'] = []
        catalog_detail_model['sync_status'] = 'NOT_STARTED'
        catalog_detail_model['tags'] = ['tag1', 'tag2']
        catalog_detail_model['thrift_uri'] = 'thrift://9c11c623-685a-444b-b3fa-989b2f7a3f8e.cfjag3sf0s5o87astjo0.databases.appdomain.cloud:32355'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Get Catalog'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a GetCatalogOKBody model
        get_catalog_ok_body_model_json = {}
        get_catalog_ok_body_model_json['catalog'] = catalog_detail_model
        get_catalog_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of GetCatalogOKBody by calling from_dict on the json representation
        get_catalog_ok_body_model = GetCatalogOKBody.from_dict(get_catalog_ok_body_model_json)
        assert get_catalog_ok_body_model != False

        # Construct a model instance of GetCatalogOKBody by calling from_dict on the json representation
        get_catalog_ok_body_model_dict = GetCatalogOKBody.from_dict(get_catalog_ok_body_model_json).__dict__
        get_catalog_ok_body_model2 = GetCatalogOKBody(**get_catalog_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert get_catalog_ok_body_model == get_catalog_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        get_catalog_ok_body_model_json2 = get_catalog_ok_body_model.to_dict()
        assert get_catalog_ok_body_model_json2 == get_catalog_ok_body_model_json


class TestModel_GetDatabaseOKBody:
    """
    Test Class for GetDatabaseOKBody
    """

    def test_get_database_ok_body_serialization(self):
        """
        Test serialization/deserialization for GetDatabaseOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        database_registration_database_details_model = {}  # DatabaseRegistrationDatabaseDetails
        database_registration_database_details_model['database_name'] = 'new_database'
        database_registration_database_details_model['hostname'] = 'netezza://abc.efg.com'
        database_registration_database_details_model['password'] = 'samplepassword'
        database_registration_database_details_model['port'] = 4353
        database_registration_database_details_model['sasl'] = True
        database_registration_database_details_model['ssl'] = True
        database_registration_database_details_model['tables'] = 'netezza_table_name'
        database_registration_database_details_model['username'] = 'sampleuser'

        database_registration_model = {}  # DatabaseRegistration
        database_registration_model['actions'] = ['update', 'delete']
        database_registration_model['associated_catalogs'] = ['iceberg_catalog', 'hive_catalog']
        database_registration_model['created_by'] = 'user1@bim.com'
        database_registration_model['created_on'] = '1686792721'
        database_registration_model['database_details'] = database_registration_database_details_model
        database_registration_model['database_display_name'] = 'new_database,'
        database_registration_model['database_id'] = 'new_database_id,'
        database_registration_model['database_properties'] = ['key1', 'key2']
        database_registration_model['database_type'] = 'netezza'
        database_registration_model['description'] = 'Description of the database'
        database_registration_model['tags'] = ['testdatabase', 'userdatabase']

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Get database'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a GetDatabaseOKBody model
        get_database_ok_body_model_json = {}
        get_database_ok_body_model_json['database'] = database_registration_model
        get_database_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of GetDatabaseOKBody by calling from_dict on the json representation
        get_database_ok_body_model = GetDatabaseOKBody.from_dict(get_database_ok_body_model_json)
        assert get_database_ok_body_model != False

        # Construct a model instance of GetDatabaseOKBody by calling from_dict on the json representation
        get_database_ok_body_model_dict = GetDatabaseOKBody.from_dict(get_database_ok_body_model_json).__dict__
        get_database_ok_body_model2 = GetDatabaseOKBody(**get_database_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert get_database_ok_body_model == get_database_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        get_database_ok_body_model_json2 = get_database_ok_body_model.to_dict()
        assert get_database_ok_body_model_json2 == get_database_ok_body_model_json


class TestModel_GetDeploymentsOKBody:
    """
    Test Class for GetDeploymentsOKBody
    """

    def test_get_deployments_ok_body_serialization(self):
        """
        Test serialization/deserialization for GetDeploymentsOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        deployment_platform_options_model = {}  # DeploymentPlatformOptions
        deployment_platform_options_model['backup_encryption_key_crn'] = '2nf8f8b3kd8wknfkf'
        deployment_platform_options_model['disk_encryption_key_crn'] = 'hjdkd8wjnnd93ujd9'
        deployment_platform_options_model['key_protect_key_id'] = '8ndkenkwjdciendj'

        deployment_model = {}  # Deployment
        deployment_model['cloud_type'] = 'aws'
        deployment_model['enable_private_endpoints'] = True
        deployment_model['enable_public_endpoints'] = True
        deployment_model['first_time_use'] = False
        deployment_model['formation_id'] = 'new_form_id'
        deployment_model['id'] = 'dep_id'
        deployment_model['plan_id'] = 'new_plan_id'
        deployment_model['platform_options'] = deployment_platform_options_model
        deployment_model['region'] = 'us-south'
        deployment_model['resource_group_crn'] = 'crn:v1:staging:public:resource-controller::a/hddrtnjjj27dh38xbw::resource-group:c02a6a94f16e4ca'
        deployment_model['type'] = 'deployment_type'
        deployment_model['version'] = '1.0.2'

        deployments_response_model = {}  # DeploymentsResponse
        deployments_response_model['deployment'] = deployment_model

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'get instance'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a GetDeploymentsOKBody model
        get_deployments_ok_body_model_json = {}
        get_deployments_ok_body_model_json['deploymentresponse'] = deployments_response_model
        get_deployments_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of GetDeploymentsOKBody by calling from_dict on the json representation
        get_deployments_ok_body_model = GetDeploymentsOKBody.from_dict(get_deployments_ok_body_model_json)
        assert get_deployments_ok_body_model != False

        # Construct a model instance of GetDeploymentsOKBody by calling from_dict on the json representation
        get_deployments_ok_body_model_dict = GetDeploymentsOKBody.from_dict(get_deployments_ok_body_model_json).__dict__
        get_deployments_ok_body_model2 = GetDeploymentsOKBody(**get_deployments_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert get_deployments_ok_body_model == get_deployments_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        get_deployments_ok_body_model_json2 = get_deployments_ok_body_model.to_dict()
        assert get_deployments_ok_body_model_json2 == get_deployments_ok_body_model_json


class TestModel_GetPrestoEngineCatalogOKBody:
    """
    Test Class for GetPrestoEngineCatalogOKBody
    """

    def test_get_presto_engine_catalog_ok_body_serialization(self):
        """
        Test serialization/deserialization for GetPrestoEngineCatalogOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        catalog_detail_model = {}  # CatalogDetail
        catalog_detail_model['actions'] = ['view', 'update', 'delete']
        catalog_detail_model['associated_buckets'] = ['ibm_cos_bucket']
        catalog_detail_model['associated_databases'] = ['iceberg_data']
        catalog_detail_model['associated_engines'] = ['presto367']
        catalog_detail_model['catalog_name'] = 'iceberg_data'
        catalog_detail_model['catalog_type'] = 'iceberg'
        catalog_detail_model['created_by'] = 'user@domain.com'
        catalog_detail_model['created_on'] = '1700633239'
        catalog_detail_model['description'] = 'catalog description'
        catalog_detail_model['hostname'] = '1234-xyz456-abc4321.lakehouse.dev.appdomain.cloud'
        catalog_detail_model['last_sync_at'] = '1602839833'
        catalog_detail_model['managed_by'] = 'ibm'
        catalog_detail_model['metastore'] = 'glue'
        catalog_detail_model['port'] = '31504'
        catalog_detail_model['status'] = 'running'
        catalog_detail_model['sync_description'] = 'Table registration was successful'
        catalog_detail_model['sync_exception'] = ['table is corrupted', 'table metadata not there']
        catalog_detail_model['sync_status'] = 'SUCCESS'
        catalog_detail_model['tags'] = ['tag1', 'tag2']
        catalog_detail_model['thrift_uri'] = 'thrift://samplehost-catalog:4354'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'get engine catalogs'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a GetPrestoEngineCatalogOKBody model
        get_presto_engine_catalog_ok_body_model_json = {}
        get_presto_engine_catalog_ok_body_model_json['catalog'] = catalog_detail_model
        get_presto_engine_catalog_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of GetPrestoEngineCatalogOKBody by calling from_dict on the json representation
        get_presto_engine_catalog_ok_body_model = GetPrestoEngineCatalogOKBody.from_dict(get_presto_engine_catalog_ok_body_model_json)
        assert get_presto_engine_catalog_ok_body_model != False

        # Construct a model instance of GetPrestoEngineCatalogOKBody by calling from_dict on the json representation
        get_presto_engine_catalog_ok_body_model_dict = GetPrestoEngineCatalogOKBody.from_dict(get_presto_engine_catalog_ok_body_model_json).__dict__
        get_presto_engine_catalog_ok_body_model2 = GetPrestoEngineCatalogOKBody(**get_presto_engine_catalog_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert get_presto_engine_catalog_ok_body_model == get_presto_engine_catalog_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        get_presto_engine_catalog_ok_body_model_json2 = get_presto_engine_catalog_ok_body_model.to_dict()
        assert get_presto_engine_catalog_ok_body_model_json2 == get_presto_engine_catalog_ok_body_model_json


class TestModel_GetPrestoEngineOKBody:
    """
    Test Class for GetPrestoEngineOKBody
    """

    def test_get_presto_engine_ok_body_serialization(self):
        """
        Test serialization/deserialization for GetPrestoEngineOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        node_description_model = {}  # NodeDescription
        node_description_model['node_type'] = 'worker'
        node_description_model['quantity'] = 1

        endpoints_model = {}  # Endpoints
        endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        endpoints_model['view_history_server'] = 'testString'
        endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        engine_details_model = {}  # EngineDetails
        engine_details_model['connection_string'] = '1.2.3.4'
        engine_details_model['endpoints'] = endpoints_model
        engine_details_model['metastore_host'] = '1.2.3.4'

        presto_engine_model = {}  # PrestoEngine
        presto_engine_model['actions'] = ['update', 'delete']
        presto_engine_model['associated_catalogs'] = ['new_catalog_1', 'new_catalog_2']
        presto_engine_model['build_version'] = '1.0.3.0.0'
        presto_engine_model['coordinator'] = node_description_model
        presto_engine_model['created_by'] = '<username>@<domain>.com'
        presto_engine_model['created_on'] = 163788384993
        presto_engine_model['description'] = 'presto engine for running sql queries'
        presto_engine_model['engine_details'] = engine_details_model
        presto_engine_model['engine_display_name'] = 'sampleEngine'
        presto_engine_model['engine_id'] = 'sampleEngine123'
        presto_engine_model['external_host_name'] = 'your-hostname.apps.your-domain.com'
        presto_engine_model['group_id'] = 'new_group_id'
        presto_engine_model['host_name'] = 'your-hostname.apps.your-domain.com'
        presto_engine_model['origin'] = 'ibm'
        presto_engine_model['port'] = 38
        presto_engine_model['region'] = 'us-south'
        presto_engine_model['size_config'] = 'starter'
        presto_engine_model['status'] = 'running'
        presto_engine_model['status_code'] = 0
        presto_engine_model['tags'] = ['tag1', 'tag2']
        presto_engine_model['type'] = 'presto'
        presto_engine_model['version'] = '1.2.0'
        presto_engine_model['worker'] = node_description_model

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'get engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a GetPrestoEngineOKBody model
        get_presto_engine_ok_body_model_json = {}
        get_presto_engine_ok_body_model_json['engine'] = presto_engine_model
        get_presto_engine_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of GetPrestoEngineOKBody by calling from_dict on the json representation
        get_presto_engine_ok_body_model = GetPrestoEngineOKBody.from_dict(get_presto_engine_ok_body_model_json)
        assert get_presto_engine_ok_body_model != False

        # Construct a model instance of GetPrestoEngineOKBody by calling from_dict on the json representation
        get_presto_engine_ok_body_model_dict = GetPrestoEngineOKBody.from_dict(get_presto_engine_ok_body_model_json).__dict__
        get_presto_engine_ok_body_model2 = GetPrestoEngineOKBody(**get_presto_engine_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert get_presto_engine_ok_body_model == get_presto_engine_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        get_presto_engine_ok_body_model_json2 = get_presto_engine_ok_body_model.to_dict()
        assert get_presto_engine_ok_body_model_json2 == get_presto_engine_ok_body_model_json


class TestModel_GetSparkEngineApplicationStatusOKBody:
    """
    Test Class for GetSparkEngineApplicationStatusOKBody
    """

    def test_get_spark_engine_application_status_ok_body_serialization(self):
        """
        Test serialization/deserialization for GetSparkEngineApplicationStatusOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        spark_engine_application_status_application_details_conf_model = {}  # SparkEngineApplicationStatusApplicationDetailsConf
        spark_engine_application_status_application_details_conf_model['spark_app_name'] = 'MyJob'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_client_auth_mode'] = 'PLAIN'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_client_plain_password'] = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_client_plain_username'] = 'ibm_lh_token_admin'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_truststore_password'] = 'changeit'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_truststore_path'] = 'file:///opt/ibm/jdk/lib/security/cacerts'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_truststore_type'] = 'JKS'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_use_ssl'] = 'true'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_implementation'] = 'hive'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_lakehouse'] = 'org.apache.iceberg.spark.SparkCatalog'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_lakehouse_type'] = 'hive'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_lakehouse_uri'] = 'testString'
        spark_engine_application_status_application_details_conf_model['spark_sql_extensions'] = 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions'
        spark_engine_application_status_application_details_conf_model['spark_sql_iceberg_vectorization_enabled'] = 'false'

        spark_engine_application_status_application_details_model = {}  # SparkEngineApplicationStatusApplicationDetails
        spark_engine_application_status_application_details_model['application'] = '/opt/xyz/spark/examples/src/main/python/wordcount.py'
        spark_engine_application_status_application_details_model['arguments'] = ['/opt/xyz/spark/examples/src/main/python/people.txt']
        spark_engine_application_status_application_details_model['conf'] = spark_engine_application_status_application_details_conf_model
        spark_engine_application_status_application_details_model['env'] = {'sparkEnvPropKey1': 'sparkEnvPropvalue1', 'sparkEnvPropKey2': 'sparkEnvPropvalue2'}
        spark_engine_application_status_application_details_model['name'] = 'SparkApplication1'

        spark_engine_application_status_state_details_items_model = {}  # SparkEngineApplicationStatusStateDetailsItems
        spark_engine_application_status_state_details_items_model['code'] = 'testString'
        spark_engine_application_status_state_details_items_model['message'] = 'testString'
        spark_engine_application_status_state_details_items_model['type'] = 'testString'

        spark_engine_application_status_model = {}  # SparkEngineApplicationStatus
        spark_engine_application_status_model['application_details'] = spark_engine_application_status_application_details_model
        spark_engine_application_status_model['application_id'] = '<application_id>'
        spark_engine_application_status_model['auto_termination_time'] = '2023-11-04T15:37:57.775Z'
        spark_engine_application_status_model['creation_time'] = 'Saturday 28 October 2023 07:17:06.856+0000'
        spark_engine_application_status_model['deploy_mode'] = 'stand-alone'
        spark_engine_application_status_model['end_time'] = '2023-11-01T15:38:07.188Z'
        spark_engine_application_status_model['failed_time'] = 'testString'
        spark_engine_application_status_model['finish_time'] = 'Saturday 28 October 2023 07:17:38.966+0000'
        spark_engine_application_status_model['id'] = 'id-ca61-454c-aab3-486d39d8c1d0'
        spark_engine_application_status_model['return_code'] = '1'
        spark_engine_application_status_model['spark_application_id'] = '<spark_application_id>'
        spark_engine_application_status_model['spark_application_name'] = 'PythonWordCount'
        spark_engine_application_status_model['start_time'] = '2023-11-01T15:37:57.775Z'
        spark_engine_application_status_model['state'] = 'failed'
        spark_engine_application_status_model['state_details'] = [spark_engine_application_status_state_details_items_model]
        spark_engine_application_status_model['submission_time'] = '2023-11-01T15:37:30.982Z'
        spark_engine_application_status_model['template_id'] = 'spark-3.3-jaas-v2-cp4d-template'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Get spark application'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a GetSparkEngineApplicationStatusOKBody model
        get_spark_engine_application_status_ok_body_model_json = {}
        get_spark_engine_application_status_ok_body_model_json['application'] = spark_engine_application_status_model
        get_spark_engine_application_status_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of GetSparkEngineApplicationStatusOKBody by calling from_dict on the json representation
        get_spark_engine_application_status_ok_body_model = GetSparkEngineApplicationStatusOKBody.from_dict(get_spark_engine_application_status_ok_body_model_json)
        assert get_spark_engine_application_status_ok_body_model != False

        # Construct a model instance of GetSparkEngineApplicationStatusOKBody by calling from_dict on the json representation
        get_spark_engine_application_status_ok_body_model_dict = GetSparkEngineApplicationStatusOKBody.from_dict(get_spark_engine_application_status_ok_body_model_json).__dict__
        get_spark_engine_application_status_ok_body_model2 = GetSparkEngineApplicationStatusOKBody(**get_spark_engine_application_status_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert get_spark_engine_application_status_ok_body_model == get_spark_engine_application_status_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        get_spark_engine_application_status_ok_body_model_json2 = get_spark_engine_application_status_ok_body_model.to_dict()
        assert get_spark_engine_application_status_ok_body_model_json2 == get_spark_engine_application_status_ok_body_model_json


class TestModel_GetTableOKBody:
    """
    Test Class for GetTableOKBody
    """

    def test_get_table_ok_body_serialization(self):
        """
        Test serialization/deserialization for GetTableOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        column_model = {}  # Column
        column_model['column_name'] = 'expenses'
        column_model['comment'] = 'expenses column'
        column_model['extra'] = 'varchar'
        column_model['type'] = 'varchar'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'get columns'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a GetTableOKBody model
        get_table_ok_body_model_json = {}
        get_table_ok_body_model_json['columns'] = [column_model]
        get_table_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of GetTableOKBody by calling from_dict on the json representation
        get_table_ok_body_model = GetTableOKBody.from_dict(get_table_ok_body_model_json)
        assert get_table_ok_body_model != False

        # Construct a model instance of GetTableOKBody by calling from_dict on the json representation
        get_table_ok_body_model_dict = GetTableOKBody.from_dict(get_table_ok_body_model_json).__dict__
        get_table_ok_body_model2 = GetTableOKBody(**get_table_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert get_table_ok_body_model == get_table_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        get_table_ok_body_model_json2 = get_table_ok_body_model.to_dict()
        assert get_table_ok_body_model_json2 == get_table_ok_body_model_json


class TestModel_JsonPatchOperation:
    """
    Test Class for JsonPatchOperation
    """

    def test_json_patch_operation_serialization(self):
        """
        Test serialization/deserialization for JsonPatchOperation
        """

        # Construct a json representation of a JsonPatchOperation model
        json_patch_operation_model_json = {}
        json_patch_operation_model_json['op'] = 'add'
        json_patch_operation_model_json['path'] = 'testString'
        json_patch_operation_model_json['from'] = 'testString'
        json_patch_operation_model_json['value'] = 'testString'

        # Construct a model instance of JsonPatchOperation by calling from_dict on the json representation
        json_patch_operation_model = JsonPatchOperation.from_dict(json_patch_operation_model_json)
        assert json_patch_operation_model != False

        # Construct a model instance of JsonPatchOperation by calling from_dict on the json representation
        json_patch_operation_model_dict = JsonPatchOperation.from_dict(json_patch_operation_model_json).__dict__
        json_patch_operation_model2 = JsonPatchOperation(**json_patch_operation_model_dict)

        # Verify the model instances are equivalent
        assert json_patch_operation_model == json_patch_operation_model2

        # Convert model instance back to dict and verify no loss of data
        json_patch_operation_model_json2 = json_patch_operation_model.to_dict()
        assert json_patch_operation_model_json2 == json_patch_operation_model_json


class TestModel_ListBucketObjectsOKBody:
    """
    Test Class for ListBucketObjectsOKBody
    """

    def test_list_bucket_objects_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListBucketObjectsOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Get bucket objects'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListBucketObjectsOKBody model
        list_bucket_objects_ok_body_model_json = {}
        list_bucket_objects_ok_body_model_json['objects'] = ['object_1']
        list_bucket_objects_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ListBucketObjectsOKBody by calling from_dict on the json representation
        list_bucket_objects_ok_body_model = ListBucketObjectsOKBody.from_dict(list_bucket_objects_ok_body_model_json)
        assert list_bucket_objects_ok_body_model != False

        # Construct a model instance of ListBucketObjectsOKBody by calling from_dict on the json representation
        list_bucket_objects_ok_body_model_dict = ListBucketObjectsOKBody.from_dict(list_bucket_objects_ok_body_model_json).__dict__
        list_bucket_objects_ok_body_model2 = ListBucketObjectsOKBody(**list_bucket_objects_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_bucket_objects_ok_body_model == list_bucket_objects_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_bucket_objects_ok_body_model_json2 = list_bucket_objects_ok_body_model.to_dict()
        assert list_bucket_objects_ok_body_model_json2 == list_bucket_objects_ok_body_model_json


class TestModel_ListBucketRegistrationsOKBody:
    """
    Test Class for ListBucketRegistrationsOKBody
    """

    def test_list_bucket_registrations_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListBucketRegistrationsOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bucket_registration_model = {}  # BucketRegistration
        bucket_registration_model['access_key'] = '<access_key>'
        bucket_registration_model['actions'] = ['browse', 'view', 'modify', 'create', 'grant', 'revoke', 'update', 'remove', 'activate', 'register']
        bucket_registration_model['associated_catalogs'] = ['iceberg_catalog']
        bucket_registration_model['bucket_display_name'] = 'iceberg-bucket'
        bucket_registration_model['bucket_id'] = 'iceberg-bucket'
        bucket_registration_model['bucket_name'] = 'iceberg-bucket'
        bucket_registration_model['bucket_type'] = 'minio'
        bucket_registration_model['created_by'] = 'user'
        bucket_registration_model['created_on'] = '1699457595'
        bucket_registration_model['description'] = 'default bucket'
        bucket_registration_model['endpoint'] = 'http://xyz-minio-svc:9000'
        bucket_registration_model['managed_by'] = 'ibm'
        bucket_registration_model['region'] = 'us-south'
        bucket_registration_model['secret_key'] = 'secret_key'
        bucket_registration_model['state'] = 'active'
        bucket_registration_model['tags'] = ['tag1', 'tag2']

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Get bucket registrations'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListBucketRegistrationsOKBody model
        list_bucket_registrations_ok_body_model_json = {}
        list_bucket_registrations_ok_body_model_json['bucket_registrations'] = [bucket_registration_model]
        list_bucket_registrations_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ListBucketRegistrationsOKBody by calling from_dict on the json representation
        list_bucket_registrations_ok_body_model = ListBucketRegistrationsOKBody.from_dict(list_bucket_registrations_ok_body_model_json)
        assert list_bucket_registrations_ok_body_model != False

        # Construct a model instance of ListBucketRegistrationsOKBody by calling from_dict on the json representation
        list_bucket_registrations_ok_body_model_dict = ListBucketRegistrationsOKBody.from_dict(list_bucket_registrations_ok_body_model_json).__dict__
        list_bucket_registrations_ok_body_model2 = ListBucketRegistrationsOKBody(**list_bucket_registrations_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_bucket_registrations_ok_body_model == list_bucket_registrations_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_bucket_registrations_ok_body_model_json2 = list_bucket_registrations_ok_body_model.to_dict()
        assert list_bucket_registrations_ok_body_model_json2 == list_bucket_registrations_ok_body_model_json


class TestModel_ListCatalogsOKBody:
    """
    Test Class for ListCatalogsOKBody
    """

    def test_list_catalogs_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListCatalogsOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        catalog_detail_model = {}  # CatalogDetail
        catalog_detail_model['actions'] = ['select', 'use', 'show', 'view', 'create', 'drop', 'alter', 'insert', 'grant', 'revoke', 'delete', 'update', 'remove', 'register']
        catalog_detail_model['associated_buckets'] = ['iceberg-bucket']
        catalog_detail_model['associated_databases'] = []
        catalog_detail_model['associated_engines'] = ['presto88']
        catalog_detail_model['catalog_name'] = 'iceberg_data'
        catalog_detail_model['catalog_type'] = 'iceberg'
        catalog_detail_model['created_by'] = 'example@ibm.com'
        catalog_detail_model['created_on'] = '1700549252'
        catalog_detail_model['description'] = 'get catalogs'
        catalog_detail_model['hostname'] = '9c11c623-685a-444b-b3fa-989b2f7a3f8e.cfjag3sf0s5o87astjo0.databases.appdomain.cloud'
        catalog_detail_model['last_sync_at'] = '0'
        catalog_detail_model['managed_by'] = 'ibm'
        catalog_detail_model['metastore'] = 'glue'
        catalog_detail_model['port'] = '32355'
        catalog_detail_model['status'] = 'Running'
        catalog_detail_model['sync_description'] = 'Registration has not started'
        catalog_detail_model['sync_exception'] = []
        catalog_detail_model['sync_status'] = 'NOT_STARTED'
        catalog_detail_model['tags'] = ['tag1', 'tag2']
        catalog_detail_model['thrift_uri'] = 'thrift://9c11c623-685a-444b-b3fa-989b2f7a3f8e.cfjag3sf0s5o87astjo0.databases.appdomain.cloud:32355'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Get Catalogs'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListCatalogsOKBody model
        list_catalogs_ok_body_model_json = {}
        list_catalogs_ok_body_model_json['catalogs'] = [catalog_detail_model]
        list_catalogs_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ListCatalogsOKBody by calling from_dict on the json representation
        list_catalogs_ok_body_model = ListCatalogsOKBody.from_dict(list_catalogs_ok_body_model_json)
        assert list_catalogs_ok_body_model != False

        # Construct a model instance of ListCatalogsOKBody by calling from_dict on the json representation
        list_catalogs_ok_body_model_dict = ListCatalogsOKBody.from_dict(list_catalogs_ok_body_model_json).__dict__
        list_catalogs_ok_body_model2 = ListCatalogsOKBody(**list_catalogs_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_catalogs_ok_body_model == list_catalogs_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_catalogs_ok_body_model_json2 = list_catalogs_ok_body_model.to_dict()
        assert list_catalogs_ok_body_model_json2 == list_catalogs_ok_body_model_json


class TestModel_ListDatabaseRegistrationsOKBody:
    """
    Test Class for ListDatabaseRegistrationsOKBody
    """

    def test_list_database_registrations_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListDatabaseRegistrationsOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        database_registration_database_details_model = {}  # DatabaseRegistrationDatabaseDetails
        database_registration_database_details_model['database_name'] = 'new_database'
        database_registration_database_details_model['hostname'] = 'netezza://ps.fyre.com'
        database_registration_database_details_model['password'] = 'samplepassword'
        database_registration_database_details_model['port'] = 4353
        database_registration_database_details_model['sasl'] = True
        database_registration_database_details_model['ssl'] = True
        database_registration_database_details_model['tables'] = 'netezza_table_name'
        database_registration_database_details_model['username'] = 'sampleuser'

        database_registration_model = {}  # DatabaseRegistration
        database_registration_model['actions'] = ['update', 'delete']
        database_registration_model['associated_catalogs'] = ['iceberg_catalog', 'hive_catalog']
        database_registration_model['created_by'] = 'user1@bim.com'
        database_registration_model['created_on'] = '1686792721'
        database_registration_model['database_details'] = database_registration_database_details_model
        database_registration_model['database_display_name'] = 'new_database'
        database_registration_model['database_id'] = 'new_database_id'
        database_registration_model['database_properties'] = ['key1', 'key2']
        database_registration_model['database_type'] = 'netezza'
        database_registration_model['description'] = 'Description of the external Database'
        database_registration_model['tags'] = ['testdatabase', 'userdatabase']

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Get database registrations'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListDatabaseRegistrationsOKBody model
        list_database_registrations_ok_body_model_json = {}
        list_database_registrations_ok_body_model_json['database_registrations'] = [database_registration_model]
        list_database_registrations_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ListDatabaseRegistrationsOKBody by calling from_dict on the json representation
        list_database_registrations_ok_body_model = ListDatabaseRegistrationsOKBody.from_dict(list_database_registrations_ok_body_model_json)
        assert list_database_registrations_ok_body_model != False

        # Construct a model instance of ListDatabaseRegistrationsOKBody by calling from_dict on the json representation
        list_database_registrations_ok_body_model_dict = ListDatabaseRegistrationsOKBody.from_dict(list_database_registrations_ok_body_model_json).__dict__
        list_database_registrations_ok_body_model2 = ListDatabaseRegistrationsOKBody(**list_database_registrations_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_database_registrations_ok_body_model == list_database_registrations_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_database_registrations_ok_body_model_json2 = list_database_registrations_ok_body_model.to_dict()
        assert list_database_registrations_ok_body_model_json2 == list_database_registrations_ok_body_model_json


class TestModel_ListDb2EnginesOKBody:
    """
    Test Class for ListDb2EnginesOKBody
    """

    def test_list_db2_engines_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListDb2EnginesOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        db2_engine_details_model = {}  # Db2EngineDetails
        db2_engine_details_model['connection_string'] = 'jdbc:db2://<hostname>:<port>/<database>'
        db2_engine_details_model['metastore_host'] = 'thrift://mh-connection-string-sample.com'

        db2_engine_model = {}  # Db2Engine
        db2_engine_model['actions'] = ['update', 'delete']
        db2_engine_model['build_version'] = '1.0.3.0.0'
        db2_engine_model['created_by'] = 'user@test.com'
        db2_engine_model['created_on'] = 1700322436
        db2_engine_model['description'] = 'db2 engine for running sql queries'
        db2_engine_model['engine_details'] = db2_engine_details_model
        db2_engine_model['engine_display_name'] = 'db2'
        db2_engine_model['engine_id'] = 'db2505'
        db2_engine_model['host_name'] = 'xyz-db2-01-db2-svc'
        db2_engine_model['origin'] = 'external'
        db2_engine_model['port'] = 38
        db2_engine_model['status'] = 'REGISTERED'
        db2_engine_model['tags'] = ['tag1', 'tag2']
        db2_engine_model['type'] = 'db2'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'db2 engines list'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListDb2EnginesOKBody model
        list_db2_engines_ok_body_model_json = {}
        list_db2_engines_ok_body_model_json['db2_engines'] = [db2_engine_model]
        list_db2_engines_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ListDb2EnginesOKBody by calling from_dict on the json representation
        list_db2_engines_ok_body_model = ListDb2EnginesOKBody.from_dict(list_db2_engines_ok_body_model_json)
        assert list_db2_engines_ok_body_model != False

        # Construct a model instance of ListDb2EnginesOKBody by calling from_dict on the json representation
        list_db2_engines_ok_body_model_dict = ListDb2EnginesOKBody.from_dict(list_db2_engines_ok_body_model_json).__dict__
        list_db2_engines_ok_body_model2 = ListDb2EnginesOKBody(**list_db2_engines_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_db2_engines_ok_body_model == list_db2_engines_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_db2_engines_ok_body_model_json2 = list_db2_engines_ok_body_model.to_dict()
        assert list_db2_engines_ok_body_model_json2 == list_db2_engines_ok_body_model_json


class TestModel_ListEnginesOKBody:
    """
    Test Class for ListEnginesOKBody
    """

    def test_list_engines_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListEnginesOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        db2_engine_details_model = {}  # Db2EngineDetails
        db2_engine_details_model['connection_string'] = '1.2.3.4'
        db2_engine_details_model['metastore_host'] = '1.2.3.4'

        db2_engine_model = {}  # Db2Engine
        db2_engine_model['actions'] = ['update', 'delete']
        db2_engine_model['build_version'] = '1.0.3.0.0'
        db2_engine_model['created_by'] = '<username>@<domain>.com'
        db2_engine_model['created_on'] = 38
        db2_engine_model['description'] = 'db2 engine for running sql queries'
        db2_engine_model['engine_details'] = db2_engine_details_model
        db2_engine_model['engine_display_name'] = 'sampleEngine'
        db2_engine_model['engine_id'] = 'sampleEngine123'
        db2_engine_model['host_name'] = 'xyz-db2-01-db2-svc'
        db2_engine_model['origin'] = 'ibm'
        db2_engine_model['port'] = 38
        db2_engine_model['status'] = 'REGISTERED'
        db2_engine_model['tags'] = ['tag1', 'tag2']
        db2_engine_model['type'] = 'db2'

        milvus_service_model = {}  # MilvusService
        milvus_service_model['actions'] = ['update', 'delete']
        milvus_service_model['created_by'] = '<username>@<domain>.com'
        milvus_service_model['created_on'] = 38
        milvus_service_model['description'] = 'milvus service for running sql queries'
        milvus_service_model['grpc_port'] = 26
        milvus_service_model['host_name'] = 'sampleMilvus'
        milvus_service_model['https_port'] = 26
        milvus_service_model['origin'] = 'native'
        milvus_service_model['service_display_name'] = 'sampleService'
        milvus_service_model['service_id'] = 'sampleService123'
        milvus_service_model['status'] = 'running'
        milvus_service_model['status_code'] = 38
        milvus_service_model['tags'] = ['tag1', 'tag2']
        milvus_service_model['type'] = 'milvus'

        netezza_engine_details_model = {}  # NetezzaEngineDetails
        netezza_engine_details_model['connection_string'] = '1.2.3.4'
        netezza_engine_details_model['metastore_host'] = '1.2.3.4'

        netezza_engine_model = {}  # NetezzaEngine
        netezza_engine_model['actions'] = ['update', 'delete']
        netezza_engine_model['build_version'] = '1.0.3.0.0'
        netezza_engine_model['created_by'] = '<username>@<domain>.com'
        netezza_engine_model['created_on'] = 38
        netezza_engine_model['description'] = 'netezza engine for running sql queries'
        netezza_engine_model['engine_details'] = netezza_engine_details_model
        netezza_engine_model['engine_display_name'] = 'sampleEngine'
        netezza_engine_model['engine_id'] = 'sampleEngine123'
        netezza_engine_model['host_name'] = 'xyz-netezza-01-netezza-svc'
        netezza_engine_model['origin'] = 'ibm'
        netezza_engine_model['port'] = 38
        netezza_engine_model['status'] = 'REGISTERED'
        netezza_engine_model['tags'] = ['tag1', 'tag2']
        netezza_engine_model['type'] = 'netezza'

        prestissimo_node_description_body_model = {}  # PrestissimoNodeDescriptionBody
        prestissimo_node_description_body_model['node_type'] = 'worker'
        prestissimo_node_description_body_model['quantity'] = 38

        prestissimo_endpoints_model = {}  # PrestissimoEndpoints
        prestissimo_endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        prestissimo_endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        prestissimo_endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        prestissimo_endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        prestissimo_endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        prestissimo_endpoints_model['view_history_server'] = 'testString'
        prestissimo_endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        prestissimo_engine_details_model = {}  # PrestissimoEngineDetails
        prestissimo_engine_details_model['connection_string'] = '1.2.3.4'
        prestissimo_engine_details_model['endpoints'] = prestissimo_endpoints_model
        prestissimo_engine_details_model['metastore_host'] = '1.2.3.4'

        prestissimo_engine_model = {}  # PrestissimoEngine
        prestissimo_engine_model['actions'] = ['update', 'delete']
        prestissimo_engine_model['associated_catalogs'] = ['new_catalog_1', 'new_catalog_2']
        prestissimo_engine_model['build_version'] = '1.0.3.0.0'
        prestissimo_engine_model['coordinator'] = prestissimo_node_description_body_model
        prestissimo_engine_model['created_by'] = '<username>@<domain>.com'
        prestissimo_engine_model['created_on'] = 38
        prestissimo_engine_model['description'] = 'prestissimo engine for running sql queries'
        prestissimo_engine_model['engine_details'] = prestissimo_engine_details_model
        prestissimo_engine_model['engine_display_name'] = 'sampleEngine'
        prestissimo_engine_model['engine_id'] = 'sampleEngine123'
        prestissimo_engine_model['external_host_name'] = 'ibm-lh-lakehouse-prestissimo-01-prestissimo-svc-cpd-instance.apps.wkclhconnectortest.cp.fyre.ibm.com'
        prestissimo_engine_model['group_id'] = 'new_group_id'
        prestissimo_engine_model['host_name'] = 'ibm-lh-lakehouse-prestissimo-01-prestissimo-svc'
        prestissimo_engine_model['origin'] = 'ibm'
        prestissimo_engine_model['port'] = 38
        prestissimo_engine_model['region'] = 'us-south'
        prestissimo_engine_model['size_config'] = 'starter'
        prestissimo_engine_model['status'] = 'running'
        prestissimo_engine_model['status_code'] = 38
        prestissimo_engine_model['tags'] = ['tag1', 'tag2']
        prestissimo_engine_model['type'] = 'prestissimo'
        prestissimo_engine_model['version'] = '1.2.0'
        prestissimo_engine_model['worker'] = prestissimo_node_description_body_model

        node_description_model = {}  # NodeDescription
        node_description_model['node_type'] = 'worker'
        node_description_model['quantity'] = 38

        endpoints_model = {}  # Endpoints
        endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        endpoints_model['view_history_server'] = 'testString'
        endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        engine_details_model = {}  # EngineDetails
        engine_details_model['connection_string'] = '1.2.3.4'
        engine_details_model['endpoints'] = endpoints_model
        engine_details_model['metastore_host'] = '1.2.3.4'

        presto_engine_model = {}  # PrestoEngine
        presto_engine_model['actions'] = ['update', 'delete']
        presto_engine_model['associated_catalogs'] = ['iceberg_data', 'hive_data']
        presto_engine_model['build_version'] = '1.0.3.0.0'
        presto_engine_model['coordinator'] = node_description_model
        presto_engine_model['created_by'] = '<username>@<domain>.com'
        presto_engine_model['created_on'] = 38
        presto_engine_model['description'] = 'presto engine for running sql queries'
        presto_engine_model['engine_details'] = engine_details_model
        presto_engine_model['engine_display_name'] = 'sampleEngine'
        presto_engine_model['engine_id'] = 'sampleEngine123'
        presto_engine_model['external_host_name'] = 'your-hostname.apps.your-domain.com'
        presto_engine_model['group_id'] = 'new_group_id'
        presto_engine_model['host_name'] = 'ibm-lh-lakehouse-presto-01-presto-svc'
        presto_engine_model['origin'] = 'ibm'
        presto_engine_model['port'] = 38
        presto_engine_model['region'] = 'us-south'
        presto_engine_model['size_config'] = 'starter'
        presto_engine_model['status'] = 'running'
        presto_engine_model['status_code'] = 38
        presto_engine_model['tags'] = ['tag1', 'tag2']
        presto_engine_model['type'] = 'presto'
        presto_engine_model['version'] = '1.2.0'
        presto_engine_model['worker'] = node_description_model

        spark_engine_details_endpoints_model = {}  # SparkEngineDetailsEndpoints
        spark_engine_details_endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        spark_engine_details_endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        spark_engine_details_endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        spark_engine_details_endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        spark_engine_details_endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        spark_engine_details_endpoints_model['view_history_server'] = 'testString'
        spark_engine_details_endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        spark_engine_details_model = {}  # SparkEngineDetails
        spark_engine_details_model['connection_string'] = 'https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>'
        spark_engine_details_model['endpoints'] = spark_engine_details_endpoints_model

        spark_engine_model = {}  # SparkEngine
        spark_engine_model['actions'] = ['update', 'delete']
        spark_engine_model['build_version'] = '1.0.3.0.0'
        spark_engine_model['created_by'] = '<username>@<domain>.com'
        spark_engine_model['created_on'] = 38
        spark_engine_model['description'] = 'spark engine for running sql queries'
        spark_engine_model['engine_details'] = spark_engine_details_model
        spark_engine_model['engine_display_name'] = 'sampleEngine'
        spark_engine_model['engine_id'] = 'sampleEngine123'
        spark_engine_model['origin'] = 'ibm'
        spark_engine_model['status'] = 'Registered'
        spark_engine_model['tags'] = ['tag1', 'tag2']
        spark_engine_model['type'] = 'spark'

        engine_model = {}  # Engine
        engine_model['db2_engines'] = [db2_engine_model]
        engine_model['milvus_services'] = [milvus_service_model]
        engine_model['netezza_engines'] = [netezza_engine_model]
        engine_model['prestissimo_engines'] = [prestissimo_engine_model]
        engine_model['presto_engines'] = [presto_engine_model]
        engine_model['spark_engines'] = [spark_engine_model]

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'engines list'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListEnginesOKBody model
        list_engines_ok_body_model_json = {}
        list_engines_ok_body_model_json['engines'] = engine_model
        list_engines_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ListEnginesOKBody by calling from_dict on the json representation
        list_engines_ok_body_model = ListEnginesOKBody.from_dict(list_engines_ok_body_model_json)
        assert list_engines_ok_body_model != False

        # Construct a model instance of ListEnginesOKBody by calling from_dict on the json representation
        list_engines_ok_body_model_dict = ListEnginesOKBody.from_dict(list_engines_ok_body_model_json).__dict__
        list_engines_ok_body_model2 = ListEnginesOKBody(**list_engines_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_engines_ok_body_model == list_engines_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_engines_ok_body_model_json2 = list_engines_ok_body_model.to_dict()
        assert list_engines_ok_body_model_json2 == list_engines_ok_body_model_json


class TestModel_ListNetezzaEnginesOKBody:
    """
    Test Class for ListNetezzaEnginesOKBody
    """

    def test_list_netezza_engines_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListNetezzaEnginesOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        netezza_engine_details_model = {}  # NetezzaEngineDetails
        netezza_engine_details_model['connection_string'] = 'jdbc:netezza://localhost:5480/database'
        netezza_engine_details_model['metastore_host'] = 'thrift://mh-connection-string-sample.com'

        netezza_engine_model = {}  # NetezzaEngine
        netezza_engine_model['actions'] = ['update', 'delete']
        netezza_engine_model['build_version'] = '1.0.3.0.0'
        netezza_engine_model['created_by'] = 'user@test.com'
        netezza_engine_model['created_on'] = 1700322469
        netezza_engine_model['description'] = 'netezza engine for running sql queries'
        netezza_engine_model['engine_details'] = netezza_engine_details_model
        netezza_engine_model['engine_display_name'] = 'netezza'
        netezza_engine_model['engine_id'] = 'netezza170'
        netezza_engine_model['host_name'] = 'xyz-netezza-01-netezza-svc'
        netezza_engine_model['origin'] = 'external'
        netezza_engine_model['port'] = 38
        netezza_engine_model['status'] = 'REGISTERED'
        netezza_engine_model['tags'] = ['tag1', 'tag2']
        netezza_engine_model['type'] = 'netezza'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'netezza engines list'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListNetezzaEnginesOKBody model
        list_netezza_engines_ok_body_model_json = {}
        list_netezza_engines_ok_body_model_json['netezza_engines'] = [netezza_engine_model]
        list_netezza_engines_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ListNetezzaEnginesOKBody by calling from_dict on the json representation
        list_netezza_engines_ok_body_model = ListNetezzaEnginesOKBody.from_dict(list_netezza_engines_ok_body_model_json)
        assert list_netezza_engines_ok_body_model != False

        # Construct a model instance of ListNetezzaEnginesOKBody by calling from_dict on the json representation
        list_netezza_engines_ok_body_model_dict = ListNetezzaEnginesOKBody.from_dict(list_netezza_engines_ok_body_model_json).__dict__
        list_netezza_engines_ok_body_model2 = ListNetezzaEnginesOKBody(**list_netezza_engines_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_netezza_engines_ok_body_model == list_netezza_engines_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_netezza_engines_ok_body_model_json2 = list_netezza_engines_ok_body_model.to_dict()
        assert list_netezza_engines_ok_body_model_json2 == list_netezza_engines_ok_body_model_json


class TestModel_ListOtherEnginesOKBody:
    """
    Test Class for ListOtherEnginesOKBody
    """

    def test_list_other_engines_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListOtherEnginesOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        other_engine_details_model = {}  # OtherEngineDetails
        other_engine_details_model['connection_string'] = 'https://other-connection-string-sample.com'
        other_engine_details_model['engine_type'] = 'netezza'
        other_engine_details_model['metastore_host'] = '1.2.3.4'

        other_engine_model = {}  # OtherEngine
        other_engine_model['created_by'] = '<username>@<domain>.com'
        other_engine_model['created_on'] = 163788384993
        other_engine_model['description'] = 'other engine for running queries'
        other_engine_model['engine_details'] = other_engine_details_model
        other_engine_model['engine_display_name'] = 'sampleEngine'
        other_engine_model['engine_id'] = 'sampleEngine123'
        other_engine_model['origin'] = 'external'
        other_engine_model['status'] = 'registered'
        other_engine_model['status_code'] = 38
        other_engine_model['tags'] = ['tag1', 'tag2']
        other_engine_model['type'] = 'other'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'engines list'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListOtherEnginesOKBody model
        list_other_engines_ok_body_model_json = {}
        list_other_engines_ok_body_model_json['other_engines'] = [other_engine_model]
        list_other_engines_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ListOtherEnginesOKBody by calling from_dict on the json representation
        list_other_engines_ok_body_model = ListOtherEnginesOKBody.from_dict(list_other_engines_ok_body_model_json)
        assert list_other_engines_ok_body_model != False

        # Construct a model instance of ListOtherEnginesOKBody by calling from_dict on the json representation
        list_other_engines_ok_body_model_dict = ListOtherEnginesOKBody.from_dict(list_other_engines_ok_body_model_json).__dict__
        list_other_engines_ok_body_model2 = ListOtherEnginesOKBody(**list_other_engines_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_other_engines_ok_body_model == list_other_engines_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_other_engines_ok_body_model_json2 = list_other_engines_ok_body_model.to_dict()
        assert list_other_engines_ok_body_model_json2 == list_other_engines_ok_body_model_json


class TestModel_ListPrestoEngineCatalogsOKBody:
    """
    Test Class for ListPrestoEngineCatalogsOKBody
    """

    def test_list_presto_engine_catalogs_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListPrestoEngineCatalogsOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        catalog_model = {}  # Catalog
        catalog_model['catalog_name'] = 'iceberg_data'
        catalog_model['creation_date'] = '16073847388'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'get engine catalogs'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListPrestoEngineCatalogsOKBody model
        list_presto_engine_catalogs_ok_body_model_json = {}
        list_presto_engine_catalogs_ok_body_model_json['catalogs'] = [catalog_model]
        list_presto_engine_catalogs_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ListPrestoEngineCatalogsOKBody by calling from_dict on the json representation
        list_presto_engine_catalogs_ok_body_model = ListPrestoEngineCatalogsOKBody.from_dict(list_presto_engine_catalogs_ok_body_model_json)
        assert list_presto_engine_catalogs_ok_body_model != False

        # Construct a model instance of ListPrestoEngineCatalogsOKBody by calling from_dict on the json representation
        list_presto_engine_catalogs_ok_body_model_dict = ListPrestoEngineCatalogsOKBody.from_dict(list_presto_engine_catalogs_ok_body_model_json).__dict__
        list_presto_engine_catalogs_ok_body_model2 = ListPrestoEngineCatalogsOKBody(**list_presto_engine_catalogs_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_presto_engine_catalogs_ok_body_model == list_presto_engine_catalogs_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_presto_engine_catalogs_ok_body_model_json2 = list_presto_engine_catalogs_ok_body_model.to_dict()
        assert list_presto_engine_catalogs_ok_body_model_json2 == list_presto_engine_catalogs_ok_body_model_json


class TestModel_ListPrestoEnginesOKBody:
    """
    Test Class for ListPrestoEnginesOKBody
    """

    def test_list_presto_engines_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListPrestoEnginesOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        node_description_model = {}  # NodeDescription
        node_description_model['node_type'] = 'bx2.4x16'
        node_description_model['quantity'] = 1

        endpoints_model = {}  # Endpoints
        endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        endpoints_model['view_history_server'] = 'testString'
        endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        engine_details_model = {}  # EngineDetails
        engine_details_model['connection_string'] = '1.2.3.4'
        engine_details_model['endpoints'] = endpoints_model
        engine_details_model['metastore_host'] = '1.2.3.4'

        presto_engine_model = {}  # PrestoEngine
        presto_engine_model['actions'] = ['view', 'use', 'update', 'select', 'access_ui', 'associate', 'disassociate', 'restart', 'pause', 'resume', 'grant', 'revoke', 'delete', 'create', 'scale']
        presto_engine_model['associated_catalogs'] = ['iceberg_data', 'hive_data']
        presto_engine_model['build_version'] = '1.1.0.0.0'
        presto_engine_model['coordinator'] = node_description_model
        presto_engine_model['created_by'] = '<username>@<domain>.com'
        presto_engine_model['created_on'] = 38
        presto_engine_model['description'] = 'presto engine for running sql queries'
        presto_engine_model['engine_details'] = engine_details_model
        presto_engine_model['engine_display_name'] = 'starter'
        presto_engine_model['engine_id'] = 'presto511'
        presto_engine_model['external_host_name'] = 'your-hostname.apps.your-domain.com'
        presto_engine_model['group_id'] = 'presto511'
        presto_engine_model['host_name'] = '1234-xyz456-abc4321.databases.appdomain.cloud'
        presto_engine_model['origin'] = 'ibm'
        presto_engine_model['port'] = 30156
        presto_engine_model['region'] = 'us-south'
        presto_engine_model['size_config'] = 'starter'
        presto_engine_model['status'] = 'running'
        presto_engine_model['status_code'] = 0
        presto_engine_model['tags'] = ['tag1', 'tag2']
        presto_engine_model['type'] = 'presto'
        presto_engine_model['version'] = 'v0.282'
        presto_engine_model['worker'] = node_description_model

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'presto engines list'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListPrestoEnginesOKBody model
        list_presto_engines_ok_body_model_json = {}
        list_presto_engines_ok_body_model_json['presto_engines'] = [presto_engine_model]
        list_presto_engines_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ListPrestoEnginesOKBody by calling from_dict on the json representation
        list_presto_engines_ok_body_model = ListPrestoEnginesOKBody.from_dict(list_presto_engines_ok_body_model_json)
        assert list_presto_engines_ok_body_model != False

        # Construct a model instance of ListPrestoEnginesOKBody by calling from_dict on the json representation
        list_presto_engines_ok_body_model_dict = ListPrestoEnginesOKBody.from_dict(list_presto_engines_ok_body_model_json).__dict__
        list_presto_engines_ok_body_model2 = ListPrestoEnginesOKBody(**list_presto_engines_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_presto_engines_ok_body_model == list_presto_engines_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_presto_engines_ok_body_model_json2 = list_presto_engines_ok_body_model.to_dict()
        assert list_presto_engines_ok_body_model_json2 == list_presto_engines_ok_body_model_json


class TestModel_ListSchemasOKBody:
    """
    Test Class for ListSchemasOKBody
    """

    def test_list_schemas_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListSchemasOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'create schema'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListSchemasOKBody model
        list_schemas_ok_body_model_json = {}
        list_schemas_ok_body_model_json['response'] = success_response_model
        list_schemas_ok_body_model_json['schemas'] = ['testString']

        # Construct a model instance of ListSchemasOKBody by calling from_dict on the json representation
        list_schemas_ok_body_model = ListSchemasOKBody.from_dict(list_schemas_ok_body_model_json)
        assert list_schemas_ok_body_model != False

        # Construct a model instance of ListSchemasOKBody by calling from_dict on the json representation
        list_schemas_ok_body_model_dict = ListSchemasOKBody.from_dict(list_schemas_ok_body_model_json).__dict__
        list_schemas_ok_body_model2 = ListSchemasOKBody(**list_schemas_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_schemas_ok_body_model == list_schemas_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_schemas_ok_body_model_json2 = list_schemas_ok_body_model.to_dict()
        assert list_schemas_ok_body_model_json2 == list_schemas_ok_body_model_json


class TestModel_ListSparkEngineApplication:
    """
    Test Class for ListSparkEngineApplication
    """

    def test_list_spark_engine_application_serialization(self):
        """
        Test serialization/deserialization for ListSparkEngineApplication
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_spark_engine_application_runtime_model = {}  # ListSparkEngineApplicationRuntime
        list_spark_engine_application_runtime_model['spark_version'] = '3.3'

        # Construct a json representation of a ListSparkEngineApplication model
        list_spark_engine_application_model_json = {}
        list_spark_engine_application_model_json['application_id'] = 'cd7cbf1f-8893-4c51-aa3d-d92729f05e99'
        list_spark_engine_application_model_json['auto_termination_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model_json['creation_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model_json['end_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model_json['failed_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model_json['finish_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model_json['id'] = 'cd7cbf1f-8893-4c51-aa3d-d92729f05e99'
        list_spark_engine_application_model_json['runtime'] = list_spark_engine_application_runtime_model
        list_spark_engine_application_model_json['spark_application_id'] = 'application_16073847388_0001'
        list_spark_engine_application_model_json['spark_application_name'] = 'testString'
        list_spark_engine_application_model_json['start_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model_json['state'] = 'RUNNING'
        list_spark_engine_application_model_json['submission_time'] = '2023-11-01T11:18:49.758Z'
        list_spark_engine_application_model_json['template_id'] = 'spark-3.3-jaas-v2-cp4d-template'

        # Construct a model instance of ListSparkEngineApplication by calling from_dict on the json representation
        list_spark_engine_application_model = ListSparkEngineApplication.from_dict(list_spark_engine_application_model_json)
        assert list_spark_engine_application_model != False

        # Construct a model instance of ListSparkEngineApplication by calling from_dict on the json representation
        list_spark_engine_application_model_dict = ListSparkEngineApplication.from_dict(list_spark_engine_application_model_json).__dict__
        list_spark_engine_application_model2 = ListSparkEngineApplication(**list_spark_engine_application_model_dict)

        # Verify the model instances are equivalent
        assert list_spark_engine_application_model == list_spark_engine_application_model2

        # Convert model instance back to dict and verify no loss of data
        list_spark_engine_application_model_json2 = list_spark_engine_application_model.to_dict()
        assert list_spark_engine_application_model_json2 == list_spark_engine_application_model_json


class TestModel_ListSparkEngineApplicationRuntime:
    """
    Test Class for ListSparkEngineApplicationRuntime
    """

    def test_list_spark_engine_application_runtime_serialization(self):
        """
        Test serialization/deserialization for ListSparkEngineApplicationRuntime
        """

        # Construct a json representation of a ListSparkEngineApplicationRuntime model
        list_spark_engine_application_runtime_model_json = {}
        list_spark_engine_application_runtime_model_json['spark_version'] = '3.3'

        # Construct a model instance of ListSparkEngineApplicationRuntime by calling from_dict on the json representation
        list_spark_engine_application_runtime_model = ListSparkEngineApplicationRuntime.from_dict(list_spark_engine_application_runtime_model_json)
        assert list_spark_engine_application_runtime_model != False

        # Construct a model instance of ListSparkEngineApplicationRuntime by calling from_dict on the json representation
        list_spark_engine_application_runtime_model_dict = ListSparkEngineApplicationRuntime.from_dict(list_spark_engine_application_runtime_model_json).__dict__
        list_spark_engine_application_runtime_model2 = ListSparkEngineApplicationRuntime(**list_spark_engine_application_runtime_model_dict)

        # Verify the model instances are equivalent
        assert list_spark_engine_application_runtime_model == list_spark_engine_application_runtime_model2

        # Convert model instance back to dict and verify no loss of data
        list_spark_engine_application_runtime_model_json2 = list_spark_engine_application_runtime_model.to_dict()
        assert list_spark_engine_application_runtime_model_json2 == list_spark_engine_application_runtime_model_json


class TestModel_ListSparkEngineApplicationsOKBody:
    """
    Test Class for ListSparkEngineApplicationsOKBody
    """

    def test_list_spark_engine_applications_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListSparkEngineApplicationsOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_spark_engine_application_runtime_model = {}  # ListSparkEngineApplicationRuntime
        list_spark_engine_application_runtime_model['spark_version'] = '3.3'

        list_spark_engine_application_model = {}  # ListSparkEngineApplication
        list_spark_engine_application_model['application_id'] = '<application_id>'
        list_spark_engine_application_model['auto_termination_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model['creation_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model['end_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model['failed_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model['finish_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model['id'] = 'cd7cbf1f-8893-4c51-aa3d-d92729f05e99'
        list_spark_engine_application_model['runtime'] = list_spark_engine_application_runtime_model
        list_spark_engine_application_model['spark_application_id'] = 'spark-application-16073847388_0001'
        list_spark_engine_application_model['spark_application_name'] = 'sample-application-name'
        list_spark_engine_application_model['start_time'] = '2020-12-08T10:00:00.000Z'
        list_spark_engine_application_model['state'] = 'running'
        list_spark_engine_application_model['submission_time'] = '2023-11-01T11:18:49.758Z'
        list_spark_engine_application_model['template_id'] = 'spark-3.3-jaas-v2-cp4d-template'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Spark engine application list'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListSparkEngineApplicationsOKBody model
        list_spark_engine_applications_ok_body_model_json = {}
        list_spark_engine_applications_ok_body_model_json['applications'] = [list_spark_engine_application_model]
        list_spark_engine_applications_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ListSparkEngineApplicationsOKBody by calling from_dict on the json representation
        list_spark_engine_applications_ok_body_model = ListSparkEngineApplicationsOKBody.from_dict(list_spark_engine_applications_ok_body_model_json)
        assert list_spark_engine_applications_ok_body_model != False

        # Construct a model instance of ListSparkEngineApplicationsOKBody by calling from_dict on the json representation
        list_spark_engine_applications_ok_body_model_dict = ListSparkEngineApplicationsOKBody.from_dict(list_spark_engine_applications_ok_body_model_json).__dict__
        list_spark_engine_applications_ok_body_model2 = ListSparkEngineApplicationsOKBody(**list_spark_engine_applications_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_spark_engine_applications_ok_body_model == list_spark_engine_applications_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_spark_engine_applications_ok_body_model_json2 = list_spark_engine_applications_ok_body_model.to_dict()
        assert list_spark_engine_applications_ok_body_model_json2 == list_spark_engine_applications_ok_body_model_json


class TestModel_ListSparkEnginesOKBody:
    """
    Test Class for ListSparkEnginesOKBody
    """

    def test_list_spark_engines_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListSparkEnginesOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Spark engines list'
        success_response_model['message_code'] = 'success'

        spark_engine_details_endpoints_model = {}  # SparkEngineDetailsEndpoints
        spark_engine_details_endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/<spark_id>/spark_applications/<application_id>'
        spark_engine_details_endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/<spark_id>/spark_history_server'
        spark_engine_details_endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        spark_engine_details_endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/<spark_id>/spark_applications'
        spark_engine_details_endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/<spark_id>/jkg/api/kernels'
        spark_engine_details_endpoints_model['view_history_server'] = 'View history server'
        spark_engine_details_endpoints_model['wxd_application_endpoint'] = '$HOST/v1/<wxd_instance_id>/engines/<engine_id>/applications'

        spark_engine_details_model = {}  # SparkEngineDetails
        spark_engine_details_model['connection_string'] = 'https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>'
        spark_engine_details_model['endpoints'] = spark_engine_details_endpoints_model

        spark_engine_model = {}  # SparkEngine
        spark_engine_model['actions'] = ['update', 'delete']
        spark_engine_model['build_version'] = '1.0.3.0.0'
        spark_engine_model['created_by'] = '<username>@<domain>.com'
        spark_engine_model['created_on'] = 163788384993
        spark_engine_model['description'] = 'Spark engines for running spark applications'
        spark_engine_model['engine_details'] = spark_engine_details_model
        spark_engine_model['engine_display_name'] = 'sampleEngine'
        spark_engine_model['engine_id'] = 'sampleEngine123'
        spark_engine_model['origin'] = 'discover'
        spark_engine_model['status'] = 'REGISTERED'
        spark_engine_model['tags'] = ['tag1', 'tag2']
        spark_engine_model['type'] = 'spark'

        # Construct a json representation of a ListSparkEnginesOKBody model
        list_spark_engines_ok_body_model_json = {}
        list_spark_engines_ok_body_model_json['response'] = success_response_model
        list_spark_engines_ok_body_model_json['spark_engines'] = [spark_engine_model]

        # Construct a model instance of ListSparkEnginesOKBody by calling from_dict on the json representation
        list_spark_engines_ok_body_model = ListSparkEnginesOKBody.from_dict(list_spark_engines_ok_body_model_json)
        assert list_spark_engines_ok_body_model != False

        # Construct a model instance of ListSparkEnginesOKBody by calling from_dict on the json representation
        list_spark_engines_ok_body_model_dict = ListSparkEnginesOKBody.from_dict(list_spark_engines_ok_body_model_json).__dict__
        list_spark_engines_ok_body_model2 = ListSparkEnginesOKBody(**list_spark_engines_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_spark_engines_ok_body_model == list_spark_engines_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_spark_engines_ok_body_model_json2 = list_spark_engines_ok_body_model.to_dict()
        assert list_spark_engines_ok_body_model_json2 == list_spark_engines_ok_body_model_json


class TestModel_ListTableSnapshotsOKBody:
    """
    Test Class for ListTableSnapshotsOKBody
    """

    def test_list_table_snapshots_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListTableSnapshotsOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'table snapshots'
        success_response_model['message_code'] = 'success'

        table_snapshot_model = {}  # TableSnapshot
        table_snapshot_model['committed_at'] = '1609379392'
        table_snapshot_model['operation'] = 'alter'
        table_snapshot_model['snapshot_id'] = '2332342122211222'
        table_snapshot_model['summary'] = {'table updated': None}

        # Construct a json representation of a ListTableSnapshotsOKBody model
        list_table_snapshots_ok_body_model_json = {}
        list_table_snapshots_ok_body_model_json['response'] = success_response_model
        list_table_snapshots_ok_body_model_json['snapshots'] = [table_snapshot_model]

        # Construct a model instance of ListTableSnapshotsOKBody by calling from_dict on the json representation
        list_table_snapshots_ok_body_model = ListTableSnapshotsOKBody.from_dict(list_table_snapshots_ok_body_model_json)
        assert list_table_snapshots_ok_body_model != False

        # Construct a model instance of ListTableSnapshotsOKBody by calling from_dict on the json representation
        list_table_snapshots_ok_body_model_dict = ListTableSnapshotsOKBody.from_dict(list_table_snapshots_ok_body_model_json).__dict__
        list_table_snapshots_ok_body_model2 = ListTableSnapshotsOKBody(**list_table_snapshots_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_table_snapshots_ok_body_model == list_table_snapshots_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_table_snapshots_ok_body_model_json2 = list_table_snapshots_ok_body_model.to_dict()
        assert list_table_snapshots_ok_body_model_json2 == list_table_snapshots_ok_body_model_json


class TestModel_ListTablesOKBody:
    """
    Test Class for ListTablesOKBody
    """

    def test_list_tables_ok_body_serialization(self):
        """
        Test serialization/deserialization for ListTablesOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'get tables'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ListTablesOKBody model
        list_tables_ok_body_model_json = {}
        list_tables_ok_body_model_json['response'] = success_response_model
        list_tables_ok_body_model_json['tables'] = ['testString']

        # Construct a model instance of ListTablesOKBody by calling from_dict on the json representation
        list_tables_ok_body_model = ListTablesOKBody.from_dict(list_tables_ok_body_model_json)
        assert list_tables_ok_body_model != False

        # Construct a model instance of ListTablesOKBody by calling from_dict on the json representation
        list_tables_ok_body_model_dict = ListTablesOKBody.from_dict(list_tables_ok_body_model_json).__dict__
        list_tables_ok_body_model2 = ListTablesOKBody(**list_tables_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert list_tables_ok_body_model == list_tables_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        list_tables_ok_body_model_json2 = list_tables_ok_body_model.to_dict()
        assert list_tables_ok_body_model_json2 == list_tables_ok_body_model_json


class TestModel_MilvusService:
    """
    Test Class for MilvusService
    """

    def test_milvus_service_serialization(self):
        """
        Test serialization/deserialization for MilvusService
        """

        # Construct a json representation of a MilvusService model
        milvus_service_model_json = {}
        milvus_service_model_json['actions'] = ['update', 'delete']
        milvus_service_model_json['created_by'] = '<username>@<domain>.com'
        milvus_service_model_json['created_on'] = 38
        milvus_service_model_json['description'] = 'milvus service for running sql queries'
        milvus_service_model_json['grpc_port'] = 26
        milvus_service_model_json['host_name'] = 'sampleMilvus'
        milvus_service_model_json['https_port'] = 26
        milvus_service_model_json['origin'] = 'native'
        milvus_service_model_json['service_display_name'] = 'sampleService'
        milvus_service_model_json['service_id'] = 'sampleService123'
        milvus_service_model_json['status'] = 'running'
        milvus_service_model_json['status_code'] = 38
        milvus_service_model_json['tags'] = ['tag1', 'tag2']
        milvus_service_model_json['type'] = 'milvus'

        # Construct a model instance of MilvusService by calling from_dict on the json representation
        milvus_service_model = MilvusService.from_dict(milvus_service_model_json)
        assert milvus_service_model != False

        # Construct a model instance of MilvusService by calling from_dict on the json representation
        milvus_service_model_dict = MilvusService.from_dict(milvus_service_model_json).__dict__
        milvus_service_model2 = MilvusService(**milvus_service_model_dict)

        # Verify the model instances are equivalent
        assert milvus_service_model == milvus_service_model2

        # Convert model instance back to dict and verify no loss of data
        milvus_service_model_json2 = milvus_service_model.to_dict()
        assert milvus_service_model_json2 == milvus_service_model_json


class TestModel_NetezzaEngine:
    """
    Test Class for NetezzaEngine
    """

    def test_netezza_engine_serialization(self):
        """
        Test serialization/deserialization for NetezzaEngine
        """

        # Construct dict forms of any model objects needed in order to build this model.

        netezza_engine_details_model = {}  # NetezzaEngineDetails
        netezza_engine_details_model['connection_string'] = '1.2.3.4'
        netezza_engine_details_model['metastore_host'] = '1.2.3.4'

        # Construct a json representation of a NetezzaEngine model
        netezza_engine_model_json = {}
        netezza_engine_model_json['actions'] = ['update', 'delete']
        netezza_engine_model_json['build_version'] = '1.0.3.0.0'
        netezza_engine_model_json['created_by'] = '<username>@<domain>.com'
        netezza_engine_model_json['created_on'] = 38
        netezza_engine_model_json['description'] = 'netezza engine for running sql queries'
        netezza_engine_model_json['engine_details'] = netezza_engine_details_model
        netezza_engine_model_json['engine_display_name'] = 'sampleEngine'
        netezza_engine_model_json['engine_id'] = 'sampleEngine123'
        netezza_engine_model_json['host_name'] = 'xyz-netezza-01-netezza-svc'
        netezza_engine_model_json['origin'] = 'ibm'
        netezza_engine_model_json['port'] = 38
        netezza_engine_model_json['status'] = 'REGISTERED'
        netezza_engine_model_json['tags'] = ['tag1', 'tag2']
        netezza_engine_model_json['type'] = 'netezza'

        # Construct a model instance of NetezzaEngine by calling from_dict on the json representation
        netezza_engine_model = NetezzaEngine.from_dict(netezza_engine_model_json)
        assert netezza_engine_model != False

        # Construct a model instance of NetezzaEngine by calling from_dict on the json representation
        netezza_engine_model_dict = NetezzaEngine.from_dict(netezza_engine_model_json).__dict__
        netezza_engine_model2 = NetezzaEngine(**netezza_engine_model_dict)

        # Verify the model instances are equivalent
        assert netezza_engine_model == netezza_engine_model2

        # Convert model instance back to dict and verify no loss of data
        netezza_engine_model_json2 = netezza_engine_model.to_dict()
        assert netezza_engine_model_json2 == netezza_engine_model_json


class TestModel_NetezzaEngineDetails:
    """
    Test Class for NetezzaEngineDetails
    """

    def test_netezza_engine_details_serialization(self):
        """
        Test serialization/deserialization for NetezzaEngineDetails
        """

        # Construct a json representation of a NetezzaEngineDetails model
        netezza_engine_details_model_json = {}
        netezza_engine_details_model_json['connection_string'] = '1.2.3.4'
        netezza_engine_details_model_json['metastore_host'] = '1.2.3.4'

        # Construct a model instance of NetezzaEngineDetails by calling from_dict on the json representation
        netezza_engine_details_model = NetezzaEngineDetails.from_dict(netezza_engine_details_model_json)
        assert netezza_engine_details_model != False

        # Construct a model instance of NetezzaEngineDetails by calling from_dict on the json representation
        netezza_engine_details_model_dict = NetezzaEngineDetails.from_dict(netezza_engine_details_model_json).__dict__
        netezza_engine_details_model2 = NetezzaEngineDetails(**netezza_engine_details_model_dict)

        # Verify the model instances are equivalent
        assert netezza_engine_details_model == netezza_engine_details_model2

        # Convert model instance back to dict and verify no loss of data
        netezza_engine_details_model_json2 = netezza_engine_details_model.to_dict()
        assert netezza_engine_details_model_json2 == netezza_engine_details_model_json


class TestModel_NodeDescription:
    """
    Test Class for NodeDescription
    """

    def test_node_description_serialization(self):
        """
        Test serialization/deserialization for NodeDescription
        """

        # Construct a json representation of a NodeDescription model
        node_description_model_json = {}
        node_description_model_json['node_type'] = 'worker'
        node_description_model_json['quantity'] = 38

        # Construct a model instance of NodeDescription by calling from_dict on the json representation
        node_description_model = NodeDescription.from_dict(node_description_model_json)
        assert node_description_model != False

        # Construct a model instance of NodeDescription by calling from_dict on the json representation
        node_description_model_dict = NodeDescription.from_dict(node_description_model_json).__dict__
        node_description_model2 = NodeDescription(**node_description_model_dict)

        # Verify the model instances are equivalent
        assert node_description_model == node_description_model2

        # Convert model instance back to dict and verify no loss of data
        node_description_model_json2 = node_description_model.to_dict()
        assert node_description_model_json2 == node_description_model_json


class TestModel_NodeDescriptionBody:
    """
    Test Class for NodeDescriptionBody
    """

    def test_node_description_body_serialization(self):
        """
        Test serialization/deserialization for NodeDescriptionBody
        """

        # Construct a json representation of a NodeDescriptionBody model
        node_description_body_model_json = {}
        node_description_body_model_json['node_type'] = 'worker'
        node_description_body_model_json['quantity'] = 38

        # Construct a model instance of NodeDescriptionBody by calling from_dict on the json representation
        node_description_body_model = NodeDescriptionBody.from_dict(node_description_body_model_json)
        assert node_description_body_model != False

        # Construct a model instance of NodeDescriptionBody by calling from_dict on the json representation
        node_description_body_model_dict = NodeDescriptionBody.from_dict(node_description_body_model_json).__dict__
        node_description_body_model2 = NodeDescriptionBody(**node_description_body_model_dict)

        # Verify the model instances are equivalent
        assert node_description_body_model == node_description_body_model2

        # Convert model instance back to dict and verify no loss of data
        node_description_body_model_json2 = node_description_body_model.to_dict()
        assert node_description_body_model_json2 == node_description_body_model_json


class TestModel_OtherEngine:
    """
    Test Class for OtherEngine
    """

    def test_other_engine_serialization(self):
        """
        Test serialization/deserialization for OtherEngine
        """

        # Construct dict forms of any model objects needed in order to build this model.

        other_engine_details_model = {}  # OtherEngineDetails
        other_engine_details_model['connection_string'] = '1.2.3.4'
        other_engine_details_model['engine_type'] = 'netezza'
        other_engine_details_model['metastore_host'] = '1.2.3.4'

        # Construct a json representation of a OtherEngine model
        other_engine_model_json = {}
        other_engine_model_json['created_by'] = '<username>@<domain>.com'
        other_engine_model_json['created_on'] = 38
        other_engine_model_json['description'] = 'engine for running sql queries'
        other_engine_model_json['engine_details'] = other_engine_details_model
        other_engine_model_json['engine_display_name'] = 'sampleEngine'
        other_engine_model_json['engine_id'] = 'sampleEngine123'
        other_engine_model_json['origin'] = 'ibm'
        other_engine_model_json['status'] = 'registered'
        other_engine_model_json['status_code'] = 38
        other_engine_model_json['tags'] = ['tag1', 'tag2']
        other_engine_model_json['type'] = 'external'

        # Construct a model instance of OtherEngine by calling from_dict on the json representation
        other_engine_model = OtherEngine.from_dict(other_engine_model_json)
        assert other_engine_model != False

        # Construct a model instance of OtherEngine by calling from_dict on the json representation
        other_engine_model_dict = OtherEngine.from_dict(other_engine_model_json).__dict__
        other_engine_model2 = OtherEngine(**other_engine_model_dict)

        # Verify the model instances are equivalent
        assert other_engine_model == other_engine_model2

        # Convert model instance back to dict and verify no loss of data
        other_engine_model_json2 = other_engine_model.to_dict()
        assert other_engine_model_json2 == other_engine_model_json


class TestModel_OtherEngineDetails:
    """
    Test Class for OtherEngineDetails
    """

    def test_other_engine_details_serialization(self):
        """
        Test serialization/deserialization for OtherEngineDetails
        """

        # Construct a json representation of a OtherEngineDetails model
        other_engine_details_model_json = {}
        other_engine_details_model_json['connection_string'] = '1.2.3.4'
        other_engine_details_model_json['engine_type'] = 'netezza'
        other_engine_details_model_json['metastore_host'] = '1.2.3.4'

        # Construct a model instance of OtherEngineDetails by calling from_dict on the json representation
        other_engine_details_model = OtherEngineDetails.from_dict(other_engine_details_model_json)
        assert other_engine_details_model != False

        # Construct a model instance of OtherEngineDetails by calling from_dict on the json representation
        other_engine_details_model_dict = OtherEngineDetails.from_dict(other_engine_details_model_json).__dict__
        other_engine_details_model2 = OtherEngineDetails(**other_engine_details_model_dict)

        # Verify the model instances are equivalent
        assert other_engine_details_model == other_engine_details_model2

        # Convert model instance back to dict and verify no loss of data
        other_engine_details_model_json2 = other_engine_details_model.to_dict()
        assert other_engine_details_model_json2 == other_engine_details_model_json


class TestModel_PrestissimoEndpoints:
    """
    Test Class for PrestissimoEndpoints
    """

    def test_prestissimo_endpoints_serialization(self):
        """
        Test serialization/deserialization for PrestissimoEndpoints
        """

        # Construct a json representation of a PrestissimoEndpoints model
        prestissimo_endpoints_model_json = {}
        prestissimo_endpoints_model_json['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        prestissimo_endpoints_model_json['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        prestissimo_endpoints_model_json['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        prestissimo_endpoints_model_json['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        prestissimo_endpoints_model_json['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        prestissimo_endpoints_model_json['view_history_server'] = 'testString'
        prestissimo_endpoints_model_json['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        # Construct a model instance of PrestissimoEndpoints by calling from_dict on the json representation
        prestissimo_endpoints_model = PrestissimoEndpoints.from_dict(prestissimo_endpoints_model_json)
        assert prestissimo_endpoints_model != False

        # Construct a model instance of PrestissimoEndpoints by calling from_dict on the json representation
        prestissimo_endpoints_model_dict = PrestissimoEndpoints.from_dict(prestissimo_endpoints_model_json).__dict__
        prestissimo_endpoints_model2 = PrestissimoEndpoints(**prestissimo_endpoints_model_dict)

        # Verify the model instances are equivalent
        assert prestissimo_endpoints_model == prestissimo_endpoints_model2

        # Convert model instance back to dict and verify no loss of data
        prestissimo_endpoints_model_json2 = prestissimo_endpoints_model.to_dict()
        assert prestissimo_endpoints_model_json2 == prestissimo_endpoints_model_json


class TestModel_PrestissimoEngine:
    """
    Test Class for PrestissimoEngine
    """

    def test_prestissimo_engine_serialization(self):
        """
        Test serialization/deserialization for PrestissimoEngine
        """

        # Construct dict forms of any model objects needed in order to build this model.

        prestissimo_node_description_body_model = {}  # PrestissimoNodeDescriptionBody
        prestissimo_node_description_body_model['node_type'] = 'worker'
        prestissimo_node_description_body_model['quantity'] = 38

        prestissimo_endpoints_model = {}  # PrestissimoEndpoints
        prestissimo_endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        prestissimo_endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        prestissimo_endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        prestissimo_endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        prestissimo_endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        prestissimo_endpoints_model['view_history_server'] = 'testString'
        prestissimo_endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        prestissimo_engine_details_model = {}  # PrestissimoEngineDetails
        prestissimo_engine_details_model['connection_string'] = '1.2.3.4'
        prestissimo_engine_details_model['endpoints'] = prestissimo_endpoints_model
        prestissimo_engine_details_model['metastore_host'] = '1.2.3.4'

        # Construct a json representation of a PrestissimoEngine model
        prestissimo_engine_model_json = {}
        prestissimo_engine_model_json['actions'] = ['update', 'delete']
        prestissimo_engine_model_json['associated_catalogs'] = ['new_catalog_1', 'new_catalog_2']
        prestissimo_engine_model_json['build_version'] = '1.0.3.0.0'
        prestissimo_engine_model_json['coordinator'] = prestissimo_node_description_body_model
        prestissimo_engine_model_json['created_by'] = '<username>@<domain>.com'
        prestissimo_engine_model_json['created_on'] = 38
        prestissimo_engine_model_json['description'] = 'prestissimo engine for running sql queries'
        prestissimo_engine_model_json['engine_details'] = prestissimo_engine_details_model
        prestissimo_engine_model_json['engine_display_name'] = 'sampleEngine'
        prestissimo_engine_model_json['engine_id'] = 'sampleEngine123'
        prestissimo_engine_model_json['external_host_name'] = 'ibm-lh-lakehouse-prestissimo-01-prestissimo-svc-cpd-instance.apps.wkclhconnectortest.cp.fyre.ibm.com'
        prestissimo_engine_model_json['group_id'] = 'new_group_id'
        prestissimo_engine_model_json['host_name'] = 'ibm-lh-lakehouse-prestissimo-01-prestissimo-svc'
        prestissimo_engine_model_json['origin'] = 'ibm'
        prestissimo_engine_model_json['port'] = 38
        prestissimo_engine_model_json['region'] = 'us-south'
        prestissimo_engine_model_json['size_config'] = 'starter'
        prestissimo_engine_model_json['status'] = 'running'
        prestissimo_engine_model_json['status_code'] = 38
        prestissimo_engine_model_json['tags'] = ['tag1', 'tag2']
        prestissimo_engine_model_json['type'] = 'prestissimo'
        prestissimo_engine_model_json['version'] = '1.2.0'
        prestissimo_engine_model_json['worker'] = prestissimo_node_description_body_model

        # Construct a model instance of PrestissimoEngine by calling from_dict on the json representation
        prestissimo_engine_model = PrestissimoEngine.from_dict(prestissimo_engine_model_json)
        assert prestissimo_engine_model != False

        # Construct a model instance of PrestissimoEngine by calling from_dict on the json representation
        prestissimo_engine_model_dict = PrestissimoEngine.from_dict(prestissimo_engine_model_json).__dict__
        prestissimo_engine_model2 = PrestissimoEngine(**prestissimo_engine_model_dict)

        # Verify the model instances are equivalent
        assert prestissimo_engine_model == prestissimo_engine_model2

        # Convert model instance back to dict and verify no loss of data
        prestissimo_engine_model_json2 = prestissimo_engine_model.to_dict()
        assert prestissimo_engine_model_json2 == prestissimo_engine_model_json


class TestModel_PrestissimoEngineDetails:
    """
    Test Class for PrestissimoEngineDetails
    """

    def test_prestissimo_engine_details_serialization(self):
        """
        Test serialization/deserialization for PrestissimoEngineDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        prestissimo_endpoints_model = {}  # PrestissimoEndpoints
        prestissimo_endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        prestissimo_endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        prestissimo_endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        prestissimo_endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        prestissimo_endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        prestissimo_endpoints_model['view_history_server'] = 'testString'
        prestissimo_endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        # Construct a json representation of a PrestissimoEngineDetails model
        prestissimo_engine_details_model_json = {}
        prestissimo_engine_details_model_json['connection_string'] = '1.2.3.4'
        prestissimo_engine_details_model_json['endpoints'] = prestissimo_endpoints_model
        prestissimo_engine_details_model_json['metastore_host'] = '1.2.3.4'

        # Construct a model instance of PrestissimoEngineDetails by calling from_dict on the json representation
        prestissimo_engine_details_model = PrestissimoEngineDetails.from_dict(prestissimo_engine_details_model_json)
        assert prestissimo_engine_details_model != False

        # Construct a model instance of PrestissimoEngineDetails by calling from_dict on the json representation
        prestissimo_engine_details_model_dict = PrestissimoEngineDetails.from_dict(prestissimo_engine_details_model_json).__dict__
        prestissimo_engine_details_model2 = PrestissimoEngineDetails(**prestissimo_engine_details_model_dict)

        # Verify the model instances are equivalent
        assert prestissimo_engine_details_model == prestissimo_engine_details_model2

        # Convert model instance back to dict and verify no loss of data
        prestissimo_engine_details_model_json2 = prestissimo_engine_details_model.to_dict()
        assert prestissimo_engine_details_model_json2 == prestissimo_engine_details_model_json


class TestModel_PrestissimoNodeDescriptionBody:
    """
    Test Class for PrestissimoNodeDescriptionBody
    """

    def test_prestissimo_node_description_body_serialization(self):
        """
        Test serialization/deserialization for PrestissimoNodeDescriptionBody
        """

        # Construct a json representation of a PrestissimoNodeDescriptionBody model
        prestissimo_node_description_body_model_json = {}
        prestissimo_node_description_body_model_json['node_type'] = 'worker'
        prestissimo_node_description_body_model_json['quantity'] = 38

        # Construct a model instance of PrestissimoNodeDescriptionBody by calling from_dict on the json representation
        prestissimo_node_description_body_model = PrestissimoNodeDescriptionBody.from_dict(prestissimo_node_description_body_model_json)
        assert prestissimo_node_description_body_model != False

        # Construct a model instance of PrestissimoNodeDescriptionBody by calling from_dict on the json representation
        prestissimo_node_description_body_model_dict = PrestissimoNodeDescriptionBody.from_dict(prestissimo_node_description_body_model_json).__dict__
        prestissimo_node_description_body_model2 = PrestissimoNodeDescriptionBody(**prestissimo_node_description_body_model_dict)

        # Verify the model instances are equivalent
        assert prestissimo_node_description_body_model == prestissimo_node_description_body_model2

        # Convert model instance back to dict and verify no loss of data
        prestissimo_node_description_body_model_json2 = prestissimo_node_description_body_model.to_dict()
        assert prestissimo_node_description_body_model_json2 == prestissimo_node_description_body_model_json


class TestModel_PrestoEngine:
    """
    Test Class for PrestoEngine
    """

    def test_presto_engine_serialization(self):
        """
        Test serialization/deserialization for PrestoEngine
        """

        # Construct dict forms of any model objects needed in order to build this model.

        node_description_model = {}  # NodeDescription
        node_description_model['node_type'] = 'worker'
        node_description_model['quantity'] = 38

        endpoints_model = {}  # Endpoints
        endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        endpoints_model['view_history_server'] = 'testString'
        endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        engine_details_model = {}  # EngineDetails
        engine_details_model['connection_string'] = '1.2.3.4'
        engine_details_model['endpoints'] = endpoints_model
        engine_details_model['metastore_host'] = '1.2.3.4'

        # Construct a json representation of a PrestoEngine model
        presto_engine_model_json = {}
        presto_engine_model_json['actions'] = ['update', 'delete']
        presto_engine_model_json['associated_catalogs'] = ['iceberg_data', 'hive_data']
        presto_engine_model_json['build_version'] = '1.0.3.0.0'
        presto_engine_model_json['coordinator'] = node_description_model
        presto_engine_model_json['created_by'] = '<username>@<domain>.com'
        presto_engine_model_json['created_on'] = 38
        presto_engine_model_json['description'] = 'presto engine for running sql queries'
        presto_engine_model_json['engine_details'] = engine_details_model
        presto_engine_model_json['engine_display_name'] = 'sampleEngine'
        presto_engine_model_json['engine_id'] = 'sampleEngine123'
        presto_engine_model_json['external_host_name'] = 'your-hostname.apps.your-domain.com'
        presto_engine_model_json['group_id'] = 'new_group_id'
        presto_engine_model_json['host_name'] = 'ibm-lh-lakehouse-presto-01-presto-svc'
        presto_engine_model_json['origin'] = 'ibm'
        presto_engine_model_json['port'] = 38
        presto_engine_model_json['region'] = 'us-south'
        presto_engine_model_json['size_config'] = 'starter'
        presto_engine_model_json['status'] = 'running'
        presto_engine_model_json['status_code'] = 38
        presto_engine_model_json['tags'] = ['tag1', 'tag2']
        presto_engine_model_json['type'] = 'presto'
        presto_engine_model_json['version'] = '1.2.0'
        presto_engine_model_json['worker'] = node_description_model

        # Construct a model instance of PrestoEngine by calling from_dict on the json representation
        presto_engine_model = PrestoEngine.from_dict(presto_engine_model_json)
        assert presto_engine_model != False

        # Construct a model instance of PrestoEngine by calling from_dict on the json representation
        presto_engine_model_dict = PrestoEngine.from_dict(presto_engine_model_json).__dict__
        presto_engine_model2 = PrestoEngine(**presto_engine_model_dict)

        # Verify the model instances are equivalent
        assert presto_engine_model == presto_engine_model2

        # Convert model instance back to dict and verify no loss of data
        presto_engine_model_json2 = presto_engine_model.to_dict()
        assert presto_engine_model_json2 == presto_engine_model_json


class TestModel_RegisterDatabaseCatalogBodyDatabaseDetails:
    """
    Test Class for RegisterDatabaseCatalogBodyDatabaseDetails
    """

    def test_register_database_catalog_body_database_details_serialization(self):
        """
        Test serialization/deserialization for RegisterDatabaseCatalogBodyDatabaseDetails
        """

        # Construct a json representation of a RegisterDatabaseCatalogBodyDatabaseDetails model
        register_database_catalog_body_database_details_model_json = {}
        register_database_catalog_body_database_details_model_json['certificate'] = 'contents of a pem/crt file'
        register_database_catalog_body_database_details_model_json['certificate_extension'] = 'pem/crt'
        register_database_catalog_body_database_details_model_json['database_name'] = 'new_database'
        register_database_catalog_body_database_details_model_json['hostname'] = 'db2@<hostname>.com'
        register_database_catalog_body_database_details_model_json['hosts'] = 'abc.com:1234,xyz.com:4321'
        register_database_catalog_body_database_details_model_json['password'] = 'samplepassword'
        register_database_catalog_body_database_details_model_json['port'] = 4553
        register_database_catalog_body_database_details_model_json['sasl'] = True
        register_database_catalog_body_database_details_model_json['ssl'] = True
        register_database_catalog_body_database_details_model_json['tables'] = 'kafka_table_name'
        register_database_catalog_body_database_details_model_json['username'] = 'sampleuser'

        # Construct a model instance of RegisterDatabaseCatalogBodyDatabaseDetails by calling from_dict on the json representation
        register_database_catalog_body_database_details_model = RegisterDatabaseCatalogBodyDatabaseDetails.from_dict(register_database_catalog_body_database_details_model_json)
        assert register_database_catalog_body_database_details_model != False

        # Construct a model instance of RegisterDatabaseCatalogBodyDatabaseDetails by calling from_dict on the json representation
        register_database_catalog_body_database_details_model_dict = RegisterDatabaseCatalogBodyDatabaseDetails.from_dict(register_database_catalog_body_database_details_model_json).__dict__
        register_database_catalog_body_database_details_model2 = RegisterDatabaseCatalogBodyDatabaseDetails(**register_database_catalog_body_database_details_model_dict)

        # Verify the model instances are equivalent
        assert register_database_catalog_body_database_details_model == register_database_catalog_body_database_details_model2

        # Convert model instance back to dict and verify no loss of data
        register_database_catalog_body_database_details_model_json2 = register_database_catalog_body_database_details_model.to_dict()
        assert register_database_catalog_body_database_details_model_json2 == register_database_catalog_body_database_details_model_json


class TestModel_RegisterDatabaseCatalogBodyDatabasePropertiesItems:
    """
    Test Class for RegisterDatabaseCatalogBodyDatabasePropertiesItems
    """

    def test_register_database_catalog_body_database_properties_items_serialization(self):
        """
        Test serialization/deserialization for RegisterDatabaseCatalogBodyDatabasePropertiesItems
        """

        # Construct a json representation of a RegisterDatabaseCatalogBodyDatabasePropertiesItems model
        register_database_catalog_body_database_properties_items_model_json = {}
        register_database_catalog_body_database_properties_items_model_json['encrypt'] = True
        register_database_catalog_body_database_properties_items_model_json['key'] = 'hive.metastore'
        register_database_catalog_body_database_properties_items_model_json['value'] = 'glue'

        # Construct a model instance of RegisterDatabaseCatalogBodyDatabasePropertiesItems by calling from_dict on the json representation
        register_database_catalog_body_database_properties_items_model = RegisterDatabaseCatalogBodyDatabasePropertiesItems.from_dict(register_database_catalog_body_database_properties_items_model_json)
        assert register_database_catalog_body_database_properties_items_model != False

        # Construct a model instance of RegisterDatabaseCatalogBodyDatabasePropertiesItems by calling from_dict on the json representation
        register_database_catalog_body_database_properties_items_model_dict = RegisterDatabaseCatalogBodyDatabasePropertiesItems.from_dict(register_database_catalog_body_database_properties_items_model_json).__dict__
        register_database_catalog_body_database_properties_items_model2 = RegisterDatabaseCatalogBodyDatabasePropertiesItems(**register_database_catalog_body_database_properties_items_model_dict)

        # Verify the model instances are equivalent
        assert register_database_catalog_body_database_properties_items_model == register_database_catalog_body_database_properties_items_model2

        # Convert model instance back to dict and verify no loss of data
        register_database_catalog_body_database_properties_items_model_json2 = register_database_catalog_body_database_properties_items_model.to_dict()
        assert register_database_catalog_body_database_properties_items_model_json2 == register_database_catalog_body_database_properties_items_model_json


class TestModel_ReplacePrestoEngineCatalogsCreatedBody:
    """
    Test Class for ReplacePrestoEngineCatalogsCreatedBody
    """

    def test_replace_presto_engine_catalogs_created_body_serialization(self):
        """
        Test serialization/deserialization for ReplacePrestoEngineCatalogsCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        catalog_model = {}  # Catalog
        catalog_model['catalog_name'] = 'iceberg_data'
        catalog_model['creation_date'] = '16073847388'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'get engine catalogs'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ReplacePrestoEngineCatalogsCreatedBody model
        replace_presto_engine_catalogs_created_body_model_json = {}
        replace_presto_engine_catalogs_created_body_model_json['catalogs'] = [catalog_model]
        replace_presto_engine_catalogs_created_body_model_json['response'] = success_response_model

        # Construct a model instance of ReplacePrestoEngineCatalogsCreatedBody by calling from_dict on the json representation
        replace_presto_engine_catalogs_created_body_model = ReplacePrestoEngineCatalogsCreatedBody.from_dict(replace_presto_engine_catalogs_created_body_model_json)
        assert replace_presto_engine_catalogs_created_body_model != False

        # Construct a model instance of ReplacePrestoEngineCatalogsCreatedBody by calling from_dict on the json representation
        replace_presto_engine_catalogs_created_body_model_dict = ReplacePrestoEngineCatalogsCreatedBody.from_dict(replace_presto_engine_catalogs_created_body_model_json).__dict__
        replace_presto_engine_catalogs_created_body_model2 = ReplacePrestoEngineCatalogsCreatedBody(**replace_presto_engine_catalogs_created_body_model_dict)

        # Verify the model instances are equivalent
        assert replace_presto_engine_catalogs_created_body_model == replace_presto_engine_catalogs_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        replace_presto_engine_catalogs_created_body_model_json2 = replace_presto_engine_catalogs_created_body_model.to_dict()
        assert replace_presto_engine_catalogs_created_body_model_json2 == replace_presto_engine_catalogs_created_body_model_json


class TestModel_ReplaceSnapshotCreatedBody:
    """
    Test Class for ReplaceSnapshotCreatedBody
    """

    def test_replace_snapshot_created_body_serialization(self):
        """
        Test serialization/deserialization for ReplaceSnapshotCreatedBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'rollback snapshots'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ReplaceSnapshotCreatedBody model
        replace_snapshot_created_body_model_json = {}
        replace_snapshot_created_body_model_json['response'] = success_response_model

        # Construct a model instance of ReplaceSnapshotCreatedBody by calling from_dict on the json representation
        replace_snapshot_created_body_model = ReplaceSnapshotCreatedBody.from_dict(replace_snapshot_created_body_model_json)
        assert replace_snapshot_created_body_model != False

        # Construct a model instance of ReplaceSnapshotCreatedBody by calling from_dict on the json representation
        replace_snapshot_created_body_model_dict = ReplaceSnapshotCreatedBody.from_dict(replace_snapshot_created_body_model_json).__dict__
        replace_snapshot_created_body_model2 = ReplaceSnapshotCreatedBody(**replace_snapshot_created_body_model_dict)

        # Verify the model instances are equivalent
        assert replace_snapshot_created_body_model == replace_snapshot_created_body_model2

        # Convert model instance back to dict and verify no loss of data
        replace_snapshot_created_body_model_json2 = replace_snapshot_created_body_model.to_dict()
        assert replace_snapshot_created_body_model_json2 == replace_snapshot_created_body_model_json


class TestModel_RunExplainAnalyzeStatementOKBody:
    """
    Test Class for RunExplainAnalyzeStatementOKBody
    """

    def test_run_explain_analyze_statement_ok_body_serialization(self):
        """
        Test serialization/deserialization for RunExplainAnalyzeStatementOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'explain analyze'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a RunExplainAnalyzeStatementOKBody model
        run_explain_analyze_statement_ok_body_model_json = {}
        run_explain_analyze_statement_ok_body_model_json['response'] = success_response_model
        run_explain_analyze_statement_ok_body_model_json['result'] = 'testString'

        # Construct a model instance of RunExplainAnalyzeStatementOKBody by calling from_dict on the json representation
        run_explain_analyze_statement_ok_body_model = RunExplainAnalyzeStatementOKBody.from_dict(run_explain_analyze_statement_ok_body_model_json)
        assert run_explain_analyze_statement_ok_body_model != False

        # Construct a model instance of RunExplainAnalyzeStatementOKBody by calling from_dict on the json representation
        run_explain_analyze_statement_ok_body_model_dict = RunExplainAnalyzeStatementOKBody.from_dict(run_explain_analyze_statement_ok_body_model_json).__dict__
        run_explain_analyze_statement_ok_body_model2 = RunExplainAnalyzeStatementOKBody(**run_explain_analyze_statement_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert run_explain_analyze_statement_ok_body_model == run_explain_analyze_statement_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        run_explain_analyze_statement_ok_body_model_json2 = run_explain_analyze_statement_ok_body_model.to_dict()
        assert run_explain_analyze_statement_ok_body_model_json2 == run_explain_analyze_statement_ok_body_model_json


class TestModel_RunExplainStatementOKBody:
    """
    Test Class for RunExplainStatementOKBody
    """

    def test_run_explain_statement_ok_body_serialization(self):
        """
        Test serialization/deserialization for RunExplainStatementOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'explain statement'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a RunExplainStatementOKBody model
        run_explain_statement_ok_body_model_json = {}
        run_explain_statement_ok_body_model_json['response'] = success_response_model
        run_explain_statement_ok_body_model_json['result'] = 'testString'

        # Construct a model instance of RunExplainStatementOKBody by calling from_dict on the json representation
        run_explain_statement_ok_body_model = RunExplainStatementOKBody.from_dict(run_explain_statement_ok_body_model_json)
        assert run_explain_statement_ok_body_model != False

        # Construct a model instance of RunExplainStatementOKBody by calling from_dict on the json representation
        run_explain_statement_ok_body_model_dict = RunExplainStatementOKBody.from_dict(run_explain_statement_ok_body_model_json).__dict__
        run_explain_statement_ok_body_model2 = RunExplainStatementOKBody(**run_explain_statement_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert run_explain_statement_ok_body_model == run_explain_statement_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        run_explain_statement_ok_body_model_json2 = run_explain_statement_ok_body_model.to_dict()
        assert run_explain_statement_ok_body_model_json2 == run_explain_statement_ok_body_model_json


class TestModel_SparkApplicationDetails:
    """
    Test Class for SparkApplicationDetails
    """

    def test_spark_application_details_serialization(self):
        """
        Test serialization/deserialization for SparkApplicationDetails
        """

        # Construct a json representation of a SparkApplicationDetails model
        spark_application_details_model_json = {}
        spark_application_details_model_json['application'] = 's3://mybucket/wordcount.py'
        spark_application_details_model_json['arguments'] = ['people.txt']
        spark_application_details_model_json['conf'] = {'key1': 'key:value'}
        spark_application_details_model_json['env'] = {'key1': 'key:value'}
        spark_application_details_model_json['name'] = 'SparkApplicaton1'

        # Construct a model instance of SparkApplicationDetails by calling from_dict on the json representation
        spark_application_details_model = SparkApplicationDetails.from_dict(spark_application_details_model_json)
        assert spark_application_details_model != False

        # Construct a model instance of SparkApplicationDetails by calling from_dict on the json representation
        spark_application_details_model_dict = SparkApplicationDetails.from_dict(spark_application_details_model_json).__dict__
        spark_application_details_model2 = SparkApplicationDetails(**spark_application_details_model_dict)

        # Verify the model instances are equivalent
        assert spark_application_details_model == spark_application_details_model2

        # Convert model instance back to dict and verify no loss of data
        spark_application_details_model_json2 = spark_application_details_model.to_dict()
        assert spark_application_details_model_json2 == spark_application_details_model_json


class TestModel_SparkEngine:
    """
    Test Class for SparkEngine
    """

    def test_spark_engine_serialization(self):
        """
        Test serialization/deserialization for SparkEngine
        """

        # Construct dict forms of any model objects needed in order to build this model.

        spark_engine_details_endpoints_model = {}  # SparkEngineDetailsEndpoints
        spark_engine_details_endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        spark_engine_details_endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        spark_engine_details_endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        spark_engine_details_endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        spark_engine_details_endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        spark_engine_details_endpoints_model['view_history_server'] = 'testString'
        spark_engine_details_endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        spark_engine_details_model = {}  # SparkEngineDetails
        spark_engine_details_model['connection_string'] = 'https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>'
        spark_engine_details_model['endpoints'] = spark_engine_details_endpoints_model

        # Construct a json representation of a SparkEngine model
        spark_engine_model_json = {}
        spark_engine_model_json['actions'] = ['update', 'delete']
        spark_engine_model_json['build_version'] = '1.0.3.0.0'
        spark_engine_model_json['created_by'] = '<username>@<domain>.com'
        spark_engine_model_json['created_on'] = 38
        spark_engine_model_json['description'] = 'spark engine for running sql queries'
        spark_engine_model_json['engine_details'] = spark_engine_details_model
        spark_engine_model_json['engine_display_name'] = 'sampleEngine'
        spark_engine_model_json['engine_id'] = 'sampleEngine123'
        spark_engine_model_json['origin'] = 'ibm'
        spark_engine_model_json['status'] = 'Registered'
        spark_engine_model_json['tags'] = ['tag1', 'tag2']
        spark_engine_model_json['type'] = 'spark'

        # Construct a model instance of SparkEngine by calling from_dict on the json representation
        spark_engine_model = SparkEngine.from_dict(spark_engine_model_json)
        assert spark_engine_model != False

        # Construct a model instance of SparkEngine by calling from_dict on the json representation
        spark_engine_model_dict = SparkEngine.from_dict(spark_engine_model_json).__dict__
        spark_engine_model2 = SparkEngine(**spark_engine_model_dict)

        # Verify the model instances are equivalent
        assert spark_engine_model == spark_engine_model2

        # Convert model instance back to dict and verify no loss of data
        spark_engine_model_json2 = spark_engine_model.to_dict()
        assert spark_engine_model_json2 == spark_engine_model_json


class TestModel_SparkEngineApplication:
    """
    Test Class for SparkEngineApplication
    """

    def test_spark_engine_application_serialization(self):
        """
        Test serialization/deserialization for SparkEngineApplication
        """

        # Construct a json representation of a SparkEngineApplication model
        spark_engine_application_model_json = {}
        spark_engine_application_model_json['application_id'] = '23c99c14-3af8-467d-9703-cc8163c60d35'
        spark_engine_application_model_json['id'] = 'cd7cbf1f-8893-4c51-aa3d-d92729f05e99'
        spark_engine_application_model_json['state'] = 'ACCEPTED'

        # Construct a model instance of SparkEngineApplication by calling from_dict on the json representation
        spark_engine_application_model = SparkEngineApplication.from_dict(spark_engine_application_model_json)
        assert spark_engine_application_model != False

        # Construct a model instance of SparkEngineApplication by calling from_dict on the json representation
        spark_engine_application_model_dict = SparkEngineApplication.from_dict(spark_engine_application_model_json).__dict__
        spark_engine_application_model2 = SparkEngineApplication(**spark_engine_application_model_dict)

        # Verify the model instances are equivalent
        assert spark_engine_application_model == spark_engine_application_model2

        # Convert model instance back to dict and verify no loss of data
        spark_engine_application_model_json2 = spark_engine_application_model.to_dict()
        assert spark_engine_application_model_json2 == spark_engine_application_model_json


class TestModel_SparkEngineApplicationStatus:
    """
    Test Class for SparkEngineApplicationStatus
    """

    def test_spark_engine_application_status_serialization(self):
        """
        Test serialization/deserialization for SparkEngineApplicationStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        spark_engine_application_status_application_details_conf_model = {}  # SparkEngineApplicationStatusApplicationDetailsConf
        spark_engine_application_status_application_details_conf_model['spark_app_name'] = 'MyJob'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_client_auth_mode'] = 'PLAIN'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_client_plain_password'] = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_client_plain_username'] = 'ibm_lh_token_admin'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_truststore_password'] = 'changeit'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_truststore_path'] = 'file:///opt/ibm/jdk/lib/security/cacerts'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_truststore_type'] = 'JKS'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_use_ssl'] = 'true'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_implementation'] = 'hive'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_lakehouse'] = 'org.apache.iceberg.spark.SparkCatalog'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_lakehouse_type'] = 'hive'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_lakehouse_uri'] = 'testString'
        spark_engine_application_status_application_details_conf_model['spark_sql_extensions'] = 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions'
        spark_engine_application_status_application_details_conf_model['spark_sql_iceberg_vectorization_enabled'] = 'false'

        spark_engine_application_status_application_details_model = {}  # SparkEngineApplicationStatusApplicationDetails
        spark_engine_application_status_application_details_model['application'] = '/opt/ibm/spark/examples/src/main/python/wordcount.py'
        spark_engine_application_status_application_details_model['arguments'] = ['testString']
        spark_engine_application_status_application_details_model['conf'] = spark_engine_application_status_application_details_conf_model
        spark_engine_application_status_application_details_model['env'] = {'anyKey': 'anyValue'}
        spark_engine_application_status_application_details_model['name'] = 'SparkApplication1'

        spark_engine_application_status_state_details_items_model = {}  # SparkEngineApplicationStatusStateDetailsItems
        spark_engine_application_status_state_details_items_model['code'] = 'testString'
        spark_engine_application_status_state_details_items_model['message'] = 'testString'
        spark_engine_application_status_state_details_items_model['type'] = 'testString'

        # Construct a json representation of a SparkEngineApplicationStatus model
        spark_engine_application_status_model_json = {}
        spark_engine_application_status_model_json['application_details'] = spark_engine_application_status_application_details_model
        spark_engine_application_status_model_json['application_id'] = 'cd7cbf1f-8893-4c51-aa3d-d92729f05e99'
        spark_engine_application_status_model_json['auto_termination_time'] = '2020-12-08T10:00:00.000Z'
        spark_engine_application_status_model_json['creation_time'] = 'Saturday 28 October 2023 07:17:06.856+0000'
        spark_engine_application_status_model_json['deploy_mode'] = 'stand-alone'
        spark_engine_application_status_model_json['end_time'] = '2020-12-08T10:00:00.000Z'
        spark_engine_application_status_model_json['failed_time'] = 'testString'
        spark_engine_application_status_model_json['finish_time'] = 'Saturday 28 October 2023 07:17:38.966+0000'
        spark_engine_application_status_model_json['id'] = 'cd7cbf1f-8893-4c51-aa3d-d92729f05e99'
        spark_engine_application_status_model_json['return_code'] = '0'
        spark_engine_application_status_model_json['spark_application_id'] = 'app-20231028071726-0000'
        spark_engine_application_status_model_json['spark_application_name'] = 'PythonWordCount'
        spark_engine_application_status_model_json['start_time'] = 'Saturday 28 October 2023 07:17:26.649+0000'
        spark_engine_application_status_model_json['state'] = 'FINISHED'
        spark_engine_application_status_model_json['state_details'] = [spark_engine_application_status_state_details_items_model]
        spark_engine_application_status_model_json['submission_time'] = '2023-11-01T11:18:49.758Z'
        spark_engine_application_status_model_json['template_id'] = 'spark-3.3-jaas-v2-cp4d-template'

        # Construct a model instance of SparkEngineApplicationStatus by calling from_dict on the json representation
        spark_engine_application_status_model = SparkEngineApplicationStatus.from_dict(spark_engine_application_status_model_json)
        assert spark_engine_application_status_model != False

        # Construct a model instance of SparkEngineApplicationStatus by calling from_dict on the json representation
        spark_engine_application_status_model_dict = SparkEngineApplicationStatus.from_dict(spark_engine_application_status_model_json).__dict__
        spark_engine_application_status_model2 = SparkEngineApplicationStatus(**spark_engine_application_status_model_dict)

        # Verify the model instances are equivalent
        assert spark_engine_application_status_model == spark_engine_application_status_model2

        # Convert model instance back to dict and verify no loss of data
        spark_engine_application_status_model_json2 = spark_engine_application_status_model.to_dict()
        assert spark_engine_application_status_model_json2 == spark_engine_application_status_model_json


class TestModel_SparkEngineApplicationStatusApplicationDetails:
    """
    Test Class for SparkEngineApplicationStatusApplicationDetails
    """

    def test_spark_engine_application_status_application_details_serialization(self):
        """
        Test serialization/deserialization for SparkEngineApplicationStatusApplicationDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        spark_engine_application_status_application_details_conf_model = {}  # SparkEngineApplicationStatusApplicationDetailsConf
        spark_engine_application_status_application_details_conf_model['spark_app_name'] = 'MyJob'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_client_auth_mode'] = 'PLAIN'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_client_plain_password'] = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_client_plain_username'] = 'ibm_lh_token_admin'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_truststore_password'] = 'changeit'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_truststore_path'] = 'file:///opt/ibm/jdk/lib/security/cacerts'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_truststore_type'] = 'JKS'
        spark_engine_application_status_application_details_conf_model['spark_hive_metastore_use_ssl'] = 'true'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_implementation'] = 'hive'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_lakehouse'] = 'org.apache.iceberg.spark.SparkCatalog'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_lakehouse_type'] = 'hive'
        spark_engine_application_status_application_details_conf_model['spark_sql_catalog_lakehouse_uri'] = 'testString'
        spark_engine_application_status_application_details_conf_model['spark_sql_extensions'] = 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions'
        spark_engine_application_status_application_details_conf_model['spark_sql_iceberg_vectorization_enabled'] = 'false'

        # Construct a json representation of a SparkEngineApplicationStatusApplicationDetails model
        spark_engine_application_status_application_details_model_json = {}
        spark_engine_application_status_application_details_model_json['application'] = '/opt/ibm/spark/examples/src/main/python/wordcount.py'
        spark_engine_application_status_application_details_model_json['arguments'] = ['testString']
        spark_engine_application_status_application_details_model_json['conf'] = spark_engine_application_status_application_details_conf_model
        spark_engine_application_status_application_details_model_json['env'] = {'anyKey': 'anyValue'}
        spark_engine_application_status_application_details_model_json['name'] = 'SparkApplication1'

        # Construct a model instance of SparkEngineApplicationStatusApplicationDetails by calling from_dict on the json representation
        spark_engine_application_status_application_details_model = SparkEngineApplicationStatusApplicationDetails.from_dict(spark_engine_application_status_application_details_model_json)
        assert spark_engine_application_status_application_details_model != False

        # Construct a model instance of SparkEngineApplicationStatusApplicationDetails by calling from_dict on the json representation
        spark_engine_application_status_application_details_model_dict = SparkEngineApplicationStatusApplicationDetails.from_dict(spark_engine_application_status_application_details_model_json).__dict__
        spark_engine_application_status_application_details_model2 = SparkEngineApplicationStatusApplicationDetails(**spark_engine_application_status_application_details_model_dict)

        # Verify the model instances are equivalent
        assert spark_engine_application_status_application_details_model == spark_engine_application_status_application_details_model2

        # Convert model instance back to dict and verify no loss of data
        spark_engine_application_status_application_details_model_json2 = spark_engine_application_status_application_details_model.to_dict()
        assert spark_engine_application_status_application_details_model_json2 == spark_engine_application_status_application_details_model_json


class TestModel_SparkEngineApplicationStatusApplicationDetailsConf:
    """
    Test Class for SparkEngineApplicationStatusApplicationDetailsConf
    """

    def test_spark_engine_application_status_application_details_conf_serialization(self):
        """
        Test serialization/deserialization for SparkEngineApplicationStatusApplicationDetailsConf
        """

        # Construct a json representation of a SparkEngineApplicationStatusApplicationDetailsConf model
        spark_engine_application_status_application_details_conf_model_json = {}
        spark_engine_application_status_application_details_conf_model_json['spark_app_name'] = 'MyJob'
        spark_engine_application_status_application_details_conf_model_json['spark_hive_metastore_client_auth_mode'] = 'PLAIN'
        spark_engine_application_status_application_details_conf_model_json['spark_hive_metastore_client_plain_password'] = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...'
        spark_engine_application_status_application_details_conf_model_json['spark_hive_metastore_client_plain_username'] = 'ibm_lh_token_admin'
        spark_engine_application_status_application_details_conf_model_json['spark_hive_metastore_truststore_password'] = 'changeit'
        spark_engine_application_status_application_details_conf_model_json['spark_hive_metastore_truststore_path'] = 'file:///opt/ibm/jdk/lib/security/cacerts'
        spark_engine_application_status_application_details_conf_model_json['spark_hive_metastore_truststore_type'] = 'JKS'
        spark_engine_application_status_application_details_conf_model_json['spark_hive_metastore_use_ssl'] = 'true'
        spark_engine_application_status_application_details_conf_model_json['spark_sql_catalog_implementation'] = 'hive'
        spark_engine_application_status_application_details_conf_model_json['spark_sql_catalog_lakehouse'] = 'org.apache.iceberg.spark.SparkCatalog'
        spark_engine_application_status_application_details_conf_model_json['spark_sql_catalog_lakehouse_type'] = 'hive'
        spark_engine_application_status_application_details_conf_model_json['spark_sql_catalog_lakehouse_uri'] = 'testString'
        spark_engine_application_status_application_details_conf_model_json['spark_sql_extensions'] = 'org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions'
        spark_engine_application_status_application_details_conf_model_json['spark_sql_iceberg_vectorization_enabled'] = 'false'

        # Construct a model instance of SparkEngineApplicationStatusApplicationDetailsConf by calling from_dict on the json representation
        spark_engine_application_status_application_details_conf_model = SparkEngineApplicationStatusApplicationDetailsConf.from_dict(spark_engine_application_status_application_details_conf_model_json)
        assert spark_engine_application_status_application_details_conf_model != False

        # Construct a model instance of SparkEngineApplicationStatusApplicationDetailsConf by calling from_dict on the json representation
        spark_engine_application_status_application_details_conf_model_dict = SparkEngineApplicationStatusApplicationDetailsConf.from_dict(spark_engine_application_status_application_details_conf_model_json).__dict__
        spark_engine_application_status_application_details_conf_model2 = SparkEngineApplicationStatusApplicationDetailsConf(**spark_engine_application_status_application_details_conf_model_dict)

        # Verify the model instances are equivalent
        assert spark_engine_application_status_application_details_conf_model == spark_engine_application_status_application_details_conf_model2

        # Convert model instance back to dict and verify no loss of data
        spark_engine_application_status_application_details_conf_model_json2 = spark_engine_application_status_application_details_conf_model.to_dict()
        assert spark_engine_application_status_application_details_conf_model_json2 == spark_engine_application_status_application_details_conf_model_json


class TestModel_SparkEngineApplicationStatusStateDetailsItems:
    """
    Test Class for SparkEngineApplicationStatusStateDetailsItems
    """

    def test_spark_engine_application_status_state_details_items_serialization(self):
        """
        Test serialization/deserialization for SparkEngineApplicationStatusStateDetailsItems
        """

        # Construct a json representation of a SparkEngineApplicationStatusStateDetailsItems model
        spark_engine_application_status_state_details_items_model_json = {}
        spark_engine_application_status_state_details_items_model_json['code'] = 'testString'
        spark_engine_application_status_state_details_items_model_json['message'] = 'testString'
        spark_engine_application_status_state_details_items_model_json['type'] = 'testString'

        # Construct a model instance of SparkEngineApplicationStatusStateDetailsItems by calling from_dict on the json representation
        spark_engine_application_status_state_details_items_model = SparkEngineApplicationStatusStateDetailsItems.from_dict(spark_engine_application_status_state_details_items_model_json)
        assert spark_engine_application_status_state_details_items_model != False

        # Construct a model instance of SparkEngineApplicationStatusStateDetailsItems by calling from_dict on the json representation
        spark_engine_application_status_state_details_items_model_dict = SparkEngineApplicationStatusStateDetailsItems.from_dict(spark_engine_application_status_state_details_items_model_json).__dict__
        spark_engine_application_status_state_details_items_model2 = SparkEngineApplicationStatusStateDetailsItems(**spark_engine_application_status_state_details_items_model_dict)

        # Verify the model instances are equivalent
        assert spark_engine_application_status_state_details_items_model == spark_engine_application_status_state_details_items_model2

        # Convert model instance back to dict and verify no loss of data
        spark_engine_application_status_state_details_items_model_json2 = spark_engine_application_status_state_details_items_model.to_dict()
        assert spark_engine_application_status_state_details_items_model_json2 == spark_engine_application_status_state_details_items_model_json


class TestModel_SparkEngineDetails:
    """
    Test Class for SparkEngineDetails
    """

    def test_spark_engine_details_serialization(self):
        """
        Test serialization/deserialization for SparkEngineDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        spark_engine_details_endpoints_model = {}  # SparkEngineDetailsEndpoints
        spark_engine_details_endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        spark_engine_details_endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        spark_engine_details_endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        spark_engine_details_endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        spark_engine_details_endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        spark_engine_details_endpoints_model['view_history_server'] = 'testString'
        spark_engine_details_endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        # Construct a json representation of a SparkEngineDetails model
        spark_engine_details_model_json = {}
        spark_engine_details_model_json['connection_string'] = 'https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>'
        spark_engine_details_model_json['endpoints'] = spark_engine_details_endpoints_model

        # Construct a model instance of SparkEngineDetails by calling from_dict on the json representation
        spark_engine_details_model = SparkEngineDetails.from_dict(spark_engine_details_model_json)
        assert spark_engine_details_model != False

        # Construct a model instance of SparkEngineDetails by calling from_dict on the json representation
        spark_engine_details_model_dict = SparkEngineDetails.from_dict(spark_engine_details_model_json).__dict__
        spark_engine_details_model2 = SparkEngineDetails(**spark_engine_details_model_dict)

        # Verify the model instances are equivalent
        assert spark_engine_details_model == spark_engine_details_model2

        # Convert model instance back to dict and verify no loss of data
        spark_engine_details_model_json2 = spark_engine_details_model.to_dict()
        assert spark_engine_details_model_json2 == spark_engine_details_model_json


class TestModel_SparkEngineDetailsEndpoints:
    """
    Test Class for SparkEngineDetailsEndpoints
    """

    def test_spark_engine_details_endpoints_serialization(self):
        """
        Test serialization/deserialization for SparkEngineDetailsEndpoints
        """

        # Construct a json representation of a SparkEngineDetailsEndpoints model
        spark_engine_details_endpoints_model_json = {}
        spark_engine_details_endpoints_model_json['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        spark_engine_details_endpoints_model_json['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        spark_engine_details_endpoints_model_json['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        spark_engine_details_endpoints_model_json['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        spark_engine_details_endpoints_model_json['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        spark_engine_details_endpoints_model_json['view_history_server'] = 'testString'
        spark_engine_details_endpoints_model_json['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        # Construct a model instance of SparkEngineDetailsEndpoints by calling from_dict on the json representation
        spark_engine_details_endpoints_model = SparkEngineDetailsEndpoints.from_dict(spark_engine_details_endpoints_model_json)
        assert spark_engine_details_endpoints_model != False

        # Construct a model instance of SparkEngineDetailsEndpoints by calling from_dict on the json representation
        spark_engine_details_endpoints_model_dict = SparkEngineDetailsEndpoints.from_dict(spark_engine_details_endpoints_model_json).__dict__
        spark_engine_details_endpoints_model2 = SparkEngineDetailsEndpoints(**spark_engine_details_endpoints_model_dict)

        # Verify the model instances are equivalent
        assert spark_engine_details_endpoints_model == spark_engine_details_endpoints_model2

        # Convert model instance back to dict and verify no loss of data
        spark_engine_details_endpoints_model_json2 = spark_engine_details_endpoints_model.to_dict()
        assert spark_engine_details_endpoints_model_json2 == spark_engine_details_endpoints_model_json


class TestModel_SparkEngineDetailsPrototype:
    """
    Test Class for SparkEngineDetailsPrototype
    """

    def test_spark_engine_details_prototype_serialization(self):
        """
        Test serialization/deserialization for SparkEngineDetailsPrototype
        """

        # Construct a json representation of a SparkEngineDetailsPrototype model
        spark_engine_details_prototype_model_json = {}
        spark_engine_details_prototype_model_json['api_key'] = 'apikey'
        spark_engine_details_prototype_model_json['connection_string'] = '1.2.3.4'
        spark_engine_details_prototype_model_json['instance_id'] = 'spark-id'
        spark_engine_details_prototype_model_json['managed_by'] = 'fully/self'

        # Construct a model instance of SparkEngineDetailsPrototype by calling from_dict on the json representation
        spark_engine_details_prototype_model = SparkEngineDetailsPrototype.from_dict(spark_engine_details_prototype_model_json)
        assert spark_engine_details_prototype_model != False

        # Construct a model instance of SparkEngineDetailsPrototype by calling from_dict on the json representation
        spark_engine_details_prototype_model_dict = SparkEngineDetailsPrototype.from_dict(spark_engine_details_prototype_model_json).__dict__
        spark_engine_details_prototype_model2 = SparkEngineDetailsPrototype(**spark_engine_details_prototype_model_dict)

        # Verify the model instances are equivalent
        assert spark_engine_details_prototype_model == spark_engine_details_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        spark_engine_details_prototype_model_json2 = spark_engine_details_prototype_model.to_dict()
        assert spark_engine_details_prototype_model_json2 == spark_engine_details_prototype_model_json


class TestModel_SuccessResponse:
    """
    Test Class for SuccessResponse
    """

    def test_success_response_serialization(self):
        """
        Test serialization/deserialization for SuccessResponse
        """

        # Construct a json representation of a SuccessResponse model
        success_response_model_json = {}
        success_response_model_json['message'] = 'Successful message'
        success_response_model_json['message_code'] = 'successfulCode'

        # Construct a model instance of SuccessResponse by calling from_dict on the json representation
        success_response_model = SuccessResponse.from_dict(success_response_model_json)
        assert success_response_model != False

        # Construct a model instance of SuccessResponse by calling from_dict on the json representation
        success_response_model_dict = SuccessResponse.from_dict(success_response_model_json).__dict__
        success_response_model2 = SuccessResponse(**success_response_model_dict)

        # Verify the model instances are equivalent
        assert success_response_model == success_response_model2

        # Convert model instance back to dict and verify no loss of data
        success_response_model_json2 = success_response_model.to_dict()
        assert success_response_model_json2 == success_response_model_json


class TestModel_TableSnapshot:
    """
    Test Class for TableSnapshot
    """

    def test_table_snapshot_serialization(self):
        """
        Test serialization/deserialization for TableSnapshot
        """

        # Construct a json representation of a TableSnapshot model
        table_snapshot_model_json = {}
        table_snapshot_model_json['committed_at'] = '1609379392'
        table_snapshot_model_json['operation'] = 'alter'
        table_snapshot_model_json['snapshot_id'] = '2332342122211222'
        table_snapshot_model_json['summary'] = {'anyKey': 'anyValue'}

        # Construct a model instance of TableSnapshot by calling from_dict on the json representation
        table_snapshot_model = TableSnapshot.from_dict(table_snapshot_model_json)
        assert table_snapshot_model != False

        # Construct a model instance of TableSnapshot by calling from_dict on the json representation
        table_snapshot_model_dict = TableSnapshot.from_dict(table_snapshot_model_json).__dict__
        table_snapshot_model2 = TableSnapshot(**table_snapshot_model_dict)

        # Verify the model instances are equivalent
        assert table_snapshot_model == table_snapshot_model2

        # Convert model instance back to dict and verify no loss of data
        table_snapshot_model_json2 = table_snapshot_model.to_dict()
        assert table_snapshot_model_json2 == table_snapshot_model_json


class TestModel_TestBucketConnectionOKBody:
    """
    Test Class for TestBucketConnectionOKBody
    """

    def test_test_bucket_connection_ok_body_serialization(self):
        """
        Test serialization/deserialization for TestBucketConnectionOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bucket_status_response_model = {}  # BucketStatusResponse
        bucket_status_response_model['state'] = True
        bucket_status_response_model['state_message'] = 'Credentials provided for <bucket-name> bucket are correct.'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Test bucket connection'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a TestBucketConnectionOKBody model
        test_bucket_connection_ok_body_model_json = {}
        test_bucket_connection_ok_body_model_json['bucket_status'] = bucket_status_response_model
        test_bucket_connection_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of TestBucketConnectionOKBody by calling from_dict on the json representation
        test_bucket_connection_ok_body_model = TestBucketConnectionOKBody.from_dict(test_bucket_connection_ok_body_model_json)
        assert test_bucket_connection_ok_body_model != False

        # Construct a model instance of TestBucketConnectionOKBody by calling from_dict on the json representation
        test_bucket_connection_ok_body_model_dict = TestBucketConnectionOKBody.from_dict(test_bucket_connection_ok_body_model_json).__dict__
        test_bucket_connection_ok_body_model2 = TestBucketConnectionOKBody(**test_bucket_connection_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert test_bucket_connection_ok_body_model == test_bucket_connection_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        test_bucket_connection_ok_body_model_json2 = test_bucket_connection_ok_body_model.to_dict()
        assert test_bucket_connection_ok_body_model_json2 == test_bucket_connection_ok_body_model_json


class TestModel_UpdateBucketRegistrationOKBody:
    """
    Test Class for UpdateBucketRegistrationOKBody
    """

    def test_update_bucket_registration_ok_body_serialization(self):
        """
        Test serialization/deserialization for UpdateBucketRegistrationOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bucket_registration_model = {}  # BucketRegistration
        bucket_registration_model['access_key'] = '<access_key>'
        bucket_registration_model['actions'] = ['create', 'update']
        bucket_registration_model['associated_catalogs'] = ['iceberg_catalog', 'hive_catalog']
        bucket_registration_model['bucket_display_name'] = 'samplebucketdisplayname'
        bucket_registration_model['bucket_id'] = 'samplebucketid'
        bucket_registration_model['bucket_name'] = 'samplebucket'
        bucket_registration_model['bucket_type'] = 'minio'
        bucket_registration_model['created_by'] = 'username@domain.com'
        bucket_registration_model['created_on'] = '1699457595'
        bucket_registration_model['description'] = 'default bucket'
        bucket_registration_model['endpoint'] = 'https://s3.<region>.cloud-object-storage.appdomain.cloud/'
        bucket_registration_model['managed_by'] = 'ibm'
        bucket_registration_model['region'] = 'us-south'
        bucket_registration_model['secret_key'] = 'secret_key'
        bucket_registration_model['state'] = 'active'
        bucket_registration_model['tags'] = ['tag1', 'tag2']

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Update bucket details'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a UpdateBucketRegistrationOKBody model
        update_bucket_registration_ok_body_model_json = {}
        update_bucket_registration_ok_body_model_json['bucket_registration'] = bucket_registration_model
        update_bucket_registration_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of UpdateBucketRegistrationOKBody by calling from_dict on the json representation
        update_bucket_registration_ok_body_model = UpdateBucketRegistrationOKBody.from_dict(update_bucket_registration_ok_body_model_json)
        assert update_bucket_registration_ok_body_model != False

        # Construct a model instance of UpdateBucketRegistrationOKBody by calling from_dict on the json representation
        update_bucket_registration_ok_body_model_dict = UpdateBucketRegistrationOKBody.from_dict(update_bucket_registration_ok_body_model_json).__dict__
        update_bucket_registration_ok_body_model2 = UpdateBucketRegistrationOKBody(**update_bucket_registration_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert update_bucket_registration_ok_body_model == update_bucket_registration_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        update_bucket_registration_ok_body_model_json2 = update_bucket_registration_ok_body_model.to_dict()
        assert update_bucket_registration_ok_body_model_json2 == update_bucket_registration_ok_body_model_json


class TestModel_UpdateDatabaseOKBody:
    """
    Test Class for UpdateDatabaseOKBody
    """

    def test_update_database_ok_body_serialization(self):
        """
        Test serialization/deserialization for UpdateDatabaseOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        database_registration_database_details_model = {}  # DatabaseRegistrationDatabaseDetails
        database_registration_database_details_model['database_name'] = 'new_database'
        database_registration_database_details_model['hostname'] = 'netezza://abc.efg.com'
        database_registration_database_details_model['password'] = 'samplepassword'
        database_registration_database_details_model['port'] = 4353
        database_registration_database_details_model['sasl'] = True
        database_registration_database_details_model['ssl'] = True
        database_registration_database_details_model['tables'] = 'netezza_table_name'
        database_registration_database_details_model['username'] = 'sampleuser'

        database_registration_model = {}  # DatabaseRegistration
        database_registration_model['actions'] = ['update', 'delete']
        database_registration_model['associated_catalogs'] = ['iceberg_catalog', 'hive_catalog']
        database_registration_model['created_by'] = 'user1@bim.com'
        database_registration_model['created_on'] = '1686792721'
        database_registration_model['database_details'] = database_registration_database_details_model
        database_registration_model['database_display_name'] = 'new_database,'
        database_registration_model['database_id'] = 'new_database_id,'
        database_registration_model['database_properties'] = ['key1', 'key2']
        database_registration_model['database_type'] = 'netezza'
        database_registration_model['description'] = 'Description of the database'
        database_registration_model['tags'] = ['testdatabase', 'userdatabase']

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Update database'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a UpdateDatabaseOKBody model
        update_database_ok_body_model_json = {}
        update_database_ok_body_model_json['database'] = database_registration_model
        update_database_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of UpdateDatabaseOKBody by calling from_dict on the json representation
        update_database_ok_body_model = UpdateDatabaseOKBody.from_dict(update_database_ok_body_model_json)
        assert update_database_ok_body_model != False

        # Construct a model instance of UpdateDatabaseOKBody by calling from_dict on the json representation
        update_database_ok_body_model_dict = UpdateDatabaseOKBody.from_dict(update_database_ok_body_model_json).__dict__
        update_database_ok_body_model2 = UpdateDatabaseOKBody(**update_database_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert update_database_ok_body_model == update_database_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        update_database_ok_body_model_json2 = update_database_ok_body_model.to_dict()
        assert update_database_ok_body_model_json2 == update_database_ok_body_model_json


class TestModel_UpdateDb2EngineOKBody:
    """
    Test Class for UpdateDb2EngineOKBody
    """

    def test_update_db2_engine_ok_body_serialization(self):
        """
        Test serialization/deserialization for UpdateDb2EngineOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        db2_engine_details_model = {}  # Db2EngineDetails
        db2_engine_details_model['connection_string'] = '1.2.3.4'
        db2_engine_details_model['metastore_host'] = 'thrift://mh-connection-string-sample.com'

        db2_engine_model = {}  # Db2Engine
        db2_engine_model['actions'] = ['update', 'delete']
        db2_engine_model['build_version'] = '1.0.3.0.0'
        db2_engine_model['created_by'] = 'user@test.com'
        db2_engine_model['created_on'] = 1700322469
        db2_engine_model['description'] = 'updated description for db2 engine.'
        db2_engine_model['engine_details'] = db2_engine_details_model
        db2_engine_model['engine_display_name'] = 'sample db2 Engine Display Name'
        db2_engine_model['engine_id'] = 'sample db2 Engine Name'
        db2_engine_model['host_name'] = 'xyz-db2-01-db2-svc'
        db2_engine_model['origin'] = 'external'
        db2_engine_model['port'] = 38
        db2_engine_model['status'] = 'REGISTERED'
        db2_engine_model['tags'] = ['tag1', 'tag2']
        db2_engine_model['type'] = 'db2'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'update db2 engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a UpdateDb2EngineOKBody model
        update_db2_engine_ok_body_model_json = {}
        update_db2_engine_ok_body_model_json['db2_engine'] = db2_engine_model
        update_db2_engine_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of UpdateDb2EngineOKBody by calling from_dict on the json representation
        update_db2_engine_ok_body_model = UpdateDb2EngineOKBody.from_dict(update_db2_engine_ok_body_model_json)
        assert update_db2_engine_ok_body_model != False

        # Construct a model instance of UpdateDb2EngineOKBody by calling from_dict on the json representation
        update_db2_engine_ok_body_model_dict = UpdateDb2EngineOKBody.from_dict(update_db2_engine_ok_body_model_json).__dict__
        update_db2_engine_ok_body_model2 = UpdateDb2EngineOKBody(**update_db2_engine_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert update_db2_engine_ok_body_model == update_db2_engine_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        update_db2_engine_ok_body_model_json2 = update_db2_engine_ok_body_model.to_dict()
        assert update_db2_engine_ok_body_model_json2 == update_db2_engine_ok_body_model_json


class TestModel_UpdateEngineOKBody:
    """
    Test Class for UpdateEngineOKBody
    """

    def test_update_engine_ok_body_serialization(self):
        """
        Test serialization/deserialization for UpdateEngineOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        node_description_model = {}  # NodeDescription
        node_description_model['node_type'] = 'worker'
        node_description_model['quantity'] = 1

        endpoints_model = {}  # Endpoints
        endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications/<application_id>'
        endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_history_server'
        endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/spark_applications'
        endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/c7b3fccf-badb-46b0-b1ef-9b3154424021/jkg/api/kernels'
        endpoints_model['view_history_server'] = 'testString'
        endpoints_model['wxd_application_endpoint'] = '$HOST/v1/1698311655308796/engines/spark817/applications'

        engine_details_model = {}  # EngineDetails
        engine_details_model['connection_string'] = '1.2.3.4'
        engine_details_model['endpoints'] = endpoints_model
        engine_details_model['metastore_host'] = '1.2.3.4'

        presto_engine_model = {}  # PrestoEngine
        presto_engine_model['actions'] = ['update', 'delete']
        presto_engine_model['associated_catalogs'] = ['new_catalog_1', 'new_catalog_2']
        presto_engine_model['build_version'] = '1.0.3.0.0'
        presto_engine_model['coordinator'] = node_description_model
        presto_engine_model['created_by'] = '<username>@<domain>.com'
        presto_engine_model['created_on'] = 163788384993
        presto_engine_model['description'] = 'updated description for presto engine'
        presto_engine_model['engine_details'] = engine_details_model
        presto_engine_model['engine_display_name'] = 'sampleEngine'
        presto_engine_model['engine_id'] = 'sampleEngine123'
        presto_engine_model['external_host_name'] = 'your-hostname.apps.your-domain.com'
        presto_engine_model['group_id'] = 'new_group_id'
        presto_engine_model['host_name'] = 'your-hostname.apps.your-domain.com'
        presto_engine_model['origin'] = 'ibm'
        presto_engine_model['port'] = 38
        presto_engine_model['region'] = 'us-south'
        presto_engine_model['size_config'] = 'starter'
        presto_engine_model['status'] = 'running'
        presto_engine_model['status_code'] = 0
        presto_engine_model['tags'] = ['tag1', 'tag2']
        presto_engine_model['type'] = 'presto'
        presto_engine_model['version'] = '1.2.0'
        presto_engine_model['worker'] = node_description_model

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'update engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a UpdateEngineOKBody model
        update_engine_ok_body_model_json = {}
        update_engine_ok_body_model_json['engine'] = presto_engine_model
        update_engine_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of UpdateEngineOKBody by calling from_dict on the json representation
        update_engine_ok_body_model = UpdateEngineOKBody.from_dict(update_engine_ok_body_model_json)
        assert update_engine_ok_body_model != False

        # Construct a model instance of UpdateEngineOKBody by calling from_dict on the json representation
        update_engine_ok_body_model_dict = UpdateEngineOKBody.from_dict(update_engine_ok_body_model_json).__dict__
        update_engine_ok_body_model2 = UpdateEngineOKBody(**update_engine_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert update_engine_ok_body_model == update_engine_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        update_engine_ok_body_model_json2 = update_engine_ok_body_model.to_dict()
        assert update_engine_ok_body_model_json2 == update_engine_ok_body_model_json


class TestModel_UpdateNetezzaEngineOKBody:
    """
    Test Class for UpdateNetezzaEngineOKBody
    """

    def test_update_netezza_engine_ok_body_serialization(self):
        """
        Test serialization/deserialization for UpdateNetezzaEngineOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        netezza_engine_details_model = {}  # NetezzaEngineDetails
        netezza_engine_details_model['connection_string'] = '1.2.3.4'
        netezza_engine_details_model['metastore_host'] = 'thrift://mh-connection-string-sample.com'

        netezza_engine_model = {}  # NetezzaEngine
        netezza_engine_model['actions'] = ['update', 'delete']
        netezza_engine_model['build_version'] = '1.0.3.0.0'
        netezza_engine_model['created_by'] = 'user@test.com'
        netezza_engine_model['created_on'] = 1700322469
        netezza_engine_model['description'] = 'updated description for netezza engine.'
        netezza_engine_model['engine_details'] = netezza_engine_details_model
        netezza_engine_model['engine_display_name'] = 'sample Netezza Engine Display Name'
        netezza_engine_model['engine_id'] = 'sample Netezza Engine Name'
        netezza_engine_model['host_name'] = 'xyz-netezza-01-netezza-svc'
        netezza_engine_model['origin'] = 'external'
        netezza_engine_model['port'] = 38
        netezza_engine_model['status'] = 'REGISTERED'
        netezza_engine_model['tags'] = ['tag1', 'tag2']
        netezza_engine_model['type'] = 'netezza'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'update netezza engine'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a UpdateNetezzaEngineOKBody model
        update_netezza_engine_ok_body_model_json = {}
        update_netezza_engine_ok_body_model_json['netezza_engine'] = netezza_engine_model
        update_netezza_engine_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of UpdateNetezzaEngineOKBody by calling from_dict on the json representation
        update_netezza_engine_ok_body_model = UpdateNetezzaEngineOKBody.from_dict(update_netezza_engine_ok_body_model_json)
        assert update_netezza_engine_ok_body_model != False

        # Construct a model instance of UpdateNetezzaEngineOKBody by calling from_dict on the json representation
        update_netezza_engine_ok_body_model_dict = UpdateNetezzaEngineOKBody.from_dict(update_netezza_engine_ok_body_model_json).__dict__
        update_netezza_engine_ok_body_model2 = UpdateNetezzaEngineOKBody(**update_netezza_engine_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert update_netezza_engine_ok_body_model == update_netezza_engine_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        update_netezza_engine_ok_body_model_json2 = update_netezza_engine_ok_body_model.to_dict()
        assert update_netezza_engine_ok_body_model_json2 == update_netezza_engine_ok_body_model_json


class TestModel_UpdateSparkEngineOKBody:
    """
    Test Class for UpdateSparkEngineOKBody
    """

    def test_update_spark_engine_ok_body_serialization(self):
        """
        Test serialization/deserialization for UpdateSparkEngineOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        spark_engine_details_endpoints_model = {}  # SparkEngineDetailsEndpoints
        spark_engine_details_endpoints_model['applications_api'] = '$HOST/v4/analytics_engines/<spark_id>/spark_applications/<application_id>'
        spark_engine_details_endpoints_model['history_server_endpoint'] = '$HOST/v2/spark/v3/instances/<spark_id>/spark_history_server'
        spark_engine_details_endpoints_model['spark_access_endpoint'] = '$HOST/analytics-engine/details/spark-<instance_id>'
        spark_engine_details_endpoints_model['spark_jobs_v4_endpoint'] = '$HOST/v4/analytics_engines/<spark_id>/spark_applications'
        spark_engine_details_endpoints_model['spark_kernel_endpoint'] = '$HOST/v4/analytics_engines/<spark_id>/jkg/api/kernels'
        spark_engine_details_endpoints_model['view_history_server'] = 'View history server'
        spark_engine_details_endpoints_model['wxd_application_endpoint'] = '$HOST/v1/<wxd_instance_id>/engines/<engine_id>/applications'

        spark_engine_details_model = {}  # SparkEngineDetails
        spark_engine_details_model['connection_string'] = 'https://xyz.<region>.ae.cloud.123.com/v3/analytics_engines/<spark_iae_id>'
        spark_engine_details_model['endpoints'] = spark_engine_details_endpoints_model

        spark_engine_model = {}  # SparkEngine
        spark_engine_model['actions'] = ['update', 'delete']
        spark_engine_model['build_version'] = '1.0.3.0.0'
        spark_engine_model['created_by'] = '<username>@<domain>.com'
        spark_engine_model['created_on'] = 163788384993
        spark_engine_model['description'] = 'Spark engines for running spark applications'
        spark_engine_model['engine_details'] = spark_engine_details_model
        spark_engine_model['engine_display_name'] = 'sampleEngine'
        spark_engine_model['engine_id'] = 'sampleEngine123'
        spark_engine_model['origin'] = 'discover'
        spark_engine_model['status'] = 'REGISTERED'
        spark_engine_model['tags'] = ['tag1', 'tag2']
        spark_engine_model['type'] = 'spark'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Spark engines list'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a UpdateSparkEngineOKBody model
        update_spark_engine_ok_body_model_json = {}
        update_spark_engine_ok_body_model_json['engine'] = spark_engine_model
        update_spark_engine_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of UpdateSparkEngineOKBody by calling from_dict on the json representation
        update_spark_engine_ok_body_model = UpdateSparkEngineOKBody.from_dict(update_spark_engine_ok_body_model_json)
        assert update_spark_engine_ok_body_model != False

        # Construct a model instance of UpdateSparkEngineOKBody by calling from_dict on the json representation
        update_spark_engine_ok_body_model_dict = UpdateSparkEngineOKBody.from_dict(update_spark_engine_ok_body_model_json).__dict__
        update_spark_engine_ok_body_model2 = UpdateSparkEngineOKBody(**update_spark_engine_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert update_spark_engine_ok_body_model == update_spark_engine_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        update_spark_engine_ok_body_model_json2 = update_spark_engine_ok_body_model.to_dict()
        assert update_spark_engine_ok_body_model_json2 == update_spark_engine_ok_body_model_json


class TestModel_UpdateSyncCatalogOKBody:
    """
    Test Class for UpdateSyncCatalogOKBody
    """

    def test_update_sync_catalog_ok_body_serialization(self):
        """
        Test serialization/deserialization for UpdateSyncCatalogOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'sync catalog'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a UpdateSyncCatalogOKBody model
        update_sync_catalog_ok_body_model_json = {}
        update_sync_catalog_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of UpdateSyncCatalogOKBody by calling from_dict on the json representation
        update_sync_catalog_ok_body_model = UpdateSyncCatalogOKBody.from_dict(update_sync_catalog_ok_body_model_json)
        assert update_sync_catalog_ok_body_model != False

        # Construct a model instance of UpdateSyncCatalogOKBody by calling from_dict on the json representation
        update_sync_catalog_ok_body_model_dict = UpdateSyncCatalogOKBody.from_dict(update_sync_catalog_ok_body_model_json).__dict__
        update_sync_catalog_ok_body_model2 = UpdateSyncCatalogOKBody(**update_sync_catalog_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert update_sync_catalog_ok_body_model == update_sync_catalog_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        update_sync_catalog_ok_body_model_json2 = update_sync_catalog_ok_body_model.to_dict()
        assert update_sync_catalog_ok_body_model_json2 == update_sync_catalog_ok_body_model_json


class TestModel_UpdateTableOKBody:
    """
    Test Class for UpdateTableOKBody
    """

    def test_update_table_ok_body_serialization(self):
        """
        Test serialization/deserialization for UpdateTableOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'update table'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a UpdateTableOKBody model
        update_table_ok_body_model_json = {}
        update_table_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of UpdateTableOKBody by calling from_dict on the json representation
        update_table_ok_body_model = UpdateTableOKBody.from_dict(update_table_ok_body_model_json)
        assert update_table_ok_body_model != False

        # Construct a model instance of UpdateTableOKBody by calling from_dict on the json representation
        update_table_ok_body_model_dict = UpdateTableOKBody.from_dict(update_table_ok_body_model_json).__dict__
        update_table_ok_body_model2 = UpdateTableOKBody(**update_table_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert update_table_ok_body_model == update_table_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        update_table_ok_body_model_json2 = update_table_ok_body_model.to_dict()
        assert update_table_ok_body_model_json2 == update_table_ok_body_model_json


class TestModel_ValidateDatabaseBodyDatabaseDetails:
    """
    Test Class for ValidateDatabaseBodyDatabaseDetails
    """

    def test_validate_database_body_database_details_serialization(self):
        """
        Test serialization/deserialization for ValidateDatabaseBodyDatabaseDetails
        """

        # Construct a json representation of a ValidateDatabaseBodyDatabaseDetails model
        validate_database_body_database_details_model_json = {}
        validate_database_body_database_details_model_json['database_name'] = 'sampledatabase'
        validate_database_body_database_details_model_json['hostname'] = 'db2@hostname.com'
        validate_database_body_database_details_model_json['password'] = 'samplepassword'
        validate_database_body_database_details_model_json['port'] = 4553
        validate_database_body_database_details_model_json['sasl'] = True
        validate_database_body_database_details_model_json['ssl'] = True
        validate_database_body_database_details_model_json['tables'] = 'kafka_table_name'
        validate_database_body_database_details_model_json['username'] = 'sampleuser'

        # Construct a model instance of ValidateDatabaseBodyDatabaseDetails by calling from_dict on the json representation
        validate_database_body_database_details_model = ValidateDatabaseBodyDatabaseDetails.from_dict(validate_database_body_database_details_model_json)
        assert validate_database_body_database_details_model != False

        # Construct a model instance of ValidateDatabaseBodyDatabaseDetails by calling from_dict on the json representation
        validate_database_body_database_details_model_dict = ValidateDatabaseBodyDatabaseDetails.from_dict(validate_database_body_database_details_model_json).__dict__
        validate_database_body_database_details_model2 = ValidateDatabaseBodyDatabaseDetails(**validate_database_body_database_details_model_dict)

        # Verify the model instances are equivalent
        assert validate_database_body_database_details_model == validate_database_body_database_details_model2

        # Convert model instance back to dict and verify no loss of data
        validate_database_body_database_details_model_json2 = validate_database_body_database_details_model.to_dict()
        assert validate_database_body_database_details_model_json2 == validate_database_body_database_details_model_json


class TestModel_ValidateDatabaseConnectionOKBody:
    """
    Test Class for ValidateDatabaseConnectionOKBody
    """

    def test_validate_database_connection_ok_body_serialization(self):
        """
        Test serialization/deserialization for ValidateDatabaseConnectionOKBody
        """

        # Construct dict forms of any model objects needed in order to build this model.

        validate_database_connection_ok_body_connection_response_model = {}  # ValidateDatabaseConnectionOKBodyConnectionResponse
        validate_database_connection_ok_body_connection_response_model['state'] = True
        validate_database_connection_ok_body_connection_response_model['state_message'] = 'connection successful'

        success_response_model = {}  # SuccessResponse
        success_response_model['message'] = 'Validate database connection'
        success_response_model['message_code'] = 'success'

        # Construct a json representation of a ValidateDatabaseConnectionOKBody model
        validate_database_connection_ok_body_model_json = {}
        validate_database_connection_ok_body_model_json['connection_response'] = validate_database_connection_ok_body_connection_response_model
        validate_database_connection_ok_body_model_json['response'] = success_response_model

        # Construct a model instance of ValidateDatabaseConnectionOKBody by calling from_dict on the json representation
        validate_database_connection_ok_body_model = ValidateDatabaseConnectionOKBody.from_dict(validate_database_connection_ok_body_model_json)
        assert validate_database_connection_ok_body_model != False

        # Construct a model instance of ValidateDatabaseConnectionOKBody by calling from_dict on the json representation
        validate_database_connection_ok_body_model_dict = ValidateDatabaseConnectionOKBody.from_dict(validate_database_connection_ok_body_model_json).__dict__
        validate_database_connection_ok_body_model2 = ValidateDatabaseConnectionOKBody(**validate_database_connection_ok_body_model_dict)

        # Verify the model instances are equivalent
        assert validate_database_connection_ok_body_model == validate_database_connection_ok_body_model2

        # Convert model instance back to dict and verify no loss of data
        validate_database_connection_ok_body_model_json2 = validate_database_connection_ok_body_model.to_dict()
        assert validate_database_connection_ok_body_model_json2 == validate_database_connection_ok_body_model_json


class TestModel_ValidateDatabaseConnectionOKBodyConnectionResponse:
    """
    Test Class for ValidateDatabaseConnectionOKBodyConnectionResponse
    """

    def test_validate_database_connection_ok_body_connection_response_serialization(self):
        """
        Test serialization/deserialization for ValidateDatabaseConnectionOKBodyConnectionResponse
        """

        # Construct a json representation of a ValidateDatabaseConnectionOKBodyConnectionResponse model
        validate_database_connection_ok_body_connection_response_model_json = {}
        validate_database_connection_ok_body_connection_response_model_json['state'] = True
        validate_database_connection_ok_body_connection_response_model_json['state_message'] = 'testString'

        # Construct a model instance of ValidateDatabaseConnectionOKBodyConnectionResponse by calling from_dict on the json representation
        validate_database_connection_ok_body_connection_response_model = ValidateDatabaseConnectionOKBodyConnectionResponse.from_dict(validate_database_connection_ok_body_connection_response_model_json)
        assert validate_database_connection_ok_body_connection_response_model != False

        # Construct a model instance of ValidateDatabaseConnectionOKBodyConnectionResponse by calling from_dict on the json representation
        validate_database_connection_ok_body_connection_response_model_dict = ValidateDatabaseConnectionOKBodyConnectionResponse.from_dict(validate_database_connection_ok_body_connection_response_model_json).__dict__
        validate_database_connection_ok_body_connection_response_model2 = ValidateDatabaseConnectionOKBodyConnectionResponse(**validate_database_connection_ok_body_connection_response_model_dict)

        # Verify the model instances are equivalent
        assert validate_database_connection_ok_body_connection_response_model == validate_database_connection_ok_body_connection_response_model2

        # Convert model instance back to dict and verify no loss of data
        validate_database_connection_ok_body_connection_response_model_json2 = validate_database_connection_ok_body_connection_response_model.to_dict()
        assert validate_database_connection_ok_body_connection_response_model_json2 == validate_database_connection_ok_body_connection_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################