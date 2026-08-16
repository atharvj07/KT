import java.util.*;
import java.io.*;
import java.math.*;
public class Main implements Runnable {
	final String filename="test";
	
	final int base = 1<<20;
	
	int[] tree = new int[base*2];
	
	void set(int x, int val)
	{
		x+=base;
		while (x>0)
		{
			tree[x] = Math.max(tree[x], val);
			x /=2;
		}
	}
	
	int getmax(int left, int right)
	{
		left+=base;
		right +=base;
		int ans = 0;
		while (left+1<right)
		{
			if (left%2!=0)
			{
				ans = Math.max(ans, tree[left]);
				left++;
			}
			if (right%2!=0)
			{
				right--;
				ans = Math.max(ans, tree[right]);
			}
			left/=2;
			right/=2;
		}
		if (left<right)
			ans = Math.max(ans, tree[left]);
		return ans;
	}
	
	void solve() throws Exception
	{
		int n = iread();
		int[] x = new int[n];
		int[] y = new int[n];
		for (int i=0; i<n; i++)
		{
			x[i] = iread()-1;
		}
		for (int j=0; j<n; j++)
		{
			y[iread()-1] = j;
		}
		for (int i=0; i<n; i++)
			x[i] = n-y[x[i]]-1;
		int ans = 0;
		for (int i=0; i<n; i++)
		{
			int v = getmax(0, x[i]) + 1;
			set(x[i], v);
			ans = Math.max(ans, v);
		}
		out.write(ans+"\n");
	}
	
	
	public static void main(String[] args) {
		Main inst = new Main();
		new Thread(inst).run();
	}
	int iread()
	{
		return Integer.parseInt(readword());
	}
	long lread()
	{
		return Long.parseLong(readword());
	}
	double dread()
	{
		return Double.parseDouble(readword());
	}
	
	String readword()
	{
		try
		{
			int c = in.read();
			while (c<=32)
			{
				if (c<0) return "";
				c = in.read();
			}
			StringBuilder sb = new StringBuilder();
			while (c>32)
			{
				sb.append((char)c);
				c = in.read();
			}
			return sb.toString();
		} catch (Exception e)
		{
			e.printStackTrace();
			System.exit(1);
			return "";
		}
	}

	BufferedReader in;
	BufferedWriter out;
	public void run() {
		try
		{
			//in = new BufferedReader(new FileReader(filename+".in"));
			//out = new BufferedWriter(new FileWriter(filename+".out"));
			in = new BufferedReader(new InputStreamReader(System.in));
			out = new BufferedWriter(new OutputStreamWriter(System.out));
			
			solve();
			out.flush();
		} catch (Exception e)
		{
			e.printStackTrace();
			System.exit(1);
		}
	}

}
