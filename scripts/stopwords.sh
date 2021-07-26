#! /bin/bash

# Set stopwords related variable(s)
PDIR=$(builtin cd ..; pwd)
stopwords_dir="$PDIR/konlpy/data/corpus/stopwords"

# Exit as soon as we fail
set -e

# Determine OS
os=$(uname)
if [[ ! $os == "Linux" ]] && [[ ! $os == "Darwin" ]]; then
    echo "This script does not support this OS."
    echo "Try consulting https://github.com/konlpy/konlpy/blob/master/scripts/stopwords.sh"
    exit 0
fi

# Determine python
# TODO: Prefer python3 and Respect pyenv
python="python3"
if hash "pyenv" &>/dev/null; then
    python="python"
fi

# Determine python site location are writable.
check_python_site_location_is_writable(){
    $python - <<EOF
import site, os
found = False
for dir in site.getsitepackages():
    if not os.path.isdir(dir):
        continue
    if os.access(dir, os.W_OK | os.X_OK):
        found = True
        break
print(1 if found else 0)
EOF
}
at_user_site=""
if [[ "$(check_python_site_location_is_writable)" == "0" ]]; then
    at_user_site="--user"
fi

collect_stopwords_raw_data(){
	pushd /tmp
	curl -LO https://bab2min.tistory.com/attachment/cfile2.uf@241D6F475873C2B1010DEA.txt
	curl -LO https://gist.githubusercontent.com/spikeekips/40eea22ef4a89f629abd87eed535ac6a/raw/4f7a635040442a995568270ac8156448f2d1f0cb/stopwords-ko.txt
	curl -LO https://raw.githubusercontent.com/6/stopwords-json/master/dist/ko.json
	curl -LO https://raw.githubusercontent.com/stopwords-iso/stopwords-iso/master/stopwords-iso.json

	for file in "cfile2.uf@241D6F475873C2B1010DEA.txt stopwords-ko.txt ko.json stopwords-iso.json"
	do
		if [[ ! -f $file ]]; then
			echo "Check $file in /tmp"
		fi
	done
	popd

    $python -m pip install $at_user_site many-stop-words

	if [[ $($python -c 'import pkgutil; print(1 if pkgutil.find_loader("many_stop_words") else 0)') == "1" ]]; then
	    echo "many_stop_words is already installed"
	else
	    echo "Install many_stop_words"
	  	echo "$python -m pip install $at_user_site many-stop-words"  
	fi
}

convert_from_raw_data(){
	$python convert_stopwords.py --install-path $stopwords_dir

	if [[ ! -f $stopwords_dir/stopwords.morph.txt ]] || [[ ! -f $stopwords_dir/stopwords.word.txt ]]; then
		echo "stopwords.morph.txt or stopwords.word.txt not in $stopwords_dir"
		echo "Please check convert_stopwords.py command"
		exit 1;
	fi
}

collect_stopwords_raw_data
convert_from_raw_data

echo "Done."
