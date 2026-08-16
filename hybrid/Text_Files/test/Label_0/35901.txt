import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;


public class P4 {
	
	static class Scanner{
		BufferedReader br=null;
		StringTokenizer tk=null;
		public Scanner(){
			br=new BufferedReader(new InputStreamReader(System.in));
		}
		public String next() throws IOException{
			while(tk==null || !tk.hasMoreTokens())
				tk=new StringTokenizer(br.readLine());
			return tk.nextToken();
		}
		public int nextInt() throws NumberFormatException, IOException{
			return Integer.valueOf(next());
		}
	}
	
	static boolean good(int number, int upper){
        if (number >= 1000 && number <= 2011)
        	return number >= upper;
        return false;
	}
	
	static int getnumber(char[] t){
		int ret = 0;
		for(int i = 0; i < 4; i++){
			ret*=10;
			ret+= t[i] - '0';
		}
		return ret;
	}
	
	static int getdate(String s,int upper){
		char[] a = s.toCharArray();
		int ret = Integer.MAX_VALUE;
		for(int i = 0; i < 4; i++){
			char real = a[i];
			for(int j = 0; j <= 9; j++){
				if (i == 0 && j == 0)
					continue;
				a[i] = (char)(j + '0');
				int aux = getnumber(a);
				if (good(aux,upper) && aux<ret)
					ret = aux;
			}
			a[i] = real;
		}
		if (ret == Integer.MAX_VALUE)
			return -1;
		return ret;
	}
	
	public static void main(String args[]) throws NumberFormatException, IOException{
		Scanner sc = new Scanner();
		int N = sc.nextInt();
		int upper = 1000;
		LinkedList<Integer> sol = new LinkedList<Integer>();
		boolean found = true;
		for(int i = 0; i < N; i++){
			int date = getdate(sc.next(), upper);
			if (date < 0){
				found = false;
				break;
			}
			sol.add(date);
			upper = date;
		}
		if (!found)
			System.out.println("No solution");
		else
			for(int v: sol)
				System.out.println(v);
	}

}
