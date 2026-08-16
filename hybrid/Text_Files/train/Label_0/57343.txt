import java.io.*;
import java.util.*;

class Main {
    static Scanner scanner = new Scanner();
    static long mod = 1000000007;

    public static void main(String[]$) {
        char[] s = scanner.next().toCharArray();
        char[] s2 = Arrays.copyOf(s, s.length);
        long k = scanner.nextInt();
        long count = 0;
        char first = s[0];
        boolean all = true;
        for (int i = 1; i < s.length; i++) {
            all &= first == s[i];
        }
        if (all) {
            System.out.println(s.length * k / 2);
        } else {
            int start = 0;
            if (s[0] == s[s.length - 1]) {
                start++;
                while (s[start] == s[start - 1]) {
                    start++;
                }
            }
            for (int i = 0; i < s.length; i++) {
                if (s[(i + start) % s.length] == s[(i + start + 1) % s.length]) {
                    s[(i + start + 1) % s.length] = '\0';
                    count++;
                }
            }
            count *= k - 1;
            for (int i = 1; i < s.length; i++) {
                if (s2[i - 1] == s2[i]) {
                    s2[i] = '\0';
                    count++;
                }
            }
            System.out.println(count);
        }
    }

    static class Scanner {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in), 1 << 15);
        StringTokenizer tokenizer;

        String next() {
            try {
                while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                    tokenizer = new StringTokenizer(reader.readLine());
                }
            } catch (IOException ignored) {
            }
            return tokenizer.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }
}
