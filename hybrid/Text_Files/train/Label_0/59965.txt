
import java.io.*;
import java.util.*;

/*


*/



 
 
 
 
 
 
 
public class P2 {
	static FastReader sc=null;
	
	public static void main(String[] args) {
		sc=new FastReader();
		PrintWriter out=new PrintWriter(System.out);
		char line[]=sc.next().toCharArray();
		int n=line.length;
		boolean front[][]=new boolean[n][n],back[][]=new boolean[n][n];
		outer:for(int i=0;i<n;i++) {
			int curr=0,q=0;
			for(int j=i;j<n;j++) {
				if(line[j]=='(')curr++;
				else if(line[j]==')') {
					if(curr>0)curr--;
					else if(q>0)q--;
					else continue outer;
				}
				else if(line[j]=='?')q++;
				if((j-i+1)%2==0) {
					if((curr-q)<=0 && (curr-q)%2==0) {
						front[i][j]=true;
					}
				}
			}
		}
		//COME FROM BACK
		reverse(line);
		outer:for(int i=0;i<n;i++) {
			int curr=0,q=0;
			for(int j=i;j<n;j++) {
				if(line[j]==')')curr++;
				else if(line[j]=='(') {
					if(curr>0)curr--;
					else if(q>0)q--;
					else continue outer;
				}
				else if(line[j]=='?')q++;
				if((j-i+1)%2==0) {
					if((curr-q)<=0 && (curr-q)%2==0) {
						back[n-j-1][n-i-1]=true;
					}
				}
			}
		}
		int count=0;
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(front[i][j]&&back[i][j]) {
					//System.out.println(i+" "+j);
					count++;
				}
			}
		}
		System.out.println(count);
		
		
		out.close();
		
	}
	
	
	static void reverseSort(int a[]) {
		ArrayList<Integer> al=new ArrayList<>();
		for(int i:a)al.add(i);
		Collections.sort(al,Collections.reverseOrder());
		for(int i=0;i<a.length;i++)a[i]=al.get(i);
	}
	static int gcd(int a,int b) {
		if(b==0)return a;
		else return gcd(b,a%b);
	}
	static long gcd(long a,long b) {
		if(b==0)return a;
		else return gcd(b,a%b);
	}
	static void reverse(int a[]) {
		int n=a.length;
		int b[]=new int[n];
		for(int i=0;i<n;i++)b[i]=a[n-1-i];
		for(int i=0;i<n;i++)a[i]=b[i];
	}
	static void reverse(char a[]) {
		int n=a.length;
		char b[]=new char[n];
		for(int i=0;i<n;i++)b[i]=a[n-1-i];
		for(int i=0;i<n;i++)a[i]=b[i];
	}
	static void ruffleSort(int a[]) {
		ArrayList<Integer> al=new ArrayList<>();
		for(int i:a)al.add(i);
		Collections.sort(al);
		for(int i=0;i<a.length;i++)a[i]=al.get(i);
	}
	
	
	
	static void print(char[] line) {
		for(char e:line) {
			System.out.print(e+" ");
		}
		System.out.println();
	}
	static void print(long a[]) {
		for(long e:a) {
			System.out.print(e+" ");
		}
		System.out.println();
	}
	
	
	static class FastReader 
    { 
        BufferedReader br; 
        StringTokenizer st; 
  
        public FastReader() 
        { 
            br = new BufferedReader(new
                     InputStreamReader(System.in)); 
        } 
  
        String next() 
        { 
            while (st == null || !st.hasMoreElements()) 
            { 
                try
                { 
                    st = new StringTokenizer(br.readLine()); 
                } 
                catch (IOException  e) 
                { 
                    e.printStackTrace(); 
                } 
            } 
            return st.nextToken(); 
        } 
  
        int nextInt() 
        { 
            return Integer.parseInt(next()); 
        } 
  
        long nextLong() 
        { 
            return Long.parseLong(next()); 
        } 
  
        double nextDouble() 
        { 
            return Double.parseDouble(next()); 
        } 
  
        String nextLine() 
        { 
            String str = ""; 
            try
            { 
                str = br.readLine(); 
            } 
            catch (IOException e) 
            { 
                e.printStackTrace(); 
            } 
            return str; 
        } 
        int[] readArray(int n) {
    		int a[]=new int [n];
    		for(int i=0;i<n;i++) {
    			a[i]=sc.nextInt();
    		}
    		return a;
    	}
        long[] readArrayL(int n) {
    		long a[]=new long [n];
    		for(int i=0;i<n;i++) {
    			a[i]=sc.nextLong();
    		}
    		return a;
    	}
    } 
}