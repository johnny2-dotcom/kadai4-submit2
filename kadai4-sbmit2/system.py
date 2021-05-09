from menu import Menu
import pandas as pd
from datetime import  datetime

# 課題１
# menu_item1 = Menu(0,'サンドイッチ',500)
# menu_item2 = Menu(1,'チョコケーキ', 400)
# menu_item3 = Menu(2,'コーヒー', 300)
# menu_item4 = Menu(3,'オレンジジュース', 200)
# menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

# 課題２、課題３
def system():

    try:
        df = pd.read_csv('menu.csv')
        codes = df['code'].tolist()
        names = df['name'].tolist()
        prices = df['price'].tolist()

        menu_items = []
        for code,name,price in zip(codes,names,prices):
            menu_item = Menu(code,name,price)
            menu_items.append(menu_item)

        for item in menu_items:
            print(item.menu_disp())

        print('***************************************')
        order = int(input('メニューの商品番号を入力してください: '))
        selected_menu = menu_items[order]
        print('選択された商品: ' + selected_menu.name)

        # 課題４ 課題５
        print('***************************************')
        count = int(input('個数を入力してください: '))
        result = selected_menu.get_total(count)
        print('注文内容は、\n選択された商品：' + selected_menu.name + '\n' + '個数：' + str(count) + '\n' + '合計金額：' + str(result) + '円\nです。')

        # 課題６
        print('***************************************')
        amount = int(input('お預かり金額を入力してください: '))
        change = amount - result
        print('お預かり金額は' + str(amount) + '円です。\nお釣りは、' + str(change) + '円です。')

        # 課題７
        now = datetime.now()
        # now_str = now.strftime('%Y/%m/%d %H:%M:%S')
        with open('{}.txt'.format(now),'w') as f:
            f.write('注文内容\n商品：' + selected_menu.name + '\n' + '個数：' + str(count) + '\n' + '合計金額：' + str(result) + '円\nお預かり金額：' + str(amount) + '円\nお釣り：' + str(change) + '円')
    except:
        print('入力内容が間違っています。最初からやり直してください。')


if __name__ == "__main__":
    system()