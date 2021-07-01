import os,configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Taobao():
    def tb(self):
        driver.get(url)
        WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'/html/body/div[6]/div[2]/iframe')))
        driver.execute_script('Object.defineProperty(navigator,"webdriver",{get:()=>false,});')
        print('正在登录...')
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div[1]/div/form/div[1]/div/input')))
        driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/form/div[1]/div/input').send_keys(username)
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div[1]/div/form/div[2]/div/input')))
        driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/form/div[2]/div/input').send_keys(password)
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div[1]/div/form/div[4]/button')))
        driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/form/div[4]/button').click()
        driver.switch_to.default_content()
        print('登录成功')
        try:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[8]/div[2]/div')))
            driver.find_element(By.XPATH,'/html/body/div[8]/div[2]/div').click()
        except:
            pass
        try:
            print('正在选择商品...')
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[6]/div/dl[1]/dd/ul/li[%s]/a'%location)))
            driver.find_element(By.XPATH,'/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[6]/div/dl[1]/dd/ul/li[%s]/a'%location).click()
            print('商品选择成功')
        except:
            print('商品仅有一个或者未找到商品')
        try:
            print('正在选择数量...')
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[6]/div/dl[2]/dd/span/input')))
            driver.find_element(By.XPATH,'/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[6]/div/dl[2]/dd/span/input').send_keys(Keys.CONTROL,'a')
            driver.find_element(By.XPATH,'/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[6]/div/dl[2]/dd/span/input').send_keys(num)
            print('数量选择成功')
        except:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[6]/div/dl/dd/span/input')))
            driver.find_element(By.XPATH,'/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[6]/div/dl/dd/span/input').send_keys(Keys.CONTROL,'a')
            driver.find_element(By.XPATH,'/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[6]/div/dl/dd/span/input').send_keys(num)
            print('数量选择成功')
        try:
            print('正在加入购物车...')
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[6]/div/div[3]/div[2]/a')))
            driver.find_element(By.XPATH,'/html/body/div[6]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[6]/div/div[3]/div[2]/a').click()
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[2]/div[2]')))
            print('加入购物车成功')
        except:
            print('加入购物车失败')
        driver.quit()
        os.system('pause')
    def tm(self):
        driver.get(url)
        WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,'/html/body/div[8]/div[2]/iframe')))
        driver.execute_script('Object.defineProperty(navigator,"webdriver",{get:()=>false,});')
        print('正在登录...')
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div[1]/div/form/div[1]/div/input')))
        driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/form/div[1]/div/input').send_keys(username)
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div[1]/div/form/div[2]/div/input')))
        driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/form/div[2]/div/input').send_keys(password)
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div[1]/div/form/div[4]/button')))
        driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/form/div[4]/button').click()
        driver.switch_to.default_content()
        print('登录成功')
        try:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[8]/div[2]/div')))
            driver.find_element(By.XPATH,'/html/body/div[8]/div[2]/div').click()
        except:
            pass
        try:
            print('正在选择商品...')
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li[%s]/a'%location)))
            driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li[%s]/a'%location).click()
            print('商品选择成功')
        except:
            print('商品仅有一个或者未找到商品')
        try:
            print('正在选择数量...')
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/dl[2]/dd/span[1]/input')))
            driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/dl[2]/dd/span[1]/input').send_keys(Keys.CONTROL,'a')
            driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/dl[2]/dd/span[1]/input').send_keys(num)
            print('数量选择成功')
        except:
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/span[1]/input')))
            driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/span[1]/input').send_keys(Keys.CONTROL,'a')
            driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/span[1]/input').send_keys(num)
            print('数量选择成功')
        try:
            print('正在加入购物车...')
            WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/div[2]/div[2]/a')))
            driver.find_element(By.XPATH,'/html/body/div[5]/div/div[2]/div/div[1]/div[1]/div/div[4]/div/div/div[2]/div[2]/a').click()
            try:
                WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[10]/div/div[1]')))
            except:
                pass
            print('加入购物车成功')
        except:
            print('加入购物车失败')
        driver.quit()
        os.system('pause')
if os.path.isfile('taobaoconfig.ini'):
    config=configparser.ConfigParser()
    config.optionxform=lambda option:option
    config.read('taobaoconfig.ini')
    url=config['taobao']['url']
    num=config['taobao']['num']
    location=config['taobao']['location']
    username=config['taobao']['username']
    password=config['taobao']['password']
    headless=config['taobao']['headless']
    if headless=='1':
        options=Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        driver=webdriver.Chrome(options=options)
    else:
        driver=webdriver.Chrome()
    if 'tmall' in url:
        Taobao().tm()
    else:
        Taobao().tb()
else:
    print('正在生成配置文件...')
    config=configparser.ConfigParser(allow_no_value=True)
    config.optionxform=lambda option:option
    config['taobao']={}
    config['taobao']['#是否打开Chrome，1不打开Chrome，其它打开Chrome']=None
    config['taobao']['headless']='1'
    config['taobao']['#商品链接，类似https://detail.tmall.com/item.htm?id=618701081184或者https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.36.29377de7VsVrGB&id=618701081184&skuId=4732522366520']=None
    config['taobao']['url']=''
    config['taobao']['#商品数量，正整数，例如1']=None
    config['taobao']['num']=''
    config['taobao']['#商品位置，从左到右，从上到下，正整数，例如1']=None
    config['taobao']['location']=''
    config['taobao']['#用户名，例如helloworld']=None
    config['taobao']['username']=''
    config['taobao']['#密码，例如helloworld']=None
    config['taobao']['password']=''
    with open('taobaoconfig.ini','w') as file:
        config.write(file)
    print('配置文件taobaoconfig.ini生成完成，填写好对应信息后再运行')
    os.system('pause')