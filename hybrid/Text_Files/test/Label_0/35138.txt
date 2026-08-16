import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.io.PrintStream;
import java.util.stream.IntStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Wolfgang Beyer
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskC solver = new TaskC();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskC {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.nextInt();
            String s = in.next();
            long xGoal = in.nextInt();
            long yGoal = in.nextInt();
            long distGoal = Math.abs(xGoal) + Math.abs(yGoal);
            if (distGoal > n || ((n - distGoal) % 2 != 0)) {
                out.println(-1);
                return;
            }
            long xEnd = StringFunctions.countChar(s, 'R') - StringFunctions.countChar(s, 'L');
            long yEnd = StringFunctions.countChar(s, 'U') - StringFunctions.countChar(s, 'D');
            if (xEnd == xGoal && yEnd == yGoal) {
                out.println(0);
                return;
            }
            int second = 0;
            long xCurrent = xEnd;
            long yCurrent = yEnd;
            int result = n;
            for (int first = 0; first < n; first++) {
                while ((Math.abs(xCurrent - xGoal) + Math.abs(yCurrent - yGoal) != second - first) && (second < n)) {
//            while ((xCurrent != xGoal || yCurrent != yGoal) && (second < n)) {
                    switch (s.charAt(second)) {
                        case 'U':
                            yCurrent--;
                            break;
                        case 'D':
                            yCurrent++;
                            break;
                        case 'R':
                            xCurrent--;
                            break;
                        case 'L':
                            xCurrent++;
                            break;
                    }
                    second++;
                }
//            if (second == n) {
//                break;
//            }
                if (Math.abs(xCurrent - xGoal) + Math.abs(yCurrent - yGoal) == second - first) {
                    result = Math.min(result, second - first);
                }
                switch (s.charAt(first)) {
                    case 'U':
                        yCurrent++;
                        break;
                    case 'D':
                        yCurrent--;
                        break;
                    case 'R':
                        xCurrent++;
                        break;
                    case 'L':
                        xCurrent--;
                        break;
                }
            }
            out.println(result);

        }

    }

    static class InputReader {
        private static BufferedReader in;
        private static StringTokenizer tok;

        public InputReader(InputStream in) {
            this.in = new BufferedReader(new InputStreamReader(in));
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }

        public String next() {
            try {
                while (tok == null || !tok.hasMoreTokens()) {
                    tok = new StringTokenizer(in.readLine());
                    //tok = new StringTokenizer(in.readLine(), ", \t\n\r\f"); //adds commas as delimeter
                }
            } catch (IOException ex) {
                System.err.println("An IOException was caught :" + ex.getMessage());
            }
            return tok.nextToken();
        }

    }

    static class StringFunctions {
        public static int countChar(String s, char c) {
            return (int) s.chars().filter(ch -> ch == c).count();
        }

    }
}

