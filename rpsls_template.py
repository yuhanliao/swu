#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��ΜU��
���ڣ�2020/4/12
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    global result
    if name=="ʯͷ":
        result=0
    elif name=="ʷ����":
        result=1
    elif name=="ֽ":
        result=2
    elif name=="����":
        result=3
    else:
        result=4
    result=int(result)
    return result
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��





def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    global result2
    if number==0:
        result2="ʯͷ"
    elif number==1:
        result2="ʷ����"
    elif number==2:
        result2="ֽ"
    elif number==3:
        result2="����"
    elif number==4:
        result2="����"
    else:
        result2="Error: No Correct Name"
    return result2
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��




def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print("----------------")
    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    player_choice=input()
    if player_choice in "ʯͷ""����""����""ֽ""ʷ����":
    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
        player_choice_number=name_to_number(player_choice)

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
        comp_number=random.randint(0,4)
    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
        comp_choice=number_to_name(comp_number)
    # ����Ļ����ʾ�����ѡ����������
        print("�����ѡ����������Ϊ��"+comp_choice)
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
        difference=(comp_number-player_choice_number)%5
    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
        if difference==0:
            print("���ͼ��������һ����")
        elif difference==1 or difference==2:
            print("�����Ӯ��")
        else:
            print("��Ӯ��")
    else:
        print("Error: No Correct Name")



# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
