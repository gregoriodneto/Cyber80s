#!/bin/bash

echo "============================"
echo "   LOCALIZADOR RETRO 80s"
echo "============================"
echo

find . -type f -name "*.log" 2>/dev/null | while read file; do
    echo -e "📁 Verificando: $file"
    grep --color=always "ERROR" "$file"
    echo "---------------------------------"    
done