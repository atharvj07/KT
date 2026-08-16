
import java.io.PrintWriter;
import java.util.*;

public class Main {

    long INF = 1L << 60;

    void run() {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Long> m = new ArrayList<>(), p = new ArrayList<>();
        PriorityQueue<Long> q = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            long x = sc.nextLong();
            if (x < 0) {
                m.add(x);
            } else {
                p.add(x);
            }
        }

        PrintWriter out = new PrintWriter(System.out);
        String[] ans = new String[n - 1];
        long max = -1;

        if (m.size() > 0 && p.size() > 0) {
            long cp = p.get(0);
            long cm = m.get(0);
            int lenp = p.size();
            int lenm = m.size();
            int cnt = 0;

            for (int i = 1; i < lenm; i++) {
                ans[cnt] = cp + " " + m.get(i);
                cp -= m.get(i);
                cnt++;
            }
            for (int i = 1; i < lenp; i++) {
                ans[cnt] = cm + " " + p.get(i);
                cm -= p.get(i);
                cnt++;
            }
            ans[cnt] = cp + " " + cm;
            max = cp - cm;
        } else {
            if (p.size() > 0) {
                Collections.sort(p);
                if (n > 2) {
                    long v = p.get(0) - p.get(1);
                    ans[0] = p.get(0) + " " + p.get(1);
                    for (int i = 2; i < n - 1; i++) {
                        ans[i - 1] = v + " " + p.get(i);
                        v = v - p.get(i);
                    }
                    ans[n - 2] = p.get(n - 1) + " " + v;
                    max = p.get(n - 1) - v;
                } else {
                    ans[0] = p.get(1) + " " + p.get(0);
                    max = p.get(1) - p.get(0);
                }
            } else {
                Collections.sort(m, Collections.reverseOrder());
                long v = m.get(0) - m.get(1);
                ans[0] = m.get(0) + " " + m.get(1);
                for (int i = 2; i < n; i++) {
                    ans[i - 1] = v + " " + m.get(i);
                    v -= m.get(i);
                }
                max = v;
            }
        }

        out.println(max);
        for (int i = 0; i < n - 1; i++) {
            out.println(ans[i]);
        }
        out.flush();
    }

    void debug(Object...os) {
        System.err.println(Arrays.deepToString(os));
    }

    public static void main(String[] args) {
        new Main().run();
    }
}
