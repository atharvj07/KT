          import java.io.*;
        import java.util.*;
        import java.lang.*;
             
            public class d {
            	public static void main (String[] args) {
            	PrintWriter pw=new PrintWriter(System.out);
            	Scanner sc=new Scanner(System.in);
            	int n=sc.nextInt();
            	int v=-1;
            	int m=sc.nextInt();
            	int[][] a=new int[n][m];
            //	for(int i=0;i<2;i++){
            	    for(int j=0;j<n;j++){
            	         v=sc.nextInt();
            	          for(int k=0;k<=v&&k<m;k++){
            	              if(k==v)
            	                a[j][k]=-1;
            	                else
            	                a[j][k]=1;
            	          }
            	           
            	    }
            	    ////////
            	    int f=0;
            	     for(int j=0;j<m;j++){
            	         v=sc.nextInt();
            	          for(int k=0;k<=v&&k<n;k++){
            	              if(k==v){
            	                  if(a[k][j]==1)
            	                    f=1;
            	                a[k][j]=-1;
            	                  
            	              }
            	                else{
            	                if(a[k][j]==-1)
            	                    f=1;
            	                a[k][j]=1;}
            	          }
            	           
            	    }
            	    
            //	}
            	int count=0;
            	for(int i=0;i<n;i++)
            	   for(int j=0;j<m;j++)
            	     if(a[i][j]==0)
            	        count++;
            	  long r=1;
                  for(int i=0;i<count;i++){
                   r*=2;
                   r%=1000000007;}
               
              
            	  if(f==1)
            	  pw.print(0);
            	  else
                pw.print(r);
                pw.close();
            	}
            }