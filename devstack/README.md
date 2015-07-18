# DevStack

In this folder and sub-folders goes the devstack / OpenStack related files and information.

## local.conf

This configures the vast majority of the OpensStack components. Have a look inside to see the detailed settings, they are commented in length.

## Deployment

For details see the superfolders README.md file.

To add a new feature:

1. Just create a new folder `my-feature`. 
2. Then create in it a `README.md` file with detailed information about the feature. 
3. Also create a `deploy.sh` file which installs the feature.
4. Add your folder`s deploy.sh script to the deploy.sh script in the same folder of this README.md file (the one you’re reading currently).

