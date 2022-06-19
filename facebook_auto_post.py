import sys
import json
import os
import re
import pyperclip
import time
import base64
import requests

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from ui.main_ui import Ui_MainWindow
from page.group_page import *



#獲取當下系統語言
local_language = QLocale.system().name()

filename = 'data.json'
facebook_api_url = "https://graph.facebook.com/v14.0/me"
chromedrive_version = ''

#紀錄目前選擇左嘅機械人
hamibot_current_robot = {'id': ' ', 'name': ' ', 'tag': ' '}

# 接收出錯的資訊
sys.stderr = open('errorlog.txt', 'wt',encoding='utf-8')

# 接收到print語句
sys.stdout = open('printlog.txt','wt',encoding='utf-8')


#判斷有無data.json呢個檔，無就寫入空白嘅數據，因無數據情況下面就咁讀資料會error
if not os.path.exists(filename):
	#第一次運行首先創建filename以及創建數據，以免下面讀嘅時侯error
	with open(filename,"w") as f_obj:
		#先寫入各種空白資料
		json.dump({"language":"","chromedrive_version":"","current_tab":1,"end_post_action":0,"wait_overtime":60,"end_post_url":"","facebook_token":"","remember_email":"","facebook_email":"","remember_pw":"","facebook_pw":"","browser_box":0,"current_posting":0,"posting_information":"","browser_location":"","chromedriver_location":"","chromedriver_location":"","browser_location":"","group_id":"","group_list":[]},f_obj)


#讀資料
with open(filename,"r") as f_obj:
    #讀取資料
    data = json.load(f_obj)

class MainWindow(Ui_MainWindow, QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)

		global chromedrive_version

		#只顯示最小化同關閉按鈕，即禁止窗口最大化按钮
		self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
		#禁止拉伸窗口大小
		self.setFixedSize(self.width(),self.height())
		

		#新增按鈕
		self.refresh_group = QPushButton(self.tr('刷新群組'))
		# 為"發帖完成後動作"戈行group埋一諂
		self.end_post_action = QButtonGroup()
		self.end_post_action.addButton(self.end_post_none,0)
		self.end_post_action.addButton(self.end_post_close_browser,1)
		self.end_post_action.addButton(self.end_post_open_url,2)

		#為tabwidget添加按鈕
		self.widget = QWidget()
		h_layout = QHBoxLayout(self.widget)
		h_layout.setContentsMargins(0, 0, 0, 0)
		h_layout.addWidget(self.refresh_group)
		self.tabWidget.setCornerWidget(self.widget)

		if data['group_list'] != []:
			self.group_table.setRowCount(len(data['group_list']))
			for i in range(len(data['group_list'])):
				# 新增CheckBox按鈕，用來多選，暫時只有咁先可以置中
				ck = QCheckBox()
				h = QHBoxLayout()
				h.setAlignment(Qt.AlignCenter)
				h.addWidget(ck)
				w = QWidget()
				w.setLayout(h)

				#增加表格高度
				self.group_table.setRowHeight(i,32)
				#為第一列加CheckBox按鈕
				self.group_table.setCellWidget(i,0,w)
				#checkbox寫入到group_table_checkbox變量到
				group_table_checkbox.append(ck)
				#讀取番True同False狀態
				group_table_checkbox[i].setChecked(data['group_list'][i]['checkbox_state'])
				self.group_table.setItem(i,1,QTableWidgetItem(data['group_list'][i]['id']))
				self.group_table.setItem(i,2,QTableWidgetItem(data['group_list'][i]['name']))
	
		self.browser_box.currentIndexChanged.connect(self.on_browser_box)
		#判斷打開邊版tabwidget
		self.tabWidget.currentChanged.connect(self.oncurrentChanged)

		#只能輸入Int
		self.current_posting.setValidator(QIntValidator())
		chromedrive_version = data['chromedrive_version']
		#默認打開設定戈版
		self.tabWidget.setCurrentIndex(data['current_tab'])
		self.end_post_action.button(data['end_post_action']).setChecked(True)
		self.wait_overtime.setText(str(data['wait_overtime']))
		self.end_post_url.setText(data['end_post_url'])
		self.tokens.setText(data['facebook_token'])
		self.group_id.setText(data['group_id'])
		self.current_posting.setText(str(data['current_posting']))
		#將之前已經填過嘅各種資料填番入指定欄位
		self.browser_location.setText(data['browser_location'])
		self.chromedriver_location.setText(data['chromedriver_location'])
		self.posting_information.setPlainText(data['posting_information'])
		self.log_bar.setStyleSheet('font:11pt')
		self.browser_box.setCurrentIndex(data['browser_box'])
		
		if data['remember_email'] == True:
			self.remember_email.setChecked(True)
			self.facebook_email.setText(base64.b85decode(data['facebook_email']).decode('utf-8'))

		if data['remember_pw'] == True:
			self.remember_pw.setChecked(True)
			self.facebook_pw.setText(base64.a85decode(data['facebook_pw']).decode('utf-8'))		


		if self.tabWidget.currentIndex() != 0:
			self.refresh_group.hide()

		if self.browser_box.currentIndex() == 0:
			self.label_8.setHidden(True)
			self.chromedriver_location.setHidden(True)
			self.get_chromedriver_url.setHidden(True)
			self.chromedriver_location_choose.setHidden(True)
			self.log_bar.setText('Chrome[模式一]：此模式會自動為Chrome下載對應版本的chromedriver。')


		#修改folder icon
		self.browser_location_choose.setPixmap('./pic/folder.png')
		self.chromedriver_location_choose.setPixmap('./pic/folder.png')

		#修改icon
		self.setWindowIcon(QIcon('./pic/icon.ico'))

		#調整group_table顯示頂部，隱藏側欄，因為好似qt	 designer有BUG整左都無顯示
		self.group_table.horizontalHeader().setVisible(True)
		self.group_table.verticalHeader().setVisible(False)
		self.group_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
		#調整group_table字型，因為好似qt designer有BUG整左都無顯示
		self.group_table.setFont(QFont("Noto Sans SC Medium",12))
		#調整group_table，指定欄位個寬
		self.group_table.setColumnWidth(0,50)
		self.group_table.setColumnWidth(1,150)
		self.group_table.setColumnWidth(2,450)


		#設定版面↓
		#修改禁得嘅連結
		self.get_tokens_url.setText("<A href='https://developers.facebook.com/tools/explorer/'>"+self.tr('（獲取token）')+"</a>")
		self.get_chromedriver_url.setText("<A href='https://chromedriver.chromium.org/downloads'>"+self.tr('（下載）')+"</a>")

		#當單擊名字欄會自動紀錄ID
		self.group_table.clicked.connect(self.group_table_clicked)
		self.all_select.clicked.connect(self.all_select_clicked)
		self.reverse_select.clicked.connect(self.reverse_select_clicked)
		self.cancel_select.clicked.connect(self.cancel_select_clicked)
		self.copy_group_id.clicked.connect(self.copy_group_id_clicked)

		#當點選folder_choose時就會彈出個瀏覽資料夾
		self.browser_location_choose.mousePressEvent = self.on_openbrowser_location
		self.chromedriver_location_choose.mousePressEvent = self.on_chromedriver_location

		self.start_auto_post_group_button.clicked.connect(self.on_start_auto_post_group_button)

		#為刷新按鈕添加功能
		self.refresh_group.clicked.connect(self.on_refresh_group_button)


		self.translator = QTranslator(app)

	def group_table_clicked(self):
		row = self.group_table.currentIndex().row()

		#當點某一行而方框狀態未勾選時，就會變成勾選
		if group_table_checkbox[row].isChecked() == False:
			group_table_checkbox[row].setChecked(True)
		else:
			group_table_checkbox[row].setChecked(False)


	def oncurrentChanged(self,i):
		#當打開指定頁面button先顯示番，唔同match原因係要python3.10，xp會用唔到
		if i == 0:
			self.refresh_group.show()
		else:
			self.refresh_group.hide()

	def all_select_clicked(self):
		for line in range(len(group_table_checkbox)):
			group_table_checkbox[line].setChecked(True)

	def reverse_select_clicked(self):
		for line in range(len(group_table_checkbox)):
			if group_table_checkbox[line].isChecked() == True:
				group_table_checkbox[line].setChecked(False)
			else:
				group_table_checkbox[line].setChecked(True)


	def copy_group_id_clicked(self):
		copy_group_id = ''
		for line in range(len(group_table_checkbox)):
			if group_table_checkbox[line].isChecked() == True:
				copy_group_id = copy_group_id + self.group_table.item(line,1).text() + ','
		pyperclip.copy(copy_group_id[:-1])

	def cancel_select_clicked(self):
		for line in range(len(group_table_checkbox)):
			group_table_checkbox[line].setChecked(False)


	def onlanguage_switch(self,i):	
		if i == 1:
			data['language'] = 'tc'
			self.log_bar.setText('更換語言後請重新打開軟件')
		elif i == 2:
			data['language'] = 'sc'
			self.log_bar.setText('更换语言后请重新打开软件')

		with open(filename,'w') as f_obj:
				json.dump(data,f_obj)


	def on_browser_box(self,index):
		if index == 0:
			self.label_8.setHidden(True)
			self.chromedriver_location.setHidden(True)
			self.get_chromedriver_url.setHidden(True)
			self.chromedriver_location_choose.setHidden(True)
			self.log_bar.setText('Chrome[模式一]：此模式會自動為Chrome下載對應版本的chromedriver。')
		else:
			self.label_5.setHidden(False)
			self.browser_location.setHidden(False)
			self.browser_location_choose.setHidden(False)
			self.label_8.setHidden(False)
			self.chromedriver_location.setHidden(False)
			self.get_chromedriver_url.setHidden(False)
			self.chromedriver_location_choose.setHidden(False)
			self.log_bar.setText('Chrome[模式二]：此模式為可選擇Chrome瀏覽器外，亦可手動下載並選擇chromedriver。')

	def on_start_auto_post_group_button(self):
		global chromedrive_version
		browser = ''
		mode = self.browser_box.currentIndex()
		group_id = self.group_id.text().replace(' ','').split(",")
		browser_location = self.browser_location.text()
	
		#用來比模式一用，自動下載，唔洗自己選chromedriver↓
		browser_location_split = browser_location.split('/')
		# 刪除最後一位
		browser_location_split.pop()
		browser_location_split_location = '/'.join(browser_location_split)
		#用來比模式一用，自動下載，唔洗自己選chromedriver↑

		chromedriver_location = self.chromedriver_location.text()
		posting_message = self.posting_information.toPlainText()
		wait_overtime = int(self.wait_overtime.text())
		current_posting = int(self.current_posting.text())
		facebook_email = self.facebook_email.text()
		facebook_pw = self.facebook_pw.text()

		if facebook_email == '':
			self.log_bar.setText('請到設定頁填寫facebook電子郵件地址')
			return
		if facebook_pw == '':
			self.log_bar.setText('請到設定頁填寫facebook密碼')
			return
		if group_id == ['']:
			self.log_bar.setText('請填寫Group_id')
			return
		if posting_message == '':
			self.log_bar.setText('請填寫帖子內容')
			return
		if mode == 0 or mode == 1:
			if browser_location == '':
				self.log_bar.setText('請填寫瀏覽器位置')
				return
			if mode == 1:
				if chromedriver_location == '':
					self.log_bar.setText('請填寫chromedriver位置')
					return
		if self.end_post_action.checkedId() == 2 and self.end_post_url.text() == '':
			self.log_bar.setText('請填寫要打開的網址')
			return
			

		facebook_name = ''
		post_state = ''
		post_count_record = 0
		post_repty_times = 0

		#facebook xPath
		enter_email_hints = "//input[@placeholder='電子郵件地址或手機號碼']"
		enter_pw_hints = "//input[@placeholder='密碼']"
		login_button_hints = "//button[text()='登入']"
		# home_text_hints = "//span[contains(text(),'你在想什麼？')]"
		home_text_hints = "//a[contains(@aria-label,'的生活時報')]"
		facebook_name_hints = "的生活時報"
		information_area_hints = "//span[text()='寫點內容......']/../.."
		post_count_hints = "//span[text()='讚好']"
		post_information_area_hints = "//div[text()='建立公開帖子......']"
		posting_button_hints = "//span[text()='發佈']"
		posting_hints = "//span[text()='發佈中']"
		#最近10個帖子有發過，則不發帖

		self.log_bar.setText('自動群組發帖運行中...')
		print('自動群組發帖運行中...')

		
		open_brower = webdriver.ChromeOptions()
		open_brower.add_experimental_option("detach", True) # 最終不關瀏覽器
		open_brower.add_experimental_option('excludeSwitches', ['enable-logging']) # disable DevTools listening
		open_brower.binary_location = browser_location

		
		try:
			if mode == 0 and chromedrive_version == '':
				# 如果第一次開就會嘗試安裝chromedrive
				browser = webdriver.Chrome(executable_path = ChromeDriverManager(path = browser_location_split_location).install(),chrome_options=open_brower)
			elif mode == 0 and chromedrive_version != '':
				# 如果唔係第一次開就會用番之前安裝
				browser = webdriver.Chrome(executable_path = browser_location_split_location + '/.wdm/drivers/chromedriver/win32/' + chromedrive_version + '/chromedriver.exe',chrome_options=open_brower)
			elif mode == 1:
				# 打開瀏覽器
				browser = webdriver.Chrome(executable_path = chromedriver_location,chrome_options=open_brower)

		except (Exception) as e:
			if "executable needs to be in PATH." in str(e):
				chromedrive_version = ''
				self.log_bar.setText('缺少chromedriver或者環境變量，請嘗試切換模式或重新嘗試‧')
			elif 'This version of ChromeDriver only supports Chrome version' in str(e):
				chromedrive_version = ''
				version = re.split(' |\n',str(e))
				chromedriver_support_version = version[17]
				get_url_chromedriver_version = []
				time.sleep(1)
				self.log_bar.setText('chromedriver只支援'+version[12]+'版本與chrome瀏覽器'+version[17]+'版本不兼容，將更新chromedriver。')
				print('chromedriver只支援'+version[12]+'版本與chrome瀏覽器'+version[17]+'版本不兼容，請更新chromedriver。')
				time.sleep(1)
				self.log_bar.setText('嘗試下載chromedriver...')
				print('嘗試下載chromedriver...')
				get_chromedriver = requests.get('https://chromedriver.storage.googleapis.com/')
				soup = BeautifulSoup(get_chromedriver.content,features='xml')
				tag_name = soup.find_all("Key")
				for name in tag_name:
					if "chromedriver_win32.zip" in name.string:
						get_url_chromedriver_version.append(name.string)
				
				for i in range(len(chromedriver_support_version)):
					for ii in range(len(get_url_chromedriver_version)):
						if chromedriver_support_version in get_url_chromedriver_version[ii]:
							chromedrive_version = get_url_chromedriver_version[ii].replace('/chromedriver_win32.zip','')
							break
					
					if chromedrive_version != '':
						break
					else:
						chromedriver_support_version = chromedriver_support_version[:-1]
				if mode == 1:
					self.log_bar.setText('由於當前路徑為舊版本chromedriver，將修改新版本chromedriver路徑。')
					print('由於當前路徑為舊版本chromedriver，將修改新版本chromedriver路徑')
					self.chromedriver_location.setText(browser_location_split_location + '/.wdm/drivers/chromedriver/win32/' + chromedrive_version + '/chromedriver.exe')

				# 下載指定版本，並重新打開瀏覽器
				browser = webdriver.Chrome(executable_path = ChromeDriverManager(path = browser_location_split_location,version=chromedrive_version).install(),chrome_options=open_brower)

			else:
				self.log_bar.setText('未知錯誤---'+str(e))
				print('未知錯誤---'+str(e))

		try:
			browser.get('http://www.facebook.com/')
		except (Exception) as e:
			print('未知錯誤---'+str(e))
		#等待元素指定秒數
		wait = WebDriverWait(browser,wait_overtime)
		#登入email密碼並登入並到首頁
		wait.until(EC.presence_of_element_located((By.XPATH,enter_email_hints))).send_keys(facebook_email)
		browser.find_element_by_xpath(enter_pw_hints).send_keys(facebook_pw)
		browser.find_element_by_xpath(login_button_hints).click()
		wait.until(EC.presence_of_element_located((By.XPATH,home_text_hints)))
		ActionChains(browser).move_by_offset(1, 1).click().perform()  # 鼠標左鍵點擊，以免彈出通知
		#獲取facebook個名
		facebook_name = browser.find_element_by_xpath(home_text_hints).get_attribute('aria-label').replace(facebook_name_hints,'')
		
		for i in range(len(group_id)):
			ActionChains(browser).reset_actions() # 重置坐標
			self.log_bar.setText('總共需要發佈'+str(i+1)+'/'+str(len(group_id))+'帖')
			print(self.log_bar.setText('總共需要發佈'+str(i+1)+'/'+str(len(group_id))+'帖'))

			post_state = 'normal'
			link = "https://www.facebook.com/groups/" + group_id[i]
			browser.get(link)
			#發帖框
			wait.until(EC.element_to_be_clickable((By.XPATH,information_area_hints)))
			ActionChains(browser).move_by_offset(1, 1).click().perform()  # 鼠標左鍵點擊，以免彈出通知

			#先檢查左有無需要發帖先↓
			#只要要求數量唔係等於0
			if current_posting !=0:
				# 有可能太小帖
				if len(browser.find_elements_by_xpath(post_count_hints)) >= current_posting:
					post_state = 'refresh'
					#發現到有post過
					if len(browser.find_elements_by_xpath("//span[text()='"+facebook_name+"']")) > 1:
						#就唔發帖
						post_state = 'non_post'
						continue
				else:
					#依家帖子數量少過要求數量
					while len(browser.find_elements_by_xpath(post_count_hints)) <= current_posting:
						post_state = 'refresh'
						#就會拉落去睇下
						browser.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)
						time.sleep(3)
						#發現到有post過，因為1係自己個頭像戈到個名
						if len(browser.find_elements_by_xpath("//span[text()='"+facebook_name+"']")) > 1:
							#就唔發帖
							post_state = 'non_post'
							break
				
						#如果拉左落去同之前個數量一樣
						if len(browser.find_elements_by_xpath(post_count_hints)) == post_count_record:
							#有可能網絡問題或者已經到底，如果超過5次都係咁，就退出去照發帖
							if post_repty_times == 5:
								break
							else:
								post_repty_times = post_repty_times + 1 
						else:
							post_count_record = len(browser.find_elements_by_xpath(post_count_hints))


			if post_state == 'non_post':
				continue
			#先檢查左有無需要發帖先↑
			elif post_state == 'refresh':
				# 重新load一次網頁，用來重新定位個發帖框
				browser.get(link)
			
			time.sleep(1)
			wait.until(EC.element_to_be_clickable((By.XPATH,information_area_hints))).click()

			posting_button = wait.until(EC.presence_of_element_located((By.XPATH,posting_button_hints)))
			try:
				# 寫點內容......
				information_area = browser.find_element_by_xpath(information_area_hints)
			except:
				# 建立公開帖子......
				information_area = browser.find_element_by_xpath(post_information_area_hints)

			# 輸入post內容
			ActionChains(browser).move_to_element(information_area).send_keys(posting_message).perform()
			posting_button.click()

			# 等待發帖完成
			try:
				while (browser.find_element_by_xpath(posting_hints)):
					time.sleep(3)
			except (Exception) as e:
				pass

			# 發完帖，等待發帖框指定xpath出來先轉版
			wait.until(EC.element_to_be_clickable((By.XPATH,information_area_hints)))
			time.sleep(2)

		self.log_bar.setText('自動群組發帖完成')

		match self.end_post_action.checkedId():
			case 1:
				browser.quit()
			case 2:
				url = self.end_post_url.text()
				if 'http://' in url:
					pass
				else:
					url = 'http://' + url
				browser.get(url)
		
			

	def on_openbrowser_location(self, event):
		if event.button() == Qt.LeftButton:
			
			#獲取依家文件夾位置
			before_FileDirectory = self.browser_location.text()

			#選擇目錄，返回選中的路徑
			FileDirectory = QFileDialog.getOpenFileName(QMainWindow(), self.tr("選擇瀏覽器"),'','Exe file(*.exe)')

			#如果選擇嘅資料夾同之前唔同
			if before_FileDirectory != FileDirectory[0]:
				before_FileDirectory = FileDirectory[0]
				#將路徑放入edit_link到
				self.browser_location.setText(FileDirectory[0])
				#增加log_bar提示
				self.log_bar.setText(self.tr('設定瀏覽器路徑為：')+FileDirectory[0])
			else:
				self.log_bar.setText(self.tr('與之前設定的瀏覽器路徑相同'))

	def on_chromedriver_location(self, event):
		if event.button() == Qt.LeftButton:
			
			#獲取依家文件夾位置
			before_FileDirectory = self.chromedriver_location.text()

			#選擇目錄，返回選中的路徑
			FileDirectory = QFileDialog.getOpenFileName(QMainWindow(), self.tr("選擇chromedriver"),'','Exe file(*.exe)')

			#如果選擇嘅資料夾同之前唔同
			if before_FileDirectory != FileDirectory[0]:
				before_FileDirectory = FileDirectory[0]
				#將路徑放入edit_link到
				self.chromedriver_location.setText(FileDirectory[0])
				#增加log_bar提示
				self.log_bar.setText(self.tr('設定chromedriver路徑為：')+FileDirectory[0])
			else:
				self.log_bar.setText(self.tr('與之前設定的chromedriver路徑相同'))


	
	def on_refresh_group_button(self):
		if  self.tokens.text() == "":
			self.log_bar.setText(self.tr('請到設定頁完整輸入token'))
			return

		#tokens變量
		access_token = self.tokens.text()
		#更新機械人頁面數據
		group_page_refresh_data(facebook_api_url,access_token,self)


	def closeEvent(self,event):
		#讀資料
		with open(filename,"r") as f_obj:
			#讀取資料
			data = json.load(f_obj)

		# 結束時侯先紀錄
		for i in range(self.group_table.rowCount()):
			#已紀錄嘅資料勾選同當刻勾選資料唔同
			if data['group_list'][i]['checkbox_state'] != group_table_checkbox[i].isChecked():
				#就會修改
				data['group_list'][i]['checkbox_state'] = group_table_checkbox[i].isChecked()

		data['chromedrive_version'] = chromedrive_version
		data['current_tab'] = self.tabWidget.currentIndex()
		data['wait_overtime'] = int(self.wait_overtime.text())
		data['end_post_action'] = self.end_post_action.checkedId()
		data['end_post_url'] = self.end_post_url.text()
		data['group_id'] = self.group_id.text().replace(' ','')
		data['current_posting'] = int(self.current_posting.text())
		data['posting_information'] = self.posting_information.toPlainText()
		data['browser_location'] = self.browser_location.text()
		data['chromedriver_location'] = self.chromedriver_location.text()
		data['facebook_token'] = self.tokens.text()
		data['browser_box'] = self.browser_box.currentIndex()


		if self.remember_email.isChecked() == True:
			data['remember_email'] =  self.remember_email.isChecked()
			data['facebook_email'] = str(base64.b85encode(self.facebook_email.text().encode('UTF-8')))[2:][:-1]
		else:
			data['remember_email'] = ''
			data['facebook_email'] = ''
		if self.remember_pw.isChecked() == True:
			data['remember_pw'] =  self.remember_pw.isChecked()
			data['facebook_pw'] = str(base64.a85encode(self.facebook_pw.text().encode('UTF-8')))[2:][:-1]
		else:
			data['remember_pw'] = ''
			data['facebook_pw'] = ''
			
		with open(filename,'w') as f_obj:
				json.dump(data,f_obj)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	
	trans = QTranslator(app)

	#當第一次使用就會根據系統嘅語言
	if data['language'] == '':
		if  'TW' in local_language or 'HK' in local_language or 'MO' in local_language:
			data['language'] = 'tc'
		elif 'CN'  in local_language:
			data['language'] = 'sc'
		else:
			data['language'] = 'tc'
		
		with open(filename,'w') as f_obj:
			json.dump(data,f_obj)


	trans.load('./language/'+data['language'])
	app.installTranslator(trans)

	mwin = MainWindow()
	# qtmodern.styles.dark(app)
	# win = qtmodern.windows.ModernWindow(mwin)
	mwin.show()

	sys.exit(app.exec_())
