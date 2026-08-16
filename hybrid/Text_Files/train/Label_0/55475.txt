import java.io.*;
import java.util.*;

/**
 * 
 * @author Saju
 *
 */

public class Main {

	static int[] dx = { 0, 1, 0, -1 };
	static int[] dy = { -1, 0, 1, 0 };

	static Map<Integer, Brick> map = new HashMap<>();
	static List<Brick> bricksList = new ArrayList<>();
	public static void main(String[] args) {

		InputReader in = new InputReader(System.in);

		 n = in.nextInt();
		 visited = new boolean[n + 1];
		 indices = new int[n + 1];
		 rotation = new String[n + 1];
		Brick[] bricksOriginal = new Brick[n];
		
		int counter[] = new int[10];
		
		for(int i = 0; i < n; i++){
			int left = in.nextInt();
			int right = in.nextInt();
			bricksOriginal[i] = new Brick(i, left, right);
			map.put(i, new Brick(i, left, right));
			bricksList.add(new Brick(i, left, right));
			counter[left]++;
			counter[right]++;
			
		}
		
		int unique = 0;
		int check = -1;
		for(int i = 0; i <= 6; i++){
//			System.out.println(counter[i]);
			if(counter[i] % 2 != 0){
				unique++;
				check = i;
			}
		}
//		System.out.println(unique);
		
		
		if(unique > 2){
			System.out.println("No solution");
		}
		else{
			if(check == -1){
				dfs(bricksList.get(0).left, 1);
			}
			else{
				dfs(check, 1);
			}
//			int first = bricksList.get(0).left;
//			int index = 1;
//			dfs(first, index);
		}
		System.out.println("No solution");
//		in.nextInt();
//		boolean[] visited = new boolean[n];
//		
//		for(int i = 0; i < n; i++){
//			Arrays.fill(visited, false);
////			Brick[] tempBricks = bricksOriginal.clone();
//				
//			visited[i] = true;
////			tempBricks[i].isUsed = true;
////			System.out.println("call1 " + i);
//			List<Brick> list = new ArrayList<>();
//			list.add(bricksOriginal[i]);
//			call(bricksOriginal, i, visited, list);
////			System.out.println();
////			System.out.println(i);
////			for(Brick b : tempBricks){
////				System.out.println(b.left + " " + b.right + " " + b.rotate + " " + b.isUsed);
////			}
//			
//			if(bricksOriginal[i].left != bricksOriginal[i].right){
////				Brick[] tempBricks1 = bricksOriginal.clone();
//			   
//				int temp = bricksOriginal[i].left;
//				bricksOriginal[i].left = bricksOriginal[i].right;
//				bricksOriginal[i].right = temp;
//				Arrays.fill(visited, false);
//				visited[i] = true;
////				tempBricks1[i].isUsed = true;
////				tempBricks1[i].rotate = true;
////				System.out.println("call2 " + i);
//				List<Brick> list1 = new ArrayList<>();
//				list1.add(bricksOriginal[i]);
//				call(bricksOriginal, i, visited, list1);
//			}
//			
//		}
//		System.out.println("No solution");
		
		System.exit(0);

	}
	static int n;
	static boolean[] visited;
//	static Map<Integer, String> result = new HashMap<>();
	static String[] rotation;
	static int[] indices;
	private static void dfs(int right, int index) {
		
		if(index > n){
			for(int i = 1; i <= n; i++){
				System.out.println(indices[i] + " " + rotation[i]);
			}
			System.exit(0);
		}
		for(int i = 0; i < bricksList.size(); i++){
			if(!visited[i]){
				if(bricksList.get(i).left == right){
//					result.put(index, "+");
					indices[index] = i + 1; 
					rotation[index] = "+";
					visited[i] = true;
					dfs(bricksList.get(i).right, index + 1);
					visited[i] = false;
				}else if(bricksList.get(i).right == right){
//					result.put(index, "-");
					visited[i] = true;
					indices[index] = i + 1; 
					rotation[index] = "-";
					dfs(bricksList.get(i).left, index + 1);
					visited[i] = false;
				}
			}
		}
	}

	private static void call(Brick[] bricks, int i, boolean[] visited, List<Brick> list) {
		System.out.println(i);
		
		
		for(int j = 0; j < bricks.length; j++){
			if(!visited[j] && i != j){
				if(bricks[i].right == bricks[j].left){
					visited[j] = true;
//					bricks[j].isUsed = true;
					list.add(bricks[j]);
					call(bricks, j, visited, list);
					visited[j] = false;
//					bricks[j].isUsed = false;
					list.remove(bricks[j]);
				}
				else if(bricks[i].right == bricks[j].right)
				{
					if(bricks[j].left!=bricks[j].right){
					visited[j] = true;
//					bricks[j].rotate = true;
					int temp = bricks[j].left;
					bricks[j].left = bricks[j].right;
					bricks[j].right = temp;
//					bricks[j].isUsed = true;
					list.add(bricks[j]);
					call(bricks, j, visited, list);
				    temp = bricks[j].left;
					bricks[j].left = bricks[j].right;
					bricks[j].right = temp;
					visited[j] = false;
//					bricks[j].isUsed = false;
//					bricks[j].rotate = false;
					list.remove(bricks[j]);
					}
				}
			}
		}
		
//		System.out.println();
//		System.out.println(i);
//		for(Brick b : bricks){
//			System.out.println(b.left + " " + b.right + " " + b.rotate + " " + b.isUsed);
//		}
		
		if(list.size() == bricks.length){
			for(Brick b : list){
				String rotate = "";
				if(b.left == map.get(b.index).left){
					rotate = "+";
				}
				else{
					rotate = "-";
				}
			
				System.out.println( (b.index + 1) + " " + rotate);
			}
			System.exit(0);
		}
		
	}

	private static class Brick{
		int left;
		int right;
//		boolean rotate;
//		boolean isUsed;
		int index;
		Brick(int index, int left, int right){
			this.index = index;
			this.left = left;
			this.right = right;
//			isUsed = false;
		}
		
	}
	
	static long dp[] = new long[100007];
	

	private static int upperBound(long[] arr, long num) {

		int start = 0;
		int end = arr.length;
		
		int mid = 0;
		int index = 0;
		while(true){
		
			if(start > end){
				break;
			}
		    mid = (start + end) / 2;
			if(arr[mid] > num){
				end = mid - 1;
				
			}
			else if(arr[mid] < num){
				start = mid + 1;
			}
			else{
				return mid;
			}
		
		}
		
//		System.out.println(mid);
		if(arr[mid] < num){
			index = mid + 1;
		}else{
			index = mid;
		}
		return index;
	}

	static class InputReader {
		public BufferedReader reader;
		public StringTokenizer tokenizer;

		public InputReader(InputStream stream) {
			reader = new BufferedReader(new InputStreamReader(stream));
			tokenizer = null;
		}

		public String next() {
			try {
				while (tokenizer == null || !tokenizer.hasMoreTokens()) {
					tokenizer = new StringTokenizer(reader.readLine());

				}
			} catch (IOException e) {
				return null;
			}
			return tokenizer.nextToken();
		}

		public String nextLine() {
			String line = null;
			try {
				tokenizer = null;
				line = reader.readLine();
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
			return line;
		}

		public int nextInt() {
			return Integer.parseInt(next());
		}

		public double nextDouble() {
			return Double.parseDouble(next());
		}

		public long nextLong() {
			return Long.parseLong(next());
		}

		public boolean hasNext() {
			try {
				while (tokenizer == null || !tokenizer.hasMoreTokens()) {
					tokenizer = new StringTokenizer(reader.readLine());
				}
			} catch (Exception e) {
				return false;
			}
			return true;
		}
	}
}