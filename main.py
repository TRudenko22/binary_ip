####################################
# Purpose: IP to Binary conversion #
# Author: Tim Rudenko              #
####################################

import typer

app = typer.Typer()

@app.command()
def convert(ip):
     print('.'.join([bin(int(x))[2:] for x in ip.split('.')]))

if __name__ == '__main__':
    app()
