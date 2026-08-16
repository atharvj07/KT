
import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
public class Ideone
{
static	class pair{
		int ele;
		int index;
		pair(int ele,int index){
			this.ele=ele;
			this.index=index;
		}
	}
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		
		Scanner in=new Scanner(System.in);
		int n=in.nextInt();
		int a[]=new int[n];
		for(int i=0;i<n;i++){
			a[i]=in.nextInt();
		}
		Arrays.sort(a);
		boolean visited[]=new boolean[n+1];
		visited[a[0]]=true;
		pair b[]=new pair[n];
		for(int i=0;i<n;i++){
			b[i]=new pair(0,0);
		}
		int k=0;
		for(int i=1;i<n;i++){
			visited[a[i]]=true;
			if(a[i]==a[i-1])
			{
				
				
				b[k].ele=a[i];
				b[k].index=i;
				k++;
			}
			
			
		}
		int c[]=new int[6001];
		int h=0;
		for(int i=1;i<=n;i++){
			
			if(visited[i]==false){
				c[h]=i;
				h++;
			}
			
		}
		for(int i=n+1;i<=6000;i++){
			c[h]=i;
			h++;
		}
		int j=0;
		int count=0;
		for(int i=0;i<k;i++){
		while(b[i].ele>=c[j]){
              j+=1;			
			}
				count+=c[j]-b[i].ele;
			j+=1;
			
			
		}
		System.out.println(count);
	}
}