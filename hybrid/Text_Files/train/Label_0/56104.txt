import java.io.*;
import java.util.*;
public class Main {
    public static void main(String args[])
    {
        FastReader input=new FastReader();
        PrintWriter out=new PrintWriter(System.out);
        int T=input.nextInt();
        long arr[]=new long[10000001];
        for(int i=1;i<10000000;i++)
        {
            for(int j=i;j<=10000000;j+=i)
            {
                arr[j]+=i;
            }
        }
        int a[]=new int[10000001];
        for(int i=1;i<=10000000;i++)
        {
            long sum=arr[i];
            if(sum<=10000000)
            {
                if(a[(int)sum]==0)
                {
                    a[(int)sum]=i;
                }
            }
        }
        while(T-->0)
        {
            int c=input.nextInt();
            if(a[c]==0)
            {
                a[c]=-1;
            }
            out.println(a[c]);
        }
        out.close();
    }
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
                catch (IOException e)
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
            String str="";
            try
            {
                str=br.readLine();
            }
            catch (IOException e)
            {
                e.printStackTrace();
            }
            return str;
        }
    }
}