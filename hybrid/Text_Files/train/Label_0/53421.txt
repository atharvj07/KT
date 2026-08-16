import javafx.util.*;
import java.util.*;
import java.io.*;
import java.math.*;

public class Test5 {

    Random rnd = new Random();
    PrintWriter pw = new PrintWriter(System.out);
    static int[] n;

    void run() {
        long a = ni(), c, k, dcnt=0;
        int[] d = new int[60];
        n = new int[(int)a];
        for(int q=0; q<a; q++) n[q] = q;
        long[] otv = new long[(int)a+1];
        d[1] = 1;
        for(int q=2; q<60; q++){
            int i=q;
            boolean nonsq=true;
            for(int w=2; w*w<=q; w++){
                if(i%w<1){
                    for(;i%w<1;dcnt++) i/=w;
                    d[q]++;
                    if(dcnt>1) nonsq = false;
                    dcnt=0;
                }
            }
            if(!nonsq) d[q] = 0;
            else {
                if (i > 1 && d[q] > -1) d[q]++;
                if (d[q] > -1) {
                    if (d[q] % 2 == 0) d[q] = 1;
                    else d[q] = -1;
                }
            }
        }
        long[] num = new long[(int)a];
        for(int q=0; q<a; q++) num[q] = nl();
        PyraSort.sort(num);
        long[] sq = new long[60];
        for(int q=2; q<60; q++){
            sq[q] = getRoot(BigDecimal.valueOf(1e18), q, 3);
        }
        for(int q=(int)a-1; q>=0; q--){
            c = num[q];
            long ans = c-1;
            sq[2] = (int)Math.sqrt(c);
            if(!(sq[2]*sq[2]<=c && (sq[2]+1)*(sq[2]+1)>c)){
                for(;!(sq[2]*sq[2]<=c && (sq[2]+1)*(sq[2]+1)>c);){
                    if(sq[2]*sq[2]>c) sq[2]--;
                    else if(sq[2]*sq[2]!=c) sq[2]++;
                }
            }
            for(int w=3; w<60; w++){
                for(;;) {
                    if (binpow(sq[w], w) <= c) break;
                    sq[w]--;
                }
            }
            for(int w=2; w<60; w++){
                k = sq[w]-1;
                ans+=k*d[w];
            }
            otv[n[q]] = ans;
        }
        for(int q=0; q<a; q++) pw.println(otv[q]);
        pw.flush();
    }

    long binpow(long o, int pow){
        if(pow==0) return 1;
        if(pow==1) return o;
        if(pow%2==0) return binpow(o*o, pow>>1);
        else return o*binpow(o*o, pow>>1);
    }

    static class PyraSort {

        private static int heapSize;

        public static void sort(long[] a) {
            buildHeap(a);
            while (heapSize > 1) {
                swap(a, 0, heapSize - 1);
                heapSize--;
                heapify(a, 0);
            }
        }

        private static void buildHeap(long[] a) {
            heapSize = a.length;
            for (int i = a.length / 2; i >= 0; i--) {
                heapify(a, i);
            }
        }

        private static void heapify(long[] a, int i) {
            int l = 2 * i + 2;
            int r = 2 * i + 1;
            int largest = i;
            if (l < heapSize && a[i] < a[l]) {
                largest = l;
            }
            if (r < heapSize && a[largest] < a[r]) {
                largest = r;
            }
            if (i != largest) {
                swap(a, i, largest);
                heapify(a, largest);
            }
        }

        private static void swap(long[] a, int i, int j) {
            a[i] ^= a[j] ^= a[i];
            a[j] ^= a[i];
            n[i] ^= n[j] ^= n[i];
            n[j] ^= n[i];
        }
    }

    long getRoot(BigDecimal num, int pow, int sc){
        BigDecimal scale = BigDecimal.valueOf(0.1).pow(sc), x, xk = BigDecimal.TEN;
        for(;;){
            x = (xk.multiply(BigDecimal.valueOf(pow-1)).add(num.divide(xk.pow(pow-1), sc+1, BigDecimal.ROUND_FLOOR))).divide(BigDecimal.valueOf(pow), sc+1, BigDecimal.ROUND_FLOOR);
            if(scale.compareTo(x.subtract(xk).abs())>0) break;
            xk = x;
        }
        return x.divide(BigDecimal.ONE, BigDecimal.ROUND_FLOOR).longValue();
    }

    public static void main(String[] args) {
        new Test5().run();
    }

    InputStream is = System.in;
    private byte[] inbuf = new byte[1024];
    public int lenbuf = 0, ptrbuf = 0;

    private int readByte() {
        if (lenbuf == -1) throw new InputMismatchException();
        if (ptrbuf >= lenbuf) {
            ptrbuf = 0;
            try {
                lenbuf = is.read(inbuf);
            } catch (IOException e) {
                throw new InputMismatchException();
            }
            if (lenbuf <= 0) return -1;
        }
        return inbuf[ptrbuf++];
    }

    private boolean isSpaceChar(int c) {
        return !(c >= 33 && c <= 126);
    }

    private int skip() {
        int b;
        while ((b = readByte()) != -1 && isSpaceChar(b)) ;
        return b;
    }

    private double nd() {
        return Double.parseDouble(ns());
    }

    private char nc() {
        return (char) skip();
    }

    private String ns() {
        int b = skip();
        StringBuilder sb = new StringBuilder();
        while (!(isSpaceChar(b))) {
            sb.appendCodePoint(b);
            b = readByte();
        }
        return sb.toString();
    }

    private char[] ns(int n) {
        char[] buf = new char[n];
        int b = skip(), p = 0;
        while (p < n && !(isSpaceChar(b))) {
            buf[p++] = (char) b;
            b = readByte();
        }
        return n == p ? buf : Arrays.copyOf(buf, p);
    }

    private char[][] nm(int n, int m) {
        char[][] map = new char[n][];
        for (int i = 0; i < n; i++) map[i] = ns(m);
        return map;
    }

    private int[] na(int n) {
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = ni();
        return a;
    }

    private int ni() {
        int num = 0, b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        while (true) {
            if (b >= '0' && b <= '9') {
                num = num * 10 + (b - '0');
            } else {
                return minus ? -num : num;
            }
            b = readByte();
        }
    }

    private long nl() {
        long num = 0;
        int b;
        boolean minus = false;
        while ((b = readByte()) != -1 && !((b >= '0' && b <= '9') || b == '-')) ;
        if (b == '-') {
            minus = true;
            b = readByte();
        }
        while (true) {
            if (b >= '0' && b <= '9') {
                num = num * 10 + (b - '0');
            } else {
                return minus ? -num : num;
            }
            b = readByte();
        }
    }
}

class Para{

    String t;
    int i;

    Para(String a, int b){
        t = a;
        i = b;
    }

}
