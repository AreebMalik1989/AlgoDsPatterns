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

    /**
     * Add new node at the beginning
     * @param {*} data - Value of node to be added
     */
    push(data) {
        
        // 1. Allocate the node
        // 2. Put in the data
        let newNode = new LinkedListNode(data);

        // 3. Make next of new node as head
        newNode.next = this.head;

        // 4. Move the head to point to new node
        this.head = newNode;

    }

    /**
     * Inserts a new node after the given prev_node
     * @param {LinkedListNode} previousNode - Previous node
     * @param {*} data - Value of new node to be added
     */
    insertAfter(previousNode, data) {

        // 1. Check if the given prev_node exists
        if(previousNode === null) return;

        // 2. Create new node
        // 3. Put in the data
        let newNode = new LinkedListNode(data);

        // 4. Make next of new_node as next of prev_node
        newNode.next = previousNode.next;

        // 5. Make next of prev_node as new_node
        previousNode.next = newNode;
    }

    /**
     * Appends a new node at the end
     * @param {*} data - Value of new node to be appended
     */
    append(data) {

        // 1. Create a new node
        // 2. Put in that data
        let newNode = new LinkedListNode(data);

        // 3. If the linked list is empty, then make the new node as head
        if(this.head === null) {
            this.head = newNode;
            return;
        }

        // 4. Else traverse till the last node
        let last = this.head;
        while(last.next !== null) {
            last = last.next;
        }

        // 5. Change the next of last node
        last.next = newNode;
    }

    /**
     * Search for the first element with data matching 'item'.
     * Takes O(n) time
     * @param {*} data - Value of node to be searched in linked list
     * @returns {LinkedListNode} First element with data matching 'item' or 'None' if not found.
     */
    find(data) {

        let curr = this.head;

        while(curr !== null && curr.data !== data) {
            curr = curr.next;
        }

        return curr;  // Will be None if not found
    }

    /**
     * Remove the first occurrence of item in the list.
     * Takes O(n) time
     * @param {*} data - Value of item to be deleted
     */
    deleteNode(data) {

        // Find the element and keep the reference to the element preceding it
        let curr = this.head;
        let prev = null;
        while(curr !== null && curr.data !== data) {
            prev = curr;
            curr = curr.next;
        }

        // Unlink from the list
        // If head node itself holds the item to be deleted
        if(prev === null) {
            this.head = curr.next;
        } else if (curr !== null) {
            prev.next = curr.next;
            curr.next = null;
        }
    }

    /**
     * Delete the node at the given position
     * @param {Number} position - Index of the node
     */
    deleteNodeAtPosition(position) {
        
        // If linked list is empty
        if(this.head === null || position < 0) return;

        // Store head node
        let curr = this.head;

        // If head need to be removed
        if(position === 0) {
            this.head = curr.next;
            curr = null;
            return;
        }

        // Find previous node of the node to be deleted
        for(let i=0; i<position-1; i++) {
            curr = curr.next;
            if(curr === null) break;
        }

        // If position is more than number of nodes
        if(curr === null) return;
        if(curr.next === null) return;

        // Node curr.next is to be deleted
        // Store pointer to the next of node to be deleted
        curr.next = curr.next.next;

        // Unlink the node from the linked list
        curr.next = null;
        curr.next = next;
    }

    /**
     * Reverse the list in-place
     * Takes O(n) time
     */
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

    /**
     * Counts number of nodes in linked list
     * @returns {Number} Number of nodes in linked list
     */
    getCount() {

        let curr = this.head;
        let count = 0;

        while(curr !== null) {
            count++;
            curr = curr.next;
        }

        return count;
    }

    /**
     * Detects loop in linked list
     * @returns {Boolean} true if there is a loop in linked list
     */
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

    /**
     * Prints the linked list
     */
    printList() {
        let curr = this.head;
        while(curr !== null) {
            console.log(curr.data);
            curr = curr.next;
        }
    }
}
