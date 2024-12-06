git clone https://github.com/python/cpython.git --branch "3.13" --single-branch
cd cpython
git checkout 5d35d279a5150fd5ea4731c53fc3459cf22f1d16
./configure
make
make test
sudo make install
