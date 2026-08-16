//-----------------------------------------------------------
// すぐ使える
//-----------------------------------------------------------
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
		// 1行目数字、2行目文字
		int N = Integer.parseInt(br.readLine());
		String s;
		String[] S = new String[N+1];
		String[] Sa = new String[N+1];
		String[] Sz = new String[N+1];
		for(int i=0; i<N; i++) { 
			s = br.readLine();
			S[i] = s;
			Sa[i] = s.replace('?', 'a') + '5';
			Sz[i] = s.replace('?', 'z') + '5';
		}
		String T = br.readLine();
		Sa[N] = T + '0';
		Sz[N] = T + '9';

//		Arrays.sort(S);
		Arrays.sort(Sa);
		Arrays.sort(Sz);

		int min=0;
		int max=0;

					//入力値確認
					for(int i=0; i < Sa.length; i++){
						//System.out.println(Sa[i]);
					}
					for(int i=0; i < Sz.length; i++){
						//System.out.println(Sz[i]);
					}

		for(int i=0; i < Sa.length; i++){
			if(Sa[i].equals(T+'0')){ min = i+1; break; }
		}
		for(int i=0; i < Sz.length; i++){
			if(Sz[i].equals(T+'9')){ max = i+1; break; }
		}
		
		//System.out.println("min=["+min+"], max=["+max+"]");
		if(min>max) {
			int i = min;
			min = max;
			max = i;
		}
		//System.out.println("min=["+min+"], max=["+max+"]");

		StringBuilder sb = new StringBuilder();
		for(int i=min; i <= max; i++){
			sb.append(i);
			if (i == max) {
				//sb.append(System.getProperty("line.separator"));
			} else {
				sb.append(" ");
			}
		}
		System.out.println(sb);

        //System.out.println(iCount + " " + s);
        return;
    }
    //-----------------------------------------------------------------
    // Debug.Print
    static void dp(String s) {
		System.out.println(s);
	}
    static void dp(StringBuilder s) { dp(s.toString()); }
    static void dp(int i) { dp(String.valueOf(i)); }
    static void dp(long i) { dp(String.valueOf(i)); }


	//-----------------------------------------------------------------
	// 入力値確認：リスト
	static void checkInput(List l) { System.out.println(l); }
	//-----------------------------------------------------------------
	// 入力値確認：配列、1次元、float型
	//   ＜使い方＞
	//     float[] f = new float[N];
	//     checkInput(f);
	static void checkInput(float[] i1) {
		StringBuilder sb = new StringBuilder();
		for(float i: i1) sb.append("[" + i + "]");
		System.out.println(sb);
	}
	//-----------------------------------------------------------------
	// 入力値確認：配列、1次元、int型
	//   ＜使い方＞
	//     int[] c = new int[N];
	//     checkInput(c);
	static void checkInput(int[] i1) {
		StringBuilder sb = new StringBuilder();
		for(int i: i1) sb.append("[" + i + "]");
		System.out.println(sb);
	}
	//-----------------------------------------------------------------
	// 入力値確認：配列、二次元、int型
	static void checkInput(int[][] i2) {
		StringBuilder sb = new StringBuilder();
		for(int[] i1: i2){
			for(int i: i1) sb.append("[" + i + "]");
			sb.append(System.getProperty("line.separator"));
		}
		System.out.println(sb);
	}
	//-----------------------------------------------------------------
	// 入力値確認：配列、二次元、int型
	static void checkInput(long[][] i2) {
		StringBuilder sb = new StringBuilder();
		for(long[] i1: i2){
			for(long i: i1) sb.append("[" + i + "]");
			sb.append(System.getProperty("line.separator"));
		}
		System.out.println(sb);
	}

}

//-----------------------------------------------------------
//-----------------------------------------------------------
