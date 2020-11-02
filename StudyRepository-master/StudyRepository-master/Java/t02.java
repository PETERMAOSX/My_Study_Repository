public class t02{
    public static void main(String [] args){
        link link_ = new link();
        link_.add(1);
        link_.add(2);
        link_.add(5);
        link_.add(8);
        link_.show();
        
    }

}

class node {
    private int data;
    private node next;

    public void setData(int data) {
        this.data = data;
    }

    public int getData() {
        return this.data;
    }

    public void setNext(node next) {
        this.next = next;
    }

    public node getNext() {
        return this.next;
    }

}

class link {
    private node head;
    private node p;
    private node q;

    public void add(int data) {
        p = new node();
        p.setData(data);
        p.setNext(null);
        if(this.head == null){
            head = p;
        }
        else{
            this.q.setNext(p);

        }
        this.q = this.p;
    }
    public void show(){
        node current = new node();
        current = head;
        while(current!=null){
            System.out.println(current.getData());
            current = current.getNext();
        }
    }
}