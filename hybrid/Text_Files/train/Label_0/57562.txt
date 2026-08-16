/*
 * PDPM IIITDM Jabalpur
 * Asutosh Rana
 */

import java.util.*;
import java.io.*;
import java.math.*;

public class Main
{
    long MOD = 1000000007;
    InputReader in;BufferedReader br;PrintWriter out;
    public static void main (String[] args) throws java.lang.Exception
    {
        Main solver = new Main();
        solver.in = new InputReader(System.in);
        solver.br = new BufferedReader(new InputStreamReader(System.in));
        solver.out = new PrintWriter(System.out);
        solver.solve();
        solver.out.flush();
        solver.out.close();
    }

    public void solve(){
        
        int tc = 1;//in.readInt();
        
        for(int cas=1;cas<=tc;cas++){
            int N = in.readInt();
            int M = in.readInt();
            boolean[] B = new boolean[N];
            boolean[] G = new boolean[M];
            int k = in.readInt();
            while(k-->0){
                int i = in.readInt();
                B[i] = true;
            }
            k = in.readInt();
            while(k-->0){
                int i = in.readInt();
                G[i] = true;
            }

            int length = 100000;//2*N*M;
            for(int i=0;i<=length;i++){
                int a = i%N;
                int b = i%M;
                boolean res = B[a] | G[b];
                B[a] = G[b] = res;
            }

            if(check(B,G))
                out.println("Yes");
            else
                out.println("No");
        }

    }

    public boolean check(boolean[] A, boolean[] B){
        for(int i=0;i<A.length;i++){
            if(!A[i])
                return false;
        }
        for(int i=0;i<B.length;i++){
            if(!B[i])
                return false;
        }
        return true;
    }
    
}
 
class InputReader{
    private InputStream stream;
    private byte[] buf = new byte[1024];
    private int curChar;
    private int numChars;
    private SpaceCharFilter filter;

    public InputReader(InputStream stream){this.stream = stream;}
    public int read(){
        if (numChars==-1) throw new InputMismatchException();
        if (curChar >= numChars){
            curChar = 0;
            try {numChars = stream.read(buf);}
            catch (IOException e){throw new InputMismatchException();}
            if(numChars <= 0) return -1;
        }
        return buf[curChar++];
    }

    public int readInt(){
        int c = read();
        while(isSpaceChar(c)) c = read();
        int sgn = 1;
        if (c == '-') {sgn = -1;c = read();}
        int res = 0;
        do {
            if(c<'0'||c>'9') throw new InputMismatchException();
            res *= 10;
            res += c - '0';
            c = read();
        }
        while (!isSpaceChar(c)); return res * sgn;
    }

    public void readInt(int[] A){
        for(int i=0;i<A.length;i++)
            A[i] = readInt();
    }

    public long readLong() {
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
        }
        while (!isSpaceChar(c));
        return res * sgn;
    }

    public void readLong(long[] A){
        for(int i=0;i<A.length;i++)
            A[i] = readLong();
    }

    public double readDouble() {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        int sgn = 1;
        if (c == '-') {
            sgn = -1;
            c = read();
        }
        double res = 0;
        while (!isSpaceChar(c) && c != '.') {
            if (c == 'e' || c == 'E')
                return res * Math.pow(10, readInt());
            if (c < '0' || c > '9')
                throw new InputMismatchException();
            res *= 10;
            res += c - '0';
            c = read();
        }
        if (c == '.') {
            c = read();
            double m = 1;
            while (!isSpaceChar(c)) {
                if (c == 'e' || c == 'E')
                    return res * Math.pow(10, readInt());
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                m /= 10;
                res += (c - '0') * m;
                c = read();
            }
        }
        return res * sgn;
    }

    public char[] readCharA(){
        return readString().toCharArray();
    }

    public String readString() {
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
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    public String next() {
        return readString();
    }

    public interface SpaceCharFilter {
        public boolean isSpaceChar(int ch);
    }

}