import java.util.*;
public class Main {
    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long [] opt = new long[n];
        for(int i=0;i<n;i++) opt[i] = sc.nextLong();
        int q = sc.nextInt();
        for(int i=0;i<q;i++){
            long A [] = opt.clone();
            int b = sc.nextInt();
            int m = sc.nextInt();
            int e = sc.nextInt();
            for(int k=0;k<e-b;k++){
                if(b+k>n) break;
                else{
                    int r = (k+(e-m)) % (e-b);
                    int t = b+r;
                    opt[t] = A[b+k];
                }
            }
        }
        System.out.print(opt[0]);
        for(int i=1;i<n;i++) System.out.print(" "+opt[i]);
        System.out.println();
    }
}
