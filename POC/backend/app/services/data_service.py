from app.repositories.data_repository import DataRepository

class DataService:
    def __init__(self):
        self.repo = DataRepository()

    def run_query(self, query, user_roles):
        # Apply RLS based on user roles
        if 'Admin' not in user_roles:
            query = f"{query} WHERE accessible_to IN ({','.join(user_roles)})"
        return self.repo.query_snowflake(query)