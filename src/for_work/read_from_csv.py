import csv

import re

import sys

'''
INSERT INTO `tumorportal`.`file_records`
(`citation`,
`comment`,
`file_name`,
`hash`,
`org_private`,
`own_private`,
`source`,
`ticket_id`,
`upload_timestamp`,
`user_id`)
VALUES
(<{citation: }>,
<{comment: }>,
<{file_name: }>,
<{hash: }>,
<{org_private: }>,
<{own_private: }>,
<{source: }>,
<{ticket_id: }>,
<{upload_timestamp: }>,
<{user_id: }>);
'''
f1 = open('../../data/letters/MYSQL', 'w+')
sys.stdout = f1
with open('../../data/letters/JIRA_Cloud.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, dialect = 'excel')
    for row in spamreader:
        issuekey = row[0]
        timestamp = row[1]
        description = row[2]
        descline = description.split()
        #print issuekey, timestamp
        #print description
        email = re.findall(r"Email = *.+", description)
        file_name = re.findall(r"Name = *.+", description)
        hash = re.findall(r"Hash Value = *.+", description)
        org_private = re.findall(r"Org Private Flag = *.+", description)
        own_private = re.findall(r"Own Private Flag = *.+", description)
        source = re.findall(r"URL for downloading = *.+", description)
        comment = re.findall(r"Comment = *.+", description)
        citation = re.findall(r"Citation = *.+", description)
        print citation, comment, file_name, hash, org_private, own_private, source, issuekey, timestamp, email
        #print '(' + '\'' + 'citation' + '\'' + ', ' + '\'' + 'comment' + '\'' + ', ' + '\'' + 'file_name' + '\'' + ', '