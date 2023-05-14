import os
import glob
from PIL import Image
from PyPDF2 import PdfMerger

week_str = 'week 18'
week_dir = 'D:/_Jessica/HomeworkMerge/' + week_str

fn_list = glob.glob(os.path.join(week_dir, "*.*"))

# for all jpg files, convert to single page pdf with PIL
for fn in fn_list:
    ext = os.path.splitext(fn)[1]
    if (ext.lower() == '.jpg') or (ext.lower() == '.jpeg'):
        print(fn, 'extension is: ', ext)
        # fn_path = os.path.join(week_dir, fn)
        # print(fn_path)
        img = Image.open(fn)
        img = img.convert('RGB')
        img = img.resize((595, 842))  # A4 size at 72 PPI
        img.save(fn + '.pdf')

# for all pdf files, merge them into one pdf with PyPDF2
pdf_list = glob.glob(os.path.join(week_dir, "*.pdf"))
print(pdf_list)

fnameFinal = f'Jessica-{week_str}-assignment.pdf'
merger = PdfMerger()
for pdf in pdf_list:
    merger.append(pdf)
merger.write(os.path.join(week_dir, fnameFinal))
merger.close()