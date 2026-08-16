import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.Random;
import java.io.IOException;
import java.util.TreeSet;
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
        PrintWriter out = new PrintWriter(outputStream);
        FDivisionOrSubstraction solver = new FDivisionOrSubstraction();
        solver.solve(1, in, out);
        out.close();
    }

    static class FDivisionOrSubstraction {
        PrintWriter out;
        InputReader in;

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            this.out = out;
            this.in = in;
            Random rand = new Random();
            long n = nl();
            long i = 0;
            TreeSet<Long> div = new TreeSet<>();
        /*TreeSet<Long> div1 = new TreeSet<>();
        for(i = 2; i <= n; i++){
            long nn = n;
            while(nn > 1){
                if(nn % i == 0)
                    nn /= i;
                else
                    nn -= i;
            }
            if(nn == 1) {
                pn(i);
                div1.add(i);
            }
           // if((n - 1) % i == 0)
               // div.add(i);
        }*/
            for (i = 1; i <= Math.sqrt(n - 1); i++) {
                if ((n - 1) % i == 0) {
                    div.add(i);
                    div.add((n - 1) / i);
                }
            }
            long nn = n;
            for (i = 2; i <= Math.sqrt(nn); i++) {
                if (nn % i == 0) {
                    long x = i;
                    long pp = n;
                    while (pp % x == 0)
                        pp /= x;
                    if (pp == 1)
                        div.add(x);
                    else if ((pp - 1) % x == 0)
                        div.add(x);
                    x = nn / i;
                    pp = n;
                    while (pp % x == 0)
                        pp /= x;
                    if (pp == 1)
                        div.add(x);
                    else if ((pp - 1) % x == 0)
                        div.add(x);
                }
            }
            div.remove(1l);
            div.add(n);
            //pn(div);
            //pn(div1);
            pn(div.size());

        }

        long nl() {
            return in.nextLong();
        }

        void pn(long zx) {
            out.println(zx);
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
                throw new UnknownError();
            if (curChar >= numChars) {
                curChar = 0;
                try {
                    numChars = stream.read(buf);
                } catch (IOException e) {
                    throw new UnknownError();
                }
                if (numChars <= 0)
                    return -1;
            }
            return buf[curChar++];
        }

        public long nextLong() {
            return Long.parseLong(next());
        }

        public String next() {
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
}

