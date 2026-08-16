import java.io.*;
import java.util.*;

public class Main {
	  public static void main(String[] args) {
	        InputStream inputStream = System.in;
	        OutputStream outputStream = System.out;
	        InputReader in = new InputReader(inputStream);
	            try (PrintWriter out = new PrintWriter(outputStream)) {
	            	TaskG solver = new TaskG();
	                solver.solve(in, out);
	            }
	    }
}
class InputReader {
    public BufferedReader reader;
    public StringTokenizer tokenizer;

    public InputReader(InputStream inputstream) {
      reader = new BufferedReader(new InputStreamReader(inputstream));
      tokenizer = null;
    }
    
    public String nextLine(){
    	String fullLine=null;
    	while (tokenizer == null || !tokenizer.hasMoreTokens()) {
            try {
              fullLine=reader.readLine();
            } catch (IOException e) {
              throw new RuntimeException(e);
            }
            return fullLine;
          }
          return fullLine;
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
	public long nextLong() {
	      return Long.parseLong(next());
	    }
    public int nextInt() {
      return Integer.parseInt(next());
    }
  }
class TaskG {
	void solve(InputReader in,PrintWriter out){
		int n=in.nextInt();
		int arr[]=new int[n];
		for(int i=0;i<n;i++){
			arr[i]=in.nextInt();
			arr[i]+=i;
		}
		Arrays.sort(arr);
		for(int i=0;i<n;i++){
			arr[i]-=i;
		}
		for(int i=0;i<n-1;i++){
			if(arr[i+1]<arr[i]){
				out.println(":(");
				return;
			}
		}
		for(int x:arr){
			out.print(x+" ");
		}
	}
}
