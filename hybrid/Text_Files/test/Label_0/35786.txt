import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        List<Data> d = new ArrayList<Data>();
        int n = sc.nextInt();
        for(int i = 0 ; i < n ; i++){
            long x = sc.nextLong();
            long y = sc.nextLong();
            d.add(new Data(x,y));
        }
        Collections.sort(d);
        Iterator<Data> it = d.iterator();
        while(it.hasNext()){
            Data a = it.next();
            a.print();
        }
    }
}
class Data implements Comparable<Data>{
    long x;
    long y;
    Data(long x, long y){
        this.x = x;
        this.y = y;
    }
    public int compareTo(Data d){
        if(x < d.x)
            return -1;
        else if(x == d.x){
            if(y < d.y)
                return -1;
            else
                return 1;
        }
        else
            return 1;
    }
    public void print(){
        System.out.println(x + " " + y);
    }
}
