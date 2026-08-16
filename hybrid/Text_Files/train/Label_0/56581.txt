/*Author LAVLESH*/
import java.util.*;
import java.io.*;
import java.math.BigInteger;
public class solution{
	static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st=new StringTokenizer("");
    
	

	static public String next() {
	        while (st == null || !st.hasMoreTokens()) {
	            try {
	                st = new StringTokenizer(br.readLine());
	            } catch (IOException e) {
	                throw new RuntimeException(e);
	            }
	        }
	        return st.nextToken();
	    }
	
	
	public static void main(String[]args)throws IOException{
		PrintWriter op =new PrintWriter(System.out,true);
		int x=2;
		int n=Integer.parseInt(next());
		if((n&(n-1))==0)op.println(0);
		else if(n%2==1)op.print(n/2);
		else{
			while(x<n)x*=2;
		x/=2;
		op.print((n-x)/2);
		}
		
		 op.close();
  }
}
 