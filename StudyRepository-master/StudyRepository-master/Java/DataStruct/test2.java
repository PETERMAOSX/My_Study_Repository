package DataStruct;


public class test2<T> {
    private static class Node<T> {
        T data;
        Node<T> next;

        Node(T data, Node<T> next) {
            this.data = data;
            this.next = next;
        }

        Node(T data) {
            this(data, null);
        }

    }

    private Node<T> head, tail;

    public test2() {
        head = tail = null;
    }

    public boolean isEmpty() {
        return head == null;

    }

    public void addHead(T item) {
        head = new Node<T>(item);
        if (tail == null) {
            tail = head;
        }
    }

    public void addTail(T item) {
        if (!isEmpty()) {
            tail.next = new Node<T>(item);
            tail = tail.next;
        } else {
            head = tail = new Node<T>(item);
        }
    }

    public void traverse() {
        if (isEmpty()) {
            System.out.println("null");
        } else {
            for (Node<T> p = head; p != null; p = p.next) {
                System.out.println(p.data);
            }
        }
    }

    public void addFromHead(T item) {
        Node<T> newNode = new Node<T>(item);
        newNode.next = head;
        head = newNode;
    }

    public void addFromTail(T item) {
        Node<T> newNode = new Node<T>(item);
        Node<T> p = head;
        while(p.next != null){
            p = p.next;
        }
        p.next = newNode;
        newNode.next = null;
    }
    public void removeFromHead(){
        if(!isEmpty()){
            head = head.next;
        }
        else{
            System.out.println("The list have been emptied!");
        }
    }
    public void removeFromTail(){
        Node<T> prev = null;
        Node<T> curr = head;
        while(curr.next!=null){
            prev = curr;
            curr = curr.next;
            if(curr.next == null){
                prev.next = null;
            }
        }
    }
    public boolean insert(T appointedItem,T item){
        Node<T> prev = head,curr = head.next,newNode;
        newNode = new Node<T>(item);
        if(!isEmpty()){
            while((curr!=null) && (!appointedItem.equals(curr.data))){
                prev = curr;
                curr = curr.next;
            }
            newNode.next = curr;
            prev.next = newNode;
            return true;
        }
        return false;
    }
    public void remove(T item){
        Node<T> curr = head;
        Node<T> prev = null;
        boolean found = false;
        while(curr!= null && !found){
            if(item.equals(curr.data)){
                if(prev == null){
                    removeFromHead();
                }
                else{
                    prev.next = curr.next;
                }
                found = true;
            }else{
                prev = curr;
                curr = curr.next;
            }
        }
        
    }
    public int indexOf(T item){
        int index = 0;
        Node<T> p;
        for(p = head;p!=null;p=p.next){
            if(item.equals(p.data))
                return index;
            index++;
        }
        return -1;
    }
    public boolean contains(T item){
        return indexOf(item) != -1;
    }
}