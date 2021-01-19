# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 랜덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number가 정수로 변환 가능할 경우는 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_digit("551")
    #   True
    #   >>> bg.is_digit("103943")
    #   True
    #   >>> bg.is_digit("472")
    #   True
    #   >>> bg.is_digit("1032.203")
    #   False
    #   >>> bg.is_digit("abc")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    for num in user_input_number:
        if "0" > num or num > "9":
            return False

    return True


def is_between_100_and_999(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    #                         입력된 값은 숫자형태의 문자열 값임이 보장된다.
    # Output:
    #   - user_input_number가 정수로 변환하여 100이상 1000미만일 경우 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_between_100_and_999("551")
    #   True
    #   >>> bg.is_between_100_and_999("103943")
    #   False
    #   >>> bg.is_between_100_and_999("472")
    #   True
    #   >>> bg.is_between_100_and_999("0")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    # is_digit이 true일 때만 실행
    number = int(user_input_number)
    if 100 <= number and number < 1000:
        return True

    return False


def is_duplicated_number(three_digit):
    # '''
    # Input:
    #   - three_digit : 문자열로 된 세자리 양의 정수 값
    #                   문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    # Output:
    #   - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
    #     그렇지 않을 경우는 False
    #   ex) 117 - True, 123 - False, 103 - False, 113 - True
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_duplicated_number("551")
    #   True
    #   >>> bg.is_duplicated_number("402")
    #   False
    #   >>> bg.is_duplicated_number("472")
    #   False
    #   >>> bg.is_duplicated_number("100")
    #   True
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    for num in three_digit:
        if three_digit.count(num) > 1:
            return True

    return False


def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False를 반환
    #        1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_validated_number("amvd")
    #   False
    #   >>> bg.is_validated_number("402")
    #   True
    #   >>> bg.is_validated_number("472")
    #   True
    #   >>> bg.is_validated_number("100")
    #   False
    #   >>> bg.is_validated_number("1000")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    # is_digit이 True, is_between_100_and_999이 True, is_duplicated_number이 False일 때 True
    if (
        is_digit(user_input_number)
        and is_between_100_and_999(user_input_number)
        and not is_duplicated_number(user_input_number)
    ):
        return True

    return False


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : 입력값이 없음
    # Output:
    #   - 중복되는 숫자가 없는 3자리 정수값을 램덤하게 생성하여 반환함
    #     정수값으로 문자열이 아님
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   125
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   634
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   583
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   381
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # get_random_number() 함수를 사용하여 random number 생성

    result = 0
    while True:
        rand_three_digit_number = get_random_number()
        is_duplicated = is_duplicated_number(str(rand_three_digit_number))

        if not is_duplicated:
            result = rand_three_digit_number
            break

    return result


def get_strikes_or_ball(user_input_number, random_number):
    # '''
    # Input:
    #   - user_input_number : 문자열값으로 사용자가 입력하는 세자리 정수
    #   - random_number : 문자열값으로 컴퓨터가 자동으로 생성된 숫자
    # Output:
    #   - [strikes, ball] : 규칙에 따라 정수형 값인 strikes와 ball이 반환됨
    #   변환 규칙은 아래와 같음
    #   - 사용자가 입력한 숫자와 컴퓨터가 생성한 숫자의
    #     한 숫자와 자릿수가 모두 일치하면 1 Strike
    #   - 자릿수는 다르나 입력한 한 숫자가 존재하면 1 Ball
    #   - 세자리 숫자를 정확히 입력하면 3 Strike
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_strikes_or_ball("123", "472")
    #   [0, 1]
    #   >>> bg.get_strikes_or_ball("547", "472")
    #   [0, 2]
    #   >>> bg.get_strikes_or_ball("247", "472")
    #   [0, 3]
    #   >>> bg.get_strikes_or_ball("742", "472")
    #   [1, 2]
    #   >>> bg.get_strikes_or_ball("472", "472")
    #   [3, 0]
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    result = [0, 0]  # [strike count, ball count]
    for i in range(3):
        for j in range(3):
            if user_input_number[i] == random_number[j]:
                if i == j:
                    result[0] += 1 # strike 추가
                else:
                    result[1] += 1 # ball 추가

    return result

def is_zero(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열값으로 사용자가 입력하는 세자리 정수
    # Output:
    #   - 0이면 True, 아니면 False 반환
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_zero("123")
    #   False
    #   >>> bg.is_zero("0")
    #   True
    #   >>> bg.is_zero("47392")
    #   False
    # '''
    if user_input_number == "0":
        return True

    return False

def is_win(strikes):
    # '''
    # Input:
    #   - strikes : 현재 strikes값
    # Output:
    #   - 3이면 True, 아니면 False 반환
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_win(3)
    #   True
    #   >>> bg.is_win(0)
    #   True
    #   >>> bg.is_win(1)
    #   False
    # '''
    if strikes == 3:
        return True

    return False

def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_yes("Y")
    # True
    # >>> bg.is_yes("y")
    # True
    # >>> bg.is_yes("Yes")
    # True
    # >>> bg.is_yes("YES")
    # True
    # >>> bg.is_yes("abc")
    # False
    # >>> bg.is_yes("213")
    # False
    # >>> bg.is_yes("4562")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    if one_more_input.lower() == "y" or one_more_input.lower() == "yes":
        return True

    return False


def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_no("Y")
    # False
    # >>> bg.is_no("b")
    # False
    # >>> bg.is_no("n")
    # True
    # >>> bg.is_no("NO")
    # True
    # >>> bg.is_no("nO")
    # True
    # >>> bg.is_no("1234")
    # False
    # >>> bg.is_no("yes")
    # False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    if one_more_input.lower() == "n" or one_more_input.lower() == "no":
        return True

    return False


def main():
    print("Play Baseball")
    
    is_terminated = False
    while True:
        random_number = str(get_not_duplicated_three_digit_number())
        print("Random Number is : ", random_number)
        
        while True: # 유저 숫자 입력
            user_input = 999
            user_input = input("Input guess number : ")

            if is_zero(user_input):
                is_terminated = True # 게임을 종료하기 위함.
                break 
            
            if not is_validated_number(user_input):
                print("Wrong Input, Input again")
            else:
                strikes, balls = get_strikes_or_ball(user_input, random_number)
                
                print(f"Strikes : {strikes} , Balls : {balls}")

                if is_win(strikes):
                    # 이김. 종료
                    break
        
        if is_terminated:
            break

        while True: # 한 번 더? 입력
            one_more_input = input("You win, one more(Y/N) ?")
            if is_yes(one_more_input):
                break
            elif is_no(one_more_input):
                is_terminated = True # 게임을 종료하기 위함.
                break
            else:
                print("Wrong Input, Input again")

        if is_terminated:
            break

        # ===Modify codes below=============
        # 위의 코드를 포함하여 자유로운 수정이 가능함

        # 사용자 숫자 입력 값이 0이면 "Thank you for using this program" 출력 후 break해서 프로그램 종료(이걸 먼저 처리하기)
        # 사용자 숫자 입력 후 is_validated_number가 false이면 "Wrong Input, Input again" 출력 후 다시 입력
        # is_no, is_yes 모두 false이면 "Wrong Input, Input again" 출력 후 다시 입력

    # ==================================
    print("Thank you for using this program")
    print("End of the Game")


if __name__ == "__main__":
    main()