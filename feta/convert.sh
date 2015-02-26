#!/bin/bash
hamlpy "$1" "$(basename $1 .haml).html"
