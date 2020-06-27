"""
Survey Qualtrics API Endpoints
"""

# Standard library imports
from typing import Optional

# Third-party imports
from requests import Response

# Local imports
from qualtrics.api import QualtricsAPI


class SurveyComponent(QualtricsAPI):

    def __init__(self, data_center: str, api_key: str) -> None:
        super().__init__(data_center, api_key)

    def get(self, surveyId: str, survey_format: Optional[str] = None) -> Response:
        """
        Returns the survey definition or in the format specified

        Args:
            format (str): the format of the survey (e.g. 'qsf')
        """
        endpoint = f'/survey-definitions/{surveyId}'

        if survey_format is not None:
            params = {'enum': survey_format}

        return self.get_request(endpoint, params=params)

