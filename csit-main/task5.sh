#!/bin/bash

git -C "$1" ls-files --cached --others --exclude-standard | sed "s|^|$(basename "$1")/|" | zip -@ "$(dirname "$1")/$(basename "$1").zip"
