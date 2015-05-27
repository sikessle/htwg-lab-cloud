#!/bin/bash

IMAGE=$1

if [ "$IMAGE" = "" ]; then
	echo "pass as first argument the path to the image you want to convert"
	exit 1
fi

echo "converting $IMAGE to openstack compatible format"

