import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Main main = new Main();
        main.solve();
    }

    public void solve() {
        Scanner scan = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int N = scan.nextInt();
        long T = scan.nextLong();
        List<Pair> zero_list = new ArrayList<>();
        List<Pair> non_zero_list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            long a = scan.nextLong();
            long b = scan.nextLong();
            Pair p = new Pair(a, b);
            if (a == 0) {
                zero_list.add(p);
            } else {
                non_zero_list.add(p);
            }
        }

        zero_list.sort(new ZeroPairComparator());
        long[] z = new long[zero_list.size()+1];
        for (int i = 0; i < zero_list.size(); i++) {
            z[i + 1] = Math.min(z[i] + zero_list.get(i).b + 1, T + 1);
        }
        TreeMap<Long, Integer> zero_tree = new TreeMap<>();
        for (int i = 0; i < z.length; i++) {
            zero_tree.put(z[i], i);
        }

        non_zero_list.sort(new NonZeroPairComparator());
        long[] dp = new long[41];
        Arrays.fill(dp, T+1);
        dp[0] = 0;
        int len = non_zero_list.size();
        for (int i = 0; i < len; i++) {
            Pair p = non_zero_list.get(i);
            for (int j = 40; 0 <= j; j--) {
                if ( T < dp[j]) {
                    continue;
                }
                long time = dp[j] + 1 + p.a * (dp[j] + 1) + p.b;
                dp[j+1] = Math.min(dp[j+1], time);
            }
        }
        long ans = 0;
        for (int i = 0; i <= 40; i++) {
            if (T < dp[i]) {
                continue;
            }
            long count = i + zero_tree.floorEntry(T - dp[i]).getValue();
            ans = Math.max(ans, count);
        }
        System.out.println(ans);
    }

    class Pair {
        long a;
        long b;
        Pair(long a, long b) {
            this.a = a;
            this.b = b;
        }
    }

    class ZeroPairComparator implements Comparator<Pair> {
        @Override
        public int compare(Pair o1, Pair o2) {
            return Long.compare(o1.b, o2.b);
        }
    }

    class NonZeroPairComparator implements Comparator<Pair> {
        @Override
        public int compare(Pair o1, Pair o2) {
            return -Long.compare(o1.a * (o2.b + 1), o2.a * (o1.b+1));
        }
    }
}
