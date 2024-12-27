import os
import urllib.request
import zipfile
import logging
import sys
from pathlib import Path
from requests import request
# Go up 4 levels: components -> textSummarizer -> src -> Project root
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent.absolute()
sys.path.insert(0, str(PROJECT_ROOT))  # Using insert(0) for higher priority

from src.textSummarizer.logging.logging import logger
from src.textSummarizer.utils.common import get_size
from src.textSummarizer.entity import DataingestionConfig

import os
import urllib.request
import zipfile
import logging
from pathlib import Path

import os
import requests
import zipfile
import logging
from pathlib import Path
import magic

def get_file_type(file_path):
    """Detect file type using magic numbers"""
    mime = magic.Magic()
    return mime.from_file(file_path)

class DataIngestion:
    def __init__(self, config):
        self.config = config
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def download_file(self):
        try:
            source_url = self.config.source_URL
            local_file = self.config.local_data_file

            # Create directory if needed
            os.makedirs(os.path.dirname(local_file), exist_ok=True)

            # Download with proper headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(source_url, headers=headers, stream=True)
            response.raise_for_status()

            # Write file in chunks
            with open(local_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            # Verify downloaded file
            if not os.path.exists(local_file):
                raise Exception("Download failed - file not created")
            
            if not zipfile.is_zipfile(local_file):
                os.remove(local_file)
                raise Exception("Downloaded file is not a valid ZIP")

            self.logger.info(f"Download successful: {local_file}")
            return local_file

        except Exception as e:
            self.logger.error(f"Download failed: {str(e)}")
            raise

    def extract_zip_file(self):
        try:
            local_file = self.config.local_data_file
            unzip_path = self.config.unzip_dir
            
            if not os.path.exists(local_file):
                raise FileNotFoundError(f"ZIP file not found: {local_file}")

            os.makedirs(unzip_path, exist_ok=True)

            with zipfile.ZipFile(local_file, 'r') as zip_ref:
                # Test ZIP file integrity before extraction
                if zip_ref.testzip() is not None:
                    raise zipfile.BadZipFile("ZIP file is corrupted")
                zip_ref.extractall(unzip_path)

            self.logger.info(f"Extraction successful: {unzip_path}")

        except Exception as e:
            self.logger.error(f"Extraction failed: {str(e)}")
            raise