class LinkedListNode {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    
    constructor() {
        this.head = null;
    }

    push(data) {
        
        let newNode = new LinkedListNode(data);

        newNode.next = this.head;

        this.head = newNode;

    }

    insertAfter(previousNode, data) {

        if(previousNode === null) {
            return;
        }

        let newNode = new LinkedListNode(data);

        newNode.next = previousNode.next;

        previousNode.next = newNode;
    }

    append(data) {

        let newNode = new LinkedListNode(data);

        if(this.head === null) {
            this.head = newNode;
            return;
        }

        let last = this.head;
        while(last.next !== null) {
            last = last.next;
        }

        last.next = newNode;
    }

    find(data) {

        let curr = this.head;

        while(curr !== null && curr.data !== data) {
            curr = curr.next;
        }

        return curr;
    }

    deleteNode(data) {

        let curr = this.head;
        let prev = null;
        while(curr !== null && curr.data !== data) {
            prev = curr;
            curr = curr.next;
        }

        if(prev === null) {
            this.head = curr.next;
        } else if (curr !== null) {
            prev.next = curr.next;
            curr.next = null;
        }
    }

    deleteNodeAtPosition(position) {
        
        if(this.head === null || position < 0) {
            return;
        }

        let curr = this.head;

        if(position === 0) {
            this.head = curr.next;
            curr = null;
            return;
        }

        for(let i=0; i<position-1; i++) {
            curr = curr.next;
            if(curr === null) {
                break;
            }
        }

        if(curr === null) {
            return;
        }

        if(curr.next === null) {
            return;
        }

        curr.next = curr.next.next;

        curr.next = null;
        curr.next = next;
    }

    reverse() {

        let curr = this.head;
        let prevNode = null;
        let nextNode = null;

        while(curr !== null) {
            nextNode = curr.next;
            curr.next = prevNode;
            prevNode = curr;
            curr = nextNode;
        }
        this.head = prevNode;
    }

    getCount() {

        let curr = this.head;
        let count = 0;

        while(curr !== null) {
            count++;
            curr = curr.next;
        }

        return count;
    }

    detectLoop() {

        let s = new Set();
        let curr = this.head;

        while(curr !== null) {
            
            if(s.has(curr)) {
                return true;
            }

            s.add(curr);
            curr = curr.next;
        }

        return false;
    }

    printList() {
        let curr = this.head;
        while(curr !== null) {
            console.log(curr.data);
            curr = curr.next;
        }
    }
}
