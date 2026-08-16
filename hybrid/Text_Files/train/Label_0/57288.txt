import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;


public class Main {
	
	public static long l=0,l2=0;
	public static void main(String[] args) throws IOException {
		//*
		//new Main().test();
		l = System.currentTimeMillis();
		new Main().exec();
		l2 = System.currentTimeMillis();
		//System.out.println(l2-l);
		/*/
		new Main().test();
		//*/
	}
	
	public void test() {
	}
	
	long[] Combi_n_2_Array = new long[200001];
	int[] charCountArray = new int[26];
	
	public void exec() throws IOException {
		SimpleInputUtil in = new SimpleInputUtil();
		PrintWriter out = new PrintWriter(System.out);
		initPattern();
		String A = in.br.readLine();
		int lenA = A.length();
		countCharacter(A);
		long patternNum = Combi_n_2_Array[lenA] + 1;
		for(int i=0; i<26; i++){
			patternNum -= Combi_n_2_Array[charCountArray[i]];
		}
		out.println(patternNum);
		out.flush();
	}
	
	private void initPattern() {
		Combi_n_2_Array[1]=0;
		Combi_n_2_Array[2]=1;
		for(int i=3; i<Combi_n_2_Array.length; i++) {
			Combi_n_2_Array[i] = Combi_n_2_Array[i-1]+i-1;
		}
	}
	
	private void countCharacter(String A) {
		for(char c: A.toCharArray()){
			charCountArray[c-'a'] ++;
		}
	}
}

class SimpleInputUtil {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public String[] readStrArray(String delim) throws NumberFormatException, IOException{
    	return br.readLine().split(delim);
    }
    
    public int nextInt() throws NumberFormatException, IOException{
    	return Integer.parseInt(br.readLine());
    }
    
    public int[] nextInt(int[] a, int num) throws NumberFormatException, IOException{
        int i=0;
        while(i<num) {
            for(String s: br.readLine().split(" ")){
            	if(i<num) {
                    a[i++] = Integer.parseInt(s);
            	}
            }
        }
        return a;
    }
}