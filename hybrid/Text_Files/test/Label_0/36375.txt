import java.util.*;
import java.io.*;
import java.util.regex.*;
import java.math.BigInteger;

public class Codeforces{
	
	static class MyScanner{
		BufferedReader br;
		StringTokenizer st;
		
		MyScanner(FileReader fileReader){
			br = new BufferedReader(fileReader);
		}
		
		MyScanner(){
			br = new BufferedReader(new InputStreamReader(System.in));
		}
		
		String nn(){
			while(st == null || !st.hasMoreElements()){
				try{
					st = new StringTokenizer(br.readLine());
				}catch(IOException e){
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}
		
		int ni(){
			return Integer.parseInt(nn());
		}
		
		long nl(){
			return Long.parseLong(nn());
		}
		
		double nd(){
			return Double.parseDouble(nn());
		}
	}
	
	private static PrintWriter out;
	
	private static int convertStringToInt(String s){
		return Integer.parseInt(s);
	}
	
	public static void main(String[] args) throws FileNotFoundException{
		
		
		// Input from file
		// File inputFile = new File("input.txt");
		// File outputFile = new File("output.txt");
		// FileReader fileReader = new FileReader(inputFile);
		// Here it ends
			
		MyScanner sc = new MyScanner();
		
		out = new PrintWriter(new BufferedOutputStream(System.out)); // Output to console
		// out = new PrintWriter(new PrintStream(outputFile)); // Output to file
		
		out.println(Math.round(sc.nd() / 10) * 10);
		
		out.close();
	}
}