import boto3
from datetime import datetime, timedelta

class CostService:
    def __init__(self):
        self.client = boto3.client('ce')

    def get_cost(self, start_date=None, end_date=None):
        if not start_date:
            start_date = (datetime.utcnow() - timedelta(days=7)).strftime('%Y-%m-%d')
        if not end_date:
            end_date = datetime.utcnow().strftime('%Y-%m-%d')
        response = self.client.get_cost_and_usage(
            TimePeriod={'Start': start_date, 'End': end_date},
            Granularity='DAILY',
            Metrics=['UnblendedCost']
        )
        return response['ResultsByTime']