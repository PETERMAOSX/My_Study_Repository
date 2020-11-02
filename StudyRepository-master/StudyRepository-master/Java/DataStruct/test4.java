package DataStruct;

import java.util.LinkedList;

class Stack<T>{
    static class Node<T>{
        T data;
        Node<T> next;
        Node(T data,Node<T> next){
            this.data = data;
            this.next = next;
        }
        Node(T data){
            this(data,null);
        }
    }
    @SuppressWarnings("rawtypes")
    static LinkedList list = new LinkedList<>();
    @SuppressWarnings("unchecked")
    public T push(T item){
        list.addFirst(item);
        return item;
    }
    public void pop(){
        list.removeFirst();
    }
    public boolean isEmpty(){
        return list.isEmpty();
    }
    public int search(T t){
        return list.indexOf(t);
    }
    public static void main(String[] args) {
        Stack<String> stack = new Stack<String>();
        System.out.println(stack.isEmpty());
        stack.push("abc");
        stack.push("def");
        stack.push("egg");
        stack.pop();
        System.out.println(stack.search("def"));
        System.out.println(stack.search("egg"));
    }

}