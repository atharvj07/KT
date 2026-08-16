import java.util.*;
class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] x = new int[n];
        int[] y = new int[n];

        for(int i = 0; i<n; i++) {
            x[i] = sc.nextInt();
            y[i] = sc.nextInt();
        }

        if(n==1) {
            System.out.println(1);
            return;

        }

        int max = 1;
        for(int i = 0; i<n; i++) {
            for(int j = 0; j<n; j++) {
                long p = x[i]-x[j];
                long q = y[i]-y[j];
                int cnt = 0;
                if(p==0 && q==0)continue;
                for(int k = 0; k<n; k++) {
                    for (int l = 0; l < n; l++) {
                        long dx1 = x[k]-x[l];
                        long dy1 = y[k]-y[l];
                        if(p==dx1 && q==dy1) cnt++;
                    }
                }
//                System.out.println(cnt);
                max = Math.max(cnt,max);
            }
        }
//        System.out.println("max"+max);
        System.out.println(n-max);
    }

}
