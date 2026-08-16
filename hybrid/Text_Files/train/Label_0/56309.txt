import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        Long ans = Long.MAX_VALUE;
        for (int i = 0; i < 1<<n; i++) {
            if(Integer.bitCount(i) < k)continue;
            long t = 0L;
            int preh = -1;
            for (int j = 0; j < n; j++) {
                if((i>>j & 1) != 1){
                    if(preh < a[j]) preh = a[j];
                    continue;
                }
                if(a[j] < preh+1) t += preh+1-a[j];
                preh = Math.max(a[j], preh+1);
            }
            if(t < ans) ans = t;
        }
        System.out.println(ans);
        sc.close();

    }

}
