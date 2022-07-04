#!/bin/bash

build_addon() (
    echo
    name="$1"
    path_to_addon="${PWD}/src/${name}"

    echo -e "#Building addon '$name':\n"
    if [ -d "$path_to_addon" ]; then
        cd $path_to_addon && zip -r "../../build/${name}.ankiaddon" *
        echo "Successfully built add-on '$name'"
    else
        echo "Add-on directory not found. Aborting."
    fi
)

build_all_addons() {
    echo -e "#Building all addons"
    for path_to_addon in "${PWD}/src/"*/; do 
        addon_filename=$(basename $path_to_addon)
        build_addon "$addon_filename"
    done
}

print_usage() {
    echo
    echo "Usage: $(basename "${BASH_SOURCE[0]}") [-h] [-a] [-f directory_name]"
    echo
    echo "Available options:"
    echo "-h                    Print this help message"
    echo "-a                    Build all of the add-ons"
    echo "-f directory_name     Build the add-on with the provided directory name"
}

mkdir -p "build"

if [[ $# -eq 0 ]] ; then
    print_usage
    exit 1
fi

while getopts 'ahf:' flag; do
  case "$flag" in
    a) build_all_addons;;
    f) file="$OPTARG" 
    build_addon $file 
    ;;
    h) print_usage
    ;;
    *) print_usage
    ;;
  esac
done