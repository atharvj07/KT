import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class C {
    FastScanner scanner;
    PrintWriter writer;

    private static final int[][] I = {
        {1, 0, 0, 0},
        {0, 0, 1, 0},
        {0, 1, 0, 0},
        {0, 0, 0, 1}
    };

    private static final int[][] C = {
        {0, 0, 1, 0},
        {0, 1, 0, 0},
        {1, 0, 0, 0},
        {0, 0, 0, 1}
    };

    private static final int[][] U = {
        {1, 0, 0, -1},
        {0, 1, 0, 0},
        {0, 0, 1, 0},
        {0, 0, 0, 1}
    };

    private static final int[][] D = {
        {1, 0, 0, 1},
        {0, 1, 0, 0},
        {0, 0, 1, 0},
        {0, 0, 0, 1}
    };

    private static final int[][] R = {
        {1, 0, 0, 0},
        {0, 1, 0, 1},
        {0, 0, 1, 0},
        {0, 0, 0, 1}
    };

    private static final int[][] L = {
        {1, 0, 0, 0},
        {0, 1, 0, -1},
        {0, 0, 1, 0},
        {0, 0, 0, 1}
    };

    void solve() throws IOException {
        scanner = new FastScanner(System.in);
        writer = new PrintWriter(System.out);

        int tests = scanner.nextInt();

        for (int test = 0; test < tests; test++) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();

            int[][] a = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    a[i][j] = scanner.nextInt() - 1;
                }
            }

            int[][] A = identity();
            Map<Character, int[][]> operators = new HashMap<>();
            operators.put('C', C);
            operators.put('I', I);
            operators.put('L', L);
            operators.put('R', R);
            operators.put('U', U);
            operators.put('D', D);

            String s = scanner.next();
            for (int i = m - 1; i >= 0; i--) {
                char c = s.charAt(i);
                int[][] op = operators.get(c);
                multiply_i(A, op);
            }

            int[][] result = new int[n][n];
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    int[] v = new int[] {i, j, a[i][j], 1};
                    int[] v1 = multiplyVector(A, v);
                    toBounds(v1, n);
                    result[v1[0]][v1[1]] = v1[2];
                }
            }
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    writer.print((result[i][j] + 1) + " ");
                }
                writer.println();
            }
            writer.println();
        }

        writer.close();
    }

    <K, V> void swap(Map<K, V> m, K k1, K k2) {
        V tmp = m.get(k1);
        m.put(k1, m.get(k2));
        m.put(k2, tmp);
    }

    void toBounds(int[] v, int n) {
        for (int i = 0; i < v.length - 1; i++) {
            v[i] = v[i] % n;
            if (v[i] < 0)
                v[i] += n;
        }
    }

    int[][] identity() {
        return new int[][] {
            {1, 0, 0, 0},
            {0, 1, 0, 0},
            {0, 0, 1, 0},
            {0, 0, 0, 1}
        };
    }

    int[] multiplyVector(int[][] m, int[] v) {
        int n = v.length;
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                res[i] += m[i][j] * v[j];
            }
        }
        return res;
    }

    void multiply_i(int[][] a, int[][] b) {
        int n = a.length;
        for (int i = 0; i < n; i++) {
            int[] v = a[i];
            a[i] = new int[n];
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    a[i][j] += v[k] * b[k][j];
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        new C().solve();
    }

    static class FastScanner {
        BufferedReader br;
        StringTokenizer tokenizer;

        FastScanner(InputStream is) {
            this.br = new BufferedReader(new InputStreamReader(is));
        }

        FastScanner(File file) throws FileNotFoundException {
            this(new FileInputStream(file));
        }

        String nextLine() throws IOException {
            return br.readLine();
        }

        String next() throws IOException {
            while (tokenizer == null || !tokenizer.hasMoreTokens())
                tokenizer = new StringTokenizer(br.readLine());

            return tokenizer.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }
    }
}
