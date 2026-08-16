    import java.util.Arrays;
    import java.util.Scanner;
     
    public class Main {
     
    static Scanner sc = new Scanner(System.in);
    static int N;
    static long[] K;
    static final long INF = 1000L * 1000 * 1000 * 1000 * 1000 * 1000;
     
    public static void main(String[] args) {
    while (true) {
    N = sc.nextInt();
    if (N == 0) break;
    K = new long[N];
    for (int i = 0; i < N; ++i) {
    K[i] = sc.nextLong();
    }
    System.out.println(solve());
    }
    }
     
    static String solve() {
    while (N > 0 && K[N - 1] == 0) {
    --N;
    }
    if (N == 0 || N > 60) return "None";
     
    long highBit = 1L << (N - 1);
    if (K[N - 1] > highBit) return "None";
     
    String ans = null;
     
    // 1. cross
    long[] countUpper = countAll(highBit + K[N - 1] - 1, highBit, N);
    long[] rem = new long[N - 1];
    for (int i = 0; i < N - 1; ++i) {
    rem[i] = K[i] - countUpper[i];
    }
    long lower = solve(highBit - 1, rem);
    if (lower != -1 && highBit + K[N - 1] - 1 <= INF) {
    ans = lower + " " + (highBit + K[N - 1] - 1);
    }
     
    // 2. cover
    for (int i = N - 2;; --i) {
    if (i == -1) {
    if (N > 1 && highBit <= INF) {
    if (ans != null) {
    ans = "Many";
    } else {
    ans = highBit + " " + highBit;
    }
    }
    break;
    }
    if (K[i] > (1L << i)) break;
    if (K[i] == 0) {
    continue;
    } else if (K[i] == K[N - 1]) {
    highBit += (1L << i);
    } else {
    highBit += (1L << i);
    long high = highBit + K[i] - 1;
    long low = highBit - (K[N - 1] - K[i]);
    long[] counts = countAll(high, low, K.length);
    // System.out.println(high + " " + low + " " + Arrays.toString(counts));
    boolean ok = true;
    for (int j = 0; j < K.length; ++j) {
    if (counts[j] != K[j]) {
    ok = false;
    break;
    }
    }
    if (ok) {
    if (high <= INF) {
    if (ans != null) {
    ans = "Many";
    } else {
    ans = low + " " + high;
    }
    }
    }
    break;
    }
    }
     
    return ans == null ? "None" : ans;
    }
     
    static long solve(long max, long[] k) {
    // System.out.println(max + " " + Arrays.toString(k));
    long[] first = countAll(max, 1, k.length);
    for (int i = 0; i < k.length; ++i) {
    if (first[i] < k[i]) return -1;
    }
    long left = 1;
    long right = max + 1;
    while (left < right - 1) {
    long mid = (left + right) / 2;
    long[] v = countAll(max, mid, k.length);
    boolean more = false;
    for (int i = 0; i < k.length; ++i) {
    if (v[i] < k[i]) {
    more = true;
    }
    }
    if (more) {
    right = mid;
    } else {
    left = mid;
    }
    }
    long[] v = countAll(max, left, k.length);
    for (int i = 0; i < k.length; ++i) {
    if (v[i] != k[i]) {
    return -1;
    }
    }
    return left;
    }
     
    static long[] countAll(long max, long min, int digits) {
    long[] ret = new long[digits];
    for (int i = 0; i < digits; ++i) {
    ret[i] = count(max, min, i);
    }
    return ret;
    }
     
    static long count(long max, long min, int digit) {
    return count(max, digit) - count(min - 1, digit);
    }
     
    static long count(long max, int digit) {
    if (max <= 0) return 0;
    ++max;
    long block = 1L << digit;
    long ret = max / (block * 2) * block;
    ret += Math.max(0, max % (block * 2) - block);
    return ret;
    }
     
    }