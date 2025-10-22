import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

class Uploader:
    """
    Our Uploader class.

    Attributes:
        connection_params (dict): Snowflake's connection paramaters.
        table_name (str): Table's name where the data will be uploaded to.
    """
    def __init__(self, connection_params, table_name):
        """
        Initializes an Uploader object setting the initial values.
        """
        self.connection_params = connection_params
        self.table_name = table_name
        
    def upload(self, df):
        """
        Establishes connection to Snowflake using the given credentials, and uploads the DataFrame provided to the target table.

        Parameters:
            df (DataFrame): Data as DataFrame.
            
        Returns:
            None.
        """
        conn = snowflake.connector.connect(**self.connection_params)
        
        try:
            success, nchunks, nrows, _ = write_pandas(conn, df, self.table_name)
            print(f"=====| Uploaded {nrows} rows to {self.table_name} |=====")
        finally:
            conn.close()