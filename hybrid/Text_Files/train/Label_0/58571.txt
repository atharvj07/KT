import java.io.BufferedInputStream;
import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
    public int mod = 1000000000 + 7;

    public void work() {
        Scanner cin = new Scanner(new BufferedInputStream(System.in));
        PrintWriter out = new PrintWriter(System.out);
        int n, K;
        n = cin.nextInt();
        K = cin.nextInt();
        int w, w50, w100;
        w50 = w100 = 0;
        for (int i = 0; i < n; ++i) {
            w = cin.nextInt();
            if (w == 50)
                ++w50;
            else
                ++w100;
        }
        int c[][] = new int[51][51];
        for (int i = 0; i <= 50; ++i) {
            c[i][i] = c[i][0] = 1;
            for (int j = 1; j < i; ++j)
                c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod;
        }
        int d[][][] = new int[1001][w50 + 1][w100 + 1];
        d[0][w50][w100] = 1;
        int ans = -1;
        for (int i = 0; i < 1000 && ans == -1; ++i)
            for (int j = 0; j <= w50 && ans == -1; ++j)
                for (int k = 0; k <= w100 && ans == -1; ++k)
                    if (d[i][j][k] > 0) {
                        if (i % 2 == 0) {
                            for (int z = j; z >= 0 && ans == -1; --z) {
                                if ((j - z) * 50 > K)
                                    break;
                                for (int zz = k; zz >= 0 && ans == -1; --zz) {
                                    if ((j - z) * 50 + (k - zz) * 100 > K)
                                        break;
                                    if (z == 0 && zz == 0) {
                                        ans = i + 1;
                                        break;
                                    }
                                    d[i + 1][z][zz] = 1;
                                }
                            }
                        } else {
                            for (int z = j; z <= w50 && ans == -1; ++z) {
                                if ((z - j) * 50 > K)
                                    break;
                                for (int zz = k; zz <= w100 && ans == -1; ++zz) {
                                    if ((z - j) * 50 + (zz - k) * 100 > K)
                                        break;

                                    if (zz == k && j == z)
                                        continue;
                                    d[i + 1][z][zz] = 1;
                                }
                            }
                        }
                    }
        out.println(ans);
        if (ans == -1)
            out.println(0);
        else {
            for (int i = 0; i < ans; ++i)
                for (int j = 0; j <= w50; ++j)
                    for (int k = 0; k <= w100; ++k)
                        d[i][j][k] = 0;
            d[0][w50][w100] = 1;
            int v;
            for (int i = 0; i < ans; ++i)
                for (int j = 0; j <= w50; ++j)
                    for (int k = 0; k <= w100; ++k)
                        if (d[i][j][k] > 0) {
                            if (i % 2 == 0) {
                                for (int z = j; z >= 0; --z) {
                                    if ((j - z) * 50 > K)
                                        break;
                                    for (int zz = k; zz >= 0; --zz) {
                                        if ((j - z) * 50 + (k - zz) * 100 > K)
                                            break;
                                        v = (int)(((long)d[i][j][k] * c[j][j - z]) % mod);
                                        v = (int)(((long)v * c[k][k - zz]) % mod);
                                        d[i + 1][z][zz] += v;
                                        d[i + 1][z][zz] %= mod;
                                    }
                                }
                            } else {
                                for (int z = j; z <= w50; ++z) {
                                    if ((z - j) * 50 > K)
                                        break;
                                    for (int zz = k; zz <= w100; ++zz) {
                                        if ((z - j) * 50 + (zz - k) * 100 > K)
                                            break;

                                        if (zz == k && j == z)
                                            continue;
                                        v = (int)(((long)d[i][j][k] * c[w50 - j][z - j]) % mod);
                                        v = (int)(((long)v * c[w100 - k][zz - k]) % mod);
                                        d[i + 1][z][zz] += v;
                                        d[i + 1][z][zz] %= mod;
                                    }
                                }
                            }
                        }
            out.println(d[ans][0][0]);
        }
        out.close();
    }

    public static void main(String[] args) {
        Main e = new Main();
        e.work();
    }

}