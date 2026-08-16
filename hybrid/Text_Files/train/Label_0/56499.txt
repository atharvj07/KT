import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main
{
    static PrintWriter pw = new PrintWriter(System.out);

    static void swap(int[] a , int x , int y)
    {
        while(y != x)
        {
            int t = a[y];
            a[y] = a[y-1];
            a[y-1] = t;
            y--;
        }
    }

    public static void main(String[] args)throws Exception
    {
        Reader.init(System.in);

        String s = Reader.next();
        int n = s.length();
        int k = Reader.nextInt();
        int[] a = new int[n+1];

        for(int i = 0 ; i<n ; i++)
            a[i+1] = s.charAt(i) - '0';

        for(int i = 1 ; i<n && k > 0 ; i++)
        {
            int[] pos = new int[10];
            for(int j = i + 1 ; j<= n ; j++)
            {
                int z = a[j];
                if(pos[z] == 0)pos[z] = j;
            }

            for(int j = 9 ; j> a[i] ; j--)
            {
                if(pos[j] == 0)continue;

                if(pos[j] - i <= k)
                {
                    k -= pos[j] - i;
                    swap(a , i , pos[j]);
                }
            }
        }

        StringBuilder res = new StringBuilder();
        for(int i = 1 ; i<=n ; i++)res.append(a[i]);

        pw.print(res);
        pw.close();
    }



}







class Reader {

    static BufferedReader reader;
    static StringTokenizer tokenizer;

    public static int pars(String x) {
        int num = 0;
        int i = 0;
        if (x.charAt(0) == '-') {
            i = 1;
        }
        for (; i < x.length(); i++) {
            num = num * 10 + (x.charAt(i) - '0');
        }

        if (x.charAt(0) == '-') {
            return -num;
        }

        return num;
    }

    static void init(InputStream input) {
        reader = new BufferedReader(
                new InputStreamReader(input));
        tokenizer = new StringTokenizer("");
    }

    static void init(FileReader input) {
        reader = new BufferedReader(input);
        tokenizer = new StringTokenizer("");
    }

    static String next() throws IOException {
        while (!tokenizer.hasMoreTokens())
        {
            String line = reader.readLine();
            if(line == null || line.equals(""))throw  new IOException();
            tokenizer = new StringTokenizer(line);
        }
        return tokenizer.nextToken();
    }

    static int nextInt() throws IOException {
        return pars(next());
    }

    static long nextLong() throws IOException {
        return Long.parseLong(next());
    }

    static double nextDouble() throws IOException {
        return Double.parseDouble(next());
    }


}