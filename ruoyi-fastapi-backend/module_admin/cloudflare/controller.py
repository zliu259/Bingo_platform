import os
from cloudflare import Cloudflare
import pandas as pd

# Ensure the environment variable is set correctly
#os.environ['CLOUDFLARE_API_TOKEN'] = 'ufOzuXUzIq8QSy8QjFaKNBR706XmIie_mucZFtz1'
#account_id = "78939a17148c390144ef58e10a619393"

class ProjectDatabase:
    def __init__(self):
        os.environ['CLOUDFLARE_API_TOKEN'] = 'lwr3p3kZZ5JnPVWUrCTtw1saiS5aQ-sx7Pt8pmM4'
        self.client = Cloudflare(api_token=os.environ.get("CLOUDFLARE_API_TOKEN"))
        self.account_id = '78939a17148c390144ef58e10a619393'
        self.database_id = '80bcc84b-4b11-4c12-bd9e-523f3f5ff26a'

    def list_all_projects(self):
        sql = "SELECT * FROM projects"
        query_result = self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )
        return query_result[0].results

    def get_project_by_uuid(self, uuid):
        sql = f"SELECT * FROM projects WHERE job_id = '{uuid}'"
        query_result = self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )
        return query_result[0].results

    def insert_project(self, projects):
        for project_data in projects:
            columns = ', '.join(project_data.keys())
            values = ', '.join([f"'{v}'" for v in project_data.values()])
            sql = f"INSERT INTO projects ({columns}) VALUES ({values})"
            self.client.d1.database.query(
                database_id=self.database_id,
                account_id=self.account_id,
                sql=sql
            )

    def update_project(self, uuid, update_data):
        set_clause = ', '.join([f"{k} = '{v}'" for k, v in update_data.items()])
        sql = f"UPDATE projects SET {set_clause} WHERE job_id = '{uuid}'"
        self.client.d1.database.query(
            database_id=self.database_id,
            account_id=self.account_id,
            sql=sql
        )

class ClientDatabase:
    def __init__(self):
        os.environ['CLOUDFLARE_API_TOKEN'] = 'lwr3p3kZZ5JnPVWUrCTtw1saiS5aQ-sx7Pt8pmM4'
        self.client = Cloudflare(api_token=os.environ.get("CLOUDFLARE_API_TOKEN"))
        self.account_id = '78939a17148c390144ef58e10a619393'
        self.database_id = '80bcc84b-4b11-4c12-bd9e-523f3f5ff26a'

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