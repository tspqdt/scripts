#!/bin/bash
if ["$1" == ""]
then
	echo "DESE SECURITY - PORTSCAN"
	echo "Modo de uso: $0 REDE"
	echo "Exemplo: $0 172.16.1"
else
for ip in {1..254};
do
hping3 -S -p 80 -c1 $1.$ip 2> /dev/null | grep "flags=SA";
done
fi