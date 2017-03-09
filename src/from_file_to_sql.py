'''
(`id`,
`email`,
`enabled`,
`family_name`,
`gender`,
`given_name`,
`name`,
`oauth_id`,
`organization`,
`picture_url`,
`authenticate`)
'''
import sys


def write_from_output_to_sql():
    file = open('../data/letters/sent/1/outputfile')
    f1 = open('../data/letters/sent/1/outputfile_MYSQL', 'w+')
    sys.stdout = f1
    count = 0
    for line in file:
        splitt = line.split(',')
        email_splt = splitt[3].split('=')[1]
        family_name = splitt[8].split('=')[1]
        gender = splitt[6].split('=')[1]
        given_name = splitt[7].split('=')[1]
        name = splitt[0].split('=')[1]
        oauth_id = splitt[1].split('=')[1]
        picture_url = splitt[9].split('=')[1]

        # print splitt[3].strip()
        print '(' + '\'' + email_splt + '\'' + ', ' + '1' + ', ' + '\'' + family_name + '\'' + ', ' + '\'' + gender + '\''\
              + ', ' + '\'' + given_name + '\'' + ', ' + '\'' + name + '\''\
              + ', ' + '\'' + oauth_id + '\'' + ', ' + '\'' + "" + '\''\
              + ', ' + '\'' + picture_url + '\''+ ', ' + '0'+')'+','
        # count = count + 1
    print count
    pass


write_from_output_to_sql()
