import java.io.*;
import java.util.*;

class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner sc = new Scanner(System.in);
		String[] str = br.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		str = br.readLine().split(" ");
		int[] a = new int[n];
		for(int i = 0; i < n; i++) a[i] = Integer.parseInt(str[i]);
		int[] b = prev_permutation(a);
		if(a != b) printArray(b);
		printArray(a);
		b = next_permutation(a);
		if(a != b) printArray(b);
	}
	public static void printArray(int[] a){
		for(int i = 0; i < a.length; i++){
			System.out.print(a[i]);
			if(i != a.length - 1) System.out.print(" ");
		}
		System.out.print("\n");
	}
	public static int[] next_permutation(int[] a){
		int[] ret = new int[a.length];
		int front = -1, rear = -1;
		for(int i = 0; i < a.length; i++){
			for(int j = i + 1; j < a.length; j++){
				if(a[i] < a[j]){
					front = i;
					rear = j;
				}
			}
		}
		if(front == -1) return a;
		for(int i = 0; i < a.length; i++){
			if(i == front) ret[i] = a[rear];
			else if(i == rear) ret[i] = a[front];
			else ret[i] = a[i];
		}
		Arrays.sort(ret, front + 1, a.length);
		return ret;
	}
	public static int[] prev_permutation(int[] a){
		int[] ret = new int[a.length];
		int front = -1, rear = -1;
		for(int i = 0; i < a.length; i++){
			for(int j = i + 1; j < a.length; j++){
				if(a[i] > a[j]){
					front = i;
					rear = j;
				}
			}
		}
		if(front == -1) return a;
		for(int i = 0; i < a.length; i++){
			if(i == front) ret[i] = a[rear];
			else if(i == rear) ret[i] = a[front];
			else ret[i] = a[i];
		}
		Arrays.sort(ret, front + 1, a.length);
		for(int i = 0; i < (a.length - front) / 2; i++){
			int bf = ret[front + 1 + i];
			ret[front + 1 + i] = ret[a.length - i - 1];
			ret[a.length - i - 1] = bf;
		}
		return ret;
	}
}

