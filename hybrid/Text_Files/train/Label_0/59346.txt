import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B
{

    public static void main(String[] args)
    {
        MyScanner in = new MyScanner();

        int N = in.nextInt();

        int[] a = new int[N];
        int[] b = new int[N];

        boolean[] afinal = new boolean[N];
        boolean[] bfinal = new boolean[N];

        int kmax = N / 2;

        for (int i = 0; i < N; i++)
        {
            a[i] = in.nextInt();
            b[i] = in.nextInt();

        }

        for (int i = 0; i < kmax; i++)
        {
            afinal[i] = true;
            bfinal[i] = true;
        }

        int bptr = 0;
        int aptr = 0;

        while (N > 0)
        {
            if (a[aptr] < b[bptr])
            {
                afinal[aptr] = true;
                aptr++;
            }
            else
            {
                bfinal[bptr] = true;
                bptr++;
            }
            N--;
        }

        StringBuilder ans = new StringBuilder();
        for (Boolean bool : afinal)
        {
            char c = bool ? '1' : '0';
            ans.append(c);
        }
        System.out.println(ans);

        ans = new StringBuilder();

        for (boolean bool : bfinal)
        {
            char c = bool ? '1' : '0';
            ans.append(c);
        }
        System.out.println(ans);

    }


    //-----------MyScanner class for faster input----------
    public static class MyScanner
    {
        BufferedReader  br;
        StringTokenizer st;


        public MyScanner()
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
    //--------------------------------------------------------    
}
