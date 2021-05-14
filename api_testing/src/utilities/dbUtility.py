
import pymysql
from api_testing.src.utilities.credentialUtility import CredentialUtility

class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialUtility()
        self.creds = creds_helper.get_db_credentials()
        self.host='localhost'
        self.socket = '/Users/rakhimyakubjanov/Library/Application Support/Local/run/qFGEsVo07/mysql/mysqld.sock'




    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.creds['db_user'], passwd=self.creds['db_password'], unix_socket=self.socket)




        return connection


    def execute_select(self, sql):


        conn = self.create_connection()

        try:
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict=cur.fetchall()
            cur.close()

        except Exception as e:
            raise  Exception('Failed to connect with DB')

        finally:
            conn.close()

        return rs_dict



    def execute_sql(self, sql):
        pass

