import requests
import json
from PySide2.QtWidgets import *
from PySide2.QtCore import *

group_table_checkbox = []

filename = 'data.json'


def group_page_refresh_data(api_url,token,self):
    print('robots_page--robots_page_refresh_data')

    #讀資料
    with open(filename,"r") as f_obj:
        #讀取資料
        data = json.load(f_obj)


    params = {
        'fields': 'groups',
        'access_token': token,
    }

    try:
        response = requests.get(api_url, params=params)
    except (requests.ConnectionError, requests.Timeout,KeyError) as e:
        if 'port=443' in str(e):
            self.log_bar.setText(self.tr('連接facebook失敗，請檢查網路'))
            return 

    response_json = requests_states(self,response)

    if response_json == False:
        return


    #獲取機械人數量同item項目
    count = len(response_json['groups']['data'])
    items = response_json['groups']['data']

    #根據群組數量而增加個table行位
    self.group_table.setRowCount(count)
    
    for i in range(count):
        #獲取item項目入面嘅資料
        id = items[i]['id']
        name = items[i]['name']

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
        #寫table每格嘅資料
        self.group_table.setItem(i,1,QTableWidgetItem(id))
        self.group_table.setItem(i,2,QTableWidgetItem(name))


        #第一次迴圈先清空
        if i == 0:
            data['group_list'] = []

        data['group_list'].append({"checkbox_state":False,"id":id,"name":name}) 
            

    with open(filename,'w') as f_obj:
        json.dump(data,f_obj)


    if response.status_code == 200:
        self.log_bar.setText(self.tr('已刷新群組'))



def requests_states(self,response):
    try:
        response_json = response.json()
        message = str(response_json['error']['message'])
        #message == '当****6*前配额不足，前往控制台获取更多 https://hamibot.com/account/quotas'
        if 'The access token could not be decrypted' in message or 'Malformed access token' in message:
            self.log_bar.setText(self.tr('輸入的token錯誤，請重新輸入'))
            return False
        elif 'Error validating access token: Session has expired on' in message:
            self.log_bar.setText(self.tr('token已過期，請重新獲取'))
            return False
        else:
            self.log_bar.setText(self.tr('未知錯誤--')+str(response_json))
            print(self.tr('未知錯誤--')+str(response_json))
            return False
    except (Exception,KeyError) as e:
        if 'error' in str(e):
            return response_json
        else:
            self.log_bar.setText(self.tr('未知錯誤--')+str(e))
            print(self.tr('未知錯誤--')+str(e))
            return False


