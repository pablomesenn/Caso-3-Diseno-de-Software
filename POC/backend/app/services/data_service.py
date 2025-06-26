from app.config.config import MOCK_DATASETS

class DataService:
    def __init__(self):
        # Mock data table
        self.mock_data = [
            {'id': 1, 'value': 'Data A', 'accessible_to': ['Admin', 'User']},
            {'id': 2, 'value': 'Data B', 'accessible_to': ['Admin']}
        ]

    def run_query(self, query, user_roles):
        # Simulate RLS by filtering data based on roles
        if 'Admin' not in user_roles:
            filtered_data = [row for row in self.mock_data if any(role in row['accessible_to'] for role in user_roles)]
        else:
            filtered_data = self.mock_data
        return filtered_data