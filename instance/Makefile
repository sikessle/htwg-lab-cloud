INSTALL_SCRIPT=install.sh
TARGET=instance-setup.sh

# Warning! Order of source files matters. ldap-login must come first!
# To add more subfolders (modules) add them to this variable:
MODULES=ldap-login home-drive block-storage

SOURCES=$(addsuffix /$(INSTALL_SCRIPT), $(MODULES))

.PHONY: clean, all

all: $(TARGET)

# just concenate the install.sh scripts in each subfolder.
$(TARGET): header.sh $(SOURCES) footer.sh
	rm -f $(TARGET)
	cat $^ > $@
	chmod +x $@

clean: 
	rm -f $(TARGET)