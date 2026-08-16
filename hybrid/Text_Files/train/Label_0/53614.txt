import java.io.*;
import java.util.*;

public class E2
{
    PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    // BufferedReader in;
    StringTokenizer tok;

    public void go() throws IOException
    {
        // long start = System.nanoTime();
        // in = new BufferedReader(new FileReader(new File("input.txt")));
        StringTokenizer tok = new StringTokenizer(in.readLine());
        int zzz = Integer.parseInt(tok.nextToken());
        for (int zz = 0; zz < zzz; zz++)
        {
            ntok();
            int n = ipar();
            int m = ipar();
            int[][] mat = new int[m][n+1];
            for (int i = 0; i < n; i++)
            {
                ntok();
                for (int e = 0; e < m; e++)
                {
                    mat[e][i] = ipar();
                }
            }
            for (int i = 0; i < m; i++)
            {
                for (int e = 0; e < n; e++)
                {
                    mat[i][n] = Math.max(mat[i][n], mat[i][e]);
                }
            }
            ArrayList<int[]> list = new ArrayList<>();
            for (int i = 0; i < m; i++)
            {
                list.add(mat[i]);
            }
            Collections.sort(list, (a, b) -> {
                return -Integer.compare(a[n], b[n]);
            });
            for (int i = 0; i < m; i++)
            {
                mat[i] = list.get(i);
            }
            m = Math.min(m, n);

            int[][] dp = new int[1 << n][m+1];
            for (int i = m-1; i >= 0; i--)
            {
                int[] temp = new int[1 << n];
                for (int r = 0; r < n; r++)
                {
                    for (int j = 0; j < 1 << n; j++)
                    {
                        temp[j] = dp[j][i+1];
                    }
                    for (int j = 0; j < n; j++)
                    {
                        int val = mat[i][(j+r)%n];
                        for (int k = 0; k < 1 << n; k++)
                        {
                            if ((k & (1 << j)) == 0)
                            {
                                temp[k | (1 << j)] = Math.max(temp[k | (1 << j)], temp[k] + val);
                            }
                        }
                    }
                    for (int j = 0; j < 1 << n; j++)
                    {
                        dp[j][i] = Math.max(dp[j][i], temp[j]);
                    }
                }
            }
            out.println(dp[(1 << n) - 1][0]);

            // int[][] best = new int[1 << n][m];
            // for (int i = 0; i < 1 << n; i++)
            // {
            //     for (int e = 0; e < m; e++)
            //     {
            //         best[i][e] = best(i, mat, e);
            //     }
            // }
            // int[][] dp = new int[1 << n][m+1];
            // for (int i = 0; i < 1 << n; i++)
            // {
            //     dp[i][m] = -1000000000;
            // }
            // dp[(1 << n) - 1][m] = 0;
            // for (int i = m-1; i >= 0; i--)
            // {
            //     for (int e = 0; e < 1 << n; e++)
            //     {
            //         dp[e][i] = dp[e][i+1];
            //         int opposite = ~e & ((1 << n) - 1);
            //         for (int w = opposite; w != 0; w = (w-1) & opposite)
            //         {
            //             dp[e][i] = Math.max(dp[e][i], best[w][i] + dp[e|w][i+1]);
            //         }
            //     }
            // }
            // out.println(dp[0][0]);
        }
        // out.printf("%.3f%n", (System.nanoTime() - start) / 1000000.0);

        out.flush();
        in.close();
    }

    public int best(int mask, int[][] mat, int col)
    {
        int max = 0;
        for (int t = 0; t < mat[0].length-1; t++)
        {
            int sum = 0;
            int mk = mask;
            for (int i = 0; i < mat[0].length-1; i++)
            {
                if (mk % 2 == 1)
                {
                    sum += mat[col][(i+t)%(mat[0].length-1)];
                }
                mk /= 2;
            }
            max = Math.max(max, sum);
        }
        return max;
    }

    public void cycle(int[][] mat, int col)
    {
        int temp = mat[col][0];
        for (int i = 0; i < mat[0].length-2; i++)
        {
            mat[col][i] = mat[col][i+1];
        }
        mat[col][mat[0].length-2] = temp;
    }

    public void ntok() throws IOException
    {
        tok = new StringTokenizer(in.readLine());
    }

    public int ipar()
    {
        return Integer.parseInt(tok.nextToken());
    }

    public int[] iapar(int n)
    {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
        {
            arr[i] = ipar();
        }
        return arr;
    }

    public long lpar()
    {
        return Long.parseLong(tok.nextToken());
    }

    public long[] lapar(int n)
    {
        long[] arr = new long[n];
        for (int i = 0; i < n; i++)
        {
            arr[i] = lpar();
        }
        return arr;
    }

    public double dpar()
    {
        return Double.parseDouble(tok.nextToken());
    }

    public String spar()
    {
        return tok.nextToken();
    }

    public static void main(String[] args) throws IOException
    {
        new E2().go();
    }
}
