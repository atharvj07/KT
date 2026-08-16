import java.awt.geom.Line2D;
import java.io.*;
import java.util.*;

public class C339D
{

private static StringTokenizer st;
    
    public static void nextLine(BufferedReader br) throws IOException
    {
        st = new StringTokenizer(br.readLine());
    }
    
    public static int nextInt()
    {
        return Integer.parseInt(st.nextToken());
    }
    
    public static String next()
    {
        return st.nextToken();
    }
    
    public static long nextLong()
    {
        return Long.parseLong(st.nextToken());
    }

    public static double nextDouble()
    {
        return Double.parseDouble(st.nextToken());
    }
    
    static int n;
    static Pair[] pairs;
    
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        nextLine(br);
        n = nextInt();
        long A = nextInt();
        long cf = nextInt();
        long cm = nextInt();
        long m = nextLong();
        nextLine(br);
        pairs = new Pair[n];
        for (int i = 0; i < n; i++)
        {
            pairs[i] = new Pair(i, nextLong());
        }
        Arrays.sort(pairs);
        // cost to perfect i skills
        long[] costf = new long[n + 1];
        costf[0] = 0;
        for (int i = 1; i <= n; i++)
        {
            costf[i] = costf[i-1] + (A - pairs[n-i].val);
        }
        // cost to bring bottom i-1 skills to the same level
        long[] costm = new long[n+1];
        costm[0] = 0;
        for (int i = 1; i < n; i++)
        {
            costm[i] = costm[i-1] + (pairs[i].val - pairs[i-1].val) * i;
        }
        long best = -1;
        int besti = -1;
        for (int i = 0; i <= n; i++)
        {
            if (costf[i] > m) break;
            long temp = bsearch(costm, m - costf[i], n-i, A);
            
            if (temp * cm + i * cf > best)
            {
                best = temp * cm + i * cf;
                besti = i;
            }
        }
        System.out.println(best);
        long temp = bsearch(costm, m - costf[besti], n-besti, A);
        long[] ans = new long[n];
        for (int i = 0; i < n-besti; i++)
        {
            if (pairs[i].val < temp) 
            {
                ans[pairs[i].index] = temp; 
            }
            else
            {
                ans[pairs[i].index] = pairs[i].val;
            }
        }
        for (int i = n-besti; i < n; i++)
        {
            ans[pairs[i].index] = A; 
        }
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < n; i++)
        {
            sb.append(ans[i] + " ");
        }
        System.out.println(sb.toString());
    }

    public static long bsearch(long[] cost, long v, int cap, long A)
    {
        if (cap == 0)
        {
            return A;
        }
        int left = 0;
        int right = cap-1;
        while (left < right)
        {
            int mid = (left + right + 1) / 2;
            if (cost[mid] > v)
            {
                right = mid - 1;
            }
            else
            {
                left = mid;
            }
        }
        long ans = pairs[left].val + (v - cost[left]) / (left + 1);
        
        return Math.min(ans, A);
    }
    
    static class Pair implements Comparable<Pair>
    {
        int index;
        long val;
        
        public Pair (int ind, long v)
        {
            index = ind; val = v;
        }
        
        @Override
        public int compareTo(Pair p)
        {
            return Long.valueOf(val).compareTo(p.val);
        }
    }
    
}