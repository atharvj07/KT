import java.util.*;
import java.io.*;
public class Main
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
    public static int gcd(int a,int b)
    {
        if(b%a==0)
        return a;
        return gcd(b%a,a);
    }
    public static void main(String args[])
    {
        FastReader fs=new FastReader();
        PrintWriter pw=new PrintWriter(System.out);
        int n=fs.nextInt();
        int p=fs.nextInt();
        int ans=-1;
        for(int i=0;i<=30;i++)
        {
            int rem=n-i*p;
            if(rem<0)
            break;
            int cnt=0;
            long set=0;
            for(int j=0;j<=30;j++)
            {
                if(((rem>>j)&1)==1)
                {
                    cnt++;
                    set+=(1L<<j);
                }
            }
            //pw.println(cnt+" "+set);
            if(cnt==i)
            {
                ans=i;
                break;
            }
            if(cnt<i&&set>=i)
            {
                ans=i;
                break;
            }
        }
        if(p>=n)
        ans=-1;
        pw.println(ans);
        pw.flush();
        pw.close();
    }
}