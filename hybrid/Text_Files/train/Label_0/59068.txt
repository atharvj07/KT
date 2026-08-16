import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class E582TwoSmallStrings {

    static PrintWriter pr = new PrintWriter(System.out);
    public static class InputReader {
        private BufferedReader reader;
        private StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public long nextLong() {
            return Long.parseLong(next());
        }
    }

    public static void main(String[] args) {
        InputReader in = new InputReader(System.in);
        int n = in.nextInt();
        String s = in.next();
        String t = in.next();

        ans(n,s,t);
        pr.flush();
    }

    private static void ans(int n, String s, String t) {

        String[] buf = { "abc", "acb", "cba", "bca", "bac", "cab"};

        ArrayList<String> list = new ArrayList<>();
        for (int i = 0; i < 6; i++) {

            StringBuilder str = new StringBuilder();

            for (int j = 0; j < n; j++) {
                str.append(buf[i]);
            }

            list.add(new String(str));
            str = new StringBuilder();

            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < n; k++) {
                    str.append(buf[i].charAt(j));
                }
            }
            list.add(new String(str));
        }

        for (String str: list) {
            if (!str.contains(s) && !str.contains(t)){
                pr.println("YES");
                pr.print(str);
                return;
            }
        }

        pr.print("NO");
    }
}