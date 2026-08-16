import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.List;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author masterbios
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        BPrincessesAndPrinces solver = new BPrincessesAndPrinces();
        solver.solve(1, in, out);
        out.close();
    }

    static class BPrincessesAndPrinces {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int t = in.nextInt();
            while (t-- > 0) {
                List<List<Integer>> list = new ArrayList<>();
                int n = in.nextInt();
                int count = n;
                boolean king[] = new boolean[n];
                boolean queen[] = new boolean[n];
                for (int i = 0; i < n; i++) {
                    List<Integer> temp = new ArrayList<>();
                    int m = in.nextInt();
                    for (int j = 0; j < m; j++) {
                        temp.add(in.nextInt() - 1);
                    }
                    list.add(temp);
                }
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < list.get(i).size(); j++) {
                        int x = list.get(i).get(j);
                        if (!king[x]) {
                            king[x] = true;
                            queen[i] = true;
                            count--;
                            break;
                        }
                    }
                }
                if (count == 0) {
                    out.println("OPTIMAL");
                } else {
                    int ans1 = 0, ans2 = 0;
                    for (int i = 0; i < n; i++) {
                        if (!queen[i]) {
                            ans1 = i + 1;
                            break;
                        }
                    }
                    for (int i = 0; i < n; i++) {
                        if (!king[i]) {
                            ans2 = i + 1;
                            break;
                        }
                    }
//                out.println(Arrays.toString(king));
//                out.println(Arrays.toString(queen));
                    out.println("IMPROVE");
                    out.println(ans1 + " " + ans2);
                }
            }
        }

    }

    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }

        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreElements()) {
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

    }
}

