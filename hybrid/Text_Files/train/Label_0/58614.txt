import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.io.FileInputStream;
import java.util.ArrayList;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        BCircus solver = new BCircus();
        solver.solve(1, in, out);
        out.close();
    }

    static class BCircus {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.nextInt();
            String str1 = in.nextLine();
            String str2 = in.nextLine();
            int A = 0, B = 0, C = 0, D = 0;
            for (int i = 0; i < n; i++) {
                if (str1.charAt(i) == '0' && str2.charAt(i) == '0') A++;
                if (str1.charAt(i) == '0' && str2.charAt(i) == '1') B++;
                if (str1.charAt(i) == '1' && str2.charAt(i) == '0') C++;
                if (str1.charAt(i) == '1' && str2.charAt(i) == '1') D++;
            }
            int P = -1, Q = -1, R = -1, S = -1;
            loop:
            for (int s = 0; s <= D; s++) {
                int p = s + (n / 2) - B - D;
                if (!(p >= 0 && p <= A)) continue;

                for (int r = 0; r <= C; r++) {
                    int q = B + D - (r + 2 * s);
                    if (q >= 0 && q <= B) {
                        P = p;
                        Q = q;
                        R = r;
                        S = s;
                        break loop;
                    }
                }
            }
            if (P == -1) {
                out.println(-1);
                out.flush();
                return;
            }
            ArrayList<Integer> al = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (str1.charAt(i) == '0' && str2.charAt(i) == '0') {
                    if (P > 0) {
                        P--;
                        al.add(i + 1);
                    }
                }
                if (str1.charAt(i) == '0' && str2.charAt(i) == '1') {
                    if (Q > 0) {
                        Q--;
                        al.add(i + 1);
                    }
                }
                if (str1.charAt(i) == '1' && str2.charAt(i) == '0') {
                    if (R > 0) {
                        R--;
                        al.add(i + 1);
                    }
                }
                if (str1.charAt(i) == '1' && str2.charAt(i) == '1') {
                    if (S > 0) {
                        S--;
                        al.add(i + 1);
                    }
                }
            }
            for (int x : al) out.printsc(x);
            out.println();
            out.flush();
        }

    }

    static class OutputWriter {
        private final PrintWriter writer;
        private ArrayList<String> res = new ArrayList<>();
        private StringBuilder sb = new StringBuilder("");

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }

        public void println(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                sb.append(objects[i]);
            }
            res.add(sb.toString());
            sb = new StringBuilder("");
        }

        public void printsc(Object... objects) {
            for (int i = 0; i < objects.length; i++) {
                sb.append(objects[i]).append(' ');
            }
        }

        public void close() {
            writer.close();
        }

        public void flush() {
            for (String str : res) writer.printf("%s\n", str);
            res.clear();
            sb = new StringBuilder("");
        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[8192];
        private int curChar;
        private int numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public InputReader(FileInputStream file) {
            this.stream = file;
        }

        public int read() {
            if (numChars == -1) {
                throw new InputMismatchException();
            }
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0) {
                    return -1;
                }
            }
            return buf[curChar++];
        }

        public int nextInt() {
            int c = read();
            while (isSpaceChar(c)) {
                c = read();
            }
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                if (c < '0' || c > '9') {
                    throw new InputMismatchException();
                }
                res = (res << 3) + (res << 1) + c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public String nextLine() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = read();
            } while (!isEndOfLine(c));
            return res.toString();
        }

        private boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        private boolean isEndOfLine(int c) {
            return c == '\n' || c == '\r' || c == -1;
        }

    }
}

