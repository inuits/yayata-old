#!/bin/bash

find . -name '*.haml' -execdir $PWD/convert.sh '{}' ';'
