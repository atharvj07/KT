import java.io.*;
import java.util.*;

public class Main{

	static class FastReader{
		BufferedReader br;
		StringTokenizer st;
		public FastReader(){
			br = new BufferedReader(new InputStreamReader(System.in));
		}
		public String next(){
			try{
				while(st==null||!st.hasMoreElements()){
					st = new StringTokenizer(br.readLine());
				}
			}catch(Exception e){
				e.printStackTrace();
			}
			return st.nextToken();
	
		}
		public int nextInt(){
			return Integer.parseInt(next());
		}
		public long nextLong(){
			return Long.parseLong(next());
		}
		public double nextDouble(){
			return Double.parseDouble(next());
		}
		public String nextLine(){
			String s = "";
			try{
				s = br.readLine();
			}catch(Exception e){
				e.printStackTrace();
			}	
			return s;		
		}
	} 
	
	public static void main(String[] args){
		FastReader in = new FastReader();
		PrintWriter out = new PrintWriter(System.out);
		int n = in.nextInt();
		String[] s = new String[n];
		
		for(int i = 0; i < n; i++){
			s[i] = in.next();
		}
		int freq[] = new int[26];
		
		for(int i =0;i<26;i++){
			boolean check =true;
			int min=1222;

			for(int j=0;j<s.length;j++){
				freq[i] = 0;
				for(int k=0;k<s[j].length();k++){
					if(s[j].charAt(k)-'a'==i){
						freq[i]++;
					}
				}
				min = Math.min(min,freq[i]);
				if(freq[i]==0){
					check=false;
					break;
				}

			}
			if(check){
				for(int j=0;j<min;j++)
					out.print((char)('a'+i));		
			}
		}
		out.flush();
		out.close();  
	}

}



