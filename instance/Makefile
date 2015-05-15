INSTALL_NAME=install.sh
TARGET=instance-setup.sh

.PHONY: clean, all

all: $(TARGET)

$(TARGET): ldap-login/$(INSTALL_NAME) home-drive/$(INSTALL_NAME)
	rm -f $(TARGET)
	cat $^ > $@
	chmod +x $@

clean: 
	rm -f $(TARGET)