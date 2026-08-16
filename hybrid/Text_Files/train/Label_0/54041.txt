import java.util.*;

public class Main {
	Scanner in = new Scanner(System.in);
	public static void main(String[] args) {
		new Main();
	}

	public Main(){
		new AOJ2508().doIt();
	}

	class AOJ2508{
		int n;
		int[] key;
		char[] list;
		char[] station;
		void doIt(){
			String a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
			station = a.toCharArray();
			while(in.hasNext()){
				int n = in.nextInt();
				if(n==0)break;
				key = new int[n];for(int i=0;i<n;i++)key[i] = in.nextInt();
				list = in.next().toCharArray();
				ArrayList<Character> result = new ArrayList<Character>();
				for(int i=0;i<list.length;i++){
					int index = i%n;
					int b = key[index];
					for(int s=52;s<=52*2;s++){
						if(list[i]==station[s]){
							result.add(station[s-b]);
							break;
						}
					}
				}
				for(int i=0;i<result.size();i++)System.out.print(result.get(i));
				System.out.println();
			}
		}
	}

}