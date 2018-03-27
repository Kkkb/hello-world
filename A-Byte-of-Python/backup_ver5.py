import os
import time
import sys
import zipfile

source = [r'f:\gakki']
target_dir = r'f:\zipbackup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Enter a comment --> ')

if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
		comment.replace(' ', '_') + '.zip'

with zipfile.ZipFile(target, 'w') as myzip:
	myzip.write(source)

'''
argv1 = sys.argv[1]
argv2 = sys.argv[2]
argv2 = [argv2]

source = [r'f:\gakki']
source.extend(argv2)
target_dir = r'f:\backup'

if not os.path.exists(target_dir):
	os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Enter a comment --> ')

if len(comment) == 0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
		comment.replace(' ', '_') + '.zip'

if argv1 == '-v':
	if not os.path.exists(today):
		os.mkdir(today)
		print('Successfully created directory', today)

	zip_command = "zip -r {0} {1}".format(target,
											  ' '.join(source))

	print('Zip command is:')
	print(zip_command)
	print('Running:')
	if os.system(zip_command) == 0:
		print('Successful backup to', target)
	else:
		print('Backup FAILED')

if argv1 == '-q':
	if not os.path.exists(today):
		os.mkdir(today)
#		print('Successfully created directory', today)
	zip_command = "zip -r {0} {1}".format(target,
										  ' '.join(source))
#	print('Zip command is:')
	zip_command
#	print('Running:')
	if os.system(zip_command) == 0:
		pass
#	print('Successful backup to', target)
	else:
		print('Backup FAILED')
'''