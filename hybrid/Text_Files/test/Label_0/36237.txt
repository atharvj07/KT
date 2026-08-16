import java.io.*;
import java.util.*;
import java.math.BigDecimal;
 
public class Main {
    public static long combination(int n, int r) {
        r = Math.min(r, n - r);
        if (r == 1) {
            return n;
        }
    
        long sum = 1;
        for (int i = 1; i <= r; i++) {
            sum = sum * (n - i + 1) / i;
        }
        return sum;
    }
    
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        ArrayList<Long> values = new ArrayList<Long>(n);
        
        for (int i = 0; i < n; i++) values.add(sc.nextLong());
        Collections.sort(values, Comparator.reverseOrder());
 
        //sum
        long ave = 0;
        for (int i = 0; i < a; i++){
            ave += values.get(i);
        } 
        System.out.println(BigDecimal.valueOf(ave / (double)a).toPlainString());
 
        //
        long border = values.get(a - 1);
        int num_border = values.lastIndexOf(border) - values.indexOf(border) + 1;
        
        long ans = 0;
        if (!values.get(0).equals(values.get(a - 1))){
            ans = combination(num_border, a - values.indexOf(border));
        }else{
            for (int i = a; i <= Math.min(b, num_border); i++){
                ans += combination(num_border, i);
            } 
        }
        System.out.println(ans);
    }
    
}