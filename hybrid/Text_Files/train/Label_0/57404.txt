import java.util.*;
import java.lang.*;
import java.io.*;
public class codechef
{
	public static void main(String args[]) throws NumberFormatException, IOException
	{
	    //Scanner sc=new Scanner(System.in);
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		int t= Integer.parseInt(br.readLine());
		for(int j=0;j<t;j++)
		{
			int n=Integer.parseInt(br.readLine());
			long sum=0;
			long a[] = new long[n];
			String line = br.readLine(); // to read multiple integers line
			String[] strs = line.trim().split("\\s+");
			long max=0;
			for (int i = 0; i < n; i++) {
			    a[i] = Long.parseLong(strs[i]);
			    sum=sum+a[i];
			    if(a[i]>max)
			    max=a[i];
			}
			
			long h=(long)Math.ceil((double)sum/(double)(n-1));
			//Arrays.sort(a);
			if(h<max)
			{
				System.out.println(max*(n-1)-sum);
			}
			else
			{
				System.out.println(h*(n-1)-sum);
				
			}
		}
	}
	
	
}
