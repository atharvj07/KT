import java.util.Scanner;

public class Main {
	static String map[][];
	static boolean used[][];
	static int h, w;
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		h = sc.nextInt();
		w = sc.nextInt();
		map = new String[h][];
		used = new boolean[h][w];
		for(int i = 0;i < h;i++){
			map[i] = sc.next().split("");
		}

		if(search(0, 0)){
			System.out.println("Possible");
		}else{
			System.out.println("Impossible");
		}

	}

	static boolean search(int a, int b){
		map[a][b] = ".";

		if(a+1 < h && b+1 < w && map[a+1][b].equals("#") && map[a][b+1].equals("#")){
			return false;
		}else if((a-1 >= 0 && map[a-1][b].equals("#")) || (b-1 >= 0 && map[a][b-1].equals("#"))){
			return false;
		}else if(a+1 < h && map[a+1][b].equals("#")){
			return search(a+1, b);
		}else if(b+1 < w && map[a][b+1].equals("#")){
			return search(a, b+1);
		}if(a == h-1 && b == w-1){
			return true;
		}else{
			return false;
		}
	}
}