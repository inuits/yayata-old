#!/bin/bash
source bin/activate
find . -name '*.haml' -execdir $PWD/convert.sh '{}' ';'
