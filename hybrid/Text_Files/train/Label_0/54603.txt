/*
    Aman Agarwal
    algo.java
*/

import java.util.*;
import java.io.*;

public class C1167
{
    static class FastReader
    {
            BufferedReader br;
            StringTokenizer st;

            public FastReader()
            {
                br = new BufferedReader(new InputStreamReader(System.in));
            }

            String next()
            {
                while (st == null || !st.hasMoreElements())
                {
                    try
                    {
                        st = new StringTokenizer(br.readLine());
                    }
                    catch (IOException  e)
                    {
                        e.printStackTrace();
                    }
                }
                return st.nextToken();
            }

            int nextInt()
            {
                return Integer.parseInt(next());
            }

            long nextLong()
            {
                return Long.parseLong(next());
            }

            double nextDouble()
            {
                return Double.parseDouble(next());
            }

            String nextLine()
            {
                String str = "";
                try
                {
                    str = br.readLine();
                }
                catch (IOException e)
                {
                    e.printStackTrace();
                }
                return str;
            }
    }


    static FastReader sc = new FastReader();
    static PrintWriter out = new PrintWriter(System.out);
    static int rank[];

    static int find(int i)
    {
        if(rank[i]<0)
            return i;
        rank[i] = find(rank[i]);
        return rank[i];
    }

    static void join(int i,int j)
    {
        i = find(i);
        j = find(j);
        if(i==j)
            return;

        if(rank[i] > rank[j])
        {
            rank[j] += rank[i];
            rank[i] = j;
        }
        else
        {
            rank[i] +=rank[j];
            rank[j] = i;
        }
    }

    public static void main(String[] args) 
    {
        int t = 1;
        //t = sc.nextInt();
        while(t-- > 0)
        {
            int n = sc.nextInt();
            int m = sc.nextInt();
            rank = new int[n];
            Arrays.fill(rank,-1);

            while(m-- > 0)
            {
                int k = sc.nextInt();
                for(int h=0,i=0;h<k;h++)
                {
                    int j = sc.nextInt()-1;
                    if(h>0)
                        join(i,j);
                    i = j;
                }
            }

            for(int i=0;i<n;i++)
                System.out.print(-rank[find(i)]+" ");
            //out.flush();
        }    
    }
}
