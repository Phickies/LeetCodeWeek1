import sltions
import prblms

if __name__ == '__main__':

    n1 = prblms.User().strInput()
    n2 = prblms.User().strInput()

    linked_list_1 = prblms.LinkedList(intMode=True)
    linked_list_2 = prblms.LinkedList(intMode=True)

    sltions.Sltions().splitToLinkedList(linked_list_1,n1)
    sltions.Sltions().splitToLinkedList(linked_list_2,n2)

    linked_list_1.printLL()
    linked_list_2.printLL()

    print(" ")

    sltions.Sltions().addTwoNumber(linked_list_1, linked_list_2).printLL()