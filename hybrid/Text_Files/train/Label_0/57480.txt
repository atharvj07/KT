import java.awt.Point;
import java.io.FileInputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
	static int n;
	static int[][] d;
	static Point[][] dp;
	
	private static Point calc(int from, int to)
	{
		if(dp[from][to] != null) return dp[from][to];
		
		ArrayList<Integer> branch = new ArrayList<Integer>();
		for(int i = 0;i < n;i++)
		{
			if(i == from || i == to) continue;
			if(d[to][i] > 0) branch.add(new Integer(i));
		}
		
		if(branch.size() == 0)
		{
			dp[from][to] = new Point(d[from][to], d[from][to]); 
			return dp[from][to];
		}
		else if(branch.size() == 1)
		{
			Point next = calc(to, branch.get(0).intValue());
			
			dp[from][to] = new Point(d[from][to] * 2 + next.x, d[from][to] * 3 + next.y); 
			return dp[from][to];
		}
		
		Point[] next = new Point[branch.size()];
		int maxnum = 0;
		int max = 0;
		for(int i = 0;i < branch.size();i++)
		{
			next[i] = calc(to, branch.get(i).intValue());
			int tmp = next[i].y - next[i].x;
			if(tmp > max)
			{
				max = tmp;
				maxnum = i;
			}
		}
		
		Point ret = new Point(d[from][to] * 2, d[from][to] * 3);
		for(int i = 0;i < next.length;i++)
		{
			if(maxnum == i)
				ret.x += next[i].x;
			else
				ret.x += next[i].y;
			
			ret.y += next[i].y;
		}
		
		dp[from][to] = ret; 
		return dp[from][to];
	}
	
	private static void start()
	{
		int min = Integer.MAX_VALUE;
		
		dp = new Point[n+1][n+1];
		for(int x = 0;x < n+1;x++)
			for(int y = 0;y < n+1;y++)
				dp[y][x] = null;
		
		for(int i = 0;i < n;i++)
		{
			Point p = calc(n, i);
			min = Math.min(min, p.x);
		}
		
		System.out.println(min);
	}
	
	public static void main(String[] args)
	{
		
		Scanner sca = new Scanner(System.in);
		
		while(true)
		{
			n = sca.nextInt();
			if(n == 0) break;
			
			int i, j;
			int[] tmp = new int[n-1];
			
			d = new int[n+1][n+1];
			for(i = 0;i < n+1;i++)
				for(j = 0;j < n+1;j++)
					d[j][i] = 0;
			
			for(i = 0;i < n-1;i++)
				tmp[i] = sca.nextInt();
			
			for(i = 0;i < n-1;i++)
			{
				d[i+1][tmp[i]-1] = d[tmp[i]-1][i+1] = sca.nextInt();
			}
			
			start();
		}
	}
}