import os
from cloudflare import Cloudflare
import pandas as pd

# Ensure the environment variable is set correctly
#os.environ['CLOUDFLARE_API_TOKEN'] = 'ufOzuXUzIq8QSy8QjFaKNBR706XmIie_mucZFtz1'
#account_id = "78939a17148c390144ef58e10a619393"


class CfDatabase:
    def __init__(self):
        os.environ['CLOUDFLARE_API_TOKEN'] = 'lwr3p3kZZ5JnPVWUrCTtw1saiS5aQ-sx7Pt8pmM4'
        self.client = Cloudflare(api_token=os.environ.get("CLOUDFLARE_API_TOKEN"))
        self.account_id = '78939a17148c390144ef58e10a619393'
        self.database_id = '80bcc84b-4b11-4c12-bd9e-523f3f5ff26a'
    #Task
    def list_all_tasks(self):
        sql = "SELECT * FROM task"
        query_result = self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )
        return query_result[0].results

    def get_task_by_id(self, uuid):
        sql = f"SELECT * FROM task WHERE task_id = '{uuid}'"
        query_result = self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )
        return query_result[0].results

    def insert_task(self, tasks):
        for task_data in tasks:
            columns = ', '.join(task_data.keys())
            values = ', '.join([f"'{v}'" for v in task_data.values()])
            sql = f"INSERT INTO task ({columns}) VALUES ({values})"
            self.client.d1.database.query(
                database_id=self.database_id,
                account_id=self.account_id,
                sql=sql
            )

    #Client
    def list_all_clients(self):
        sql = "SELECT * FROM clients"
        query_result = self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )
        return query_result[0].results

    def get_client_by_id(self, uuid):
        sql = f"SELECT * FROM projects WHERE client_id = '{uuid}'"
        query_result = self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )
        return query_result[0].results

    def insert_client(self, clients):
        for client_data in clients:
            columns = ', '.join(client_data.keys())
            values = ', '.join([f"'{v}'" for v in client_data.values()])
            sql = f"INSERT INTO clients ({columns}) VALUES ({values})"
            self.client.d1.database.query(
                database_id=self.database_id,
                account_id=self.account_id,
                sql=sql
            )

    def delete_client(self, uuid):
        sql = f"DELETE FROM clients WHERE client_id = '{uuid}'"
        self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )

    def update_client(self, uuid, update_data):
        set_clause = ', '.join([f"{k} = '{v}'" for k, v in update_data.items()])
        sql = f"UPDATE clients SET {set_clause} WHERE client_id = '{uuid}'"
        self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )

    #Provider
    def list_all_providers(self):
        sql = "SELECT * FROM provider"
        query_result = self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )
        return query_result[0].results

    def insert_provider(self, provider):
        for provider_data in provider:
            columns = ', '.join(provider_data.keys())
            values = ', '.join([f"'{v}'" for v in provider_data.values()])
            sql = f"INSERT INTO provider ({columns}) VALUES ({values})"
            self.client.d1.database.query(
                database_id=self.database_id,
                account_id=self.account_id,
                sql=sql
            )

    #Quotation
    def get_all_quotations(self):
        sql = "SELECT * FROM quotation"
        query_result = self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )
        return query_result[0].results

    def insert_quotation(self, quotation):
        for quotation_data in quotation:
            columns = ', '.join(quotation_data.keys())
            values = ', '.join([f"'{v}'" for v in quotation_data.values()])
            sql = f"INSERT INTO quotation ({columns}) VALUES ({values})"
            self.client.d1.database.query(
                database_id=self.database_id,
                account_id=self.account_id,
                sql=sql
            )

    #Member
    def list_all_members(self):
        sql = "SELECT * FROM member"
        query_result = self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )
        return query_result[0].results