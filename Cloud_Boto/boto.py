import boto
from boto.ec2.regioninfo import RegionInfo
import sys
from boto.s3.key import Key

access_key = 'd34bf614c56d4f7c852c6fdbe8a36d0c'
secret_key = '258aa03e21b84c99831b5cc5ed63f702'
# if the parameter is 'start', then start a new instance.
is_start = False
# terminate a instance, user need to provide the ID of the instance
is_terminate = False
#Create a new volume
is_createvolume = False
terminate_id = ''

is_show_images = False

instance_ids = []
if len(sys.argv) > 1:
	if sys.argv[1] == 'start':
		is_start = True
	elif sys.argv[1] == 'terminate':
		is_terminate = True
		terminate_id = sys.argv[2] if len(sys.argv) > 2 else ''
	elif sys.argv[1] == 'createvolume':
		is_createvolume = True
	elif sys.argv[1] == 'showimages':
		is_show_images = True
	else:
		print 'Sorry, the command is not existed'

region=RegionInfo(name='melbourne', endpoint='nova.rc.nectar.org.au')

ec2_conn = boto.connect_ec2(aws_access_key_id=access_key, aws_secret_access_key=secret_key, is_secure=True, region=region, port=8773, path='/services/Cloud', validate_certs=False)

s3 = boto.connect_s3(aws_access_key_id=access_key, aws_secret_access_key=secret_key, is_secure=True, host='swift.rc.nectar.org.au', port=8888, path='/')

print '-'*25,'Basic Information of Your Cloud','-'*25
if is_show_images:
	images = ec2_conn.get_all_images() 
	for img in images:
		print 'id: ', img.id, 'name: ', img.name

reservations = ec2_conn.get_all_reservations()
#for idx, res in enumerate(reservations):
#	print idx, res.id, res.instances

for reservation in reservations:
	print 'reservation id:',reservation.id 
	for instance in reservation.instances:
		print 'instance id:',instance.id
		print 'instance ip address:',instance.ip_address
		print 'instance location:',instance.placement
		print 'instance profile:',instance.instance_profile
		print '-'*25, 'End of the instance','-'*25
		instance_ids.append(instance.id)
	print '*' * 50
#s3.create_bucket('mybucket')
print 'All your buckets:'
buckets = s3.get_all_buckets()
for b in buckets:
	print b.name
	#k = Key('testupload.ics')
	#k.key = 'cluster' 
	#k.set_contents_from_string('hello world')
	#k.set_contents_from_filename('testupload.ics')
	#break

# Start a new instances.
if is_start:
	ec2_conn.run_instances('ami-000022c5', key_name='cluster', instance_type='m1.small', security_groups=['ssh'],instance_profile_name='node1')

if is_terminate:
	ec2_conn.terminate_instances(instance_ids=terminate_id)

if is_createvolume:
	vol_req = ec2_conn.create_volume(1, "monash-01")
	print 'Volume Created Successful'
	curr_vol = ec2_conn.get_all_volumes([vol_req.id])[0] 
	print curr_vol.status
	print curr_vol.zone
	print curr_vol.id
	for ids in instance_ids:
		ec2_conn.attach_volume (curr_vol.id, ids, "/dev/vdc")

