import pandas

class Validator:
    """
    Our Validator class.

    Attributes:
        expected_columns (str): Number of columns expected to be present in the csv file.
    """
    
    def __init__(self, expected_columns=16):
        """
        Initializes a Validator object by setting up the expected_columns value.
        """
        self.expected_columns = expected_columns
        
    def validate(self, file):
        """
        Compares the csv columns number against the expected_columns number.

        Parameters:
            file (str): File path.
            
        Returns:
            response (DataFrame): The csv file as DataFrame.
        """
        try:
            df = pandas.read_csv(file)
            
            if len(df.columns) != self.expected_columns:
                raise ValueError(f"Expected {self.expected_columns} columns, got {len(df.columns)} columns")
            
            return df
        except Exception as e:
            print(f"Validation failed for {file}: {e}")
            return False