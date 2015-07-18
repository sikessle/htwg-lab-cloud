# Instance

In this folder and sub-folders goes the (virtual machine) instance related files and information.

## Structure

Each feature (ldap login, home drive, etc.) is contained in subdirectories. Each subdir contains an `README.md` file with information about the feature and an `install.sh` script, which installs the feature on the instance. The scripts are run at rc.local run-time, so quite late in the boot process. The `instance-setup.sh` script consists of the `header.sh`, `install.sh` of each feature and a `footer.sh` script. The header script does some preparation like updating apt-get and setting the `$USER` variable. The footer does some cleanup und basically reboots the machine.

**Caveat** The `image` folder is not a feature, but more a toolset to create the ubuntu base image.

So to add a new feature:

1. Create a new folder `my-feature`
2. Create a `README.md` file and explain in detail what this feature does and requires.
3. Create an `install.sh` script which installs your feature on the machine. (You can use the $USER variable there).
4. Run `make` to generate the instance-setup.sh file and test your feature.

## Deployment

Independent from OpenStack installation.

- To generate a single installation script run `make` in this folder.
- This will generate a `instance-setup.sh` file, which must be run in each instance to configure the instance, by passing it as a user-data script. Ensure to change the contained variable `$USER` in the file before passing it as user-data script to an instance.

## Operating System

- Ubuntu 14.04 LTS

## Bugs

- Graphical Login must be issued twice for LDAP users due to Ubuntu bugs in lightdm.