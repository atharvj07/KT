        import java.util.*;
        import java.io.*;
        import java.lang.*;
        import java.math.*;
        
         
         
        public class test2{
          public static void main (String [] args) throws IOException
          {
           
        	  
        	  try {
        		  Scanner sc=new Scanner(System.in);
        		  int t=sc.nextInt();
        		  
        		  for(int i=0;i<t;i++)
        		  {
        		   
        		     int n=sc.nextInt();
        		     int k=sc.nextInt();
        		     int ans=n;
        		     
        		     if(k>=n)
        		     ans=1;
        		     else
        		     {
        		        int po=(int)Math.pow(n,0.5);
        		        //po=po+3;
        		        // System.out.println(po);
        		        int temp=Math.min(po,k);
        		        for(int j=2;j<=temp;j++)
        		        {
        		           if(n%j==0)
        		           {
        		              ans=Math.min(ans,n/j);
        		              if(n/j<=k)
        		              ans=Math.min(ans,j);
        		           }
        		        }
        		     }
        		     
        		     
        		     System.out.println(ans);
        		     
        		  }
                  
        	  }	 
        	  
        	  catch (Exception e) {
        		return;
        	}
         
        }
         
        }  