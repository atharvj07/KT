import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n,k,t,u,v,l;
        n = sc.nextInt();
        k = sc.nextInt();
        t = sc.nextInt();
        u = sc.nextInt();
        v = sc.nextInt();
        l = sc.nextInt();

        int[] d = new int[n+1];
        for (int i = 0; i < n; ++i) d[i] = sc.nextInt();
        d[n] = l;

        int pos = 0, c = 0, nk = 0;
        double tm = 0;

        while (pos < l) {
            // ??????????????????????????´???????????????
            if (pos < d[c]) {
                // ?????????????????£?????????
                if (nk > 0) {
                    nk--;
                    int x = Math.min(l, pos+t*v);
                    tm += (x-pos)/(double)v;
                    pos = x;
                }
                // ?????£??????????????£??????
                else {
                    tm += (d[c]-pos)/(double)u;
                    pos = d[c];
                }
            }
            //  ?????????????????´???????????£??????
            else {
                // ?????????????????£??????????????£??????
                if (d[c] == pos) {
                    int x = Math.min(l, pos+t*v);
                    tm += (x-pos)/(double)v;
                    pos = x;
                    ++c;
                }
                else {
                    if (nk < k) {
                        c++;
                        nk++;
                    }
                    else {
                        int x = Math.min(l, d[c++]+t*v);
                        tm += (x-pos)/(double)v;
                        pos = x;
                    }
                }
            }
        }
        System.out.println(tm);
    }
}