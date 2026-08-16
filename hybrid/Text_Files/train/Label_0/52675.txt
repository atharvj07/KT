
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Andy Phan
 */
public class i {
    static int MAX = 6;
    static long MOD = 1_000_000_007;
    public static void main(String[] args) {
        FS in = new FS(System.in);
        PrintWriter out = new PrintWriter(System.out);
        
//        StringBuilder tmp = new StringBuilder();
//        for(int i = 0; i < 125000; i++) tmp.append('a');
//        tmp.append('\n');
//        for(int i = 0; i < 125000; i++) tmp.append('a');
//        tmp.append('\n');
//        
//        Scanner in = new Scanner(tmp.toString());
        
        char[] s = in.next().toCharArray();
        char[] t = new StringBuilder(in.next()).reverse().toString().toCharArray();
        long[][] sA = new long[MAX][s.length];
        long[][] tA = new long[MAX][t.length];
        for(int i = 0; i < MAX; i++) {
            for(int j = 0; j < s.length; j++) {
                if(s[j] == i+'a') sA[i][j] = 1;
            }
        }
        for(int i = 0; i < MAX; i++) {
            for(int j = 0; j < t.length; j++) {
                if(t[j] == i+'a') tA[i][j] = 1;
            }
        }
        
        long[][][] convs = new long[MAX][MAX][];
        for(int i = 0; i < MAX; i++) for(int j = 0; j < MAX; j++) convs[i][j] = FFT.multiply(sA[i], tA[j]);
        
        for(int i = t.length-1; i < s.length; i++) {
            int num = 0;
            DSU dsu = new DSU(MAX);
            for(int j = 0; j < MAX; j++) {
                for(int k = 0; k < MAX; k++) {
                    if(convs[j][k][i] > 0) {
                        if(dsu.merge(j, k)) {
                            num++;
                        }
                    }
                }
            }
            out.println(num);
        }
        
        out.close();
    }
    
    static class DSU {
        int[] p;
        
        public DSU(int n) {
            p = new int[n];
            Arrays.fill(p, -1);
        }
        
        public int par(int i) {
            return p[i] < 0 ? i : (p[i] = par(p[i]));
        }
        
        public boolean merge(int a, int b) {
            a = par(a);
            b = par(b);
            if(a == b) return false;
            if(p[a] == p[b]) p[a]--;
            if(p[a] < p[b]) {
                p[b] = a;
            } else {
                p[a] = b;
            }
            return true;
        }
    }
    
    // SET maxk appropriately!!! ~log(maxn) //%
    static class FFT {

        static final int maxk = 19, maxn = (1 << maxk) + 1;
        // Init: wR, wI, rR, rI, aR, aI   to   new double[maxn] !!!
        //#
        static double[] wR = new double[maxn],
            wI = new double[maxn],
            rR = new double[maxn],
            rI = new double[maxn],
            aR = new double[maxn],
            aI = new double[maxn]; //$
        static int n, k, lastk = -1, dp[] = new int[maxn];

        static void fft(boolean inv) {
            if (lastk != k) {
                lastk = k;
                dp[0] = 0;
                for (int i = 1, g = -1; i < n; i++) {
                    if ((i & (i - 1)) == 0) {
                        g++;
                    }
                    dp[i] = dp[i ^ (1 << g)] ^ (1 << (k - 1 - g));
                }
                wR[1] = 1;
                wI[1] = 0;
                for (int t = 0; t < k - 1; t++) {
                    double a = Math.PI / n * (1 << (k - 1 - t));
                    double curR = Math.cos(a), curI = Math.sin(a);
                    int p2 = (1 << t), p3 = p2 * 2;
                    for (int j = p2, k = j * 2; j < p3; j++, k += 2) {
                        wR[k] = wR[j];
                        wI[k] = wI[j];
                        wR[k + 1] = wR[j] * curR - wI[j] * curI;
                        wI[k + 1] = wR[j] * curI + wI[j] * curR;
                    }
                }
            }
            for (int i = 0; i < n; i++) {
                int d = dp[i];
                if (i < d) {
                    double tmp = aR[i];
                    aR[i] = aR[d];
                    aR[d] = tmp;
                    tmp = aI[i];
                    aI[i] = aI[d];
                    aI[d] = tmp;
                }
            }
            if (inv) {
                for (int i = 0; i < n; i++) {
                    aI[i] = -aI[i];
                }
            }
            for (int len = 1; len < n; len <<= 1) {
                for (int i = 0; i < n; i += len) {
                    int wit = len;
                    for (int it = 0, j = i + len; it < len; it++, i++, j++) {
                        double tmpR = aR[j] * wR[wit] - aI[j] * wI[wit];
                        double tmpI = aR[j] * wI[wit] + aI[j] * wR[wit];
                        wit++;
                        aR[j] = aR[i] - tmpR;
                        aI[j] = aI[i] - tmpI;
                        aR[i] += tmpR;
                        aI[i] += tmpI;
                    }
                }
            }
        }

        static long[] multiply(long[] a, long[] b) {
            int na = a.length, nb = b.length;
            for (k = 0, n = 1; n < na + nb - 1; n <<= 1, k++) {
            }
            for (int i = 0; i < n; ++i) {
                aR[i] = i < na ? a[i] : 0;
                aI[i] = i < nb ? b[i] : 0;
            }
            fft(false);
            aR[n] = aR[0];
            aI[n] = aI[0];
            double q = -1.0 / n / 4.0;
            for (int i = 0; i <= n - i; ++i) {
                double tmpR = aR[i] * aR[i] - aI[i] * aI[i];
                double tmpI = aR[i] * aI[i] * 2;
                tmpR -= aR[n - i] * aR[n - i] - aI[n - i] * aI[n - i];
                tmpI -= aR[n - i] * aI[n - i] * -2;
                aR[i] = -tmpI * q;
                aI[i] = tmpR * q;
                aR[n - i] = aR[i];
                aI[n - i] = -aI[i];
            }
            fft(true);
            long[] ans = new long[n = na + nb - 1]; // ONLY MOD IF NEEDED
            for (int i = 0; i < n; i++) {
                ans[i] = Math.round(aR[i]) % MOD;
            }
            return ans;
        }

        static void fft2(double[][] xr, double[][] xi, boolean inv) {
            n = xr[0].length;
            k = Integer.numberOfTrailingZeros(n);
            for (int i = 0; i < xr.length; i++) {
                for (int j = 0; j < n; j++) {
                    aR[j] = xr[i][j];
                    aI[j] = xi[i][j];
                }
                fft(inv);
                for (int j = 0; j < n; j++) {
                    xr[i][j] = aR[j] / (inv ? n : 1);
                    xi[i][j] = aI[j] / (inv ? -n : 1);
                }
            }
            n = xr.length;
            k = Integer.numberOfTrailingZeros(n);
            for (int j = 0; j < xr[0].length; j++) {
                for (int i = 0; i < n; i++) {
                    aR[i] = xr[i][j];
                    aI[i] = xi[i][j];
                }
                fft(inv);
                for (int i = 0; i < n; i++) {
                    xr[i][j] = aR[i] / (inv ? n : 1);
                    xi[i][j] = aI[i] / (inv ? -n : 1);
                }
            }
        }

        static long[][] multiply2(long[][] a, long[][] b) {
            int n1, n2;
            for (n1 = 1; n1 < a.length + b.length - 1; n1 <<= 1) {
            }
            for (n2 = 1; n2 < a[0].length + b[0].length - 1; n2 <<= 1) {
            }
            double[][] ar = new double[n1][n2], ai = new double[n1][n2];
            double[][] br = new double[n1][n2], bi = new double[n1][n2];
            for (int i = 0; i < a.length; i++) {
                for (int j = 0; j < a[i].length; j++) {
                    ar[i][j] = a[i][j];
                }
            }
            for (int i = 0; i < b.length; i++) {
                for (int j = 0; j < b[i].length; j++) {
                    br[i][j] = b[i][j];
                }
            }
            fft2(ar, ai, false);
            fft2(br, bi, false);
            for (int i = 0; i < n1; i++) {
                for (int j = 0; j < n2; j++) {
                    double r1 = ar[i][j], r2 = br[i][j];
                    double i1 = ai[i][j], i2 = bi[i][j];
                    double real = r1 * r2 - i1 * i2;
                    ai[i][j] = i1 * r2 + i2 * r1;
                    ar[i][j] = real;
                }
            }
            fft2(ar, ai, true);
            long[][] result = new long[n1 = a.length + b.length - 1][n2 = a[0].length + b[0].length - 1];
            for (int i = 0; i < n1; i++) {
                for (int j = 0; j < n2; j++) {
                    result[i][j] = Math.round(ar[i][j]);
                }
            }
            return result;
        }
        //#

        static long[] multiplyPrecise(long[] a, long[] b) {
            long k = (long) (Math.sqrt(MOD));
            long[] a1 = new long[a.length], a2 = new long[a.length];
            long[] b1 = new long[b.length], b2 = new long[b.length];
            for (int i = 0; i < a.length; i++) {
                a1[i] = a[i] % k;
                a2[i] = a[i] / k;
            }
            for (int i = 0; i < b.length; i++) {
                b1[i] = b[i] % k;
                b2[i] = b[i] / k;
            }
            long[] r11 = multiply(a1, b1), r12 = multiply(a1, b2), r21 = multiply(a2, b1), r22 = multiply(a2, b2);
            long[] res = new long[r11.length];
            for (int i = 0; i < res.length; i++) {
                res[i] = (k * k * r22[i] + k * (r12[i] + r21[i]) + r11[i]) % MOD;
            }
            return res;
        }
        //$
        //#

        static long[] multiplyOr(long[] eq1, long[] eq2) {
            int n = Math.max(eq1.length, eq2.length);
            if ((n & (n - 1)) != 0) {
                n = Integer.highestOneBit(n) * 2;
            }
            eq1 = fftOr(eq1, n, false);
            eq2 = fftOr(eq2, n, false);
            for (int i = 0; i < eq1.length; i++) {
                eq1[i] *= eq2[i];
            }
            eq1 = fftOr(eq1, n, true);
            return eq1;
        }
        //$
        // To use: FFT both, product, iFFT (n is next power of 2)

        static long[] fftOr(long[] arr, int n, boolean invert) {
            long[] ans = Arrays.copyOf(arr, n);
            for (int b = 1; b < n; b <<= 1) {
                for (int i = 0; i < n; i++) {
                    if ((i & b) != 0) {
                        continue;
                    }
                    ans[i + b] += invert ? -ans[i] : ans[i];
                }
            }
            return ans;
        }

        static long[] fftXor(long[] arr, int n, boolean invert) {
            long[] ans = Arrays.copyOf(arr, n);
            for (int b = 1; b < n; b <<= 1) {
                for (int i = 0; i < n; i++) {
                    if ((i & b) != 0) {
                        continue;
                    }
                    long u = ans[i], v = ans[i + b];
                    ans[i] = u + v;
                    ans[i + b] = u - v;
                }
            }
            if (invert) {
                for (int i = 0; i < n; i++) {
                    ans[i] /= n;
                }
            }
            return ans;
        }
    }
    
    static class FS {

        BufferedReader in;
        StringTokenizer token;
        
        public FS(InputStream str) {
            in = new BufferedReader(new InputStreamReader(str));
        }
        
        public String next() {
            if (token == null || !token.hasMoreElements()) {
                try {
                    token = new StringTokenizer(in.readLine());
                } catch (IOException ex) {
                }
                return next();
            }
            return token.nextToken();
        }
        
        public int nextInt() {
            return Integer.parseInt(next());
        }
    }
}
