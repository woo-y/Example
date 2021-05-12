import random
import time


print("컴퓨터가 자신의 숫자를 정하는 중입니다...")
time.sleep(0.5)
print("컴퓨터가 자신의 숫자를 결정했습니다.")
num_count = 0
a = int(random.randrange(0,20))
end = True
input_str = 0

while end :
    if input_str == 0 :
        input_str = str(input("주사위의 숫자는 {}입니다. 재시도 하시겠습니까? (현재 재시도 횟수는 {} 입니다.)\n".format(a,num_count)))
    
    elif input_str == "y" or input_str =="Y" :
        num_count += 1
        a = int(random.randrange(0,20))
        input_str = str(input("주사위의 숫자는 {}입니다. 재시도 하시겠습니까? (현재 재시도 횟수는 {} 입니다.)\n".format(a,num_count)))

    elif input_str == "n":
        print("당신의 주사위는 {} 입니다.".format(a))
        end = False
        break

    else : 
        print("입력 실수")
        end = False
        break

    
    #         ##input_num < a:
    #         print("당신이 입력한 숫자는 컴퓨터의 숫자보다 작습니다.")
    #         num_count += 1
    #         input_num = int(input("새로운 숫자를 입력해주세요. (현재 카운트는 {} 입니다.)".format(num_count)))
    #         break##
    # else:
    #     num_count +=1
    #     print("정답을 맞추셨습니다! 정답은 {}입니다. 카운트 = {}".format(a,num_count))
    #     end = 1
    #     break            
    # else :
    #     input_num = int(input("잘못 되었습니다. 다시 숫자를 입력해주세요! "))


