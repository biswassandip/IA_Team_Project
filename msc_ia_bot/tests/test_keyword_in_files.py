import os
from docx import Document
from openpyxl import load_workbook
import xml.etree.ElementTree as ET
from PyPDF2 import PdfReader
import zipfile
import sys
from src.common.general_handlers.utils import Utils
from src.common.file_handlers.file_event_handler import KeywordInFile

cons_source_dir = "/Users/gini/TeamProject/IA_Team_Project/msc_ia_bot/tests/TEST_PATHS/source_dir/"

class TestKeywordInFile:
    def setup_class(cls):
        cls.keyword_in_file = KeywordInFile()

    def test_search_keyword_in_text_file(self):
        """
        Test the search_keyword_in_text_file method of KeywordInFile class.
        """
        file_path = cons_source_dir + 'test_file.txt'
        keyword = 'example'
        result = self.keyword_in_file.search_keyword_in_text_file(file_path, keyword)
        assert result is True

    def test_search_keyword_in_docx_file(self):
        """
        Test the search_keyword_in_docx_file method of KeywordInFile class.
        """
        file_path = cons_source_dir + 'test_file.docx'
        keyword = 'example'
        result = self.keyword_in_file.search_keyword_in_docx_file(file_path, keyword)
        assert result is True

    def test_search_keyword_in_excel_file(self):
        """
        Test the search_keyword_in_excel_file method of KeywordInFile class.
        """
        file_path = cons_source_dir + 'test_file.xlsx'
        keyword = 'example'
        result = self.keyword_in_file.search_keyword_in_excel_file(file_path, keyword)
        assert result is True

    def test_search_keyword_in_xml_file(self):
        """
        Test the search_keyword_in_xml_file method of KeywordInFile class.
        """
        file_path = cons_source_dir + 'test_file.xml'
        keyword = 'example'
        result = self.keyword_in_file.search_keyword_in_xml_file(file_path, keyword)
        assert result is True

    def test_search_keyword_in_pdf_file(self):
        """
        Test the search_keyword_in_pdf_file method of KeywordInFile class.
        """
        file_path = cons_source_dir + 'test_file.pdf'
        keyword = 'example'
        result = self.keyword_in_file.search_keyword_in_pdf_file(file_path, keyword)
        assert result is True

    def test_search_keyword_in_zip_file(self):
        """
        Test the search_keyword_in_zip_file method of KeywordInFile class.
        """
        file_path = cons_source_dir + 'test_file.zip'
        keyword = 'example'
        result = self.keyword_in_file.search_keyword_in_zip_file(file_path, keyword)
        assert result is True
