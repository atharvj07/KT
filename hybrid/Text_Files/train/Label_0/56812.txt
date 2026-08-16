import java.io.*;
import java.util.*;
import java.lang.ArrayIndexOutOfBoundsException;
import java.math.BigInteger;

/**
 * @author yoshikyoto
 */
class Main {
	public static void main(String[] args) throws Exception{
		Scanner sc = new Scanner(new InputStreamReader(System.in));
		// 1行目
		int w = sc.nextInt();
		int h = sc.nextInt();
		int n = sc.nextInt();
		int ww = 2*w+1;
		int hh = 2*h+1;
		
		// 2行目
		int start_x = sc.nextInt() * 2;
		int start_y = sc.nextInt() * 2;
		int end_x = sc.nextInt() * 2;
		int end_y = sc.nextInt() * 2;
		int[][] table = new int[ww][hh];
		
		for(int i = 0; i < n; i++){
			// それぞれのスタッフの動き
			int x = sc.nextInt() * 2 + 1;
			int y = sc.nextInt() * 2 + 1;
			int t = sc.nextInt();
			char[] seq = sc.next().toCharArray();
			long len = seq.length;
			
			for(long j = 0; j < len*t; j++){
				char c = seq[(int)(j%len)];
				int[] d = getD(c);
				int next_x = x + d[0] * 2;
				int next_y = y + d[1] * 2;
				// System.out.println(next_x + " " + next_y + " " + ww + " " + hh);
				if(inside(next_x, next_y, ww, hh)){
					// System.out.println("inside");
					table[x+d[0]][y+d[1]]++;
					x = next_x;
					y = next_y;
				}
			}
		}

		// print(table);
		
		// 次はケーブルの幅優先探索
		Coordinate start = new Coordinate(start_x, start_y, 1);
		PriorityQueue<Coordinate> q = new PriorityQueue<Coordinate>(w*h, new CComp());
		q.add(start);
		table[start.x][start.y] = 1;
		
		int[] dx = {-1, 1, 0, 0};
		int[] dy = {0, 0, -1, 1};
		int ans = 0;
		while(!q.isEmpty()){
			Coordinate curr = q.poll();
			if(table[curr.x][curr.y] < curr.cost) continue;
			// System.out.println("while: " + curr.x + " " + curr.y);
			// System.out.println("while: " + curr.cost);
			if(curr.x == end_x && curr.y == end_y){
				ans = curr.cost;
				break;
			}
			for(int k = 0; k < 4; k++){
				Coordinate next = new Coordinate(curr.x + dx[k]*2, curr.y + dy[k]*2, curr.cost);
				if(inside(next.x, next.y, ww, hh)){
					next.cost += table[curr.x + dx[k]][curr.y + dy[k]];
					if(table[next.x][next.y] == 0L || table[next.x][next.y] > next.cost){
						q.add(next);
						table[next.x][next.y] = next.cost;
					}
				}
			}
		}
		System.out.println(ans - 1L);
	}
	
	static void print(long[][] table){
		for(int i = 0; i < table.length; i++){
			StringBuffer buf = new StringBuffer();
			for(int j = 0; j < table[i].length; j++){
				buf.append(table[i][j] + " ");
			}
			System.out.println(buf.toString());
		}
	}
	
	static boolean inside(int x, int y, int w, int h) {
		return 0 <= x && x < w && 0 <= y && y < h;
	}
	
	static int[] getD(char c){
		int[] ret = new int[2];
		switch (c) {
		case 'U':
			ret[1] = -1;
			break;
		case 'D':
			ret[1] = 1;
			break;
		case 'L':
			ret[0] = -1;
			break;
		case 'R':
			ret[0] = 1;
			break;
		}
		return ret;
	}
}

class Coordinate{
	int x, y;
	int cost;
	Coordinate(int x, int y, int cost){
		this.x = x;
		this.y = y;
		this.cost = cost;
	}
	
	public String toString(){
		return "(" + x + ", " + y + ")";
	}
}

/**
 * 昇順
 */
class CComp implements Comparator<Coordinate> {
	public int compare(Coordinate a, Coordinate b) {
		return a.cost - b.cost;
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