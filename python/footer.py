if __name__ == "__main__":
    from bs4 import BeautifulSoup


class footer():
    def __init__(self):
        f = open('../index.html',mode='r',encoding='utf8')
        self.soup = BeautifulSoup(f.read(),features='lxml')
        f.close()
    def change_image(self,url='img/logo-light.png'):
        f = open('../index.html',mode='w',encoding='utf8')
        self.soup.find(id='footer-image').findChildren()[0]['src'] = url
        f.write(str(self.soup.prettify()))
        f.close()
    def change_address(self,column,number,street,city,phone):
        '''
        column: cột muốn sửa, điền 1, 2 hoặc 3
        number: số nhà
        street: đường
        city: thành phố
        phone: số điện thoại
        '''
        f = open('../index.html',mode='w',encoding='utf8')
        self.soup.find_all(attrs={'class':'address-city'})[column-1].string = city
        self.soup.find_all(attrs={'class':'address-phone'})[column-1].contents[0].replace_with('%s, %s, %s' %(number,street,city))
        self.soup.find_all(attrs={'class':'address-phone'})[column-1].contents[1].string = phone
        f.write(str(self.soup.prettify()))
        f.close()
    def change_copyright(self,copy_right='© copyright 2020. All Rights Reserved.'):
        f = open('../index.html',mode='w',encoding='utf8')
        self.soup.find(id='copyright').string = copy_right
        f.write(str(self.soup.prettify()))
        f.close()

# ví dụ
ft = footer()
ft.change_image('img/logo-light.png')
ft.change_address(1,'123','New York Street','New York','(123) 456-7890')
ft.change_copyright('© copyright 2021. All Rights Reserved.')