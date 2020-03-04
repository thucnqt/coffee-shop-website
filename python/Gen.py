 # -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
class create():
    def __init__(self):
        f = open('../index.html',encoding='utf8',mode='r')
        self.soup = BeautifulSoup(f.read(),features='lxml')
        f.close()
    def to_html(self,change):
        f = open('../index_new.html',encoding='utf8',mode='w')
        f.write(change)
        f.close()
class banner(create):
    def change_text(self,slide,line,text):
        # slide: điền trang muốn thay đổi; 1 hoặc 2
        # line: điền dòng muốn thay đổi; 1, 2 hoặc 3
        # text: điền nội dung thay đổi
        self.soup.find(id=[['bannertext1','bannertitle1','bannertyping1'],
                           ['bannertext2','bannertitle2','bannertyping2']][slide-1][line-1]).string.replace_with(text)
        self.to_html(str(self.soup.prettify()))
class header(create):
    def change_items(self,items):
        for item in range(8): # navbar có 8 mục không đổi
            self.soup.find_all(attrs={'class':'header-link'})[item].string.replace_with(items[item])
        self.to_html(str(self.soup.prettify()))
    def change_logo(self,url='img/logo.png'):
        self.soup.find(id='logo-img')['src'] = url
        self.to_html(str(self.soup.prettify()))

class photo(create):
    def change_image(self,item_n,img_after_click='img/coffee1.jpg',img_page='img/coffee1.jpg'):
        self.soup.find_all(attrs={'class':'item-photo'})[item_n-1].findChildren()[0]['href'] = img_after_click
        self.soup.find_all(attrs={'class':'item-photo'})[item_n-1].findChildren()[1]['src'] = img_page
        self.to_html(str(self.soup.prettify()))

class footer(create):
    def change_image(self,url='img/logo-light.png'):
        self.soup.find(id='footer-image').findChildren()[0]['src'] = url
        self.to_html(str(self.soup.prettify()))
    def change_address(self,column,number,street,city,phone):
        '''
        column: cột muốn sửa, điền 1, 2 hoặc 3
        number: số nhà
        street: đường
        city: thành phố
        phone: số điện thoại
        '''
        self.soup.find_all(attrs={'class':'address-city'})[column-1].string = city
        self.soup.find_all(attrs={'class':'address-phone'})[column-1].contents[0].replace_with('%s, %s, %s' %(number,street,city))
        self.soup.find_all(attrs={'class':'address-phone'})[column-1].contents[1].string = phone
        self.to_html(str(self.soup.prettify()))
    def change_copyright(self,copy_right='© copyright 2020. All Rights Reserved.'):
        self.soup.find(id='copyright').string = copy_right
        self.to_html(str(self.soup.prettify()))

# p = photo()
# p.change_image(1,'img/coffee3.jpg','img/coffee3.jpg')
# b = banner()
# b.change_text(slide=1,line=2,text='fresh porto coffee')
# # ví dụ
# ft = footer()
# ft.change_image('img/logo-light.png')
# ft.change_address(1,'123','New York Street','New York','(123) 456-7890')
# ft.change_copyright('© copyright 2021. All Rights Reserved.')

# # ví dụ
# new_items = ['new home','new about','reservations','menu','news','location','elements','buy porto!']
# b = header()
# b.change_items(new_items)
# b.change_logo('img/logo2.png')