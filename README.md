# abstractbook
Small gathering of all the code needed to automatize an abstract book creation

From Edvin Fuglebakk 2016

1. Export excel file from Mach.

2. Run convert.py to get a text file with '|' as field delimiter and '$' as record delimiter, 
and with unrecognised unicode character fixed. File will be encoded as UTF-16

3. Use the mail merge templates to generate a file with the abstract for talks (talks.docx), 
one for posters (posters.docx) and a file for each table of contents (talks_toc.docx and posters_toc.docx).
IMPORTANT: set sorting in mail merge - options (lastname, firstname, entry). 
This is necessary for the assigned numbers to match in the abstract header and in the table of contants. 
Double check this afterward

4. Update the master document and export pdf.

(0. In addition some abstracts was edited prior to export from Mach, to avoid errors in the word import. 
Particularly unmatched quotation marks are problematic.)

This roundabout procedures is necessary because Word can't import properly from excel-files 
(gives garbled text in some abstracts) and Word can't read the csv format exported by Mach(?) if fields contain line breaks or commas. 
The former is obviously a bug and might not be an issue with other version of Word or Excel.

To get the data from Mach on a format Word understands we therefore need a plain text format like csv, 
with fields by '|' (rather than ',' or ';') and records by "$" (rather than line breaks), 
other choices are of course possible, but Word does not allow all characters as delimiters. 
the argument eol=windows in step 3 makes sure records are terminated by both newline and carrige return, 
while other line breaks are specified by newline only. 
This allows us to selectively specify line breaks that terminate records in step 4.
