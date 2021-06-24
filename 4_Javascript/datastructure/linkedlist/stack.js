class Stack {
    
    constructor() {
        this.stack = []
        this.top = -1
    }

    push(value) {
        this.top++;
        this.stack.push(value)
    }

    pop() {
        if(this.isEmpty())
            throw new Error('Stack underflow')
        return this.stack[this.top--]
    }

    isEmpty(){
        return this.top === -1
    }
}
