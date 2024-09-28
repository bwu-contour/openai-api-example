pip install -r requirements.txt
pytest test_open_api.py -v -s
pytest --html=report.html