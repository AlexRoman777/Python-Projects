from mergepdf import clear_terminal, merge_pdf, merger, get_output_file, root, get_input_files
import os
import pytest


def test_clear_terminal_success(self):
    clear_terminal()
    # assert that the terminal screen is cleared
    assert os.system('cls' if os.name == 'nt' else 'clear') == 0


def test_clear_terminal_wrong_os(self):
    # change the os name to an unrecognized value
    os.name = 'unknown'
    # assert that the function raises a system error
    with pytest.raises(SystemError):
        clear_terminal()


def test_merge_pdf_happy_path(self, mocker):
    # Mocking the file dialog functions
    mocker.patch('tkinter.filedialog.askopenfilenames',
                 return_value=('file1.pdf', 'file2.pdf'))
    mocker.patch('tkinter.filedialog.asksaveasfilename',
                 return_value='output.pdf')

    # Calling the function
    merge_pdf()

    # Assertions
    assert merger.output.name == 'output.pdf'
    assert len(merger.pages) == 2


def test_get_output_file_returns_valid_file_path(self):
    # Happy path test
    # Simulate user selecting a valid file name and destination
    root.filename = "test.pdf"
    assert get_output_file() == "test.pdf"


def test_happy_path_select_one_file(self, mocker):
    # Mocking the filedialog.askopenfilenames method to return a single file path
    mocker.patch('tkinter.filedialog.askopenfilenames',
                 return_value=('path/to/file.pdf',))
    assert get_input_files() == ['path/to/file.pdf']
