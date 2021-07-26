# Deployment instructions
# 0. Fill in `pypirc.sample`, and `cp pypirc.sample ~/.pypirc`
# 1. Check changelogs.rst and check if documents are up-to-date (make show_docs, make show_docs_ko will help you out)
# 2. Check translations at docs/locale/ko/LC_MESSAGES/*.po
# 3. Check version at konlpy/konlpy/about.py
# 4. $ make testpypi
# 5. $ make pypi  # Beware not to change the version number at this stage!!!
# 6. Document update at RTD (latest)
# 7. Push tag
# 8. Document update at RTD (current version)
#
# TODO: use flake8 and/or pylint

build:
	python setup.py sdist --formats=gztar,zip

check:
	check-manifest
	pyroma dist/konlpy-*tar.gz
	pep8 --ignore=E501 konlpy/*.py
	pep8 --ignore=E501 konlpy/*/*.py

testpypi:
	python setup.py register -r pypitest
	python setup.py sdist --formats=gztar upload -r pypitest
	python setup.py bdist_wheel upload -r pypitest
	# Execute below manually
	# 	cd /tmp
	# 	virtualenv venv
	# 	source venv/bin/activate
	# 	pip install -i https://testpypi.python.org/pypi konlpy
	# 	deactivate
	# 	virtualenv-3.4 venv3
	# 	source venv3/bin/activate
	# 	pip3 install -i https://testpypi.python.org/pypi konlpy
	# 	deactivate

pypi:
	python setup.py register -r pypi
	python setup.py sdist --formats=gztar upload -r pypi
	python setup.py bdist_wheel upload -r pypi

java:
	ant clean compile

jcc:
	python -m jcc \
	    --jar konlpy/java/jhannanum-0.8.4.jar \
	    --classpath konlpy/java/bin/kr/lucypark/jhannanum \
	    --python pyhannanum \
	    --version 0.1.0 \
	    --build --install

testall:
	python -m pytest --cov=konlpy test/
	python3 -m pytest --cov=konlpy test/

init_i18n:
	pip install mock sphinx sphinx-intl
	git submodule init
	git submodule update

show_docs:
	cd docs\
		&& make html \
		&& cd _build/html \
		&& python -m SimpleHTTPServer

show_docs_ko:
	cd docs\
		&& make -e SPHINXOPTS="-D language='ko'" html \
		&& cd _build/html \
		&& python -m SimpleHTTPServer

extract_i18n:
	cd docs\
	    && make gettext\
	    && sphinx-intl update -p _build/locale -l ko

update_i18n:
	cd docs\
	    && sphinx-intl build\
	    && make -e SPHINXOPTS="-D language='ko'" html
