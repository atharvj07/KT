import java.io.OutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.InputMismatchException;
import java.io.InputStream;

/**
 * Built using CHelper plug-in
 * Actual solution is at the top
 * @author George Marcus
 */
public class Main {
	public static void main(String[] args) {
		InputStream inputStream = System.in;
		OutputStream outputStream = System.out;
		StreamInputReader in = new StreamInputReader(inputStream);
		PrintWriter out = new PrintWriter(outputStream);
		TaskC solver = new TaskC();
		solver.solve(1, in, out);
		out.close();
	}
}

class TaskC {
	public void solve(int testNumber, StreamInputReader in, PrintWriter out) {
        long left = in.readLong();
        long right = in.readLong();

        long a = go(right);
        long b = go(left - 1);

        out.print(a - b);
	}

    private long go(long upper) {
        String repr = Long.toString(upper);
        int len = repr.length();
        long ret = 0;
        long ways = 1;
        for(int i = 0; i < len - 1; i++) {
            if(i == 0)
                ret += 10;
            else {
                ret += 9 * ways;
            }

            if(i >= 1)
                ways *= 10;
        }

        if(len == 1)
            ret += repr.charAt(0) - '0' + 1;
        else {
            long samelen = (long) ((repr.charAt(0) - '1') * Math.pow(10, repr.length() - 2));
            if(repr.charAt(0) > '0') {
                if(repr.charAt(0) > repr.charAt(repr.length() - 1))
                    samelen += go2(repr, 1, true);
                else
                    samelen += go2(repr, 1, false);
            }
            ret += samelen;
        }

        return ret;
    }

    private long go2(String repr, int pos, boolean smaller) {
        long ret = 0;
        int len = repr.length();
        if(pos >= len - 1) {
            if(smaller)
                return 0;
            return 1;
        }
        if(smaller) {
            ret += Math.pow(10, len - pos - 2) * (repr.charAt(pos) - '0');
            ret += go2(repr, pos + 1, true);
        }
        else {
            ret += Math.pow(10, len - pos - 2) * (repr.charAt(pos) - '0');
            ret += go2(repr, pos + 1, false);
        }

        return ret;
    }
}

class StreamInputReader extends InputReader {
    private InputStream stream;
    private byte[] buf = new byte[1024];
    private int curChar, numChars;

    public StreamInputReader(InputStream stream) {
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

    }

abstract class InputReader {

    public abstract int read();

    public long readLong() {
        return Long.parseLong(readString());
    }

    public String readString() {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        StringBuffer res = new StringBuffer();
        do {
            res.appendCodePoint(c);
            c = read();
        } while (!isSpaceChar(c));
        return res.toString();
    }

    private boolean isSpaceChar(int c) {
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    }

