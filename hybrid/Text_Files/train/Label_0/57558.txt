import java.util.*;
import java.io.*;

public class Main {
	
	List<Integer> prime;
	public List<Integer> initialize(){
		List<Integer> list = new ArrayList<Integer>();
		list.add(2); list.add(3);
		for(int i = 5; i < 102; i += 2){
			for(Integer x : list){
				if( x > Math.sqrt(i) ){
					list.add(i);
					break;
				}
				if( i%x == 0 ){
					break;
				}
			}
		}
		return list;
	}
	public  void solve() throws IOException{
		prime = new ArrayList<Integer>(initialize());
		int n;
		while( (n = nextInt() ) != 0 ){
			boolean flag = false;
			n = (n%2 == 0) ? n-1 : n;
		out:for(int i = n;; i -= 2){
				for(Integer x : prime){
					if( x > Math.sqrt(i) ){
						if( flag ){
							writer.println(i + " " + (i+2));
							break out;
						} else {
							flag = true;
							break;
						}
					}
					if( i%x == 0 ){
						flag = false;
						break;
					}
				}
			}
		}
		writer.flush();
	}
	public static void main (String args[]) throws IOException{
		new Main().run();
	}
	
	BufferedReader reader;
	StringTokenizer tokenizer;
	PrintWriter writer;
	
	public void run() throws IOException{
		try{
			reader = new BufferedReader(new InputStreamReader(System.in));
			tokenizer = null;
			writer = new PrintWriter(System.out);
			solve();
			reader.close();
			writer.close();
		} catch (Exception e){
			e.printStackTrace();
			System.exit(1);
		}
	}
	public int nextInt() throws IOException{
		return Integer.parseInt(nextToken());
	}		
	public String nextToken() throws IOException{
		while( tokenizer == null || !tokenizer.hasMoreTokens() ){
			tokenizer = new StringTokenizer(reader.readLine());
		}
		return tokenizer.nextToken();
	}
}