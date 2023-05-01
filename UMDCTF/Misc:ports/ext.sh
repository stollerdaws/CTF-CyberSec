#!/bin/bash

# Set your directory path containing the zip files
directory_path="/home/ubuntu/Downloads/ports"

curPort=443
while true; do
  # Extract the password (number) from the filename
  base_filename="port-${curPort}.txt.zip"
  zip_filepath="${directory_path}/${base_filename}"
  # Unzip the file using the password
  unzip -P "${curPort}" -o "${zip_filepath}" -d "${directory_path}"

  # Read the extracted txt file and search for the flag
  txt_filename="port-${curPort}.txt"
  txt_filepath="$directory_path/$txt_filename"
  content=$(cat "${txt_filepath}")


  # If the flag is found, print it and exit
  if [[ ! "${content}" =~ ":(" ]]; then
    echo "Flag found: $content"
    exit 0
  fi
  nextPort=$(echo "${content}" | grep -o -E '[0-9]{1,6}') 
  echo "$nextPort"
  # Remove the extracted txt file
  rm "$txt_filepath"
  curPort="${nextPort}"
done

echo "Flag not found."
