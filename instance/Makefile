INSTALL_NAME=install.sh
TARGET=instance-setup.sh

.PHONY: clean, all

all: $(TARGET)

# Warning! Order of source files matters. ldap-login must come first!
$(TARGET): header.sh ldap-login/$(INSTALL_NAME) home-drive/$(INSTALL_NAME) remote-desktop/$(INSTALL_NAME)
	rm -f $(TARGET)
	cat $^ > $@
	chmod +x $@

clean: 
	rm -f $(TARGET)