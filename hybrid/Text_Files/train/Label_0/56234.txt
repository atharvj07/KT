import java.io.*;
import java.util.Formatter;
import java.util.Locale;

public class C {

    void solve() throws IOException {
        in = new InputReader("__std");
        out = new OutputWriter("__std");

        int testCount = in.readInt();
        for (int test = 1; test <= testCount; ++test) {
            long n = in.readLong();
            out.println(n * 2 - Long.bitCount(n * 2));
        }

        exit();
    }

    void exit() {
        out.close();
        //System.err.println((System.currentTimeMillis() - startTime) + " ms");
        System.exit(0);
    }

    InputReader in;
    OutputWriter out;

    //long startTime = System.currentTimeMillis();

    public static void main(String[] args) throws IOException {
        new C().solve();
    }

    class InputReader {

        private InputStream stream;

        private byte[] buffer = new byte[1024];
        private int pos, len;

        private int cur;

        private StringBuilder sb = new StringBuilder(32);

        InputReader(String name) throws IOException {
            if (name.equals("__std")) {
                stream = System.in;
            } else {
                stream = new FileInputStream(name);
            }
            cur = read();
        }

        private int read() throws IOException {
            if (len == -1) {
                throw new EOFException();
            }
            if (pos >= len) {
                pos = 0;
                len = stream.read(buffer);
                if (len == -1) return -1;
            }
            return buffer[pos++] & 0xff;
        }

        boolean whitespace() {
            return cur == ' ' || cur == '\t' || cur == '\r' || cur == '\n' || cur == -1;
        }

        boolean eol() {
            return cur == '\r' || cur == '\n' || cur == -1;
        }

        boolean eof() {
            return cur == -1;
        }

        byte readByte() throws IOException {
            if (eof()) {
                throw new EOFException();
            }
            byte res = (byte) cur;
            cur = read();
            return res;
        }

        char readChar() throws IOException {
            if (eof()) {
                throw new EOFException();
            }
            char res = (char) cur;
            cur = read();
            return res;
        }

        int readInt() throws IOException {
            if (eof()) {
                throw new EOFException();
            }
            while (whitespace()) {
                cur = read();
            }
            if (eof()) {
                throw new EOFException();
            }
            int sign = 1;
            if (cur == '-') {
                sign = -1;
                cur = read();
                if (cur < '0' || cur > '9') {
                    throw new NumberFormatException();
                }
            }
            int res = 0;
            while (!whitespace()) {
                if (cur < '0' || cur > '9') {
                    throw new NumberFormatException();
                }
                res *= 10;
                res += cur - '0';
                cur = read();
            }
            return res * sign;
        }

        long readLong() throws IOException {
            if (eof()) {
                throw new EOFException();
            }
            while (whitespace()) {
                cur = read();
            }
            if (eof()) {
                throw new EOFException();
            }
            int sign = 1;
            if (cur == '-') {
                sign = -1;
                cur = read();
                if (cur < '0' || cur > '9') {
                    throw new NumberFormatException();
                }
            }
            long res = 0;
            while (!whitespace()) {
                if (cur < '0' || cur > '9') {
                    throw new NumberFormatException();
                }
                res *= 10;
                res += cur - '0';
                cur = read();
            }
            return res * sign;
        }

        double readDouble() throws IOException {
            return Double.parseDouble(readToken());
        }

        String readToken() throws IOException {
            if (eof()) {
                throw new EOFException();
            }
            while (whitespace()) {
                cur = read();
            }
            if (eof()) {
                throw new EOFException();
            }
            sb.setLength(0);
            while (!whitespace()) {
                sb.append((char) cur);
                cur = read();
            }
            return sb.toString();
        }

        String readLine() throws IOException {
            if (eof()) {
                throw new EOFException();
            }
            sb.setLength(0);
            while (!eol()) {
                sb.append((char) cur);
                cur = read();
            }
            if (cur == '\r') {
                cur = read();
            }
            if (cur == '\n') {
                cur = read();
            }
            return sb.toString();
        }

        void skipLine() throws IOException {
            if (eof()) {
                throw new EOFException();
            }
            while (!eol()) {
                cur = read();
            }
            if (cur == '\r') {
                cur = read();
            }
            if (cur == '\n') {
                cur = read();
            }
        }
    }

    class OutputWriter {

        private PrintWriter writer;

        OutputWriter(String name) throws IOException {
            if (name.equals("__std")) {
                writer = new PrintWriter(System.out);
            } else {
                writer = new PrintWriter(name);
            }
        }

        void print(String format, Object ... args) {
            writer.print(new Formatter(Locale.US).format(format, args));
        }

        void println(String format, Object ... args) {
            writer.println(new Formatter(Locale.US).format(format, args));
        }

        void print(Object value) {
            writer.print(value);
        }

        void println(Object value) {
            writer.println(value);
        }

        void println() {
            writer.println();
        }

        void printArray(int[] a) {
            boolean first = true;
            for (int v : a) {
                if (!first) {
                    writer.print(' ');
                } else {
                    first = false;
                }
                writer.print(v);
            }
            writer.println();
        }

        void printArray(int[][] a) {
            for (int[] v : a) {
                printArray(v);
            }
        }

        void flush() {
            writer.flush();
        }

        void close() {
            writer.close();
        }
    }
}
