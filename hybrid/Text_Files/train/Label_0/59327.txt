import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Scanner;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        Scanner in = new Scanner(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        Recording solver = new Recording();
        solver.solve(1, in, out);
        out.close();
    }

    static class Recording {
        public void solve(int testNumber, Scanner in, PrintWriter out) {
            int n = in.nextInt();
            int c = in.nextInt();

            int[][] tv = new int[31][100009];
            for (int i = 0; i < n; i++) {
                int s = in.nextInt();
                int t = in.nextInt();
                int cc = in.nextInt();
                for (int j = s; j <= t; j++) {
                    tv[cc][j] = 1;
                }
            }

            for (int i = 1; i <= 30; i++) {
                for (int j = 1; j <= 100000; j++) {
                    if (tv[i][j] == 0 && tv[i][j] == 1) {
                        tv[i][j] = 1;
                    }
                }
            }

            long result = 0;
            for (int j = 1; j <= 100000; j++) {
                long cal = 0;
                for (int i = 1; i <= 30; i++) {
                    if (tv[i][j] == 1) {
                        cal++;
                    }
                }
                result = Math.max(result, cal);
            }

            out.println(result);
        }

    }
}

