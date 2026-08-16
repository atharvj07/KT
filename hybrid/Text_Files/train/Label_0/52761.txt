import java.util.*;
import java.io.*;
import java.math.*;
public final class Solution 
{
    public static void main(String[] args)
    {
    	 Reader input = new Reader();
         PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
         int n = input.nextInt(), k = input.nextInt(), t = input.nextInt();
         if(t <= k)
        	 out.println(t);
         else if(t <= n)
        	 out.println(k);
         else
        	 out.println(k - (t-n));
		 out.close();		 
    }  
    public static class Reader
    {
    	BufferedReader br;
    	StringTokenizer st;
    	public Reader()
    	{
    		br = new BufferedReader(new InputStreamReader(System.in));    		
    	}
    	public String next()
    	{
    		try
    		{
        		if(st == null || !st.hasMoreTokens())
        			st = new StringTokenizer(br.readLine());
    		}
    		catch(IOException ex)
    		{
    			ex.printStackTrace();
    			System.exit(1);
    		}    		
    		return st.nextToken();
    	}
    	public int nextInt()
    	{
    		return Integer.parseInt(next());
    	}
    	public double nextDouble()
    	{
    		return Double.parseDouble(next());
    	}
    	public long nextLong()
    	{
    		return Long.parseLong(next());
    	}
    	public String nextLine()
    	{
    		try
    		{
    			return br.readLine();
    		}
    		catch(IOException ex)
    		{
    			ex.printStackTrace();
    			System.exit(1);
    		}
    		return "";
    	}
    }
}