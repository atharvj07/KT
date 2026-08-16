import java.io.*;
import java.util.*;
import java.lang.ArrayIndexOutOfBoundsException;
import java.math.BigInteger;

/**
 * @author yoshikyoto
 */
class Main extends MyUtil{
	public static void main(String[] args) throws Exception{
		int n = readInt();
		for (int i = 0; i < n; i++) {
			int h = readIntMap(0);
			int w = readIntMap(1);
			char[][] c = new char[h][];
			for (int j = 0; j < h; j++) {
				c[j] = readLine().toCharArray();
			}
			if(solve(c, h, w)){
				System.out.println("SAFE");
			}else{
				System.out.println("SUSPICIOUS");
			}
		}
	}
	
	static boolean solve(char[][] c, int h, int w){
		// System.out.println("solve");
		while(checkThisTurn(c, h, w));
		// 全部消えたかチェック
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if(c[i][j] != '.' && c[i][j] != '*'){
					return false;
				}
			}
		}
		return true;
	}
	
	static boolean checkThisTurn(char[][] c, int h, int w){
		// System.out.println("turn check");
		HashSet<Character> checked = new HashSet<Character>();
		checked.add('.');
		checked.add('*');
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if(!checked.contains(c[i][j])){
					// System.out.println(c[i][j]);
					if(checkRect(c, h, w, c[i][j])){
						// 長方形だったら
						return true;
					}else{
						// 長方形でなかったら
					}
				}
				// このターンでは確認済み
				checked.add(c[i][j]);
			}
		}
		return false;
	}
	
	static boolean checkRect(char[][] c, int h, int w, char target){
		int top = h, bottom = 0, left = w, right = 0;
		// 上下左右の端を確認
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if(c[i][j] == target){
					top = Math.min(top, i);
					bottom = Math.max(bottom, i);
					left = Math.min(left, j);
					right = Math.max(right, j);
				}
			}
		}
		
		// そこが埋まっているか確認
		if(isFilled(c, h, w, target, top, bottom, left, right)){
			//埋まってる
			for(int i = top; i <= bottom; i++){
				for(int j = left; j <= right; j++){
					// 次からワイルとカードとして扱える
					c[i][j] = '*';
				}
			}
			return true;
		}else{
			//埋まってない
			return false;
		}
	}
	
	static boolean isFilled(char[][] c, int h, int w, int target,
			int top, int bottom, int left, int right){
		for(int i = top; i <= bottom; i++){
			for(int j = left; j <= right; j++){
				if(c[i][j] != target && c[i][j] != '*'){
					return false;
				}
			}
		}
		return true;
	}
}



class BinaryIndexedTree{
    int n;
    int[] bit;
    BinaryIndexedTree(int n){
        this.n = n;
        bit = new int[n+1];
    }
    int sum(int i){
        int sum = 0;
        while(i > 0){
            sum += bit[i];
            i -= i & -i;
        }
        return sum;
    }
    void add(int i, int v){
        while(i <= n){
            bit[i] += v;
            i += i & -i;
        }
    }
}


// --- ここから下はライブラリ ----------
/**
 * MyUtil
 * @author yoshikyoto
 */
class MyUtil {
	public static int toInt(boolean[] a){
		int pow = 1, ret = 0, l = a.length;
		for(int i = 0; i < l; i++){
			if(a[i]) ret += pow;
			pow *= 2;
		}
		return ret;
	}
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static int ins[];
	public static int[] readIntMap() throws IOException{return parseInt(readLine().split(" "));}
	public static int readIntMap(int i) throws Exception{
		if(i == 0) ins = readIntMap();
		return ins[i];
	}
	public static int[][] readIntMap(int n, int m) throws IOException{
		int[][] ret = new int[n][];
		for(int i = 0; i < n; i++) ret[i] = readIntMap();
		return ret;
	}
	public static int[] readIntToMap(int n) throws IOException{
		int[] ret = new int[n];
		for(int i = 0; i < n; i++) ret[i] = readInt();
		return ret;
	}
	public static int[] readNoDistIntMap() throws IOException{
		String[] strs = readLine().split("");
		int l = strs.length;
		int[] ret = new int[l-1];
		for(int i = 1; i < l; i++)
			ret[i-1] = parseInt(strs[i]);
		return ret;
	}
	public static String readLine() throws IOException{return br.readLine();}
	public static int readInt() throws IOException{return Integer.parseInt(br.readLine());}
	public static int[] parseInt(String[] arr){
		int[] res = new int[arr.length];
		for(int i = 0; i < arr.length; i++)res[i] = Integer.parseInt(arr[i]);
		return res;
	}
	public static double[] parseDouble(String[] arr){
		double[] res = new double[arr.length];
		for(int i = 0; i < arr.length; i++)res[i] = Double.parseDouble(arr[i]);
		return res;
	}
	public static boolean[] parseBool(String[] arr){
		int[] t = parseInt(arr);
		boolean[] res = new boolean[t.length];
		for(int i = 0; i < t.length; i++){
			if(t[i] == 1){res[i] = true;
			}else{res[i] = false;}
		}
		return res;
	}
	public static int parseInt(Object o){
		return Integer.parseInt(o.toString());
	}
}