package linkedlist

import "fmt"

type node struct {
	Val	int
	Next	*node
	Prev	*node
}

type DoublyLinkedList struct {
	length	int
	Head	*node
}

func NewNode(val int) *node {
	return &node{val, nil, nil}
}

func CreateList() *DoublyLinkedList {
	return &DoublyLinkedList{}
}

func (ll *DoublyLinkedList) Count() int {
	return ll.length
}

func (ll *DoublyLinkedList) AddAtBeg(val int) {
	n := NewNode(val)
	n.Next = ll.Head
	ll.Head.Prev = n
	ll.Head = n
	ll.length++
}

func (ll *DoublyLinkedList) AddAtEnd(val int) {
	n := NewNode(val)
	if ll.Head == nil {
		ll.Head = n
		ll.length++
		return
	}
	cur := ll.Head
	for ; cur.Next != nil ; cur = cur.Next {
	}
	cur.Next = n
	n.Prev = cur
	ll.length++
}

func (ll *DoublyLinkedList) DelAtBeg() int {
	if ll.Head == nil {
		return nil
	}
	cur := ll.Head
	ll.Head = cur.Next
	if ll.Head != null {
		ll.Head.Prev = nil
	}
	ll.length--
	return cur.Val
}

func (ll *DoublyLinkedList) DelAtEnd() int {
	if ll.Head == nil {
		return nil
	}
	if ll.Head.Next == nil {
		ll.length--
		return ll.DelAtBeg()
	}
	cur := ll.Head
	for ; cur.Next.Next != nil; cur = cur.Next {
	}
	val := cur.Next.Val
	cur.Next = nil
	ll.length--
	return val
}

func (ll *DoublyLinkedList) Reverse() {
	var prev, next *node
	cur := ll.Head
	for cur != nil {
		next = cur.Next
		cur.Next = prev
		cur.Prev = next
		prev = cur
		cur = next
	}
	ll.Head = prev
}

func (ll *DoublyLinkedList) Display() {
	for cur := ll.Head; cur != nil; cur = cur.Next {
		fmt.Print(cur.Val, " ")
	}
	fmt.Print("\n")
}
