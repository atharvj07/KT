import java.util.*;
public class Main {
    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long L [] =  new long[n];
        for(int i=0;i<n;i++) L[i] = sc.nextLong();
        int q = sc.nextInt();
        for(int i=0;i<q;i++){
            int b = sc.nextInt();
            int e = sc.nextInt();
            int num = 1;
            for(int j=b;j<(b+e)/2;j++){
                long now = L[j];
                L[j] = L[e-num];
                L[e-num] = now;
                num++;
            }
        }
        System.out.print(L[0]);
        for(int i=1;i<n;i++) System.out.print(" "+L[i]);
        System.out.println();
    }
}
