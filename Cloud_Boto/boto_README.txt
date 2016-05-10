There are four parameters for the Boto Script:
1. start: create a new instance
2. terminate: end a instance, but the instance ID should be provided (just follow this parameter)
3. create volume: create and attach a Volume
4. show images: show all images of a Cloud

If no parameter is provided, then just show the information of a Cloud.

Run:
python boto.py start
python boto.py terminate
python boto.py createvolume
python boto.py showimages