import java.util.Scanner;

/**
 *
 * @author HP
 */
public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n  = s.nextInt();
        int m  = s.nextInt();
        int limit = s.nextInt();

        int a[] = new int[n];
        long sumA[] = new long[n+1];
        int b[] = new int[m];
        long sumB[] = new long[m+1];

        for(int i = 1; i <= n; ++i) {
            a[i-1] =  s.nextInt();
            sumA[i] = sumA[i-1] + a[i-1];
//            System.out.println(sumA[i]);
        }

        for(int i = 1; i <= m; ++i) {
            b[i-1] =  s.nextInt();
            sumB[i] = sumB[i-1] + b[i-1];
//            System.out.println(sumB[i]);
        }

        int j = m;
        int ans = 0;
        for(int i = 0; i <= n; i++) {
            if(sumA[i] > limit)
                break;
            while(limit - sumA[i] < sumB[j])
                j--;
            ans = Math.max(ans,i+j);
        }
        System.out.println(ans);
    }
}