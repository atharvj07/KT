import java.io.OutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.util.*;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.InputStream;

public class java1 {
    public static void main(String[] args) {
        InputStream inputStream = System.in;
        OutputStream outputStream = System.out;
        InputReader in = new InputReader(inputStream);
        PrintWriter out = new PrintWriter(outputStream);
        TaskB solver = new TaskB();
        solver.solve(1, in, out);
        out.close();
    }
    static class TaskB {

        public void solve(int testNumber, InputReader in, PrintWriter out) {
            int t=in.nextInt();
            outer: while(t-- >0)
            {
            	int k=in.nextInt();
            	int n=in.nextInt();
            	int m=in.nextInt();
            	int na[]=in.inputarInt(n); int A=0;
            	int ma[]=in.inputarInt(m); int B=0;
            	int ans[]=new int[n+m];
            	
            	for(int x=1;x<=n+m;x++)
            	{
            		if(A<=n-1 && na[A]==0)
            		{
            			ans[x-1]=0;
            			A++;
            			k++;
            		}
            		else if(B<=m-1 &&ma[B]==0)
            		{
            			ans[x-1]=0;
            			k++;
            			B++;
            		}
            		else if(A<=n-1 && B<= m-1)
            		{
            			if(na[A] <=ma[B])
            			{
            				if(na[A] <=k)
            				{
            					ans[x-1]=na[A];
            					A++;
            				}
            				else
            				{
            					out.println("-1"); continue outer;
            				}
            			}
            			else
            			{
            				if(ma[B] <=k)
            				{
            					ans[x-1]=ma[B];
            					B++;
            				}
            				else
            				{
            					out.println("-1"); continue outer;
            				}
            			}
            		}
            		else if(A<=n-1)
            		{
            			if(na[A] <=k)
        				{
        					ans[x-1]=na[A];
        					A++;
        				}
        				else
        				{
        					out.println("-1"); continue outer;
        				}
            		}
            		else
            		{
            			if(ma[B] <=k)
        				{
        					ans[x-1]=ma[B];
        					B++;
        				}
        				else
        				{
        					out.println("-1"); continue outer;
        				}
            		}
            	}
            	for(int x=0;x<n+m;x++)
            	{
            		out.print(ans[x]+" ");
            	}
out.println();            	
            	
            	
            	
            			
            }
        }
        static void sort(int[] a) {
    		ArrayList<Integer> l=new ArrayList<>();
    		for (int i:a) l.add(i);
    		Collections.sort(l);
    		for (int i=0; i<a.length; i++) a[i]=l.get(i);
    	}
        
    }
    static class InputReader {
        public BufferedReader reader;
        public StringTokenizer tokenizer;

        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream), 32768);
            tokenizer = null;
        }
        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
        public int nextInt() {
            return Integer.parseInt(next());
        }
        public long nextLong() {
            return Long.parseLong(next());
        }
        public int[] inputarInt(int n)
        {
        	int ar[]=new int[n];
        	for(int x=0;x<n;x++)
        	{
        		ar[x]=nextInt();
        	}
        	return ar;
        }
        public long[] inputarLong(int n)
        {
        	long ar[]=new long[n];
        	for(int x=0;x<n;x++)
        	{
        		ar[x]=nextLong();
        	}
        	return ar;
        }
    }
}