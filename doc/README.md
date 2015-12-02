# pcDuino8 Uno Get Started Kit User Guide

This user guide has English and Chinese version, and supports gitbook to compile as a ebook.

### [English](en/)
### [中文](zh/)

If you want to generate a book, take the following steps.

## How to use gitbook to generate this user guide
Take Ubuntu as example:

### 1. Install software
```
$ sudo apt-get install -y retext git nodejs npm
$ sudo ln -fs /usr/bin/nodejs /usr/bin/node
$ sudo apt-get install -y calibre fonts-arphic-gbsn00lp
$ sudo npm install gitbook-cli -g
```

### 2. Download doc
```
$ git clone https://github.com/pcduino/pcduino8-uno-guide
$ cd pcduino8-uno-guide/doc/en/
```

### 3. Compile
```
$ gitbook build  // generate html
$ gitbook pdf    // generate pdf
```
