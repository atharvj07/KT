import java.util.Scanner;

class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int m = in.nextInt();
		int[] box = new int[n];
		boolean[] boxred = new boolean[n];
		
		boxred[0] = true;
		for (int i = 1; i < n; i++) {
			boxred[i] = false;
		}
		for (int i = 0; i < n; i++) {
			box[i] = 1;
		}
		

		for (int i = 0; i < m; i++) {
			int x = in.nextInt()-1;
			int y = in.nextInt()-1;
			if(boxred[x] == true){
				if(box[x] == 1){
					boxred[x] = false;
					boxred[y] = true;
				}else{
					boxred[y] = true;
				}
			}
			box[x]--;
			box[y]++;	
		}
		int ans = 0;
		for (int i = 0; i < n; i++) {
			if(boxred[i] == true){
				ans++;
			}
		}
		System.out.println(ans);
		in.close();
	}
	

}