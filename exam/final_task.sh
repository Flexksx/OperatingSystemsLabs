#!/bin/bash

# Ensure a directory is provided
validate_input() {
  if [ -z "$1" ]; then
    echo "Usage: $0 <test_directory>"
    exit 1
  fi
}

# Check if the directory exists
check_directory_exists() {
  if [ ! -d "$1" ]; then
    echo "Directory $1 does not exist."
    exit 1
  fi
}

# Check if the directory is empty
check_directory_not_empty() {
  if [ -z "$(ls -A "$1")" ]; then
    echo "Directory $1 is empty."
    exit 1
  fi
}

# Organize files into directories by their extensions
organize_files_by_extension() {
  local test_dir="$1"
  local existing_extensions=()

  for file in "$test_dir"/*; do
    # Skip hidden files and non-regular files
    if [[ -f "$file" && "$(basename "$file")" != .* ]]; then
      local ext="${file##*.}"
      if [[ ! " ${existing_extensions[@]} " =~ " $ext " ]]; then
        mkdir -p "$test_dir/$ext"
        existing_extensions+=("$ext")
      fi
      mv "$file" "$test_dir/$ext"
      echo "Moved $file to $test_dir/$ext"
    fi
  done
}

get_file_permissions() {
  local file="$1"
  stat -f "%Sp" "$file"
}

check_and_change_permission() {
  local file="$1"
  local log_file="$test_dir/permissions_log.txt"
  local required_permissions="$2"
  local required_permissions_octal="$3"
  current_permissions=$(get_file_permissions "$file")
    if [[ "$current_permissions" != "$required_permissions" ]]; then
        chmod "$required_permissions_octal" "$file"
        new_permissions=$(get_file_permissions "$file")
        echo "Changed permissions for $file from $current_permissions to $new_permissions" >>"$log_file"
    else
        echo "Permissions for $file already meet the criteria" >>"$log_file"
    fi
}

# Manage file and directory permissions
manage_permissions() {
  local test_dir="$1"


  for item in "$test_dir"/* "$test_dir"/*/*; do
    # Skip the log file
    if [ "$item" == "$log_file" ]; then
      continue
    fi 
    if [ -e "$item" ]; then
    current_permissions=$(get_file_permissions "$item")
      if [ -f "$item" ]; then
        # File: Readable and writable by the owner only
        check_and_change_permission "$item" "-rw-------" 600
      elif [ -d "$item" ]; then
        check_and_change_permission "$item" "drwx------" 700 
      fi
    fi
  done
}

# Main script execution
main() {
  validate_input "$1"
  local test_dir="$1"
  check_directory_exists "$test_dir"
  check_directory_not_empty "$test_dir"
  organize_files_by_extension "$test_dir"
  manage_permissions "$test_dir"
}

main "$@"
