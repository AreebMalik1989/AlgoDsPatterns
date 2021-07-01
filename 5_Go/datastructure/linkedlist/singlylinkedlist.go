package singlylinkedlist

import "fmt"

type node struct {
	val	interface{}
	next	*node
}

type SinglyLinkedList struct {
	length	int
	head	*node
}

func CreateList() *SinglyLinkedList {
	return &SinglyLinkedList{}
}

func NewNode(val interface{}) *node {
	return &node{val, nil}
}

func (ll *SinglyLinkedList) Count() int {
	return ll.length
}

func (ll *SinglyLinkedList) AddAtBeg(val interface{}) {
	n := NewNode(val)
	n.next = ll.head
	ll.head = n
	ll.length++
}

func (ll *SinglyLinkedList) AddAtEnd(val interface{}) {
	n := NewNode(val)
	if ll.head == nil {
		ll.head = n
		ll.length++
		return
	}
	cur := ll.head
	for ; cur.next != nil; cur = cur.next {
	}
	cur.next = n
	ll.length++
}

func (ll *SinglyLinkedList) DelAtBeg() interface{} {
	if ll.head == nil {
		return -1
	}
	cur := ll.head
	ll.head = cur.next
	ll.length--
	return cur.val
}

func (ll *SinglyLinkedList) DelAtEnd() interface{} {
	if ll.head == nil {
		return -1
	} else if ll.head.next = nil {
		return DelAtBeg()
	}
	cur := ll.head
	for ; cur.next.next != nil; cur = cur.next {
	}
	val := cur.next.val
	cur.next = nil
	ll.length--
	return val
}

func (ll *SinglyLinkedList) Reverse() {
	var prev, next *node
	cur = ll.head
	for cur != nil {
		next = cur.next
		cur.next = prev
		prev = cur
		cur = next
	}
	ll.head = prev
}

func (ll *SinglyLinkedList) Display() {
	for cur := ll.head; cur != nil; cur = cur.next {
		fmt.Print(cur.val, " ")
	}
	fmt.Print("\n")
}
