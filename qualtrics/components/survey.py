"""
Survey Qualtrics API Endpoints
"""

# Third-party imports
from requests import Response

# Local imports
from api import QualtricsAPI


class SurveyComponent(QualtricsAPI):

    def __init__(self, data_center: str, api_key: str) -> None:
        super().__init__(data_center, api_key)

    def get(self, surveyId: str) -> Response:
        endpoint = f'/survey-definitions/{surveyId}'
        return self.get_request(endpoint)
