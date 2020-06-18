"""
Qualtrics API Client
"""

# Local imports
from api import QualtricsAPI
import components


class QualtricsClient(QualtricsAPI):
    """
    Ties in functionality of individual components
    """

    def __init__(self, data_center, api_key):
        super().__init__(data_center, api_key)

    ### Components ###

    @property
    def survey(self) -> components.survey.SurveyComponent:
        return components.survey.SurveyComponent(self.config['data_center'], self.config['api_key'])
