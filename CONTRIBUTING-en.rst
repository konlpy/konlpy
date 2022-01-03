CONTRIBUTING
============
KoNLPy is an open source project. Anyone can become a KoNLpy contributor if they want.

1. Discussing and Learning
------------------
You can solve your questions regarding KoNLPy through the following channels.

- Home Page: http://konlpy.org
- Issue Tracker: http://github.com/konlpy/konlpy/issues
- Mailing List: `konlpy@googlegroups.com <http://groups.google.com/forum/#!forum/konlpy>`_
- Discussion Room: http://gitter.im/konlpy/konlpy


2. Answering your Questions
------------------

1. If you are stuck while using KoNLPy, first check if the `issue <http://github.com/konlpy/konlpy/issues>`_ has already been submitted.

2. If the issue has already been submitted,
    - If the issue is marked as closed : This means the problem has been solved and will most likely be solved in the latest KoNLPy release. Nevertheless, it's useful to read the thread to see how the issue was solved. 
    - If the issue is marked as open: This means the problem hasn't been solved. In this case please describe the problem in the comments. The more users with the same problem comment their issue details the faster the problem can be solved.

3. If the issue hasn't been submitted, you can create a new issue by clicking the "New Issue" button. If you are sumbitting a new issue please describe the OS and the package version you are using to help solve the problem quickly.


3. Suggest/Solve Issues
---------------------
- You can suggest, solve or discuss ways to solve issues or improve the code on the `github issues `github issues <https://github.com/konlpy/konlpy/issues>`_ 

- Please consider the following code standards when writing code.
    1. Use 4 spaces instead of tabs.
    2. For features that are not specifically mentioned in this document write specifications and include references to parts of the code (Also please update this document so other people can follow the same standard)
    3. Commit messages should be as descriptive as possible.

- After completing your code make sure it passes all tests.
    1. If you modified the java code::

         # Install `Apache Ant <http://ant.apache.org/manual/install.html>`_
        make java

    1. If you only modified one line of code::

        pip install -r requirements-dev.txt
        pip3 install -r requirements-dev.txt
        make build      # create tar.gz
        make check      # check code styles
        make testall    # run tests

- Please consider the following before sending a Pull Request.
    1. Once the PR is submitted, the code is subject to KoNLPy's open source license.
    2. If requested to change part of the code after sending the PR, modify the commit with ``git commit --amend`` .



4. Editing documents
----------------

- Spelling correction: If you find a typo or a mispelled word and want to request a correction, you can edit the document yourself.
- Adding content: You can add descriptions to content that you don't understand well or that lack a proper explanation. KoNLP is oriented towards documentation with examples. Please share any examples you would like to add to the documentation.
- Translation: KoNLP's documents are in english and korean. Therefore, you can correct awkward or incorrect translations.


> Note: If you are an existing user, please download and modify the code to send the PR so you can contribute accurately. If the process is to complicated or difficult and you don't want to recieve attribution, you can send an email to konlpy@googlegroups.com 



Setup docs
''''''''''

1. Fork and clone KoNLPy::

    git clone git@github.com:[your_github_id]/konlpy.git

2. Include the following lines in your `~/.bashrc`::

    export LC_ALL=en_US.UTF-8
    export LANG=en_US.UTF-8

3. Install dependencies::

    $ make init_i18n


Modify and push docs
''''''''''''''''''''

1. Modify a document file::

    $ cd docs             # Move to the `docs` folder
    $ vi some_file.rst    # Modify corresponding `*.rst` files

2. Build docs::

    $ make html

3. Extract translation phrases::

    $ make extract_i18n

4. Modify translations::

    $ cd locale/ko/LC_MESSAGES
    $ vi some_file.po

5. Update translations::

    $ make update_i18n

6. Commit and push your repository

7. Send a pull request


5. Add test
------------------

- Add test cases that haven't been covered yet to test the full extent of your code.
