import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, k;
    static long[] a, b;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        a = new long[n];
        b = new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Long.parseLong(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            b[i] = Long.parseLong(st.nextToken());
        }
        long min = 0;
        long max = 2000000001;
        while (max > min + 1) {
            if (ok((min + max) / 2)) {
                min = (min + max) / 2;
            } else {
                max = (min + max) / 2;
            }
        }
        System.out.println(min);
    }

    static boolean ok(long m) {
        long curr = k;
        for (int i = 0; i < n; i++) {
            curr -= Math.max(m * a[i] - b[i], 0);
            if (curr < 0) {
                return false;
            }
        }
        return true;
    }
}
