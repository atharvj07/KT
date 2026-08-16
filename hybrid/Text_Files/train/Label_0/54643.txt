import java.io.*;
import java.math.BigInteger;
import java.util.*;


/**
 * @author yoshikyoto
 */
class Main extends MyUtil{
	public static ArrayList<ArrayList<Integer>> g;
	public static HashSet<Integer> set;
	
	public static void main(String args[]) throws Exception{
		String[] words = readLine().split(" ");
		int max = 0; String max_word = "";
		HMSI map = new HMSI();
		for(String word : words){
			int l = word.length();
			if(l > max){
				max = l;
				max_word = word;
			}
			map.add(word);
		}
		int freq = 0; String freq_word = "";
		for(String word : map.keySet()){
			int v = map.get(word);
			if(v > freq){
				freq = v;
				freq_word = word;
			}
		}
		p(freq_word + " " + max_word);
	}
}

/**
 * 整数を数え上げたりするクラス
 * new Prime(int n) でnまでエラトステネスの篩を実行。
 * @author yoshikyoto
 * @param a[i] iが素数の時true
 * @param count[i] i以下の素数の数
 */
class Prime{
	boolean[] a;
	int[] count;
	Prime(int n){
		a = new boolean[n+1];
		a[0] = false; a[1] = false;
		for(int i = 2; i <= n; i++) a[i] = true;
		// ふるい
		for(int i = 2; i < (n - 3) / 2; i++)
			if(a[i]) for(int j = 2; j * i <= n; j++)
					a[j * i] = false;
		
		// 数え上げ
		count = new int[n+1];
		count[0] = 0;
		for(int i = 1; i <= n; i++){
			int gain = 0;
			if(a[i]) gain = 1;
			count[i] = count[i-1] + gain;
		}
	}
}

class AI extends ArrayList<Integer>{}
class SI extends Stack<Integer>{}

class HMI<E> extends HashMap<E, Integer>{
	ArrayList<E> keyArray = new ArrayList<E>();
	public void add(E key){add(key, 1);}
	public void add(E key, Integer value){
		if(containsKey(key)){value += get(key);
		}else{keyArray.add(key);}
		put(key, value);
	}
}

class HMSI extends HMI<String>{}

class MyUtil extends MyIO{
	public static long start_time = 0;
	public static void start(){start_time = System.currentTimeMillis();}
	public static void end(){
		if(start_time == 0) return;
		long time = System.currentTimeMillis() - start_time;
		if(DEBUG) p(time + "ms");
	}
	public static int digit(int n){return String.valueOf(n).length();}
	public static String reverse(String s){
		StringBuffer sb = new StringBuffer(s);
		return sb.reverse().toString();
	}
	public static void sort(int[] a){Arrays.sort(a);}
	public static void dsort(int[] a){
		Arrays.sort(a);
		int l = a.length;
		for(int i = 0; i < l/2; i++){
			int tmp = a[i]; a[i] = a[l-1-i]; a[l-1-i] = tmp;
		}
	}
	public static void sleep(int t){try{Thread.sleep(t);}catch(Exception e){}}
}

class MyIO extends MyMath{
	static Scanner sc = new Scanner(new InputStreamReader(System.in));
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	public static boolean DEBUG = false;
	public static int[] readIntMap() throws IOException{return parseInt(readLine().split(" "));}
	public static String readLine() throws IOException{return br.readLine();}
	public static int readInt() throws IOException{return Integer.parseInt(br.readLine());}
	public static void p(Object o){System.out.println(o.toString());}
	public static void pr(Object o){System.out.print(o.toString());}
	public static void d(Object o){if(DEBUG)System.out.println(o.toString());}
	public static void dr(Object o){if(DEBUG)System.out.print(o.toString());}
	public static void da(Object[] o){if(DEBUG)System.out.println(Arrays.toString(o));}
	public static void da(int[] arr){if(DEBUG)System.out.println(Arrays.toString(arr));}
	public static void da(double[] arr){if(DEBUG)System.out.println(Arrays.toString(arr));}
	public static void da(boolean[] arr){if(DEBUG)System.out.println(Arrays.toString(arr));}
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
	public static int parseInt(Object o){return Integer.parseInt(o.toString());}
}

class MyMath{
	/**
	 * 弧度法の角度を入力してsinの値を返す（Math.sin の入力はラジアン）
	 */
	public static double sin(int r){return Math.sin(Math.toRadians(r));}

	/**
	 * 弧度法の角度を入力してcosの値を返す（Math.sin の入力はラジアン）
	 */
	public static double cos(int r){return Math.cos(Math.toRadians(r));}
	public static int max(int a, int b){return Math.max(a, b);}
	public static int min(int a, int b){return Math.min(a, b);}
	public static boolean isCross(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4){
	    // 並行な場合
	    int m = (x2-x1)*(y4-y3)-(y2-y1)*(x4-x3);
	    if(m == 0) return false;
	    // 媒介変数の値が0より大きく1以下なら交差する、これは問題の状況によって変わるかも。
	    double r =(double)((y4-y3)*(x3-x1)-(x4-x3)*(y3-y1))/m;
	    double s =(double)((y2-y1)*(x3-x1)-(x2-x1)*(y3-y1))/m;
	    return (0 < r && r <= 1 && 0 < s && s <= 1);
	}
	public static boolean isParallel(int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4){
	    if((x2-x1)*(y4-y3) == (y2-y1)*(x4-x3)) return true;
	    else return false;
	}
	public static double square(double d){return d*d;}
	public static int square(int i){return i*i;}
	public static int sqdist(int x1, int y1, int x2, int y2){
		return square(x1-x2) + square(y1-y2);}
	public static double sqdist(double x1, double y1, double x2, double y2){
		return square(x1-x2) + square(y1-y2);}
	public static double dist(int x1, int y1, int x2, int y2){
		return Math.sqrt(sqdist(x1, y1, x2, y2));}
	public static double dist(double x1, double y1, double x2, double y2){
		return Math.sqrt(sqdist(x1, y1, x2, y2));}
}