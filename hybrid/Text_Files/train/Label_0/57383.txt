import java.io.*;
import java.util.*;
public class LittleDimaandEquation 
{
    public static void main(String[] args) throws IOException
    {
        Reader in = new Reader();
        StringBuilder out = new StringBuilder();
        TreeSet<Long> set = new TreeSet<Long>();
        int a, b, c, sum, count;
        long x, temp;
        //for (int i = 0; i < 1; i++) 
        {
            a = in.nextInt();
            b = in.nextInt();
            c = in.nextInt();
            set.clear();
            count = 1;
            while(count <= 81)
            {
                x = (b*1L*(int)Math.pow(count, a)+c);
                
                if(x <= 0 || x >= 1000000000)
                {
                    count++;
                    continue;
                }
                
                temp = x;
                sum = 0;
                while(temp > 0)
                {
                    sum += temp%10;
                    temp /= 10;
                }
                
                if ( sum == count++)
                    set.add(x);
                
            }
            out.append(set.size()+"\n");
            for(Long j : set)
                out.append(j+" ");
            out.deleteCharAt(out.length()-1).append("\n");
        }
        System.out.print(out);
    }
    static class  Reader 
    {
        BufferedReader br;
        StringTokenizer st;
        Reader() { // To read from the standard input
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        Reader(int i) throws IOException { // To read from a file
            br = new BufferedReader(new FileReader("Sample Input.txt"));
        }
       String next() throws IOException {
          while (st == null || !st.hasMoreTokens())
             st = new StringTokenizer(br.readLine());
          return st.nextToken();
       }
       int nextInt() throws IOException { return Integer.parseInt(next()); }
       long nextLong() throws IOException { return Long.parseLong(next()); }
       double nextDouble() throws IOException { return Double.parseDouble(next()); }
       String nextLine() throws IOException { return br.readLine(); }
    }

}