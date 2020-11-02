package DataStruct;

public class test1 {
    public static void main(String[] args) {
        int value[] = new int[10];
        for(int i=0;i<value.length;i++){
            value[i] = i;
        }
        delete(value,3);
        traverse(value);
        System.out.println();
    }
    public static int[] insert(int[] old,int value,int index){
        for(int k=old.length-1;k>index;k--){
            old[k] = old[k-1];
        }
        old[index] = value;
        return old;
    }
    public static void traverse(int [] data){
        for(int j=0;j<data.length;j++){
            System.out.print(data[j]+" ");
        }
    }
    public static int[] delete(int[] old,int index){
        for(int h = index;h<old.length - 1; h++) {
            old[h] = old[h + 1];
        }
        old[old.length - 1] = 0;
        return old;
    }
}
