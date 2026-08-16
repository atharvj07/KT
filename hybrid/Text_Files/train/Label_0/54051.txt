import java.util.*;
import java.lang.*;
import java.io.*;

public class Code
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner s = new Scanner(System.in);
		int n= s.nextInt();
		int[][] a = new int[2*n+1][2];
	    for(int i=0;i<2*n;i++){
	        int temp = s.nextInt();
	        if(a[temp][0]==0)
	        a[temp][0]=i+1;
	        else
	        a[temp][1]=i+1;
	    }
	    long ans=0;
	    int tempposs=1;
	    int tempposd=1;
	    for(int j=1;j<=n;j++){
	        int temp1=Math.max(a[j][0]-tempposs,tempposs-a[j][0]);
	        int temp2=Math.max(a[j][1]-tempposs,tempposs-a[j][1]);
	        int temp3=Math.max(a[j][0]-tempposd,tempposd-a[j][0]);
	        int temp4=Math.max(a[j][1]-tempposd,tempposd-a[j][1]);
	        if(temp1+temp4<=temp2+temp3){
	            tempposs=a[j][0];
	            tempposd=a[j][1];
	            ans=ans+temp1+temp4;
	        }
	        else{
	            tempposs=a[j][1];
	            tempposd=a[j][0];
	            ans=ans+temp2+temp3;
	        }
	    }
	    System.out.println(ans);
	}
}
