from bs4 import BeautifulSoup
import bs4
import os

class AnalyzeHtml():
    def __init__(self,Filedir):
        self.Filedir=Filedir

    # def FindFileList(self):
    #     '''获取文件列表'''
    #     for Root,Dirs,Files in os.walk(self.Filedir):
    #         return Files

    def open_html_file(self,FileName):
        '''打开Html文件,并返回文件handle'''
        FileDir=self.Filedir+'/'+FileName
        with open(FileDir,encoding='utf-8') as file:
            HtmlHandle=file.read()
            return HtmlHandle

    def analyze_html(self,File):
        '''分析Html,返回指定节点内容'''
        # Files=self.FindFileList()
        # for File in Files:
        FileContent=self.open_html_file(File)
        soup=BeautifulSoup(FileContent,"html.parser")
        ulist=[]
        for tr in soup.find('tbody').children:
            if isinstance(tr,bs4.element.Tag):
                tds = tr('td')
                BugId=tds[0].find('a')
                Title=tds[3]['title']
                ConfirmOrNot=tds[3].find('span').string
                BugTitleAndConfirmOrNot=ConfirmOrNot+" "+Title
                ulist.append([int(BugId.string), int(tds[1].string),BugTitleAndConfirmOrNot,tds[4].string])
        return ulist

if __name__=='__main__':
    parentdir = os.path.dirname(__file__)
    filedir=parentdir+r"/html"
    # soap=AnalyzeHtml(filedir).OpenHtmlFile('null.htm')
    soap=AnalyzeHtml(filedir).analyze_html('null.htm')
    print(soap)
