
import java.util.*;

public class cf242b {

    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        
        pair[] a = new pair[n];
        
        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        
        for (int i = 0; i < n; i++) {
            
            int x = in.nextInt();
            int y = in.nextInt();
            
            a[i] = new pair(x, y);
            
            max = Math.max(y, max);
            min = Math.min(x, min);
            
        }
        
        int i = 1;
        
        for (pair object : a) {
            
            if (object.x == min && object.y == max) {
                System.out.println(i);
                return;
            }
            i++;
            
        }
        System.out.println(-1);
        
    }
    
    static class pair {
        int x; 
        int y;

        public pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
    }

}
