if __name__ == "__main__":
    from bs4 import BeautifulSoup

class footer():
    def __init__(self):
        f = open('../index.html',mode='r',encoding='utf8') # bắt buộc có sẵn
        self.soup = BeautifulSoup(f.read(),features='lxml')
        f.close()
    def to_html(self,change):
        f = open('../index_newfooter.html',mode='w',encoding='utf8')
        f.write(change)
        f.close()
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

# ví dụ
ft = footer()
ft.change_image('img/logo-light.png')
ft.change_address(1,'1231111111111111111111111111111111111111','New York Street12111111111111111113','New York','(123) 456-7890')
ft.change_copyright('© copyright 2021. All Rights Reservedaaa.')
