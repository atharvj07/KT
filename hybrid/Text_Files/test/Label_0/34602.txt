import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;

/**
 * User: dmitry
 */
public class Main {
    public static InputStream is = System.in;
    public static BufferedReader br = new BufferedReader(new InputStreamReader(is));
    public static StringTokenizer stok;

    public static String next() {
        String nxt;
        try {
            if (stok != null && stok.hasMoreElements()) return stok.nextToken();
            if ((nxt = br.readLine()) != null) {
                stok = new StringTokenizer(nxt);
                if (stok.hasMoreElements()) return stok.nextToken();
            } else return null;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }

    public static Integer nextInt() {
        return Integer.valueOf(next());
    }

    public static Long nextLong() {
        return Long.valueOf(next());
    }

    public static void main(String[] args) {
        long n = nextLong();
        List<Long> dels = getDels(n);
        if (!check(dels, n)) {
            System.out.println(n);
            return;
        }
        for (Long del : dels) {
            List<Long> mdels = getDels(del);
            if (!check(mdels, del)) {
                System.out.println(del);
                return;
            }
        }
    }

    public static List<Long> getDels(long n) {
        Set<Long> ll = new HashSet<>();
        Set<Long> dels = new HashSet<>();
        dels.add(1l);
        dels.add(n);
        for (long i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                ll.add(i);
            }
        }
        dels.addAll(ll);
        for (Long aLong : ll) {
            long N = n;
            while (N % aLong == 0) {
                dels.add(N / aLong);
                N /= aLong;
            }
        }
        List<Long> ans = new ArrayList<>();
        ans.addAll(dels);
        Collections.sort(ans, new Comparator<Long>() {
            @Override
            public int compare(Long o1, Long o2) {
                return o2.compareTo(o1);
            }
        });
        return ans;
    }

    private static boolean check(List<Long> dels, long n) {
        for (Long del : dels) {
            long N = n;
            if (del > 1)
                if (N % del == 0) {
                    N /= del;
                    if (N % del == 0) {
                        return true;
                    }
                }
        }
        return false;
    }

}