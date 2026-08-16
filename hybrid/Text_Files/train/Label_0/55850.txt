import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.HashSet;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author lebegio
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        MyReader in = new MyReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskC solver = new TaskC();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskC {
        public void solve(int testNumber, MyReader in, PrintWriter out) {
            String str = in.next();
            int SIZE = 13;
            HashSet<Character> set = new HashSet<Character>();
            char CH = 'x';
            for (char ch : str.toCharArray()) {
                if (set.contains(ch)) {
                    CH = ch;
                    break;
                }
                set.add(ch);
            }
            int start = -1;
            int end = 0;
            for (int i = 0; i < str.length(); i++) {
                if (str.charAt(i) == CH) {
                    if (start == -1) start = i;
                    else end = i;
                }
            }

            if (end - start <= 1) {
                out.println("Impossible");
                return;
            }

            String upStr = "" + CH;
            String downStr = "";
            int x = start + 1;
            int y = end - 1;
            while (y > x) {
                upStr += str.charAt(x);
                downStr += str.charAt(y);
                x++;
                y--;
            }
            if (x == y) downStr += str.charAt(x);

            start--;
            end++;
            while (start >= 0 && upStr.length() < SIZE) {
                upStr = str.charAt(start) + upStr;
                start--;
            }

            while (end < str.length() && downStr.length() < SIZE) {
                downStr = str.charAt(end) + downStr;
                end++;
            }
            int p = 0;
            while (p <= start) {
                downStr = str.charAt(p) + downStr;
                p++;
            }
            p = str.length() - 1;
            while (p >= end) {
                upStr = str.charAt(p) + upStr;
                p--;
            }

            out.println(upStr);
            out.println(downStr);
        }

    }

    static class MyReader {
        private BufferedReader buffReader;
        private StringTokenizer strTokenizer;
        private static final int SIZE = 32768;

        public MyReader(InputStream inputStream) {
            buffReader = new BufferedReader(new InputStreamReader(inputStream), SIZE);
        }

        public String next() {
            if (strTokenizer == null || !strTokenizer.hasMoreTokens()) {
                try {
                    strTokenizer = new StringTokenizer(buffReader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return strTokenizer.nextToken();
        }

    }
}

