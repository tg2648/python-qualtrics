"""
Base Qualtrics API
"""

# Standard library imports
from typing import Dict, Any

# Third-party imports
import requests


class QualtricsAPI(object):
    """
    Provides base API functionality
    """

    def __init__(self,
                 data_center: str,
                 api_key: str) -> None:
        """Creates a new API client.

        Args:
            api_key (str): Qualtrics API key
            data_center (str): Data center code

        Raises:
            ValueError: If api_key is None
        """

        self.config = {
            'data_center': data_center,
            'api_key': api_key,
            'base_url': f'https://{data_center}.qualtrics.com/API/v3/'
        }

    ### Helper methods ###

    def url_for(self,
                endpoint: str) -> str:
        """
        Get full URL for an endpoint.

        Args:
            endpoint (str): API endpoint

        Returns:
            Full URL: base url + endpoint
        """

        if endpoint.startswith('/'):
            endpoint = endpoint[1:]
        if endpoint.endswith("/"):
            endpoint = endpoint[:-1]

        return self.config['base_url'] + endpoint

    ### API methods ###

    def get_request(self,
                    endpoint: str,
                    params: Dict[str, Any] = None,
                    headers: Dict[str, str] = None) -> requests.Response:
        """
        GET request.

        Args:
            endpoint (str): API endpoint
            headers (dict): Request headers

        Returns:
            `requests.Response` object
        """

        if headers is None:
            headers = {'x-api-token': self.config['api_key']}

        return requests.get(self.url_for(endpoint), headers=headers)

    def post_request(self,
                     endpoint: str,
                     payload: Dict[str, Any],
                     params: Dict[str, Any] = None,
                     headers: Dict[str, str] = None) -> requests.Response:
        """
        POST request.

        Args:
            endpoint (str): API endpoint
            payload (dict): Data to be sent
            headers (dict): Request headers

        Returns:
            `requests.Response` object
        """

        if headers is None:
            headers = {'x-api-token': self.config['api_token']}

        return requests.post(self.url_for(endpoint), json=payload, headers=headers)

    def put_request(self,
                    endpoint: str,
                    payload: Dict[str, Any],
                    params: Dict[str, Any] = None,
                    headers: Dict[str, str] = None) -> requests.Response:
        """
        PUT request.

        Args:
            endpoint (str): API endpoint
            payload (dict): Data to be sent
            headers (dict): Request headers

        Returns:
            `requests.Response` object
        """

        if headers is None:
            headers = {'x-api-token': self.config['api_token']}

        return requests.post(self.url_for(endpoint), json=payload, headers=headers)

    def delete_request(self,
                       endpoint: str,
                       payload: Dict[str, Any],
                       params: Dict[str, Any] = None,
                       headers: Dict[str, str] = None) -> requests.Response:
        """
        DELETE request.

        Args:
            endpoint (str): API endpoint
            payload (dict): Data to be sent
            headers (dict): Request headers

        Returns:
            `requests.Response` object
        """

        if headers is None:
            headers = {'x-api-token': self.config['api_token']}

        return requests.delete(self.url_for(endpoint), json=payload, headers=headers)
