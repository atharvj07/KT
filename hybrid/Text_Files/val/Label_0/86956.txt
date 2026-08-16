import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.*;
import java.util.concurrent.ThreadLocalRandom;
import java.util.concurrent.atomic.AtomicLong;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main2 {

    static long mod = 1000000007L;
    static FastScanner scanner;

    static int[] leftDiff, rightDiff;

    public static void main(String[] args) {
        scanner = new FastScanner();
        int n = scanner.nextInt();
        int[] a = scanner.nextIntArray(n);
        TreeSet<Int> values = new TreeSet<>();
        values.add(new Int(-1));
        values.add(cache[n]);
        TreeMap<Integer, List<Integer>> valueToPosition = new TreeMap<>(Comparator.reverseOrder());
        for (int i = 0; i < n; i++) {
            //values.add(cache[i]);
            valueToPosition.computeIfAbsent(a[i], kk -> new LinkedList<Integer>()).add(i);
        }
        leftDiff = findDiff(a, 0, n, 1);
        rightDiff = findDiff(a, n - 1, -1, -1);

        long result = 0;
        for (List<Integer> indexes : valueToPosition.values()) {
            //Collections.reverse(indexes);
            for (int ind : indexes) {
                int left = values.lower(cache[ind]).val + 1;
                int right = values.higher(cache[ind]).val - 1;
                if (left < right) {
                    result += calcForRange(left, right, a[ind], ind);
                }
                values.add(cache[ind]);
            }
        }
        System.out.println(result);
    }

    static int[] findDiff(int[] a, int start, int end, int step) {
        int[] result = new int[a.length];
        int[] bits = new int[32];
        Arrays.fill(result, -1);
        Arrays.fill(bits, -1);
        for (int i = start; i != end; i+=step) {
            int c = a[i];
            int j = 0;
            while (c > 0) {
                if ((c & 1) == 0) {
                    if (bits[j] != -1) {
                        if (result[i] == -1) {
                            result[i] = bits[j];
                        } else {
                            result[i] = step == 1 ? Math.max(result[i], bits[j]) : Math.min(result[i], bits[j]);
                        }
                    }
                }
                c >>= 1;
                j++;
            }

            c = a[i];
            j = 0;
            while (c > 0) {
                if ((c & 1) == 1) {
                    bits[j] = i;
                }
                c >>= 1;
                j++;
            }
        }
        return result;
    }

    static long calcForRange(int from, int to, int max, int maxI) {
        int l = leftDiff[maxI] != -1 && leftDiff[maxI] >= from ? leftDiff[maxI] : -1;
        int r = rightDiff[maxI] != -1 && rightDiff[maxI] <= to ? rightDiff[maxI] : Integer.MAX_VALUE;

        if (l == -1 && r == Integer.MAX_VALUE) {
            return 0;
        } else if (r == Integer.MAX_VALUE) {
            return (long)(l - from + 1) * (long)(to - maxI + 1);
        } else if (l == -1) {
            return (long)(maxI - from + 1) * (long)(to - r + 1);
        } else  {
            return (long)(maxI - from + 1) * (long)(to - r + 1) +  (long)(l - from + 1) * (long)(r - maxI);
        }
    }

    static Int[] cache = new Int[200010];
    static {
        for (int i = 0; i < 200010; i++) cache[i] = new Int(i);
    }

    static class Int implements Comparable<Int> {
        int val;

        public Int(int val) {
            this.val = val;
        }

        @Override
        public int compareTo(Int o) {
            return Integer.compare(val, o.val);
        }
    }

    static class Range {
        int from, to, max, maxI;

        public Range(int from, int to, int max, int maxI) {
            this.from = from;
            this.to = to;
            this.max = max;
            this.maxI = maxI;
        }

        @Override
        public String toString() {
            return "Range{" +
                    "from=" + from +
                    ", to=" + to +
                    ", max=" + max +
                    ", maxI=" + maxI +
                    '}';
        }
    }

    static class Pt{
        long x, y;

        public Pt(long x, long y) {
            this.x = x;
            this.y = y;
        }
    }
    public static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        public FastScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String nextToken() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        String nextLine() {
            try {
                return br.readLine();
            } catch (Exception e) {
                e.printStackTrace();
                throw new RuntimeException();
            }
        }

        int nextInt() {
            return Integer.parseInt(nextToken());
        }

        long nextLong() {
            return Long.parseLong(nextToken());
        }

        double nextDouble() {
            return Double.parseDouble(nextToken());
        }

        int[] nextIntArray(int n) {
            int[] res = new int[n];
            for (int i = 0; i < n; i++) res[i] = nextInt();
            return res;
        }

        long[] nextLongArray(int n) {
            long[] res = new long[n];
            for (int i = 0; i < n; i++) res[i] = nextLong();
            return res;
        }

        String[] nextStringArray(int n) {
            String[] res = new String[n];
            for (int i = 0; i < n; i++) res[i] = nextToken();
            return res;
        }
    }

    static class PrefixSums {
        long[] sums;

        public PrefixSums(long[] sums) {
            this.sums = sums;
        }

        public long sum(int fromInclusive, int toExclusive) {
            if (fromInclusive > toExclusive) throw new IllegalArgumentException("Wrong sum");
            return sums[toExclusive] - sums[fromInclusive];
        }

        public static PrefixSums of(int[] ar) {
            long[] sums = new long[ar.length + 1];
            for (int i = 1; i <= ar.length; i++) {
                sums[i] = sums[i - 1] + ar[i - 1];
            }
            return new PrefixSums(sums);
        }

        public static PrefixSums of(long[] ar) {
            long[] sums = new long[ar.length + 1];
            for (int i = 1; i <= ar.length; i++) {
                sums[i] = sums[i - 1] + ar[i - 1];
            }
            return new PrefixSums(sums);
        }
    }

    static class ADUtils {
        static void sort(int[] ar) {
            Random rnd = ThreadLocalRandom.current();
            for (int i = ar.length - 1; i > 0; i--)
            {
                int index = rnd.nextInt(i + 1);
                // Simple swap
                int a = ar[index];
                ar[index] = ar[i];
                ar[i] = a;
            }
            Arrays.sort(ar);
        }

        static void sort(long[] ar) {
            Random rnd = ThreadLocalRandom.current();
            for (int i = ar.length - 1; i > 0; i--)
            {
                int index = rnd.nextInt(i + 1);
                // Simple swap
                long a = ar[index];
                ar[index] = ar[i];
                ar[i] = a;
            }
            Arrays.sort(ar);
        }
    }

    static class MathUtils {
        static long modpow(long b, long e, long m) {
            long result = 1;

            while (e > 0) {
                if ((e & 1) == 1) {
            /* multiply in this bit's contribution while using modulus to keep
             * result small */
                    result = (result * b) % m;
                }
                b = (b * b) % m;
                e >>= 1;
            }

            return result;
        }

        static long submod(long x, long y, long m) {
            return (x - y + m) % m;
        }
    }
}
