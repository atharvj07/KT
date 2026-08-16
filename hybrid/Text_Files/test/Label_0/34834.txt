import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.TreeSet;
import java.util.ArrayList;
import java.io.Writer;
import java.io.OutputStreamWriter;
import java.util.Comparator;
import java.util.Collections;
import java.io.InputStream;
/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 *
 * @author Alex
 */
public class Main {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        OutputWriter out = new OutputWriter(outputStream);
        TaskB solver = new TaskB();
        solver.solve(1, in, out);
        out.close();
    }
    static class TaskB {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.readInt(), m = in.readInt();
            int hotels = in.readInt();
            int[] xs = new int[hotels], ys = new int[hotels];
            IOUtils.readIntArrays(in, xs, ys);
            // calculate x + y = 20 center
            // calculate x - y = 10 center
            //           2 * y = 10
            //           y = 5
            //           x = 15
            int shitwantx = -1, shitwanty = -1;
            {
                int minxplusy = Integer.MAX_VALUE, maxxplusy = Integer.MIN_VALUE;
                int minxminusy = Integer.MAX_VALUE, maxxminusy = Integer.MIN_VALUE;
                for (int i = 0; i < hotels; i++) {
                    {
                        int xplusy = xs[i] + ys[i];
                        minxplusy = Math.min(minxplusy, xplusy);
                        maxxplusy = Math.max(maxxplusy, xplusy);
                    }
                    {
                        int xminusy = xs[i] - ys[i];
                        minxminusy = Math.min(minxminusy, xminusy);
                        maxxminusy = Math.max(maxxminusy, xminusy);
                    }
                }
                int avgxplusy = (int) ((long) minxplusy + maxxplusy) / 2;
                int avgxminusy = (int) ((long) minxminusy + maxxminusy) / 2;
                int twoy = avgxplusy - avgxminusy;
                int y = twoy / 2;
                int x = avgxplusy - y;
                shitwantx = x;
                shitwanty = y;
            }
            final int wantx = shitwantx;
            final int wanty = shitwanty;
//        out.printLine(wantx, wanty);
//        int wantx = middle(xs);
//        int wanty = middle(ys);
            TreeSet<IntIntPair> already = new TreeSet<>();
            int numrests = in.readInt();
            ArrayList<Rest> rests = new ArrayList<>();
            for (int i = 0; i < numrests; i++) {
                int x = in.readInt(), y = in.readInt();
                if (already.contains(new IntIntPair(x, y))) continue;
                already.add(new IntIntPair(x, y));
                rests.add(new Rest(x, y, i + 1));
            }
//        out.printLine("RESTS SIZE ", rests.size());
            Collections.sort(rests, new Comparator<Rest>() {
                public int compare(Rest a, Rest b) {
                    int adist = Math.abs(a.x - wantx) + Math.abs(a.y - wanty);
                    int bdist = Math.abs(b.x - wantx) + Math.abs(b.y - wanty);
                    return Integer.compare(adist, bdist);
                }
            });
            int resval = Integer.MAX_VALUE;
            int resindex = -1;
            for (int restindex = 0; restindex < Math.min(rests.size(), 500); restindex++) {
                Rest a = rests.get(restindex);
                int act = 0;
                for (int i = 0; i < hotels; i++)
                    act = Math.max(act, Math.abs(xs[i] - a.x) + Math.abs(ys[i] - a.y));
                if (act < resval) {
                    resval = act;
                    resindex = a.index;
                }
            }
            out.printLine(resval);
            out.printLine(resindex);
        }
        class Rest {
            int x;
            int y;
            int index;
            public Rest(int x, int y, int index) {
                this.x = x;
                this.y = y;
                this.index = index;
            }
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
            if (numChars == -1)
                throw new InputMismatchException();
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new InputMismatchException();
                }
                if (numChars <= 0)
                    return -1;
            }
            return buf[curChar++];
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
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }
        public boolean isSpaceChar(int c) {
            if (filter != null)
                return filter.isSpaceChar(c);
            return isWhitespace(c);
        }
        public static boolean isWhitespace(int c) {
            return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
        }
        public interface SpaceCharFilter {
            public boolean isSpaceChar(int ch);
        }
    }
    static class IOUtils {
        public static void readIntArrays(InputReader in, int[]... arrays) {
            for (int i = 0; i < arrays[0].length; i++) {
                for (int j = 0; j < arrays.length; j++)
                    arrays[j][i] = in.readInt();
            }
        }
    }
    static class IntIntPair implements Comparable<IntIntPair> {
        public final int first;
        public final int second;
        public IntIntPair(int first, int second) {
            this.first = first;
            this.second = second;
        }
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            IntIntPair pair = (IntIntPair) o;
            return first == pair.first && second == pair.second;
        }
        public int hashCode() {
            int result = Integer.hashCode(first);
            result = 31 * result + Integer.hashCode(second);
            return result;
        }
        public String toString() {
            return "(" + first + "," + second + ")";
        }
        @SuppressWarnings ({"unchecked"})
        public int compareTo(IntIntPair o) {
            int value = Integer.compare(first, o.first);
            if (value != 0) {
                return value;
            }
            return Integer.compare(second, o.second);
        }
    }
}

