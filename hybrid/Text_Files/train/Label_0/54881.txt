import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.InputMismatchException;

public class E {
    static int MOD = 1000000007;
    public static void main(String[] args) throws Exception{
        InputReader in = new InputReader(System.in);
        PrintWriter out = new PrintWriter(System.out);
        
        int n = in.nextInt();
        int[] sum = new int[1<<n];
        int mask = 1;
        for(int i = 0; i < n; i++){
            sum[mask] = in.nextInt();
            mask <<= 1;
        }
        
        for(int i = 1; i < (1<<n); i++){
            int lowBit = i & -i;
            int prev = i - lowBit;
            sum[i] = sum[prev] + sum[lowBit];
            //cap so no overflow, because we only care for sum of 2 numbers <= 10^9
            //and we only need sum[i] != any of the bad numbers
            if(sum[i] > 1000000000){
                sum[i] = 1000000001;
            }
        }
        
        int k = in.nextInt();
        int b1 = -1;
        int b2 = -1;
        if(k >= 1) b1 = in.nextInt();
        if(k == 2) b2 = in.nextInt();
        
        //dp[state] = number of good paths that can be formed using the 1's
        //try ineff
        int[] dp = new int[1<<n];
        dp[0] = 1;
        
        for(int i = 1; i < (1<<n); i++){
            //sum will be untouched before we alter it for dp[i]
            if(sum[i] == b1 || sum[i] == b2){
                dp[i] = 0;
            }else{
                long ans = 0;
                //try all the possible ending sequence of the good paths
                mask = 1;
                for(int j = 0; j < n; j++){
                    if((i & mask) != 0){
                        int prev = i ^ mask;
                        ans += dp[prev];
                    }
                    mask <<= 1;
                }
                dp[i] = (int)( ans % MOD);
            }
        }
        
        out.println(dp[(1<<n)-1]);
        out.close();
    }

    static class InputReader {
        private InputStream stream;
        private byte[] buf = new byte[1024];
        private int curChar;
        private int numChars;
        private SpaceCharFilter filter;

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

        public int nextInt() {
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

        public long nextLong() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            int sgn = 1;
            if (c == '-') {
                sgn = -1;
                c = read();
            }
            long res = 0;
            do {
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                res *= 10;
                res += c - '0';
                c = read();
            } while (!isSpaceChar(c));
            return res * sgn;
        }
        

        public String nextToken() {
            int c = read();
            while (isSpaceChar(c))
                c = read();
            StringBuilder res = new StringBuilder();
            do {
                res.appendCodePoint(c);
                c = read();
            } while (!isSpaceChar(c));
            return res.toString();
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


}