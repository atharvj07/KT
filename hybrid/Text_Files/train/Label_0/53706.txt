import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.util.Arrays;
import java.io.BufferedWriter;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.InputMismatchException;
import java.io.IOException;
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
        TaskC2 solver = new TaskC2();
        solver.solve(1, in, out);
        out.close();
    }

    static class TaskC2 {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.readInt();
            int maxK = in.readInt();
            int p = in.readInt();
            int[] a = IOUtils.readIntArray(in, n);
            for (int i = 0; i < a.length; i++) {
                a[i] %= p;
            }
            int[][][] memMem = new int[2][maxK + 1][p];
            ArrayUtils.fill(memMem, -1);
            int toggle = 0;
            {
                int[][] mem = memMem[toggle];
                for (int i = 0; i < mem.length; i++) {
                    mem[i][0] = 0;
                }
            }
            for (int index = a.length - 1; index >= 0; index--) {
                int[][] mem = memMem[toggle];
                int[][] newMem = memMem[toggle ^ 1];
                ArrayUtils.fill(newMem, -1);
                for (int k = 0; k <= maxK; k++) {
                    // include next one
                    {
                        int[] include = mem[k];
                        for (int nxtVal = 0; nxtVal < include.length; nxtVal++) {
                            if (include[nxtVal] < 0) continue;
                            int actualVal = (nxtVal + a[index]) % p;
                            newMem[k][actualVal] = Math.max(newMem[k][actualVal], include[nxtVal]);
                        }
                    }
                    // do not include the next
                    if (k > 1) {
                        int[] noInclude = mem[k - 1];
                        for (int nxtVal = 0; nxtVal < noInclude.length; nxtVal++) {
                            if (noInclude[nxtVal] < 0) continue;
                            newMem[k][a[index]] = Math.max(newMem[k][a[index]], nxtVal + noInclude[nxtVal]);
                        }
                    }
                }
                toggle ^= 1;
            }
            int[] res = memMem[toggle][maxK];
            int ans = 0;
            for (int i = 0; i < res.length; i++) {
                if (res[i] != -1) {
                    ans = Math.max(ans, i + res[i]);
                }
            }
            out.printLine(ans);
        }
    }
    static class OutputWriter {
        private final PrintWriter writer;

        public OutputWriter(OutputStream outputStream) {
            writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
        }

        public OutputWriter(Writer writer) {
            this.writer = new PrintWriter(writer);
        }

        public void close() {
            writer.close();
        }

        public void printLine(int i) {
            writer.println(i);
        }
    }
    static class IOUtils {
        public static int[] readIntArray(InputReader in, int size) {
            int[] array = new int[size];
            for (int i = 0; i < size; i++) {
                array[i] = in.readInt();
            }
            return array;
        }
    }
    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private InputReader.SpaceCharFilter filter;

        public InputReader(InputStream stream) {
            this.stream = stream;
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

        public int readInt() {
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
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }

        public boolean isSpaceChar(int c) {
            if (filter != null) {
                return filter.isSpaceChar(c);
            }
            return isWhitespace(c);
        }

        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }

        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);
        }
    }
    static class ArrayUtils {
        public static void fill(int[][] array, int value) {
            for (int[] row : array) {
                Arrays.fill(row, value);
            }
        }

        public static void fill(int[][][] array, int value) {
            for (int[][] subArray : array) {
                fill(subArray, value);
            }
        }
    }
}

