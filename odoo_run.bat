@echo off
::start
echo ========================
echo     RUNNING ODOO
echo ========================

:: Pindah ke direktori C:\ERP\ODOO
cd C:\ERP\ODOO

:: Jalankan perintah py14_inst dengan path lengkap
start /min py14_inst "C:\ERP\ODOO\INST\server\odoo-bin" -c "C:\ERP\ODOO\conf\odoo-server.conf"

:: ini adalah anchor comment .bat
::pause