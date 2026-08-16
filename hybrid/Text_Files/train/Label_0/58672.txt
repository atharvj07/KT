import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		new Main().run();
		}
	public void run() {
		Scanner sc = new Scanner(System.in);
		int sx = sc.nextInt();
		int sy = sc.nextInt();
		int tx = sc.nextInt();
		int ty = sc.nextInt();
		move(sx,tx,'R');
		move(sy,ty,'U');
		move(sx,tx,'L');
		move(sy,ty+1,'D');
		move(sx,tx+1,'R');
		move(sy,ty+1,'U');
		move(0,1,'L');
		move(0,1,'U');
		move(sx,tx+1,'L');
		move(sy,ty+1,'D');
		move(0,1,'R');
		System.out.println();
		sc.close();
	}
	public void move(int s, int t, char C) {
		for (int i = 0; i < t - s; i++) {
			System.out.print(C);
		}
	}
}
