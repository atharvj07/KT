import java.io.*;
import java.util.*;
import java.util.Map.Entry;


public class Task_Rnd664_B {

	final static String input_file_name = "input/Rnd664_B.txt";
	
	public static void main(String[] args)
	{
		//!!!!!!!!!!111
		reader.init(true);		//to server
		//reader.init(false);
		
		run();
		wr.flush();
	}

    public static void run()
    {
    	String s = reader.readln();
    	
    	int xx = 0;
    	int kk = 0;
    	int nn = 0;
    	boolean plus = true;
    	for (int ii = 0; ii < s.length(); ii++)
    	{
    		char cc = s.charAt(ii);
    		if (cc == '+')
    			plus = true;
    		if (cc == '-')
    			plus = false;
    		if (cc == '?')
    		{
    			if (plus)
    				xx++;
    			else
    				kk++;
    		}
    		if (cc == '=')
    		{
    			String s2 = s.substring(ii+1, s.length());
    			s2 = s2.trim();
    			nn = Integer.valueOf(s2);
    			break;
    		}
    	}
    	
    	if (xx*nn - kk * 1 < nn || xx * 1 - kk * nn > nn)
    	{
        	wr.print("Impossible");
    		wr2.endl();
    		return;
    	}
    	
    	int vv = xx * nn - kk * 1;
    	int ll = vv - nn;
    	
    	int aa1[] = new int[xx];
    	int aa2[] = new int[kk+1];
    	
    	for (int ii = 0; ii < xx; ii++)
    		aa1[ii] = nn;

    	for (int ii = 0; ii < kk; ii++)
    		aa2[ii] = 1;
    	
    	int ii = 0;
    	while (ll > 0 && ii < xx)
    	{
    		int bb = aa1[ii]-1;
    		if (bb > ll)
    			bb = ll;
    		aa1[ii] -= bb;
    		ll -= bb;
    		ii++;
    	}

    	ii = 0;
    	while (ll > 0 && ii < kk)
    	{
    		int bb = nn-aa2[ii];
    		if (bb > ll)
    			bb = ll;
    		aa2[ii] += bb;
    		ll -= bb;
    		ii++;
    	}
    	
    	if (ll > 0)
    	{
        	wr.print("Impossible");
    		wr2.endl();
    		return;
    	}

    	wr.print("Possible");
    	wr2.endl();
    	int ind1 = 0;
    	int ind2 = 0;
    	plus = true;
    	for (int jj = 0; jj < s.length(); jj++)
    	{
    		char cc = s.charAt(jj);
    		if (cc == '+')
    		{
    			plus = true;
    			wr.print("+ ");
    		}
    		if (cc == '-')
    		{
    			plus = false;
    			wr.print("- ");
    		}
    		if (cc == '?')
    		{
    			if (plus)
    			{
    				wr.print(aa1[ind1++]);
    				wr.print(" ");
    			}
    			else
    			{
    				wr.print(aa2[ind2++]);
    				wr.print(" ");
    			}
    		}
    		if (cc == '=')
    		{
    			String s2 = s.substring(jj, s.length());
    			wr.print(s2);
    			break;
    		}
    	}
    	
    	
		wr2.endl();
    }
	
     
    static public PrintWriter wr; 
    static OutputWriter wr2=new OutputWriter(System.out);
	static class reader{
		static BufferedReader br; static StringTokenizer tkn;
		static String readln() { try { return br.readLine(); } catch (Exception e) { return ""; } }
		static void init(boolean console) {
			if (console) { br=new BufferedReader(new InputStreamReader(System.in)); }
			else { try { br=new BufferedReader(new InputStreamReader(new FileInputStream(input_file_name))); }
				catch (Exception e) { System.exit(551); } }
			tkn=new StringTokenizer("");
		}
		static String next() { while (!tkn.hasMoreTokens()){ tkn=new StringTokenizer(readln()); } return tkn.nextToken(); }
		static int nextInt(){ while (!tkn.hasMoreTokens()){ tkn=new StringTokenizer(readln()); } return Integer.parseInt(tkn.nextToken()); }
		static long nextLong(){ while (!tkn.hasMoreTokens()){ tkn=new StringTokenizer(readln()); } return Long.parseLong(tkn.nextToken()); }
		static double nextDouble(){ while (!tkn.hasMoreTokens()){ tkn=new StringTokenizer(readln()); } return Double.parseDouble(tkn.nextToken()); }
	}
    static class OutputWriter {
        OutputWriter(OutputStream stream) { wr = new PrintWriter(stream); }
        public void printf(String format, Object... args) { wr.print(String.format(Locale.ENGLISH, format, args)); }
        public void endl() { wr.print("\n"); }
    }
}
