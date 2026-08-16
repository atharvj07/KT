import java.util.*;
import java.io.*;
public class bfs {   
	static int gcd(int a, int b) 
    { 
        if (b == 0) 
            return a; 
        return gcd(b, a % b);  
          
    }


	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

		int t=Integer.parseInt(reader.readLine());
		while(t-->0){
			
			int n=Integer.parseInt(reader.readLine());
			String[] temp=reader.readLine().split(" ");
			int[] arr=new int[n];
			for (int i=0;i<n;i++) {
				arr[i]=Integer.parseInt(temp[i]);
			}
			if(n<=3) {System.out.println("0 0 0");
				continue;
			}
			int g=0,s=0,b=0;
			ArrayList<Integer> jj=new ArrayList<>();
			int count=1;
			for( int i=1;i<=n/2;i++) {
			
				if (arr[i-1]==arr[i]) {
					count++;
				}
				else {
					jj.add(count);
					count=1;
				}
				if(arr[i]==arr[n/2]) break;
			}
			
			int ss=jj.size();
			if(!jj.isEmpty())
			g=jj.get(0);
			else {
				System.out.println("0 0 0");continue;
			}
			for( int i=1;i<ss;i++) {
			
				
				 if(s<=g ) {
					s+=jj.get(i);
				}
				else  {
					b+=jj.get(i);
				}
				
			
			}		
			
		if(g>=s || g>=b || s==0 || b==0) {
			System.out.println("0 0 0");
		}else 
			System.out.println(g+" "+s+" "+b);
			
		}
			
}}
