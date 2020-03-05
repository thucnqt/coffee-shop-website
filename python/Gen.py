 # -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os.path
import json

# Tạo class: Mở  File, Sau đó đọc với thư viện BeautifulSoup.
# Ghi đè những nội dung thay đổi
class create():
    def __init__(self):
        # Kiểm tra file index_new.html (là file được generate ra) 
        # nếu tồn tại tiếp tục đọc và ghi đè thông tin cần thay đổi.
        # k có file đó thì đọc và ghi lên 1 file mới.
        if os.path.isfile('../index_new.html'):
            f = open('../index_new.html',encoding='utf8',mode='r')
            self.soup = BeautifulSoup(f.read(),features='lxml')
            f.close()
        else:
            f = open('../index.html',encoding='utf8',mode='r')
            self.soup = BeautifulSoup(f.read(),features='lxml')
            f.close()
    def to_html(self,change):
        f = open('../index_new.html',encoding='utf8',mode='w')
        f.write(change)
        f.close()

# Tạo class banner: thay đội nội dung phần slide, kế thừa lớp create
class banner(create):
    def change_text(self,slide,line,text):
        # slide: điền trang muốn thay đổi; 1 hoặc 2
        # line: điền dòng muốn thay đổi; 1, 2 hoặc 3
        # text: điền nội dung thay đổi
        self.soup.find(id=[['bannertext1','bannertitle1','bannertyping1'],
                           ['bannertext2','bannertitle2','bannertyping2']][slide-1][line-1]).string.replace_with(text)
        self.to_html(str(self.soup.prettify()))

# Tạo class headers: thay đổi nội dung phần navbar, kế thừa lớp create
class header(create):
    def change_items(self,items):
        for item in range(8): # navbar có 8 mục không đổi
            self.soup.find_all(attrs={'class':'header-link'})[item].string.replace_with(items[item])
        self.to_html(str(self.soup.prettify()))
    def change_logo(self,url='img/logo.png'):
        self.soup.find(id='logo-img')['src'] = url
        self.to_html(str(self.soup.prettify()))

# Tạo class photo: thay đổi  hình ảnh phần photo, kế thừa lớp create
class photo(create):
    def change_image(self,item_n,img_after_click='img/coffee1.jpg',img_page='img/coffee1.jpg'):
        self.soup.find_all(attrs={'class':'item-photo'})[item_n-1].findChildren()[0]['href'] = img_after_click
        self.soup.find_all(attrs={'class':'item-photo'})[item_n-1].findChildren()[1]['src'] = img_page
        self.to_html(str(self.soup.prettify()))

# Tạo class menu: Thay đổi thực đơn, giá bán.
class menu(create):
    def change_main(self,head='Our menu',detail ='Cap nhat nhung mon ăn ngon vch'):
        self.soup.find(id='our_menu').find('h2').string = head
        self.soup.find(id='our_menu').find('p').string = detail
        self.to_html(str(self.soup.prettify()))
    def change_menu(self,item_n, item, price, detail):
        self.soup.find_all(attrs={'class':'info_item'})[item_n-1].find_all("h3")[0] = item
        self.soup.find_all(attrs={'class':'info_item'})[item_n-1].find_all("p")[0] = price
        self.soup.find_all(attrs={'class':'detail'})[item_n-1].string = detail
        self.to_html(str(self.soup.prettify()))
    def change_button(self,button_name='view'):
        self.soup.find_all(attrs={'class':'button_menu'})[0].string = button_name
        self.to_html(str(self.soup.prettify()))
# c = menu()
# c.change_button("hello wỏld")
# c = menu()
# c.change_menu(5,'Ca phe', '$2', 'Hạt, đường, sữa')
# Tạo class about
# class about(create):
#     def change_title(self, title, abc):
#        self.soup.find(attrs={'class':'rotator-word'}).find('h2').string = title
#        self.soup.find_all(attrs={'class':'_item1'}).string = abc
#        self.to_html(str(self.soup.prettify()))

# a = about()
# Tạo class reservations
class reservations(create):
    def change_info(self,head,detail,phone_number):
       self.soup.find(attrs={'class':'wraper1'}).find('h2').string = head
       self.soup.find(attrs={'class':'wraper1'}).find('p').string = detail
       self.soup.find(attrs={'class':'wraper1'}).find('a').string = phone_number
       self.to_html(str(self.soup.prettify()))
    def change_time(self,n_day,day,n_time,time):
        self.soup.find(attrs={'class':'wraper2'}).find_all('h2')[n_day-1].string = day
        self.soup.find(attrs={'class':'wraper2'}).find_all('p')[n_time-1].string = time
        self.to_html(str(self.soup.prettify()))


# r = reservations()
# r.change_time(1,'MON - TUS',2,'9:00PM - 10:00 PM')
# r.change_info('Phuc vu hang ngay', ' San sang ho tro ban moi ngay', '098766161s')
# Test: 65 Cao Thắng lat: 10.771250 long: 106.680616

# Tạo class New: thay đổi nội dung phần News, kế thừa lớp create
class New(create):
    def change_main(self,head='New & photo',detail ='Cap nhat nhung tin tuc nong hoi'):
        self.soup.find_all(attrs={'class':'first_news'})[0].string = head
        self.soup.find_all(attrs={'class':'first_news'})[1].string = detail
        self.to_html(str(self.soup.prettify()))
    def change_content(self,column,head='',date='',detail='',autor=''):
        self.soup.find_all(attrs={'class':'_head'})[column-1].string = head
        self.soup.find_all(attrs={'class':'_date'})[column-1].string = date
        self.soup.find_all(attrs={'class':'_detail'})[column-1].string = detail
        self.soup.find_all(attrs={'class':'_autor'})[column-1].string = autor
        self.to_html(str(self.soup.prettify()))
    def change_button(self,button_name='view'):
        self.soup.find_all(attrs={'class':'button_news'})[0].string = button_name
        self.to_html(str(self.soup.prettify()))

# Tạo class footer: thay đổi nội dung phần footer, kế thừa lớp create
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

# Example test 
# p = photo()
# p.change_image(1,'img/coffee2.jpg','img/coffee2.jpg')
# # b = banner()
# # b.change_text(slide=1,line=2,text='fresh porto coffee')
# # # ví dụ
# # ft = footer()
# # ft.change_image('img/logo-light.png')
# # ft.change_address(1,'123','New York Street','New York','(123) 456-7890')
# # ft.change_copyright('© copyright 2021. All Rights Reserved.')

# # # ví dụ
# # new_items = ['new home','new about','reservations','menu','news','location','elements','buy porto!']
# # b = header()
# # b.change_items(new_items)
# # b.change_logo('img/logo2.png')


# a = New()
# a.change_button('Xem them di')

# a.change_main('New home112321321','la mot ngoi nha moi')