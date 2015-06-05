INSTALL_SCRIPT=install.sh
TARGET=instance-setup.sh

# Warning! Order of source files matters. ldap-login must come first!
# Add in the following line the modules:
MODULES=ldap-login home-drive block-storage

SOURCES=$(addsuffix /$(INSTALL_SCRIPT), $(MODULES))

.PHONY: clean, all

all: $(TARGET)

$(TARGET): header.sh $(SOURCES) footer.sh
	rm -f $(TARGET)
	cat $^ > $@
	chmod +x $@

clean: 
	rm -f $(TARGET)