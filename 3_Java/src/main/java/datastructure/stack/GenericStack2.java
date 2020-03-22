package datastructure.stack;

import java.util.*;

/**
 * Generic stack data structure implemented using LinkedList
 * @param <T>
 */
public class GenericStack2<T> implements Iterable<T>{

    LinkedList<T> list = new LinkedList<>();

    /**
     * Creates an empty stack
     */
    public GenericStack2(){}

    /**
     * Creates an stack with initial element
     * @param firstElement : first element on the stack
     */
    public GenericStack2(T firstElement) {
        push(firstElement);
    }

    /**
     * Returns the number of elements in stack
     * @return : size of the stack
     */
    public int size() {
        return list.size();
    }

    /**
     * Checks if stack is empty
     * @return : true if stack is empty
     */
    public boolean isEmpty() {
        return size() == 0;
    }

    /**
     * Push an element on the stack
     * @param element : element to be pushed on stack
     */
    public void push(T element) {
        list.addLast(element);
    }

    /**
     * Pop an element off the stack
     * Throws exception if stack is empty
     * @return : Last element from the stack
     */
    public T pop(){
        if(isEmpty())
            throw new EmptyStackException();
        return list.removeLast();
    }

    /**
     * Peek the top of the stack without removing the element
     * Throws exception if stack is empty
     * @return : Last element of the stack
     */
    public T peek() {
        if(isEmpty())
            throw new EmptyStackException();
        return list.peekLast();
    }

    /**
     * Allows user to iterate through the stack using an iterator
     * @return : Iterator
     */
    @Override
    public Iterator<T> iterator() {
        return list.iterator();
    }
}
