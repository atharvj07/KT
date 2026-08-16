import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.io.BufferedWriter;
import java.util.InputMismatchException;
import java.io.IOException;
import java.util.ArrayList;
import java.util.AbstractMap;
import java.util.TreeMap;
import java.util.Map;
import java.io.Writer;
import java.io.OutputStreamWriter;
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
        TaskD solver = new TaskD();
        solver.solve(1, in, out);
        out.close();
    }
    static class TaskD {
        public void solve(int testNumber, InputReader in, OutputWriter out) {
            int n = in.readInt();
            int m = in.readInt();
            int[] a = IOUtils.readIntArray(in, n);
            ArrayList<Integer>[] modded = new ArrayList[m];
            for (int i = 0; i < modded.length; i++) modded[i] = new ArrayList<>();
            for (int val : a) {
                modded[val % m].add(val);
            }
            int res = 0;
            for (int i = 1; i <= m / 2; i++) {
                int ii = m - i;
                if (i == ii) break;
                res += process(modded[i], modded[ii]);
            }
            res += modded[0].size() / 2;
            if (m % 2 == 0) {
                res += modded[m / 2].size() / 2;
            }
            out.printLine(res);
        }
        private int process(ArrayList<Integer> a, ArrayList<Integer> b) {
            TreeMap<Integer, Integer> acount = new TreeMap<>();
            for (int val : a) acount.merge(val, 1, Integer::sum);
            TreeMap<Integer, Integer> bcount = new TreeMap<>();
            for (int val : b) bcount.merge(val, 1, Integer::sum);
            int aodd = 0, bodd = 0;
            for (int val : acount.values()) if (val % 2 == 1) aodd++;
            for (int val : bcount.values()) if (val % 2 == 1) bodd++;
            int res = Math.min(aodd, bodd);
            aodd -= res;
            bodd -= res;
            TreeMap<Integer, Integer> newacount = new TreeMap<>();
            TreeMap<Integer, Integer> newbcount = new TreeMap<>();
            for (int key : acount.keySet())
                if (acount.get(key) > 1) {
                    if (acount.get(key) % 2 == 0) newacount.put(key, acount.get(key));
                    else newacount.put(key, acount.get(key) - 1);
                }
            acount = newacount;
            for (int key : bcount.keySet())
                if (bcount.get(key) > 1) {
                    if (bcount.get(key) % 2 == 0) newbcount.put(key, bcount.get(key));
                    else newbcount.put(key, bcount.get(key) - 1);
                }
            bcount = newbcount;
//        for (int key : acount.keySet()) if (acount.get(key) % 2 == 1) {
//            if (acount.get(key) == 1) acount.remove(key);
//            else acount.put(key, acount.get(key) - 1);
//        }
//        for (int key : bcount.keySet()) {
//            if (bcount.get(key) == 1) bcount.remove(key);
//            else bcount.put(key, bcount.get(key) - 1);
//        }
            while (aodd > 0) {
                if (!bcount.isEmpty()) {
                    int firstKey = bcount.firstKey();
                    res++;
                    aodd--;
                    bcount.put(firstKey, bcount.get(firstKey) - 1);
                    if (bcount.get(firstKey) == 0) bcount.remove(firstKey);
                } else break;
            }
            while (bodd > 0) {
                if (!acount.isEmpty()) {
                    int firstKey = acount.firstKey();
                    res++;
                    bodd--;
                    acount.put(firstKey, acount.get(firstKey) - 1);
                    if (acount.get(firstKey) == 0) acount.remove(firstKey);
                } else break;
            }
            for (int val : acount.values()) res += val / 2;
            for (int val : bcount.values()) res += val / 2;
            return res;
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
}

