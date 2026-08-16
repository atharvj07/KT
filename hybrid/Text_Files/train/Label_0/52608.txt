import java.io.*;
import java.util.*;

public class D
{
    PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer tok;
    HashMap<List<Long>, Long> map = new HashMap<>();

    public void go() throws IOException
    {
        StringTokenizer tok = new StringTokenizer(in.readLine());
        int zzz = Integer.parseInt(tok.nextToken());
        for (int zz = 0; zz < zzz; zz++)
        {
            ntok();
            long n = lpar();
            long l = lpar()-1;
            long r = lpar()-1;
            for (long i = l; i <= r; i++) {
                out.print(getIndex2(n, i));
                out.print(' ');
            }
            out.println();
            // for (long i = 0; i <= n*(n-1); i++) {
            //     if (getIndex(n, i) != getIndex2(n, i)) {
            //         out.println("WRONG " + i);
            //         break;
            //     }
            // }
            // for (long i = 0; i <= n*(n-1); i++) {
            //     out.print(getIndex(n, i));
            //     out.print(' ');
            // }
            // out.println();
            // for (long i = 0; i <= n*(n-1); i++) {
            //     out.print(getIndex2(n, i));
            //     out.print(' ');
            // }
            // out.println();
            // printOrder((int)n);
        }

        out.flush();
        in.close();
    }

    public void printOrder(int n) {
        boolean[][] mat = new boolean[n][n];
        for (boolean[] arr : mat) {
            Arrays.fill(arr, true);
        }
        for (int i = 0; i < n; i++) {
            mat[i][i] = false;
        }
        int curr = 0;
        out.print('1');
        for (int i = 0; i < n*(n-1); i++) {
            for (int e = 0; e < n; e++) {
                if (mat[curr][e]) {
                    mat[curr][e] = false;
                    curr = e;
                    break;
                }
            }
            out.print(' ');
            out.print(curr+1);
        }
        out.println();
    }

    public long getIndex2(long n, long i) {
        List<Long> pair = new ArrayList<>();
        pair.add(n);
        pair.add(i);
        if (map.containsKey(pair)) {
            return map.get(pair);
        }
        long ans;
        if (i < (n-1)*2) {
            ans = i % 2 == 0 ? 1 : i/2+2;
        } else if (i == n*(n-1)-1) {
            ans = n;
        } else if (i == n*(n-1)) {
            ans = 1;
        } else {
            long l = 1;
            long r = n-1;
            while (r > l+1) {
                long mid = (r+l)/2;
                long minus = 2 * ((n*(n-1)/2) - ((n-mid)*(n-mid-1)/2));
                if (minus > i) {
                    r = mid - 1;
                } else {
                    l = mid;
                }
            }
            long minus = 2 * ((n*(n-1)/2) - ((n-l)*(n-l-1)/2));
            ans = getIndex2(n-l, i - minus) + l;
        }
        map.put(pair, ans);
        return ans;
    }

    public long getIndex(long n, long i) {
        List<Long> pair = new ArrayList<>();
        pair.add(n);
        pair.add(i);
        if (map.containsKey(pair)) {
            return map.get(pair);
        }
        long ans;
        if (i < (n-1)*2) {
            ans = i % 2 == 0 ? 1 : i/2+2;
        } else if (i == n*(n-1)-1) {
            ans = n;
        } else if (i == n*(n-1)) {
            ans = 1;
        } else {
            // long l = 1;
            // long r = n;
            // while (r > l+1) {
            //     long mid = (r+l)/2;
            //     long minus = 2 * ((n*(n-1)/2) - ((n-mid)*(n-mid-1)/2));
            //     if (minus > i) {
            //         r = mid - 1;
            //     } else {
            //         l = mid;
            //     }
            // }
            // long minus = 2 * ((n*(n-1)/2) - ((n-l)*(n-l-1)/2));
            // ans = getIndex(n-1, i - minus) + l;
            ans = getIndex(n-1, i - (n-1)*2) + 1;
        }
        map.put(pair, ans);
        return ans;
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
        new D().go();
    }
}
