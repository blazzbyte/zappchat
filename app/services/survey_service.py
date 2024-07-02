# services/survey/survey_service.py

class SurveyService:
    def __init__(self):
        self.surveys = {}

    def create_survey(self, survey_id: str, survey_details: dict):
        self.surveys[survey_id] = survey_details

    def get_survey(self, survey_id: str):
        return self.surveys.get(survey_id)

    def update_survey(self, survey_id: str, updated_details: dict):
        if survey_id in self.surveys:
            self.surveys[survey_id].update(updated_details)

    def delete_survey(self, survey_id: str):
        if survey_id in self.surveys:
            del self.surveys[survey_id]

    def list_surveys(self):
        return list(self.surveys.values())

    def add_question(self, survey_id: str, question: str):
        if survey_id in self.surveys:
            if 'questions' not in self.surveys[survey_id]:
                self.surveys[survey_id]['questions'] = []
            self.surveys[survey_id]['questions'].append(question)

    def get_survey_questions(self, survey_id: str):
        return self.surveys.get(survey_id, {}).get('questions', [])