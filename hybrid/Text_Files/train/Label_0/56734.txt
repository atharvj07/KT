import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.function.IntPredicate;

public class C {
    private static int binSearch(int l, int r, IntPredicate predicate) {
        while (l + 1 < r) {
            int m = (l + r) / 2;
            if (predicate.test(m)) {
                r = m;
            } else {
                l = m;
            }
        }
        return r;
    }

    public static void main(String[] args) throws IOException {
        try (FastScanner s = new FastScanner(System.in)) {
            PrintStream out = System.out;

            char[] c = s.nextString().toCharArray();
            int[] amount = new int[26];
            for (int i = 0; i < c.length; i++) {
                char c1 = c[i];
                amount[c1 - 'a']++;
            }

            List<Integer> withOddAmount = new ArrayList<>();
            for (int i = 0; i < amount.length; i++) {
                if(amount[i] % 2 == 1) {
                    withOddAmount.add(i);
                }
            }

            int inCenter = -1;

            for (int i = 0; i < withOddAmount.size() / 2; i++) {
                int j = withOddAmount.get(i);
                int j2 = withOddAmount.get(withOddAmount.size() - 1 - i);
                amount[j]++;
                amount[j2]--;
            }

            if (c.length % 2 == 1) {
                inCenter = withOddAmount.get(withOddAmount.size() / 2);
            }

            StringBuilder leftPart = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                for (int k = 0; k < amount[i] / 2; k++) {
                    leftPart.append((char)('a' + i));
                }
            }
            String result;
            if (inCenter >= 0) {
                result = leftPart.toString() + (char)(inCenter + 'a') + leftPart.reverse().toString();
            } else {
                result = leftPart.toString() + leftPart.reverse().toString();
            }

            out.println(result);
        }
    }

    static class FastScanner implements AutoCloseable {
        private String line;
        private StringTokenizer tokenizer;
        private BufferedReader reader;

        public FastScanner(InputStream is) throws FileNotFoundException {
            reader = new BufferedReader(new InputStreamReader(is));
        }

        public int nextInt() throws IOException {
            return Integer.parseInt(nextString());
        }

        public long nextLong() throws IOException {
            return Long.parseLong(nextString());
        }

        public String nextString() throws IOException {
            if (line == null || !tokenizer.hasMoreTokens()) {
                line = reader.readLine();
                tokenizer = new StringTokenizer(line);
            } else {
                return tokenizer.nextToken();
            }
            return nextString();
        }

        @Override
        public void close() throws IOException {
            reader.close();
        }
    }
}
