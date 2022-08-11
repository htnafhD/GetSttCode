import sys
result = []
if len(sys.argv) == 1:
    print('Instructions: python(3) what_status_codes_you_want_question_mark.py f [--file_directory] s [--status_code]')
    quit()
for x in range(0, len(sys.argv), 1):
    if sys.argv[x].lower() == 's':
        try:
            status_code = sys.argv[x+1].split(',')
        except:
            print('Status code must be seperate with ","')
            quit()
    else:
        continue
for y in range(0, len(sys.argv), 1):
    if sys.argv[y].lower() == 'f':
        try:
            f_name = sys.argv[y+1].strip()
            with open(f_name, 'r') as f:
                f_content = f.readlines()
                for line in f_content:
                    for codes in status_code:
                        if line.startswith(codes.strip()):
                            line = line.replace('\n', '')
                            result.append(line)
            result.sort()
            for records in result:
                print(records)
        except:
            print('Can not open file, make sure that the directory is correct and out file is from dirsearch.py')
    else:
        continue
if (result == None):
    print('Instructions: python(3) what_status_codes_you_want_question_mark.py f [--file_directory] s [--status_code]')
