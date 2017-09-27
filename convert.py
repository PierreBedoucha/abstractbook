import os, sys
import codecs
replacements = {
    "\r\n": "$",
    "\u03b3": u'\u03b3',
    "\u0394": u'\u0394',
    "\u237a": u'\u237a',
    "\u03b2": u'\u03b2',
    "\u03bb": u'\u03bb',
    "\u03b1": u'\u03b1'
}

def assert_ok(line):
    for replacement in replacements.values():
        assert not replacement in line
        
def process(line):
    l = line
    for token, replacement in replacements.items():
        l = l.replace(token, replacement)
    return l
    
def process_lines(lines):
    processed_lines = []
    for l in lines:
        assert_ok(l)
        processed_lines.append(process(l))
    return processed_lines
    
def fix_file(filename):
    with codecs.open(filename, "r", encoding='MacRoman') as f:
        lines = f.readlines()
    lines = process_lines(lines)
    with codecs.open(filename, "w+", encoding='UTF-16') as f:
        for l in lines:
            f.write(l)

def run_convert(excel_file, new_file):
    os.system("export LC_ALL=\"en_US.UTF-8\"")
    os.system("ssconvert %s %s -O \"quoting-mode=never charset=MacRoman separator=| eol=windows\"" % (excel_file, new_file))
        
if __name__ == "__main__":
    # excelfilename = sys.argv[1]
    excelfilename = "BiB2017-Abstract_submission_MODIF.csv"
    textfilename = excelfilename.replace(".csv", ".txt")
    run_convert(excelfilename, textfilename)
    fix_file(textfilename)