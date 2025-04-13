#!/bin/bash

mkdir -p meus_logs

mv *.log meus_logs/ 2>/dev/null

echo "🗂️ Arquivos movidos para a pasta 'meus_logs':"
ls -lh meus_logs/

echo ""
echo "🚨 Quantidade de linhas com 'ERROR':"
grep -i "ERROR" meus_logs/*.log 2>/dev/null | wc -l