import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Spandan Mishra
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        EYutori solver = new EYutori();
        solver.solve(1, in, out);
        out.close();
    }

    static class EYutori {
        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int n = in.readInt();
            int k = in.readInt(); // work k days
            int c = in.readInt(); // absent days after a work day
            String s = in.readString();
            StringBuilder sb = new StringBuilder();
            int[] l = new int[n];
            int[] r = new int[n];

            char[] S = s.toCharArray();
            int cntl = 1;
            int cntr = 0;
            for (int i = 0; i < n && cntl <= k; i++) {
                if (S[i] == 'o') {
                    l[i] = cntl;
                    cntl++;
                    i += c;
                }
            }
            if (cntl >= k) {

                cntr = k;
                for (int i = n - 1; i >= 0 && cntr > 0; i--) {
                    if (S[i] == 'o') {
                        r[i] = cntr;
                        cntr--;
                        i -= c;
                    }
                }
            }

            if (cntl >= k && cntr <= 0) {
                for (int i = 0; i < n; i++)
                    if (l[i] == r[i] && l[i] != 0)
                        sb.append((i + 1) + "\n");
            }

            System.out.print(sb);
        }

    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;

        public InputReader(InputStream stream) {
            this.stream = stream;
        }

        public int read() {
            if (numChars == -1)
                throw new RuntimeException();
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new RuntimeException();
                }
                if (numChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public String readString() {
            final StringBuilder stringBuilder = new StringBuilder();
            int c = read();
            while (isSpaceChar(c))
                c = read();
            do {
                stringBuilder.append((char) c);
                c = read();
            } while (!isSpaceChar(c));
            return stringBuilder.toString();
        }

        public int readInt() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            int res = 0;
            do {
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public boolean isSpaceChar(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

    }
}

