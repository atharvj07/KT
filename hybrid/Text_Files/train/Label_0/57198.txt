import java.util.Scanner;


public class Main {
	public static void main(String args[]){
		new Main().run();
	}
	
	void run(){
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int a[] = new int[n];
		for (int i = 0; i < n; i++) {
			String s = sc.next();
			a[i] = s.equals("A") ? 0 : 1;
		}
		boolean used[] = new boolean[n];
		boolean yes = true;
		for(int i = 0; i < n; ++i){
			if(a[i] == 0){
				boolean found = false;
				for(int j = i+1; j < n; ++j){
					if(used[j] || a[j] == 0) continue;
					used[j] = true;
					found = true;
					break;
				}
				if(!found) yes = false;
			} else {
				if(!used[i]) yes = false;
			}
			if(!yes) break;
		}
		System.out.println(yes ? "YES" : "NO");
		sc.close();
	}
}