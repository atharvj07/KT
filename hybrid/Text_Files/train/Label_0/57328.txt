import java.util.*;
import java.io.*;

public final class Solution 
{
    public static void main(String[] args) 
    {
        Reader input = new Reader();
        PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));
        char[] s = input.next().toCharArray();
        int x = 0 , y = 0;
        String result = "";
        for(int i = 0 ; i < s.length ; i++)
        {
        	if(s[i] == 'x')
        		x++;
        	else
        		y++;
        }
        if(x > y) 
        {
        	int n = x - y;
        	char[] temp = new char[n];
        	Arrays.fill(temp,'x');
        	result = new String(temp);        	
        }
        else
        {
        	int n = y - x;
        	char[] temp = new char[n];
        	Arrays.fill(temp,'y');
        	result = new String(temp); 
        }
        out.println(result);
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