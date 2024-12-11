install:
	python -m pip install -r src/requirements.txt

run:
	python src/main.py

activate:
	source .venv/bin/activate

deactivate:
	deactivate