import java.util.*;
import java.io.*;
public class Solution
{
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
    static final long mod=(long)1e9+7;
    public static long pow(long a,int p)
    {
        long res=1;
        while(p>0)
        {
            if(p%2==1)
            {
                p--;
                res*=a;
                res%=mod;
            }
            else
            {
                a*=a;
                a%=mod;
                p/=2;
            }
        }
        return res;
    }
    // static class Pair
    // {
    //     int u,v;
    //     Pair(int u,int v)
    //     {
    //         this.u=u;
    //         this.v=v;
    //     }
    // }
    static class Pair implements Comparable<Pair>
    {
        int u;
        long v;
        Pair(int uu,long vv)
        {
            this.u=uu;
            this.v=vv;
        }
        public int compareTo(Pair p)
        {
            if(p.u!=u)
            return p.u-u;
            if(p.v<v)
            return 1;
            return -1;
        }
    }
    static long gcd(long a,long b)
    {
        if(b%a==0)
        return a;
        return gcd(b%a,a);
    }
    // public static class comp implements Comparator<Pair>
    // {
    //     public int compare(Pair p1,Pair p2)
    //     {
    //         if(p1.v>p2.v)
    //         return 1;
    //         return -1;
    //     }
    // }
    public static void dfs(int u,int dist[],ArrayList<Integer> edge[],boolean vis[])
    {
        vis[u]=true;
        for(int v:edge[u])
        {
            if(!vis[v])
            {
                dist[v]=dist[u]+1;
                dfs(v,dist,edge,vis);
            }
        }
    }
    static double c,m,p,v,ans;
    //static HashMap<Double,Integer> hmap=new HashMap<>();
    public static void recur(long c,long m,long p,long v,int cnt,double mul)
    {
        ans+=cnt*mul*(p/Math.pow(10,10));
        if(m==0&&c==0){
            return;
        }
        if(c>0)
        {
            if(c-v>0)
            {
                long newm,newp,newc=c-v;
                if(m==0)
                {
                    newm=0;
                    newp=p+v;
                }
                else
                {
                    newm=m+v/2;
                    newp=p+v/2;
                }
                recur(newc,newm,newp,v,cnt+1,mul*(c/Math.pow(10,10)));
            }
            else
            {
                long newm,newp;
                if(m==0)
                {
                    newm=0;
                    newp=p+c;
                }
                else
                {
                    newm=m+c/2;
                    newp=p+c/2;
                }
                recur(0,newm,newp,v,cnt+1,mul*(c/Math.pow(10,10)));
            }
        }
        if(m>0)
        {
            if(m-v>0)
            {
                long newc,newp,newm=m-v;
                if(c==0)
                {
                    newc=0;
                    newp=p+v;
                }
                else
                {
                    newc=c+v/2;
                    newp=p+v/2;
                }
                recur(newc,newm,newp,v,cnt+1,mul*(m/Math.pow(10,10)));
            }
            else
            {
                long newc,newp;
                if(c==0)
                {
                    newp=p+m;
                    newc=0;
                }
                else
                {
                    newc=c+m/2;
                    newp=p+m/2;
                }
                recur(newc,0,newp,v,cnt+1,mul*(m/Math.pow(10,10)));
            }
        }
    }
    public static void main(String args[])throws Exception
    {
        FastReader fs=new FastReader();
        PrintWriter pw=new PrintWriter(System.out);
        int tc=fs.nextInt();
        while(tc-->0)
        {
            ans=0;
            String str[]=fs.nextLine().split(" ");
            c=Double.parseDouble(str[0]);
            m=Double.parseDouble(str[1]);
            p=Double.parseDouble(str[2]);
            v=Double.parseDouble(str[3]);
            long cc=(long)(c*Math.pow(10,10));
            long mm=(long)(m*Math.pow(10,10));
            long pp=(long)(p*Math.pow(10,10));
            long vv=(long)(v*Math.pow(10,10));
            recur(cc,mm,pp,vv,1,1);
            pw.println(String.format("%.8f",ans));
        }
        pw.flush();
        pw.close();
    }
}