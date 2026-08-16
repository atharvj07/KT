import java.util.*;
import static java.util.Arrays.*;

public class Main {

	static Scanner sc = new Scanner(System.in);
	static int n;
	static Team[] teams;
	
	static boolean read() {
		n = sc.nextInt(); 
		if(n == 0) return false;
		
		teams = new Team[n];
		int win, lose, k; 
		String name;
		for(int i = 0; i < n; i++) {
			name = sc.next();
			win = lose = 0;
			for(int j = 0; j < n - 1; j++) {
				k = sc.nextInt();
				if(k == 0) win++;
				else if(k == 1) lose++;
			}
			teams[i] = new Team(name, win, lose);
		}
		return true;
	}
	
	static void solve() {
		sort(teams);
		for(Team t : teams) {
			System.out.println(t.name);
		}
		
	}
	
	public static void main(String[] args) {
		while(read()) {
			solve();
		}	
	}
}

class Team implements Comparable<Team>{
	String name;
	int win, lose;
	
	Team(String name, int win, int lose) {
		this.name = name;
		this.win = win;
		this.lose = lose;
	}
	
	public int compareTo(Team t) {
		int ret = t.win - this.win;
		if(ret == 0) {
			return this.lose - t.lose;
		} else {
			return ret;
		}
	}
}