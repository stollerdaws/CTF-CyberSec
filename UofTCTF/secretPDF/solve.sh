#!/bin/bash

pdf=secret

pdftotext ${pdf}.pdf

grep -o "uoftctf{.*}" ${pdf}.txt

rm ${pdf}.txt