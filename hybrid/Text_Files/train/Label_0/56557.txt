import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;
public class Main
{
    static BufferedReader reader;
    static StringTokenizer tokenizer;
    static void init(InputStream input)
    {
        reader = new BufferedReader( new InputStreamReader(input) );
        tokenizer = new StringTokenizer("");
    }
    static String next() throws IOException
    {
        while ( ! tokenizer.hasMoreTokens() )
        {
            tokenizer = new StringTokenizer(reader.readLine() );
        }
        return tokenizer.nextToken();
    }
 
    static long nextInt() throws IOException
    {
        return Long.parseLong( next() );
    }
    static PrintWriter writer;
    static void outit(OutputStream outputStream)
    {
        writer = new PrintWriter(new BufferedWriter(new OutputStreamWriter(outputStream)));
    }
    static void print(Object...objects) {
        for (int i = 0; i < objects.length; i++) {
            if (i != 0)
                writer.print(' ');
            writer.print(objects[i]);
        }
    }
 
    static void println(Object...objects) {
        print(objects);
        writer.println();
    }
 
    static void close() {
        writer.close();
    }
 
    static void flush() {
        writer.flush();
    }
    public static void main(String [] args) throws IOException
    {
        init(System.in) ;
        outit(System.out) ;
//    	int t = (int) nextInt() ;
//    	for(int i =0 ; i<t ; i++)
        output() ;
        flush();
        close();
    }
    public static int p(int i)
    {
    	return (int)Math.pow(2,i) ;
    }
    static int [][][] a ;
    static long  p ;
    static long [] tree ;
    static long [] x ;
    static long [] y ;
    static double pi = 3.14159 ;
    static double [] ang ;
    static char [][] board ;
    static boolean [][] spec ;
    static boolean [][] visited_a ;
    static boolean [][] visited_w ;
    static boolean check ;
    static double PI = 3.14159 ;
    public static final int MAXN = 1000 * 1001;
    static int n ;
    static int k ;
    static ArrayList<ArrayList<Integer>> ar ;
    static boolean [] visited ;
    public static void output() throws IOException
    {
    	n = (int)nextInt() ;
    	int k = (int)nextInt() ;
    	k = Math.min(k,n-k) ;
    	long [] BIT = new long[n+1] ;
    	Arrays.fill(BIT,0);
    	long ans = 1 ;
    	int start = 1 ;
    	int end = 1 ;
    	for(int i = 1 ; i<=n ; i++)
    	{
    		start = end ;
    		if(start+k>n)
    		{
    			end = start+k-n ;
    		}
    		else
    		{
    			end = start+k ;
    		}
    		updateBIT(BIT,start,1) ;
    		updateBIT(BIT,end,1) ;
    		int inter = split_q(BIT,start+1,end-1) ;
//    		println(start+" "+end) ;
//    		print_BIT(n,BIT) ;
//    		println("*"+inter) ;
    		ans+=inter+1 ;
    		print(ans+" ") ;
    	}
    	println() ;
    }
    static void print_BIT(int n,long [] BIT)
    {
    	for(int i = 1 ; i<=n ; i++)
    	{
    		print(query(BIT,i)-query(BIT,i-1)+" ") ;
    	}
    	println() ;
    }
    static int split_q(long [] BIT,int start, int end)
    {
    	if(start>end)
    	{
    		return q_u(BIT,start,n)+q_u(BIT,1,end) ;
    	}
    	else
    	{
    		return q_u(BIT,start,end) ;
    	}
    }
    static int q_u(long [] BIT,int x, int y)
    {
    	return query(BIT,y)-query(BIT,x-1) ;
    }
    static void updateBIT(long[] arr, int pos, int val) 
    {
        int len = arr.length;
        for (; pos < len; pos |= (pos + 1)) 
            arr[pos] += val;
    }
    static int query(long[] arr, int pos) 
    {
        int sum = 0;
        for (; pos >= 0; pos = (pos & (pos + 1)) - 1) 
            sum += arr[pos];
        return sum;
    }
} 