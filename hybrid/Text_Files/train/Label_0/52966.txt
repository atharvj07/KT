import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BuytheString
{
    public static void main(String[] args)
    {
        FastReader sc = new FastReader();
        int t = sc.nextInt();
        while(t-->0)
        {
            int n ,c0,c1,h;
            n = sc.nextInt();
            c0 = sc.nextInt();
            c1 = sc.nextInt();
            h = sc.nextInt();
            String s = sc.next();
            long total = 0;
            for(int i = 0;i<n;i++)
            {
                char c = s.charAt(i);
                if(c=='0')
                    total+=c0;
                else
                    total+=c1;
            }
            System.out.println(solve(s,n,c0,c1,h));


//          if(c1>(c0+h))
//            {
//                long sum = 0l;
//
//                for(int i = 0;i<n && total>sum;i++)
//                {
//                    char     c = s.charAt(i);
//                    if(c=='1')
//                    {
//                        total-=c1;
//                        sum+=(h+c0);
//                    }
//                    else
//                    {
//                        sum+=c0;
//                        total-=c0;
//                    }
//
//
//                }
//                System.out.println(sum+total);
//
//
//
//
//
//                }
//            else if(c0>(c1+h))
//            {
//                long sum = 0l;
//
//                for(int i = 0;i<n && total>sum;i++)
//                {
//                    char     c = s.charAt(i);
//                    if(c=='0')
//                    {
//                        total-=c0;
//                        sum+=(h+c1);
//                    }
//                    else
//                    {
//                        sum+=c1;
//                        total-=c1;
//                    }
//
//
//                }
//                System.out.println(sum+total);
//
//            }
//            else
//              System.out.println(total);
//


        }

    }

    static  long solve(String s , int n,int c0,int c1,int h)
    {

        long total = 0l;
        for(int i = 0;i<n;i++)
        {
            char c = s.charAt(i);
            if(c=='0')
            {
                total+=min(c0,h+c1);
            }
            else
            {
                total+=min(c1,h+c0);
            }


        }

        return total;

    }
    static  long min(int a,int b)
    {
    return a<b?a:b;  }
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
