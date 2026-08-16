import java.util.*;
public class Main {
    static void find(long a[]){
        long max=a[0];
        for (long i:a)max=Math.max(i,max);
        for (long i=0;i<a.length;i++)a[(int)i]=max-a[(int)i];
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long T = sc.nextLong();
        outer:while (T-- >= 1) {
            long n = sc.nextLong();
            long k=sc.nextLong();
            long a[] = new long[(int) n];
            for (long i = 0; i < n; i++) {
                a[(int) i] = sc.nextLong();
            }
            if (k%2!=0){
                find(a);
                for (long i:a) System.out.print(i+" ");
            }
            System.out.println();
             if (k%2==0){
                find(a);
                find(a);
                 for (long i:a) System.out.print(i+" ");

            }
            System.out.println();




        }
    }
}