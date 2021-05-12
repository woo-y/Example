import random
import time


print("컴퓨터가 자신의 숫자를 정하는 중입니다...")
time.sleep(0.5)
print("컴퓨터가 자신의 숫자를 결정했습니다.")
num_count = 0
a = int(random.uniform(0,101))
input_num = int(input("0부터 100 사이의 하나의 숫자를 정하고, 정한 숫자를 알려주세요 = \n"))
end = 0

while True :
    if end >= 1:
        break
    if 0<= input_num < 101:
        while True:
            if input_num > a:
                    print("당신이 입력한 숫자는 컴퓨터의 숫자보다 큽니다.")
                    num_count += 1
                    input_num = int(input("새로운 숫자를 입력해주세요. (현재 카운트는 {} 입니다.)".format(num_count)))
                    break
            elif input_num < a:
                    print("당신이 입력한 숫자는 컴퓨터의 숫자보다 작습니다.")
                    num_count += 1
                    input_num = int(input("새로운 숫자를 입력해주세요. (현재 카운트는 {} 입니다.)".format(num_count)))
                    break
            else:
                num_count +=1
                print("정답을 맞추셨습니다! 정답은 {}입니다. 카운트 = {}".format(a,num_count))
                end = 1
                break            
    else :
        input_num = int(input("잘못 되었습니다. 다시 숫자를 입력해주세요! "))


