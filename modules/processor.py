import shutil, os

class Processor:
    """
    Our Processor class.

    Attributes:
        validator (Validator): Validator object.
        uploader (Uploader): Uploader object.
        processed_path (str): Directory path where the file is moved if it is successfully processed.
        error_path (str): Directory path where the file is moved if processing fails.
    """
    def __init__(self, validator, uploader, processed_path, error_path):
        """
        Initializes a Processor object setting the initial values.
        """
        self.validator = validator
        self.uploader = uploader
        self.processed_path = processed_path
        self.error_path = error_path
        
    def process(self, file):
        """
        Processes a file by validating it, uploading it, and moving it to the appropriate target directory depending on whether the file is valid or not.

        Parameters:
            file (str): File path.
            
        Returns:
            None.
        """
        df = self.validator.validate(file)
        
        if not df is False:
            self.uploader.upload(df)
            self._move(file, self.processed_path)
        else:
            self._move(file, self.error_path)
            
    def _move(self, file, target_path):
        """
        Protected method that creates target directory if it does not exist and moves the file there.

        Parameters:
            file (str): File path.
            target_path (str): Target directory path.
            
        Returns:
            None.
        """
        os.makedirs(target_path, exist_ok=True)
        shutil.move(file, os.path.join(target_path, os.path.basename(file)))
        