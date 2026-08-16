import java.util.*;
 
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        int[] a = new int[n];
        for(int i=0; i<n; i++) {
            a[i] = Integer.parseInt(sc.next());
        }
        
        Arrays.sort(a);
        boolean[] boo = new boolean[a[n-1]+1];
        for(int i=0; i<a[n-1]+1; i++) {
            boo[i] = true;
        }
        
        int count = 0;
        for(int i=0; i<n; i++) {
            if(i>0) {
                if(a[i] == a[i-1] && boo[a[i]]) {
                    boo[a[i]] = false;
                    count--;
                    continue;
                }
            }
            if(boo[a[i]] == true) {
                int x = 2;
                while(a[i]*x <= a[n-1]) {
                    boo[a[i]*x] = false;
                    x++;
                }
                count++;
            } 
        }
        System.out.println(count);
    }
}