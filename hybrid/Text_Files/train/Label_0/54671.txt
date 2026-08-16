/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author dipankar12
 */
import java.io.*;
import java.util.*;
public class r466d {
    public static void main(String args[])
    {
        fastio in=new fastio(System.in);
        PrintWriter pw=new PrintWriter(System.out);

        int n=in.nextInt();
        int a[]=new int[n];
        int max=-1000000000,min=1000000000;
        for(int i=0;i<n;i++)
        {
            a[i]=in.nextInt();
            
        }
        
        String b=in.readString();
        for(int i=4;i<n;i++)
        {
            if(b.charAt(i)=='1'&&b.charAt(i-1)=='0'&&b.charAt(i-2)=='0'&&b.charAt(i-3)=='0'&&b.charAt(i-4)=='0')
            {
                int x=a[i-1];
                int y=a[i-2];
                int z=a[i-3];
                int p=a[i-4];
                int q=a[i];
                max=Math.max(max, Math.max(q, Math.max(p, Math.max(z, Math.max(y, x)))));
            }
            else if(b.charAt(i)=='0'&&b.charAt(i-1)=='1'&&b.charAt(i-2)=='1'&&b.charAt(i-3)=='1'&&b.charAt(i-4)=='1')
            {
                int x=a[i-1];
                int y=a[i-2];
                int z=a[i-3];
                int p=a[i-4];
                int q=a[i];
                min=Math.min(min, Math.min(q, Math.min(p, Math.min(z, Math.min(y, x)))));
            }
        }
        pw.println((max+1)+" "+(min-1));
        pw.close();
    }

    static class fastio {
     
            private final InputStream stream;
            private final byte[] buf = new byte[8192];
            private int cchar, snchar;
            private SpaceCharFilter filter;
     
            public fastio(InputStream stream) {
                this.stream = stream;
            }
     
            public int nxt() {
                if (snchar == -1)
                    throw new InputMismatchException();
                if (cchar >= snchar) {
                    cchar = 0;
                    try {
                        snchar = stream.read(buf);
                    } catch (IOException e) {
                        throw new InputMismatchException();
                    }
                    if (snchar <= 0)
                        return -1;
                }
                return buf[cchar++];
            }
     
            public int nextInt() {
                int c = nxt();
                while (isSpaceChar(c)) {
                    c = nxt();
                }
                int sgn = 1;
                if (c == '-') {
                    sgn = -1;
                    c = nxt();
                }
                int res = 0;
                do {
                    if (c < '0' || c > '9')
                        throw new InputMismatchException();
                    res *= 10;
                    res += c - '0';
                    c = nxt();
                } while (!isSpaceChar(c));
                return res * sgn;
            }
     
            public long nextLong() {
                int c = nxt();
                while (isSpaceChar(c)) {
                    c = nxt();
                }
                int sgn = 1;
                if (c == '-') {
                    sgn = -1;
                    c = nxt();
                }
                long res = 0;
                do {
                    if (c < '0' || c > '9')
                        throw new InputMismatchException();
                    res *= 10;
                    res += c - '0';
                    c = nxt();
                } while (!isSpaceChar(c));
                return res * sgn;
            }
     
            public int[] nextIntArray(int n) {
                int a[] = new int[n];
                for (int i = 0; i < n; i++) {
                    a[i] = nextInt();
                }
                return a;
            }
     
            public String readString() {
                int c = nxt();
                while (isSpaceChar(c)) {
                    c = nxt();
                }
                StringBuilder res = new StringBuilder();
                do {
                    res.appendCodePoint(c);
                    c = nxt();
                } while (!isSpaceChar(c));
                return res.toString();
            }
     
            public String nextLine() {
                int c = nxt();
                while (isSpaceChar(c))
                    c = nxt();
                StringBuilder res = new StringBuilder();
                do {
                    res.appendCodePoint(c);
                    c = nxt();
                } while (!isEndOfLine(c));
                return res.toString();
            }
     
            public boolean isSpaceChar(int c) {
                if (filter != null)
                    return filter.isSpaceChar(c);
                return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
            }
     
            private boolean isEndOfLine(int c) {
                return c == '\n' || c == '\r' || c == -1;
            }
     
            public interface SpaceCharFilter {
                public boolean isSpaceChar(int ch);
            }
        }
    

}
