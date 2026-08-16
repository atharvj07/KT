import java.util.*;
import java.io.*;
import java.lang.*;
//import static java.lang.Math.*;
public class Main
{
	public static char [][] A = new char[101][101];
	public static int [][] color = new int[101][101];
	public static boolean [][] visited = new boolean[101][101];
	public static Scanner scan = new Scanner(System.in);
	static long gcd(long A,long B)
	{
		if(A==0)
			return B;
		if(B==0)
			return A;
		return gcd(B,A%B);
	}
	static int lower_bound(long[] a,int N,long value)
    {
    	int low = 0,high = N;
    	while(low<high)
    	{
    		int mid = low + (high-low)/2;
    		if(a[mid]==value)
    			high=mid;
    		else if(a[mid]<value)
    			low=mid+1;
    		else
    			high=mid;
    	}
    	if(a[low]!=value)
    		return low+1;
    	return low;
    }
    static int upper_bound(long[] a,int N,long value)
    {
    	int low = 0,high = N;
    	while(low<high)
    	{
    		int mid = low + (high-low)/2;
    		if(a[mid]==value)
    			low=mid+1;
    		else if(a[mid]<value)
    			low=mid+1;
    		else
    			high=mid;
    	}
    	if(a[high]!=value)
    		return high+1;
    	return high;
    }
  	public static void main(String args[])
    {
        int testcases=1;
       // testcases = scan.nextInt();
        while(testcases-->0)
        {
            solve();
        }
    }
    static void Fill(int start,int end,int count,int N,int M)
    {
    	if(start<0||end<0||start>=N||end>=M)
    		return;
    	else if(visited[start][end]==true)
    		return;
    	else if(A[start][end]!='B')
    		return;
    	else
    	{
    		color[start][end]=count;
    		visited[start][end]=true;
    		//if(visited[start-1][end]==false)
    			Fill(start-1,end,count,N,M);
    		//if(visited[start+1][end]==false)
    			Fill(start+1,end,count,N,M);
    		//if(visited[start][end-1]==false)
    			Fill(start,end-1,count,N,M);
    		//if(visited[start][end+1]==false)
    			Fill(start,end+1,count,N,M);
    	}
    }
    static void solve()
    {
		int N,M;
		N=scan.nextInt();
		M=scan.nextInt();
		//char [][] A = new char[N][M];
		scan.nextLine();
		for(int i=0;i<N;i++)
		{
			A[i]=scan.nextLine().toCharArray();
		}
		//int [][] color = new int[N][M];
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				color[i][j]=0;
				visited[i][j]=false;
			}
		}
		int count=1;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				if(A[i][j]=='B'&&color[i][j]==0&&visited[i][j]==false)
				{
					Fill(i,j,count,N,M);
					count++;
				}
			}
		}
		count=0;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<M;j++)
			{
				count = Math.max(count,color[i][j]);
			}
		}
		System.out.println(count);
    }
}