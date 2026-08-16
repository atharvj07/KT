/*
Permission to Dance!
Hobi Luv
<3
 */
import static java.lang.Math.*;
import static java.lang.System.out;
import java.util.*;
import java.io.*;
import java.math.*;

public class x1550E
{
    static final int INF = Integer.MAX_VALUE/5;
    public static void main(String hi[]) throws Exception
    {
        FastScanner infile = new FastScanner();
        int N = infile.nextInt();
        int K = infile.nextInt();
        char[] input = infile.nextLine().trim().toCharArray();
        int[] arr = new int[N];
        for(int i=0; i < N; i++)
        {
            if(input[i] == '?')
                arr[i] = -1;
            else
                arr[i] = input[i]-'a';
        }
        int low = 0;
        int high = N/K;
        while(low != high)
        {
            int mid = (low+high+1)>>1;
            int[][] right = new int[K][N];
            for(int c=0; c < K; c++)
            {
                Arrays.fill(right[c], INF);
                int tot = 0;
                for(int i=0; i < mid; i++)
                    if(arr[i] == c || arr[i] == -1)
                        tot++;
                if(tot == mid)
                    right[c][0] = mid;
                for(int i=mid; i < N; i++)
                {
                    if(arr[i-mid] == c || arr[i-mid] == -1)
                        tot--;
                    if(arr[i] == c || arr[i] == -1)
                        tot++;
                    if(tot == mid)
                        right[c][i-mid+1] = i+1;
                }
                for(int i=N-2; i >= 0; i--)
                    right[c][i] = min(right[c][i], right[c][i+1]);
            }
            int[] dp = new int[1<<K];
            Arrays.fill(dp, INF);
            dp[0] = 0;
            for(int mask=0; mask < 1<<K; mask++)
                if(dp[mask] < N)
                    for(int b=0; b < K; b++)
                        if((mask&(1<<b)) == 0)
                            dp[mask|(1<<b)] = min(dp[mask|(1<<b)], right[b][dp[mask]]);
            if(dp[(1<<K)-1] == INF)
                high = mid-1;
            else
                low = mid;
        }
        System.out.println(low);
    }
}
class FastScanner
{
    //I don't understand how this works lmao
    private int BS = 1 << 16;
    private char NC = (char) 0;
    private byte[] buf = new byte[BS];
    private int bId = 0, size = 0;
    private char c = NC;
    private double cnt = 1;
    private BufferedInputStream in;

    public FastScanner() {
        in = new BufferedInputStream(System.in, BS);
    }

    public FastScanner(String s) {
        try {
            in = new BufferedInputStream(new FileInputStream(new File(s)), BS);
        } catch (Exception e) {
            in = new BufferedInputStream(System.in, BS);
        }
    }

    private char getChar() {
        while (bId == size) {
            try {
                size = in.read(buf);
            } catch (Exception e) {
                return NC;
            }
            if (size == -1) return NC;
            bId = 0;
        }
        return (char) buf[bId++];
    }

    public int nextInt() {
        return (int) nextLong();
    }

    public int[] nextInts(int N) {
        int[] res = new int[N];
        for (int i = 0; i < N; i++) {
            res[i] = (int) nextLong();
        }
        return res;
    }

    public long[] nextLongs(int N) {
        long[] res = new long[N];
        for (int i = 0; i < N; i++) {
            res[i] = nextLong();
        }
        return res;
    }

    public long nextLong() {
        cnt = 1;
        boolean neg = false;
        if (c == NC) c = getChar();
        for (; (c < '0' || c > '9'); c = getChar()) {
            if (c == '-') neg = true;
        }
        long res = 0;
        for (; c >= '0' && c <= '9'; c = getChar()) {
            res = (res << 3) + (res << 1) + c - '0';
            cnt *= 10;
        }
        return neg ? -res : res;
    }

    public double nextDouble() {
        double cur = nextLong();
        return c != '.' ? cur : cur + nextLong() / cnt;
    }

    public double[] nextDoubles(int N) {
        double[] res = new double[N];
        for (int i = 0; i < N; i++) {
            res[i] = nextDouble();
        }
        return res;
    }

    public String next() {
        StringBuilder res = new StringBuilder();
        while (c <= 32) c = getChar();
        while (c > 32) {
            res.append(c);
            c = getChar();
        }
        return res.toString();
    }

    public String nextLine() {
        StringBuilder res = new StringBuilder();
        while (c <= 32) c = getChar();
        while (c != '\n') {
            res.append(c);
            c = getChar();
        }
        return res.toString();
    }

    public boolean hasNext() {
        if (c > 32) return true;
        while (true) {
            c = getChar();
            if (c == NC) return false;
            else if (c > 32) return true;
        }
    }
}