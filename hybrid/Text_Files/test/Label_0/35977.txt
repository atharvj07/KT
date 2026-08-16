import java.util.*;
import java.io.*;

public class E {
    private FastScanner in;
    private PrintWriter out;

    private void solve() throws IOException {
        int n = in.nextInt(), m = in.nextInt();
        char[][] values = new char[n + 1][m];
        int[][] back = new int[n + 1][3];

        HashMap<String, Integer> names = new HashMap<>();
        names.put("?", 0);
        for (int i = 1; i <= n; i++) {
            String name = in.next(), eq = in.next();
            char[] value = in.next().toCharArray();
            names.put(name, i);
            boolean flag = true;
            for (char c : value) {
                if (c != '0' && c != '1') {
                    flag = false;
                    break;
                }
            }

            if (flag) {
                values[i] = value;
                back[i][0] = i;
                back[i][1] = i;
                back[i][2] = 0;
            } else {
                String op = in.next(), value1 = String.valueOf(value), value2 = in.next();
                back[i][0] = names.get(value1);
                back[i][1] = names.get(value2);
                back[i][2] = Objects.equals(op, "AND") ? 0 : Objects.equals(op, "OR") ? 1 : 2;
            }
        }

        char[] min = new char[m], max = new char[m];
        for (int bit = 0; bit < m; bit++) {
            int sum1 = 0, sum2 = 0;
            values[0][bit] = '0';
            for (int i = 1; i <= n; i++) {
                sum1 += (values[i][bit] = compute(values[back[i][0]][bit], values[back[i][1]][bit], back[i][2])) - '0';
            }
            values[0][bit] = '1';
            for (int i = 1; i <= n; i++) {
                sum2 += (values[i][bit] = compute(values[back[i][0]][bit], values[back[i][1]][bit], back[i][2])) - '0';
            }

            if (sum1 < sum2) {
                min[bit] = '0';
                max[bit] = '1';
            } else if (sum1 == sum2) {
                min[bit] = '0';
                max[bit] = '0';
            } else {
                min[bit] = '1';
                max[bit] = '0';
            }
        }

        out.println(String.valueOf(min));
        out.println(String.valueOf(max));
    }

    char compute(char i, char j, int op) {
        return op == 0 ? and(i, j) : op == 1 ? or(i, j) : xor(i, j);
    }

    char and(char i, char j) {
        return i == '1' && j == '1' ? '1' : '0';
    }

    char or(char i, char j) {
        return i == '1' || j == '1' ? '1' : '0';
    }

    char xor(char i, char j) {
        return i == '1' ^ j == '1' ? '1' : '0';
    }

    public void run() {
        try {
            in = new FastScanner();
            out = new PrintWriter(System.out);

            solve();

            out.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }

    public static void main(String[] arg) {
        new E().run();
    }
}