

import java.util.*;
import java.lang.*;
import java.io.*;


public class Solution
{
	public static void main (String[] args) throws java.lang.Exception
	{
		
		BufferedReader br1=new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
		int t=Integer.parseInt(br1.readLine());
		int l=0;
		while(t>l)
		{
		    l=l+1;
		    //int n=Integer.parseInt(br1.readLine());
		    int num=Integer.parseInt(br1.readLine());
		    if(num<=9)
		    {
		        System.out.println(num);
		    }
		    else if(num>45)
		    {
		        System.out.println("-1");
		    }
		    else
		    {
		        String s=new String("");
		        int num1=9;
		        while((num>0)&&(num1>0))
		        {
		            s=s+num1;
		            num=num-num1;
		            if((num<9)&&(num<num1))
		            {
		                s=s+num;
		                break;
		            }
		            num1=num1-1;
		        }
		        String ans=new String("");
		        for(int i=s.length()-1;i>=0;i--)
		        {
		            ans=ans+s.charAt(i);
		        }
		        System.out.println(ans);
		    }
		    
		}
	}
}
