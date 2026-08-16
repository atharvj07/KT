import java.io.*;
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.*;

public class Main {
    static Input in = new Input(System.in);
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) {
        int N = in.nextInt();
        Map<Long, Map<Long, Long>> map0 = new HashMap<>();
        Map<Long, Map<Long, Long>> map1 = new HashMap<>();
        long zero = 0;
        for (int i = 0; i < N; i++) {
            long A = in.nextLong();
            long B = in.nextLong();
            if (A < 0) {
                A = -A;
                B = -B;
            }
            if (A == 0 && B < 0)
                B = -B;
            long gcd = Math.max(1, gcd(A, Math.abs(B)));
            A /= gcd;
            B /= gcd;
            if (A == 0 && B == 0) {
                zero++;
            } else if (B > 0) {
                Map<Long, Long> map = map0.computeIfAbsent(A, k -> new HashMap<>());
                map.put(B, map.getOrDefault(B, 0L) + 1);
            } else {
                Map<Long, Long> map = map1.computeIfAbsent(-B, k -> new HashMap<>());
                map.put(A, map.getOrDefault(A, 0L) + 1);
            }
        }
        Set<Long> keys0 = new HashSet<>();
        keys0.addAll(map0.keySet());
        keys0.addAll(map1.keySet());
        long ans = 1;
        for (Long key0 : keys0) {
            Map<Long, Long> map00 = map0.getOrDefault(key0, new HashMap<>());
            Map<Long, Long> map11 = map1.getOrDefault(key0, new HashMap<>());
            Set<Long> keys1 = new HashSet<>();
            keys1.addAll(map00.keySet());
            keys1.addAll(map11.keySet());
            for (Long key1 : keys1) {
                long l = -1;
                l += mPow(2, map00.getOrDefault(key1, 0L));
                l += mPow(2, map11.getOrDefault(key1, 0L));
                l %= MOD;
                ans *= l;
                ans %= MOD;
            }
        }
        ans += zero + MOD - 1;
        ans %= MOD;
        out.println(ans);

        out.flush();
    }

    static long gcd(long p, long q) {
        if (p < q) {
            long tmp = p;
            p = q;
            q = tmp;
        }
        while(q != 0) {
            long tmp = p % q;
            p = q;
            q = tmp;
        }
        return p;
    }

    static final int MOD = 1_000_000_007;

    static long mPow(long a, long b) {
        long ret = 1;
        while (b > 0) {
            if (b % 2 == 1)
                ret = (ret * a) % MOD;
            a = (a * a) % MOD;
            b /= 2;
        }
        return ret;
    }

    static class Input {
        private BufferedReader br;
        private String[] buff;
        private int index = 0;

        Input(InputStream is) {
            br = new BufferedReader(new InputStreamReader(is));
        }
        String nextLine() {
            try {
                return br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return null;
        }
        String next() {
            while (buff == null || index >= buff.length) {
                buff = nextLine().split(" ");
                index = 0;
            }
            return buff[index++];
        }
        byte nextByte() {
            return Byte.parseByte(next());
        }
        short nextShort() {
            return Short.parseShort(next());
        }
        int nextInt() {
            return Integer.parseInt(next());
        }
        long nextLong() {
            return Long.parseLong(next());
        }
        float nextFloat() {
            return Float.parseFloat(next());
        }
        double nextDouble() {
            return Double.parseDouble(next());
        }
        BigInteger nextBigInteger() {
            return new BigInteger(next());
        }
        BigDecimal nextBigDecimal() {
            return new BigDecimal(next());
        }
    }
}

