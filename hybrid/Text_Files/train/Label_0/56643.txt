import java.util.Arrays;
import java.util.Scanner;


//http://codeforces.com/contest/360/problem/A
/*
 * PSEUDOCODE:
 * initialize a[i] to 10^9
 * initialize change[i] to 0
 *  
 *  for each command
 *  if increment(l, r, d)
 *      for i from l to r
 *          change[i] += d
 *  if max(l, r, m)
 *      for i from l to r
 *          if a[i] + change[i] > m
 *              a[i] = m - change[i];
 *  //suppose there actually exists a correct array a*[i]
 *  //then at this point, we've computed a[i] >= a*[i] for all i
 *  
 *  reset change[i] = 0
 *  do operations on recovered array to check...
 */
public class ArrayRecovery {
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int size = in.nextInt();
        int ops = in.nextInt();
        long[][] oparr = new long[ops][4];
        
        long[] a = new long[size];
        long[] change = new long[size];
        Arrays.fill(a, (long) Math.pow(10, 9));
        Arrays.fill(change, 0);
        
        for (int i = 0; i < ops; i++) {
            int op = in.nextInt();
            int l = in.nextInt() - 1;
            int r = in.nextInt() - 1;
            if (op == 1) { //increment
                long d = in.nextLong();
                oparr[i] = new long[] {op, l, r, d};
                for (int j = l; j <= r; j++) {
                    change[j] += d;
                }
            }
            else { //max
                long m = in.nextLong();
                oparr[i] = new long[] {op, l, r, m};
                for (int j = l; j <= r; j++) {
                    if (a[j] + change[j] > m) {
                        a[j] = m - change[j];
                    }
                }
            }
        }
        
        Arrays.fill(change, 0);
        for (int i = 0; i < ops; i++) {
            if (oparr[i][0] == 1) {
                for (int j = (int) oparr[i][1]; j <= (int) oparr[i][2]; j++) {
                    change[j] += oparr[i][3];
                }
            }
            else {
                long biggest = Long.MIN_VALUE;
                for (int j = (int) oparr[i][1]; j <= (int) oparr[i][2]; j++) {
                    if (a[j] + change[j] > biggest) {biggest = a[j] + change[j];}
                }
                if (biggest != oparr[i][3]) {System.out.println("NO"); return;}
            }
        }
        System.out.println("YES");
        for (int i = 0; i < size; i++) {
            System.out.print(a[i]);
            if (i != size - 1) {System.out.print(" ");}
            else {System.out.println();}
        }
    }
}
