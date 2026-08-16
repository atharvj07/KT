import java.util.*;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
		int[] arr=new int[n+1];
		int maxneg=0;
		int maxnegpos=-1;
		for(int i=0;i<n;++i)
		{   arr[i]=sc.nextInt();
		    if(arr[i]>=0)
		    {   arr[i]=-arr[i]-1;   
		    }
		    if(arr[i]<maxneg)
		    {
		        maxneg=arr[i];
		        maxnegpos=i;
		    }
		}
		if(n%2==1)
		{
		  arr[maxnegpos]=-arr[maxnegpos]-1;
		}
		for(int i=0;i<n;++i)
    		System.out.print(arr[i]+" ");
        
    }
}