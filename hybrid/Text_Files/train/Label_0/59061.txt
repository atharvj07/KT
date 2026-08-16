
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import static java.lang.Math.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        Reader.init(System.in);
        long n = in.nextLong();
        long a = in.nextLong();
        long b = in.nextLong();
        long c = in.nextLong();
        long co = n;

        while (co % 4 != 0) {
            co++;
        }

        long x = abs(co - n);
        ArrayList<Long> arr = new ArrayList();
        if (x == 0) {
            System.out.println(0);
            return;
        }
        if (x == 3) {
            //3
            arr.add(c);
            arr.add(a * 3);
            arr.add((b + (a )));
        }
        if (x == 2) {
            //2
            arr.add(b);
            arr.add(2 * a);
        }

        if (x == 1) {
            //1
            arr.add(a);
        }
        if (x + 4 == 4) {
            //4
            arr.add(4 * a);
            arr.add(2 * b);
            arr.add((2 * a) + b);
            arr.add(c + a);
        }
        if (x + 4 == 5) {
            //5
            arr.add(5 * a);
            arr.add((2 * b) + a);
            arr.add((3 * a) + b);
            arr.add((2 * a) + c);
            arr.add(c + b);  
        }
        if (x + 4 == 6) {//6
            arr.add(6 * a);
            arr.add(3 * b);
            arr.add((4 * a) + b);
            arr.add((2 * a) + (2 * b));
            arr.add((2 * c));
            arr.add(a + b + c);
            arr.add((3 * a) + c);
        }
        if (x + 4 == 7) {  //7
          
            arr.add(7 * a);
            arr.add((3 * b) + a);
            arr.add((3 * a) + (2 * b));
            arr.add((5 * a) + (b));
            arr.add((a) + (2 * c));
            arr.add((a * 2) + (b + c));
            arr.add((a * 4) + (c));
            arr.add((b * 2) + (c));
        }
        arr.add(3*c);
        Collections.sort(arr);
        System.out.println(arr.get(0));

    }

    static int prime(int p) {
        int t = (int) sqrt(Integer.parseInt(p + ""));
        if (t <= 1) {
            return 0;
        }
        for (long i = 2; i <= t; i++) {
            if (p % i == 0) {
                return 0;
            }

        }
        return 1;
    }

    static int Obe(long a, long b) {
        BigInteger b1 = new BigInteger("" + a);
        BigInteger b2 = new BigInteger("" + b);
        BigInteger gcd = b1.gcd(b2);
        return gcd.intValue();
    }

    static int che(int[] w) {
        Set<Integer> list = new LinkedHashSet<>();
        for (int i = 0; i < w.length; i++) {
            list.add(w[i]);
        }
        return list.size();
    }

    private static ArrayList<BigInteger> fibCache = new ArrayList<BigInteger>();

    static {
        fibCache.add(BigInteger.ZERO);
        fibCache.add(BigInteger.ONE);
    }

    public static BigInteger fib(int n) {
        if (n >= fibCache.size()) {
            fibCache.add(n, fib(n - 1).add(fib(n - 2)));
        }

        return fibCache.get(n);
    }

}

class Reader {

    static BufferedReader reader;
    static StringTokenizer tokenizer;

    static void init(InputStream input) {
        reader = new BufferedReader(
                new InputStreamReader(input));
        tokenizer = new StringTokenizer("");
    }

    static String next() throws IOException {
        while (!tokenizer.hasMoreTokens()) {
            tokenizer = new StringTokenizer(
                    reader.readLine());
        }
        return tokenizer.nextToken();
    }

    static int nextInt() throws IOException {
        return Integer.parseInt(next());
    }

    static long nextLong() throws IOException {
        return Long.parseLong(next());
    }

    static double nextDouble() throws IOException {
        return Double.parseDouble(next());

    }

}
