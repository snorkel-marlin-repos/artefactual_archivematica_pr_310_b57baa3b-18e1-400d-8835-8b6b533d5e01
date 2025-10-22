import os
import subprocess

JSON = '[{"dc.title": "This is a test item", "filename": "objects/test.txt"}]'
CSV = 'filename,dc.title\r\nobjects/test.txt,This is a test item\r\n'

JSON_MULTICOLUMN = '[{"filename": "objects/test.txt", "dc.subject": ["foo", "bar", "baz"], "dc.title": "This is a test item"}]'
CSV_MULTICOLUMN = 'filename,dc.subject,dc.subject,dc.subject,dc.title\r\nobjects/test.txt,foo,bar,baz,This is a test item\r\n'

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

def test_json_csv_conversion(tmpdir):
    json_path = os.path.join(str(tmpdir), 'metadata.json')
    csv_path = os.path.join(str(tmpdir), 'metadata.csv')
    with open(json_path, 'w') as jsonfile:
        jsonfile.write(JSON)
    subprocess.check_call([os.path.join(THIS_DIR, '../lib/clientScripts/jsonMetadataToCSV.py'), '', json_path])
    with open(csv_path) as csvfile:
        csvdata = csvfile.read()

    assert csvdata == CSV


def test_json_csv_conversion_with_repeated_columns(tmpdir):
    json_path = os.path.join(str(tmpdir), 'metadata.json')
    csv_path = os.path.join(str(tmpdir), 'metadata.csv')
    with open(json_path, 'w') as jsonfile:
        jsonfile.write(JSON_MULTICOLUMN)
    subprocess.call([THIS_DIR + '/../lib/clientScripts/jsonMetadataToCSV.py', '', json_path])
    with open(csv_path) as csvfile:
        csvdata = csvfile.read()

    assert csvdata == CSV_MULTICOLUMN
