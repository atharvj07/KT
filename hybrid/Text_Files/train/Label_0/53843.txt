import java.util.*;
import java.io.*;
import java.math.*;

public class D {
    public static Scanner scan = new Scanner(System.in);
    public static boolean bg = true;

    public static void main(String[] args) throws Exception {
        int n1 = Integer.parseInt(scan.next());
        
        int[] data = new int[n1];
        
        TreeSet<Integer> t1 = new TreeSet();
        
        for (int i=0;i<n1;i++){
            int k1 = Integer.parseInt(scan.next());
            data[i]=k1;
            t1.add(i);
        }
        ArrayList<Integer> inv = new ArrayList<>();
        
        for (int i=0;i<data.length-1;i++){
            if (data[i]>data[i+1]) inv.add(i);
        }
        int count = 0;
        for (;;){
            ArrayList<Integer> nextinv = new ArrayList<>();
            HashSet<Integer> del2 = new HashSet<>();
            for (int e: inv){
                
                if (del2.contains(e)) continue;
                int ptr = e;
                for (;;){
                    if (t1.higher(ptr)==null) break;
                    int next = t1.higher(ptr);
                    if (data[ptr]>data[next]){
                        del2.add(ptr);
                    }
                    else {
                        if (data[e]>data[next]){
                            nextinv.add(e);
                        }
                        break;
                    }
                    ptr= next;
                }
            }
            inv = nextinv;
            
            if (del2.size()==0) break;
            for (int e: del2){
                t1.remove(t1.higher(e));
            }
            count++;
        }
        System.out.println(count);
    }
}

