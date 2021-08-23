import os
import time
import pandas as pd
import datetime

CSV_PATH="item_master.csv"
RECEIPT_FOLDER="./receipt"

class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        # self.item_count_list=[]
        self.item_master=item_master
        self.set_datetime()
    
    # #
    # def set_datetime(self):
    #     self.datetime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    
    # def add_item_order(self,item_code):
    #     self.item_order_list.append(item_code)
        
    # def view_item_list(self):
    #     for item in self.item_order_list:
    #         print("商品コード:{}".format(item))

    
    def view_order(self):
        number=1
        self.sum_price=0
        self.sum_count=0
        self.receipt_name="receipt_{}.log".format(self.datetime)
        for item_order in self.item_order_list:
            result = self.get_item_order(item_order)
            print(result)
            
            # 「商品番号の入力→オーダー登録」で止まっている為、個数についてはコメントアウト
            # self.sum_price+=result[1]*int(item_count)
            # self.sum_count+=int(item_count)
            # receipt_data="{0}.{2}({1}) : ￥{3:,}　{4}個 = ￥{5:,}".format(number,item_order,result[0],result[1],item_count,int(result[1])*int(item_count))
            # self.write_receipt(receipt_data)
            # number+=1

    


    def write_receipt(self,text):
        print(text)
    
    # 疑問２（できていないところ）
    #ここに問題があると考えられる。
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)
        # self.item_count_list.append(item_count)
    
    def get_item_order(self,item_code):
        for m in self.item_master:
            if item_code == m.item_code:
                return m.item_code,m.item_name,m.price
    
    #課題２
    def input_order(self):
        buy_item_code = input("購入したい商品の番号を入力してください")
        
        # 疑問１
        #item_order_listは関数の外からでも持ってこれるのが、まだ理解できていない状態です。
        # 継承されているのでしょうか。引数のselfが、item_order_listを持ってきているのか。
        self.add_item_order(buy_item_code)
        
        # 「商品番号の入力→オーダー登録」で止まっている為、個数についてはコメントアウト
        # buy_item_count=input("個数を入力してください　>>> ")
        # self.add_item_order(buy_item_code,buy_item_count

# 課題３
def add_item_master_by_csv(csv_path):
    item_master=[]
    item_master_df=pd.read_csv(csv_path,dtype={"item_code":object}) # CSVでは先頭の0が削除されるためこれを保持するための設定
    for item_code,item_name,price in zip(list(item_master_df["item_code"]),list(item_master_df["item_name"]),list(item_master_df["price"])):
        item_master.append(Item(item_code,item_name,price))
        print("{}({})".format(item_name,item_code))


    
### メイン処理
def main():
    # マスタ登録（課題３）
    item_master=add_item_master_by_csv(CSV_PATH)
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))
    
    
    # オーダー登録
    order=Order(item_master)
    # order.add_item_order("001")
    # order.add_item_order("002")
    # order.add_item_order("003")
    order.input_order()
    
    # 課題１ オーダー登録した商品の一覧表示
    order.view_order()
    # order.view_item_list()
    
if __name__ == "__main__":
    main()