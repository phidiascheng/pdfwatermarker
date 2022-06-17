from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
	pdf_output = PdfFileWriter()
	input_stream = open(pdf_file_in, 'rb')
	pdf_input = PdfFileReader(input_stream, strict=False)
 	# 获取PDF文件的页数
	pageNum = pdf_input.getNumPages()
	# 读入水印pdf文件
	pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
	# 给每一页打水印
	for i in range(pageNum):
		page = pdf_input.getPage(i)
		page.mergePage(pdf_watermark.getPage(0))
		page.compressContentStreams() # 压缩内容
		pdf_output.addPage(page)
	pdf_output.write(open(pdf_file_out, 'wb'))

if __name__ == '__main__':

	files = ['1绪论','2水的循环','3空隙和水','4赋存','5流动','6包气带','7化学组分',
				'8补给排泄','9流动系统','10动态均衡','11孔隙水','12裂隙水',
				'13岩溶水','14动力学基础']
#	for root,dirs,files in os.walk(os.path.dirname(os.path.realpath(__file__))):
	for filename in files:
#		if file[-4:] == '.pdf':
#			filename = file[:-4]
		pdf_file_in = filename+'.pdf'
		pdf_file_out = filename+'w.pdf'
		pdf_file_mark = 'watermark.pdf'
		add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
	
