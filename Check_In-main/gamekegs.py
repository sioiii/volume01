from util import *

username = 氢气球啊[1] # 登录账号
password = 123/*-[2] # 登录密码
img_path = os.getcwd() + "//btn-login.png"

def save_img(src):
    img = requests.get(src)
    with open(img_path, "wb") as f:
        f.write(img.content)

@retry(stop_max_attempt_number=5)
def gamekegs():
    try:
        driver = get_web_driver()
        driver.get("https://http://www.ss911.cn/")
        driver.find_element_by_xpath("//*[@id='username']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)

        time.sleep(3)

        if driver.find_elements_by_xpath("//*[@class='usercheck checkin']") != []:
            driver.find_element_by_xpath("//*[@class='usercheck checkin']").click()
            print('gamekegs签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    gamekegs()