import java.io.*;
import java.util.*;

public class E
{
    private static final int oo = 1000000000;
    public static void main(String[] args) throws Exception
    {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        if(n > m)
        {
            int t = n;
            n = m;
            m = t;
        }

        int [][] curr = new int[1<<n][1<<n];
        fill(curr, oo);
        Arrays.fill(curr[0], 0);

        for(int j = 0 ; j < m ; j++)
        {
            int [][] next = new int[1<<n][1<<n];
            fill(next, oo);
            for(int c0 = 0 ; c0 < 1<<n ; c0++)
                for(int c1 = 0 ; c1 < 1<<n ; c1++)
                    if(curr[c0][c1] != oo)
                        for(int c2 = 0 ; c2 < (j == m-1 ? 1 : 1<<n) ; c2++)
                        {
                            int all = (1<<n) - 1;
                            int done = (all&(c1>>1)) | (all&(c1<<1)) | c0 | c2;
                            done &= (all^c1);

                            next[c1][c2] = Math.min(next[c1][c2], curr[c0][c1] + n - Integer.bitCount(done));

                        }
            curr = next;
        }

        int res = oo;
        for(int i = 0 ; i < 1<<n ; i++)
            for(int j = 0 ; j < 1<<n ; j++)
                res = Math.min(res, curr[i][j]);

        System.out.println(n*m - res);
    }

    private static void fill(int[][] array, int val)
    {
        for(int [] fill : array)
            Arrays.fill(fill, val);
    }
}