# 재고 현황 표시
class Product:
    count = 0

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        Product.count += 1
        self.number = Product.count
        
pd1 = Product("무선 이어폰", 89000, 3)
pd2 = Product("텀블러", 15000, 10)
pd3 = Product("보조배터리", 32000, 5)
pd4 = Product("마우스패드", 9000, 0)
pd5 = Product("USB 허브", 18000, 4)

class Cart:

    def __init__(self):
        self.grap = []
    def cart_in (self, select_pd, quantity):
        
        if quantity <= 0: 
            print("1개 이상의 상품만 담으실 수 있습니다.")
            return False

        if quantity > select_pd.stock:
            print("재고보다 많은 수량의 상품을 담으실 수 없습니다.")
            return False
        

        for grap in self.grap:
            if select_pd in grap :
                if grap[select_pd] + quantity > select_pd.stock:
                    print("재고보다 많은 수량의 상품을 담으실 수 없습니다.")
                    return False
                grap[select_pd] += quantity
                return True

        self.grap.append({select_pd:quantity})
        return True    
                


        




product = [pd1, pd2, pd3, pd4, pd5]

# 번호 선택
while True:
    # 실행 화면 타이틀
    print("-"*77)
    print("1. 상품목록 | 2. 담기 | 3. 빼기 | 4. 장바구니 | 5. 쿠폰 | 6. 결제 | q. 종료")
    print("-"*77)

    user_num = input("원하시는 항목의 번호를 입력해주세요.:")
    if user_num == "q" or user_num == "Q":
        print("종료되었습니다.")
        break

    if not user_num.isdecimal():
        print("선택 항목에 있는 번호만 입력해주세요.")
        continue

    user_num = int(user_num)

    if user_num > 6 or user_num <= 0:
        print("선택 항목에 있는 번호만 입력해주세요.")
        continue

    