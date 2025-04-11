#!/bin/bash

while true; do
    clear
    echo "========================================"
    echo "=================MENU==================="
    echo "========================================"
    echo "1 - Ver arquivos"
    echo "2 - Mostrar data"
    echo "3 - Sair"
    echo -n "Escolha uma opção: "

    read OPTION

    case "$OPTION" in
        1)
            echo -e "\n🗂 Arquivos no diretório atual:"
            ls
            ;;
        2)
            echo -e "\n📅 Data atual:"
            date +%d/%m/%Y
            ;;
        3)
            echo -e "\n🚪 Saindo do sistema retrô..."
            break
            ;;
        *)
            echo -e "\n❌ Opção inválida. Tente novamente."
            ;;
    esac

    echo -e "\nPressione Enter para continuar..."
    read
done
