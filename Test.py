# 질문이 길게 많은데 무엇을 어떻게 해결했는지 답글로 담는 것도 좋은 것 같음
from tkinter import Tk, Entry, Button
from tkinter import *            # tkinter 라이브러리에 모든 함수를 사용하겠다.
root = Tk()                      # root라는 창을 생성
root.geometry("400x400")       # 창 크기설정
root.title("학교 양식을 선택하십시오")    # 창 제목설정
root.option_add("*Font", "맑은고딕 15")  # 폰트설정
root.resizable(False, False)  # x, y 창 크기 변경 불가


# entry_widgets가 있는데 왜 한 번 더 함수로 작업하는거야?
# 이게 왜 필요하냐면. 설계를 버튼을 눌렀을 때 앤트리에 적혀진 값을 저장하는 형태
# 즉, 버튼을 눌렀을 때 저장하는 형태이기에 이에 맞는 command가 있어야 저장할 수 있는거지
# 작성은 언제든 가능하지만 저장은 버튼/command가 실행되었을 때만 저장되니까


def get_entry_value(entry_list):

    for entry in entry_list:
        value = entry.get()
        print("앤트리 값 : " + value)
    # value = entry_widget.get()
    # print("앤트리 값 : " + value)


def btn2press():                   # 함수 btn2press() 정의   / widget 부품
    root.destroy()
    if Radio_value.get() == 1:         # 각 양식 별 입력 데이터를 제시
        root2 = Tk()
        root2.title("대학교 양식 입력창")
        root2.geometry('400x300')

        Total_lebel = Label(root2, text='총인원 ')
        Total_Entry = Entry(root2)
        Total_lebel.grid(row=0, column=0, padx=10, pady=10)
        Total_Entry.grid(row=0, column=1, padx=10, pady=10)

        xlcel_lebel = Label(root2, text='엑셀 파일주소 ')
        xlcel_Entry = Entry(root2)
        xlcel_lebel.grid(row=1, column=0, padx=10, pady=10)
        xlcel_Entry.grid(row=1, column=1, padx=10, pady=10)
        # entry_widgets.append(Total_Entry) # !!!!!!
        # 전혀 값이 저장되고 있지 않음. 상식적으로 생각해도
        # 버튼을 눌러서 command가 동작할 때 값이 전달되는 형태로 설계한건데
        # 그게 아니라는 거지. 지금은 빈 앤트리를 widget에 넣으려는 형태
        # 고로 command함수에서 앤트리.get으로 값을 가져와 저장해야하는데
        # 앤트리.get이 메인-함수에서는 잘 되는데, 함수-함수 형태라서 안되는 것 같음
        # 현재 코드 구성상 함수-함수에서 벗어나긴 힘듦

        entry_widgets = []  # ******************************************************************************************************************************
        entry_widgets.append(Total_Entry)
        entry_widgets.append(xlcel_Entry)
        # 두 번째 상세 데이터 제출 버튼
        ButtonCollege = Button(root2, text="제출", width=10, command=lambda: (
            get_entry_value(entry_widgets), root2.destroy()))  # lamda를 사용하면 두 개의 command를 사용할 수 있는걸 알게되었다. 왜인진 아직 모르겠다
        ButtonCollege.grid(row=2, column=1)

    if Radio_value1.get() == 1:
        root3 = Tk()
        root3.title("중/고등학교 양식 입력창")
        root3.geometry('400x300')

        Freshman_lebel = Label(root3, text='1학년 ')  # 라벨 이름
        Sophomore_lebel = Label(root3, text='2학년 ')
        Junior_lebel = Label(root3, text='3학년 ')
        Freshman_Entry = Entry(root3)     # 라벨 옆 입력칸
        Sophomore_Entry = Entry(root3)
        Junior_Entry = Entry(root3)

        Freshman_lebel.grid(row=1, column=0)
        Freshman_Entry.grid(row=1, column=2)
        Sophomore_lebel.grid(row=2, column=0)
        Sophomore_Entry.grid(row=2, column=2)
        Junior_lebel.grid(row=3, column=0)
        Junior_Entry.grid(row=3, column=2)

        print("1학년 : " + Freshman_Entry.get())

    # 다른건 알겠는데 get_entry_value에서 entry_widget으로 Entry를 받는데, 중/고등학교는 입력 엔트리가 여러개이다. 이걸 어쩌면 좋을까?
    # 엔트리들을 리스트에 저장해서 리스트로 활용하면 됨.....


Radio_value = IntVar()                             # chkvar에 int 형으로 값을 저장
RadioBox = Radiobutton(
    root, text="대학교", variable=Radio_value, value=1)   # root라는 창에 체크박스 생성
RadioBox.pack()                                 # 체크박스 배치

Radio_value1 = IntVar()                            # Radio_value1에 int 형으로 값을 저장
RadioBox1 = Radiobutton(root, text="중/고등학교",
                        variable=Radio_value1, value=2)  # root라는 창에 체크박스 생성
RadioBox1.pack()                                # 체크박스 배치


btn2 = Button(root)                # root라는 창에 버튼 생성
btn2.config(text="선택")          # 버튼 내용
btn2.config(width=10)              # 버튼 크기
btn2.config(command=btn2press)      # 버튼 기능 (btn2pree() 함수 호출)
btn2.pack()                        # 버튼 배치

# lb = Label(root)                 # root라는 창에 레이블 생성
# lb.pack()                        # 레이블 배치

root.mainloop()                  # 창 실행


# 문제점
# 1번 root 양식선택까지는 ok
# 2번 여러 앤트리의 값을 다루는 것, 제출 버튼 함수. 이 두 가지 기능이 모두 오류


# def calculate():
#     # 앤트리에서 데이터 가져오기
#     user_input = entry.get()
#     # 데이터 처리 또는 계산
#     result = int(user_input) * 2
#     # 처리 결과 출력
#     print("계산 결과:", result)
#     root.destroy()


# # 메인 윈도우 생성
# root = Tk()
# root.title("앤트리로 데이터 입력받기")

# # 앤트리 위젯 생성
# entry = Entry(root)
# entry.pack()

# # 버튼 생성 및 클릭 시 데이터 계산
# button = Button(root, text="계산", command=calculate)
# button.pack()

# # Tkinter 이벤트 루프 실행
# root.mainloop()
