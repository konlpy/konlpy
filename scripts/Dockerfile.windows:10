FROM mcr.microsoft.com/windows:1809

# Install Chocolatey
RUN @powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin

# New Powershell, so choco is available
SHELL ["powershell"]

# Choco disable upload progress
RUN choco feature disable --name showDownloadProgress

# python 3.
RUN choco install -y python3
RUN py -m pip install --upgrade pip

# Jpype requires: (and respect caching)
RUN choco install -y vcbuildtools  # XXX: so long...
RUN choco install -y adoptopenjdk11 --version 11.0.5.10  # XXX: version fixed for JAVA_HOME.
ENV JAVA_HOME "C:\\Program Files\\AdoptOpenJDK\\jdk-11.0.5.10-hotspot"

# TestEnv
RUN choco install -y git.install
RUN & 'C:\Program Files\Git\bin\git.exe' clone https://github.com/konlpy/konlpy konlpy.git
WORKDIR konlpy.git

RUN & 'C:\Program Files\Git\bin\git.exe' checkout master
RUN py -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ konlpy==0.5.2-rc.2
RUN py -m pip install -r .\requirements-dev.txt
CMD py -m pytest -v .