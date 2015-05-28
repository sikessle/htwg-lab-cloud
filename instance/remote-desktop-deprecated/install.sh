# This script is only a part of a the main script in the superfolder!

X11_CONF="/etc/init/x11vnc.conf"

echo "installing x11vnc"
apt-get install -y x11vnc

# Uncomment to enable passwords (beware: not yet an unattended install)
#echo "configuring password"
#mkdir /etc/x11vnc
#x11vnc -storepasswd in /etc/x11vnc/passwd
#x11vnc -storepasswd /etc/x11vnc/passwd

echo "configuring lightdm and vnc"
echo "start on login-session-start" > $X11_CONF
echo "script" >> $X11_CONF
# To use a password, add to the next line as paramter: -rfbauth /etc/x11vnc/passwd
echo "sudo x11vnc -xkb -forever -auth /var/run/lightdm/root/:0 -display :0 -rfbport 5900 -bg -o /var/log/x11vnc.log" >> $X11_CONF
echo "end script" >> $X11_CONF
