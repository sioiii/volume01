from util import *

username = 氢气球啊[1] # 登录账号
password = 123/*-[2] # 登录密码
img_path = os.getcwd() + "/btn-login.png"

@retry(stop_max_attempt_number=5)
def moyupai():
    try:
        driver = get_web_driver()
        driver.get("https://www.ss911.cn/")
        driver.find_element_by_xpath("//*[@id='nameOrEmail']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='loginPassword']").send_keys(password)
        driver.find_element_by_xpath("//*[@class='enter']").click()

        driver.find_element_by_xpath("//*[@id='enter']").click()
        print('tuili签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    tuili()
