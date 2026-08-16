import java.io.PrintWriter;
import java.util.Scanner;

public class E {

    static int n;
    static int all;
    static long collectedTime;
    static int cacheSize;

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        n = in.nextInt();
        all = (1 << n) - 1;
        int m = in.nextInt();
        cacheSize = 1 << (Math.max(n - 2, 0));
        int cache[][] = new int[cacheSize][n];
        int b[] = cache[0];

        PrintWriter out = new PrintWriter(System.out);

        for (int i = 0; i < n; i++) {
            b[i] = (1 << i);
        }
        for (int i = 0; i < m; i++){
            int x = in.nextInt() - 1;
            int y = in.nextInt() - 1;
            b[y] = b[y] | (1 << x);
            b[x] = b[x] | (1 << y);
        }
        long start = System.nanoTime();

        if (checkIsDone(b)) {
            out.print(0);
            out.close();
            return;
        }
        int min = -1;
        int mj = 0;
        int c[] = new int[n];
        int old[];
        int newA[];

        for (int i = 0; i < n; i++) {
            int k = 1 << i;
            for (int j = 0; j < k; j++) {
                int nj = j | k;
                int ones = getOnes(nj);
                if (min > -1 && ones > min) {
                    continue;
                }
                if (j == 0) {
                    old = b;
                } else if (j < cacheSize) {
                    old = cache[j];
                } else {
                    old = cache[j & (cacheSize - 1)];
                }

                if (nj < cacheSize) {
                    newA = cache[nj];
                } else {
                    newA = c;
                }
                if (mult(newA, old, nj, j, i)) {
                    if (min == -1 || ones < min) {
                        min = ones;
                        mj = nj;
                    }
                }
            }
        }
        out.println(min);
        int i = 0;
        while (mj > 0) {
            if ((mj & 1) == 1) {
                out.print(1 + i);
                if (--min > 0) {
                    out.print(" ");
                }
            }
            i++;
            mj = mj >>> 1;
        }
        //out.println("tottime : " + (System.nanoTime() - start));
       //out.println("collected : " + (collectedTime));
        out.close();
    }

    private static int getOnes(int nj) {
        int q = 0;
        while (nj > 0) {
            if ((nj & 1) != 0) {
                q++;
            }
            nj = nj >>> 1;
        }
        return q;
    }

    private static boolean mult(int[] b1, int[] b0, int nj, int oldj, int newi) {
        for (int j = 0; j < n; j++) {
            b1[j] = b0[j];
        }
        //long start = System.nanoTime();

        int t = nj;
        int i = 0;
        if (oldj > 0) {
            if ( oldj < cacheSize) {
                t = t >>> (newi);
                i = newi;
            } else {
                t = t >>> (n - 2);
                i = n - 2;
            }
        }
        while (t > 0) {
            if ((t & 1) > 0) {
                int mask = b1[i];

                for (int x = 0; x < n; x++) {
                    if ((mask & (1 << x)) != 0) {
                        b1[x] = b1[x] | mask;
                    }
                }
            }
            i++;
            t = t >>> 1;
        }
        //collectedTime += (System.nanoTime() - start);
        return checkIsDone(b1);
    }

    private static boolean checkIsDone(int[] b1) {
        for (int j = 0; j < n; j++) {
            if (b1[j] != all) {
                return false;
            }
        }
        return true;
    }

}
