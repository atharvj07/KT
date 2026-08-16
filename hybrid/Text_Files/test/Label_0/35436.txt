// package com.company.codeforces;


import java.io.*;
import java.util.*;

public class Solution {
    static ArrayList<Integer> tree[];
    static int in[],low[],timer=0,vis[];
    static PrintWriter pw = new PrintWriter(System.out);
    static class Pair{
        int x;
        int y;
        Pair(int a,int b){
            x=a;
            y=b;
        }
    }
    static ArrayList<Pair> res;


    public static void main(String[] args) {
        FastReader input=new FastReader();

            int n=input.nextInt();
            int m=input.nextInt();
            tree=new ArrayList[n+1];
            vis=new int[n+1];
            in=new int[n+1];
            low=new int[n+1];
            res=new ArrayList<>();

            for (int i = 0; i <=n ; i++) {
                tree[i]=new ArrayList<>();
            }

            for (int i = 0; i <m ; i++) {
                int x=input.nextInt();
                int y=input.nextInt();
                tree[x].add(y);
                tree[y].add(x);
            }
            dfs(1,0);

            if (!hasbridge) {
                for (Pair p : res) {
                    pw.println(p.x + " " + p.y);
                }
            }else {
                pw.println(0);
            }
            pw.flush();
            pw.close();
        }

   static boolean hasbridge=false;

    private static void dfs(int root, int par) {
        in[root]=low[root]=timer++;
        vis[root]=1;
        for (int child:tree[root]) {
            if (child==par) continue;
            if (vis[child]==1){
                low[root]=Math.min(in[child],low[root]);
//                System.out.println(low[child]);
                if (in[root]>in[child])
                 res.add(new Pair(root,child));
            }else {
                dfs(child,root);
                low[root]=Math.min(low[child],low[root]);
                if (low[child]>in[root]){
//                    System.out.println(root+""+child);
                    hasbridge=true;
                }
                res.add(new Pair(root,child));

            }

        }

    }
    static class FastReader
    {
        BufferedReader br;
        StringTokenizer st;

        public FastReader()
        {
            br = new BufferedReader(new
                    InputStreamReader(System.in));
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


}
