package linkedlist

import "fmt"

type node struct {
	Val	interface{}
	Next	*node
}

type SinglyLinkedList struct {
	length	int
	Head	*node
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
	n.Next = ll.Head
	ll.Head = n
	ll.length++
}

func (ll *SinglyLinkedList) AddAtEnd(val interface{}) {
	n := NewNode(val)
	if ll.Head == nil {
		ll.Head = n
		ll.length++
		return
	}
	cur := ll.Head
	for ; cur.Next != nil; cur = cur.Next {
	}
	cur.Next = n
	ll.length++
}

func (ll *SinglyLinkedList) DelAtBeg() interface{} {
	if ll.Head == nil {
		return -1
	}
	cur := ll.Head
	ll.Head = cur.Next
	ll.length--
	return cur.Val
}

func (ll *SinglyLinkedList) DelAtEnd() interface{} {
	if ll.Head == nil {
		return -1
	} else if ll.Head.Next = nil {
		return DelAtBeg()
	}
	cur := ll.Head
	for ; cur.next.Next != nil; cur = cur.Next {
	}
	val := cur.Next.Val
	cur.Next = nil
	ll.length--
	return val
}

func (ll *SinglyLinkedList) Reverse() {
	var prev, next *node
	cur = ll.Head
	for cur != nil {
		next = cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}
	ll.Head = prev
}

func (ll *SinglyLinkedList) Display() {
	for cur := ll.Head; cur != nil; cur = cur.Next {
		fmt.Print(cur.Val, " ")
	}
	fmt.Print("\n")
}
